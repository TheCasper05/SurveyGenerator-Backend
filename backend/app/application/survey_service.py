from app.domain.survey import Survey
from app.infrastructure.repositories.survey_repository import SurveyRepository

class SurveyService:
    def __init__(self, repo: SurveyRepository):
        self.repo = repo

    def create_survey(self, survey: Survey):
        return self.repo.save(survey)
