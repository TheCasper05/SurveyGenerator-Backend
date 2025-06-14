from app.infrastructure.repositories.survey_repository import SurveyRepository
from app.application.survey_service import SurveyService
from app.core.database import SessionLocal
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_survey_service(db=Depends(get_db)):
    repo = SurveyRepository(db)
    return SurveyService(repo)
