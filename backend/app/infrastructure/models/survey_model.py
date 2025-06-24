from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM
from app.core.database import Base

# ENUM ya existente, no volver a crearlo
question_type_enum = ENUM(
    'multiple_choice',
    'satisfaction',
    'text',
    name='question_type_enum',
    create_type=False
)

class SurveyModel(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    questions = relationship("QuestionModel", back_populates="survey", cascade="all, delete-orphan")


class QuestionModel(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"))
    text = Column(String, nullable=False)
    question_type = Column(question_type_enum, nullable=False)
    order = Column(Integer, nullable=False)  # Nuevo campo

    survey = relationship("SurveyModel", back_populates="questions")
    options = relationship("QuestionOptionModel", back_populates="question", cascade="all, delete-orphan")



class QuestionOptionModel(Base):
    __tablename__ = "question_options"  

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
    text = Column(String, nullable=False)

    question = relationship("QuestionModel", back_populates="options")
    
class AnswerModel(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer = Column(String, nullable=False)  

