from pydantic import BaseModel

class SurveyCreate(BaseModel):
    title: str
    description: str

class SurveyResponse(SurveyCreate):
    id: int
