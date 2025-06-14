from fastapi import APIRouter, Depends
from app.schemas.survey_schema import SurveyCreate, SurveyResponse
from app.dependencies.di import get_survey_service

router = APIRouter()

@router.post("/", response_model=SurveyResponse)
def create_survey(survey: SurveyCreate, service = Depends(get_survey_service)):
    return service.create_survey(survey)
