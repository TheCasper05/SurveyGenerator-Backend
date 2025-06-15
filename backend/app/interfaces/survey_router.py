from fastapi import APIRouter, Depends
from app.schemas.survey_schema import Survey, SurveyCreate
from app.dependencies.di import get_db
from sqlalchemy.orm import Session
from typing import List
from app.application.survey_service import survey_service



router = APIRouter()

@router.post("/surveys/", response_model=Survey)
def create_survey(survey:SurveyCreate, db:Session = Depends(get_db)):
    return survey_service.create_survey(db, survey)

@router.get("/surveys/", response_model=List[Survey])
def read_surveys(db: Session = Depends(get_db)):
    return survey_service.get_surveys(db)

@router.get("/surveys/{survey_id}", response_model= Survey)
def read_survey(survey_id: int, db:Session = Depends(get_db)):
    return survey_service.get_survey_by_id(db, survey_id)

