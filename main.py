from fastapi import FastAPI, HTTPException, Depends
from models import ToDo
from database import get_db
from sqlalchemy.orm import declarative_base, Session
from typing import Optional, List
import uvicorn
from schema import ToDo_pydantic, ToDoIn_pydantic


app = FastAPI()


@app.get("/", response_model=List[ToDo_pydantic])
def todo_list(db: Session = Depends(get_db)):
    return db.query(ToDo).all()


@app.post("/", response_model=ToDo_pydantic)
def create_task_view(task: ToDoIn_pydantic, db: Session = Depends(get_db)):
    todo_task = ToDo(**task.dict())
    db.add(todo_task)
    db.commit()
    db.refresh(todo_task)
    return todo_task


@app.get('/task/{task_id}', response_model=ToDo_pydantic)
def get_task_view(task_id: int, db: Session = Depends(get_db)):
    task = db.query(ToDo).where(ToDo.id == task_id).first()
    if not task:
        raise HTTPException(status_code=400, detail="Oops!! Task not found!")
    return task


@app.put('/task/', response_model=ToDo_pydantic)
def update_task_view(task: ToDo_pydantic, db: Session = Depends(get_db)):
    task_dict = task.dict()        
    task = db.query(ToDo).where(ToDo.id == task_dict['id']).first()
    if not task:
        raise HTTPException(status_code=400, detail="Oops!! Task not found!")
    task.title = task_dict['title'] 
    task.description = task_dict['description']
    db.add(task)
    db.commit()
    return task


@app.delete('/task/{task_id}')
def delete_task_view(task_id: int, db: Session = Depends(get_db)):
    try:
        db.query(ToDo).filter(ToDo.id == task_id).delete()
        db.commit()
        return {"message": "Task successfully deleted"}
    except:
        raise HTTPException(status_code=400, detail="Oops!! Task not found!")




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)