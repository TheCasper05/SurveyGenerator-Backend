from pydantic import BaseModel
from typing import Literal
from enum import Enum

class QuestionType(str, Enum):
    multiple_choice = "multiple_choice"
    satisfaction = "satisfaction"
    text = "text"

class SurveyCreate(BaseModel):
    title: str
    description: str | None = None

class SurveyUpdate(BaseModel):
    title: str
    description: str
    
    model_config = {
    "from_attributes": True
    }
class Survey(BaseModel):
    id: int
    title: str
    description: str
    
    model_config = {
    "from_attributes": True
}
    
class QuestionBase(BaseModel):
    text: str
    question_type: QuestionType
    
class QuestionCreate(BaseModel):
    pass


class Question(QuestionBase):
    id: int
    
    model_config = {
    "from_attributes": True
    }