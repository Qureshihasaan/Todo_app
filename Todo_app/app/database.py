from sqlmodel import SQLModel , Field , create_engine
from typing import Optional
from app import setting



class Todo(SQLModel,table=True):
    id : Optional[int] = Field(primary_key=True , index=True)
    content : str = Field(default=None)
    description : str = Field(default=None)
    is_done : bool = Field(default=False)
    
# class TodoResponse(SQLModel):
#     pass

class TodoUpdate(SQLModel):
    content: str = None
    description: str = None
    is_done: bool = None


connection_strings = str(setting.DATA_BASE_URL).replace(
    "postgresql" , "postgresql+psycopg"
)

engine = create_engine(connection_strings , connect_args={} , pool_recycle=300)


def create_db_and_tables()->None:
    SQLModel.metadata.create_all(engine)