from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class SurveyModel(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
    questions = relationship("QuestionModel", back_populates="survey", cascade="all, delete-orphan")


class QuestionModel(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key = True, index = True)
    survey_id = Column(Integer, ForeignKey("surveys.id"))
    text = Column(String, nullable=False)
    question_type = Column(Enum("multiple_choice", "satisfaction", "text", name="question_type_enum"), nullable=False)
    
    survey = relationship("SurveyModel", back_populates="questions")