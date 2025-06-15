from sqlalchemy.orm import Session
from app.schemas.survey_schema import SurveyCreate
from app.infrastructure.repositories.survey_repository import SurveyRepository
from app.infrastructure.models.survey_model import SurveyModel
from fastapi import HTTPException

class SurveyService:
    def create_survey(self, db: Session, survey: SurveyCreate):
        repository = SurveyRepository(db)
        return repository.save(survey)


    def get_surveys(self, db: Session):
        return SurveyRepository.get_surveys(db)
    
    def get_survey_by_id(self, db:Session, survey_id: int):
        survey = db.query(SurveyModel).filter(SurveyModel.id == survey_id).first()
        if not survey:
            raise HTTPException(status_code=404, detail="Survey not found")
        return survey


survey_service = SurveyService()



