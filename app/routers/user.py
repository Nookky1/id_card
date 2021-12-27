from fastapi import APIRouter
from typing import Optional
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

    