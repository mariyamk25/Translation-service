# from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker, Session



import models

def create_translation_task(db: Session, text: str, Languages: list):
    task = models.TranslationTask(text=text, languages=Languages)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
def get_translation_task(db: Session, task_id: int):
    return db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()


def update_translation_task(db: Session, task_id: int, translations: dict):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id== task_id).first()
    task.translations =translations
    task.status = "completed"
    db.commit()
    db.refresh(task)
    return task