from app.domain.survey import Survey
from app.infrastructure.models.survey_model import SurveyModel
from app.core.database import SessionLocal

class SurveyRepository:
    def __init__(self, db_session):
        self.db = db_session

    def save(self, survey: Survey):
        db_survey = SurveyModel(title=survey.title, description=survey.description)
        self.db.add(db_survey)
        self.db.commit()
        self.db.refresh(db_survey)
        return db_survey
