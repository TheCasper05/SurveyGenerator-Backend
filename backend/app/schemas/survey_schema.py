from pydantic import BaseModel

class SurveyCreate(BaseModel):
    title: str
    description: str | None = None

class Survey(BaseModel):
    id: int
    title: str
    description: str
    
    model_config = {
    "from_attributes": True
}
