from pydantic import BaseModel
from typing import Literal
from enum import Enum
from typing import List

class QuestionType(str, Enum):
    multiple_choice = "multiple_choice"
    satisfaction = "satisfaction"
    text = "text"
    
class QuestionBase(BaseModel):
    text: str
    question_type: QuestionType
    
class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    
    model_config = {
    "from_attributes": True
    }

class SurveyCreate(BaseModel):
    title: str
    description: str | None = None
    questions: List[QuestionCreate] = []

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
class AnswerCreate(BaseModel):
    answer: str

class Answer(BaseModel):
    id: int
    survey_id: int
    question_id: int
    answer: str

    model_config = {
        "from_attributes": True
    }


