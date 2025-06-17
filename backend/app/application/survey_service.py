from sqlalchemy.orm import Session
from app.schemas.survey_schema import SurveyCreate, SurveyUpdate, QuestionCreate
from app.infrastructure.repositories.survey_repository import SurveyRepository
from app.infrastructure.models.survey_model import SurveyModel, QuestionModel
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

    def update_survey(self, db: Session, survey_id: int, survey_data: SurveyUpdate):
        survey = db.query(SurveyModel).filter(SurveyModel.id == survey_id).first()
        if not survey:
            raise HTTPException(status_code=404, detail="Survey not found")
        
        survey.title = survey_data.title
        survey.description = survey_data.description
        
        db.commit()
        db.refresh(survey)
        return survey
    
    def delete_survey_by_id(self, db:Session, survey_id: int):
        survey = db.query(SurveyModel).filter(SurveyModel.id == survey_id).first()
        if not survey:
            raise HTTPException(status_code=404, detail="Survey not found")
        db.delete(survey)
        db.commit()
        return {"message": "Survey deleted successfully"}
    
    def add_question_to_survey(self, db: Session, survey_id: int, question: QuestionCreate):
        db_survey = db.query(SurveyModel).filter(SurveyModel.id == survey_id).first()
        if not db_survey:
             raise HTTPException(status_code=404, detail="Survey not found")
         
        db_question = QuestionModel(**question.model_dump(), survey_id=survey_id)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question  
    
    def get_questions_for_survey(self, db: Session, survey_id: int):
        survey = db.query(SurveyModel).filter(SurveyModel.id == survey_id).first()
        if not survey:
            raise HTTPException(status_code=404, detail="Survey not found")
    
        return db.query(QuestionModel).filter(QuestionModel.survey_id == survey_id).all()


survey_service = SurveyService()



