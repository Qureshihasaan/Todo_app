from fastapi import FastAPI , Depends , HTTPException
from typing import Annotated , AsyncGenerator 
from .database import engine , Todo , create_db_and_tables , TodoUpdate
from contextlib import asynccontextmanager
from sqlmodel import Session , select


@asynccontextmanager
async def lifespan(app : FastAPI)->AsyncGenerator[None ,None]:
    print("Creating Tables...")
    create_db_and_tables()
    yield
    
    
app : FastAPI = FastAPI(lifespan=lifespan , version="1.0.0",
                        title="Todo App With DB" ,
                           servers=[{
              
                  "url": "https://trademarks-sorts-wine-camp.trycloudflare.com         ",
                  "description": "Development Server"
              }]
                        )


def get_db():
    with Session(engine) as session:
        yield session
        
        
        
@app.get("/")
def get_route():
    return {"message" : "Hello, world!"}


@app.get("/single_todo{todo_id}")
async def get_single_todo(todo_id : int ,
    db: Annotated[Session , Depends(get_db)]):
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.get("/todo")
async def get_all_todo(db :Annotated[Session , Depends(get_db)]):
     get_todo = db.exec(select(Todo)).all()
     return get_todo
  
@app.post("/create_todo")
async def create_todo(todo : Todo , db : Annotated[Session , Depends(get_db)]):
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.put("/update_todo{todo_id}" , response_model=TodoUpdate)
async def update_todo(todo_id : int , todo_update : TodoUpdate , db : Annotated[Session , Depends(get_db)]):
    todo = db.get(Todo , todo_id)
    if todo is None:
        raise HTTPException(status=404 , detail="Todo not found")
    todo.content = todo_update.content
    todo.description = todo_update.description
    todo.is_done = todo_update.is_done
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/delete_todo{todo_id}" , response_model=Todo)
async def delete_todo(todo_id : int , db : Annotated[Session , Depends(get_db)]):
    todo = db.get(Todo , todo_id)
    if not todo:
        raise HTTPException(status_code=404 , detail="Todo not found")
    db.delete(todo)
    db.commit()
    return todo