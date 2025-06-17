from app.domain.survey import Survey
from app.infrastructure.models.survey_model import SurveyModel, QuestionModel
from app.core.database import SessionLocal
from sqlalchemy.orm import Session



class SurveyRepository:
    def __init__(self, db_session):
        self.db = db_session

    def save(self, survey: Survey):
        db_survey = SurveyModel(title=survey.title, description=survey.description)
        self.db.add(db_survey)
        self.db.commit()
        self.db.refresh(db_survey)
        return db_survey
    
    def get_surveys(db: Session):
        return db.query(SurveyModel).all()
    
    def get_questions_by_survey_id(db: Session, survey_id: int):
        return db.query(QuestionModel).filter(QuestionModel.survey_id == survey_id).all()


