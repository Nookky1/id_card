from pydantic import BaseModel ,constr ,Field
from typing import Optional ,List


class User(BaseModel):
    firstname :  str = Field( example='Watcharapon')
    lastname : str = Field(example='Weeraborirak')
    nickname : Optional[str] = Field(None,example='Kane')
    age : Optional[int] = Field(None, example=24)
    major : Optional[str] = Field(None,example='Computer Engineer')
    id_card : constr(min_length=13,max_length=13) = Field(example='1102002743832')
    

class ID(BaseModel):
    firstname :  str = Field( example='Watcharapon')
    lastname : str = Field(example='Weeraborirak')
    nickname : Optional[str] = Field(None,example='Kane')
    age : Optional[int] = Field(None, example=24)
    major : Optional[str] = Field(None,example='Computer Engineer')
    id_card : constr(min_length=13,max_length=13) = Field(example='1102002743832')
    id : str = Field(None, example='ID ObjectID auto generate')
    
class Users(BaseModel):
    Users : List[ID]