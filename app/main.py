from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
import schemas
import crud
import models
from database import get_db, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

templates= Jinja2Templates(directory= "templates")

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):   
    return templates.TemplateResponse("index.html", {"request": request}) 
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest):

    task = crud.create_translation_task(db, request.text, request.languages)
    background_tasks.add_task(perform_translation, task.id, request.text, request.languages, db)
    print("Hello")   
    return{"task_id": {task.id}}

