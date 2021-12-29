from fastapi import APIRouter,HTTPException, status
from typing import Optional

from fastapi.params import Depends
from pymongo import response
from models.users import User,Users,ID
from db.db import MongoDB
from db import object_str
from bson import ObjectId

router = APIRouter()
client = 'mongodb://localhost:27017'
db = MongoDB(database_name='ID_Card',uri=client)

def generate_token(engine):
    obj = object_str.CutId(_id=engine)
    Id = obj.dict()['id']
    return Id

    
@router.get('/')
async def Get_users():
    users = db.find(collection='user',query={})
    users = list(users)
    return users


@router.post('/')
async def Create_User(payload:User):
    payload = payload.dict()
    payload['id'] = generate_token(engine=ObjectId())
    card = db.find_one(collection='user',query={'id_card': payload['id_card']})
    if card:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user duplicate"
        )
    elif not card:
        db.insert_one(collection='user',data=payload)
        payload.pop('_id')
        return payload
    
    