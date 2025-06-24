from sqlalchemy.orm import Session
from app.schemas.survey_schema import SurveyCreate, SurveyUpdate, QuestionCreate, AnswerCreate, Answer
from app.infrastructure.repositories.survey_repository import SurveyRepository
from app.infrastructure.models.survey_model import SurveyModel, QuestionModel, AnswerModel
from fastapi import HTTPException

class SurveyService:
    def create_survey(self, db: Session, survey: SurveyCreate):
        repository = SurveyRepository(db)
    
        # Crear la encuesta
        db_survey = SurveyModel(title=survey.title, description=survey.description)
        db.add(db_survey)
        db.commit()
        db.refresh(db_survey)

        # Crear preguntas con el campo order
        for index, question_data in enumerate(survey.questions):
            db_question = QuestionModel(**question_data.model_dump(), survey_id=db_survey.id, order=index)
            db.add(db_question)
    
        db.commit()
        return db_survey




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
    
        return db.query(QuestionModel).filter(QuestionModel.survey_id == survey_id).order_by(QuestionModel.order).all()


    def add_answer_to_question(self, db: Session, survey_id: int, question_id: int, answer: AnswerCreate):
        db_survey = db.query(SurveyModel).filter(SurveyModel.id == survey_id).first()
        if not db_survey:
            raise HTTPException(status_code=404, detail="Survey not found")

        db_question = db.query(QuestionModel).filter(QuestionModel.id == question_id).first()
        if not db_question:
            raise HTTPException(status_code=404, detail="Question not found")

        db_answer = AnswerModel(**answer.model_dump(), survey_id=survey_id, question_id=question_id)
        db.add(db_answer)
        db.commit()
        db.refresh(db_answer)
        return db_answer

    def get_answers_for_question(self, survey_id: int, question_id: int, db: Session):
        db_survey = db.query(SurveyModel).filter(SurveyModel.id == survey_id).first()
        if not db_survey:
            raise HTTPException(status_code=404, detail="Survey not found")

        db_question = db.query(QuestionModel).filter(QuestionModel.id == question_id).first()
        if not db_question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        return db.query(AnswerModel).filter(AnswerModel.survey_id == survey_id, AnswerModel.question_id == question_id).all()

        
survey_service = SurveyService()



