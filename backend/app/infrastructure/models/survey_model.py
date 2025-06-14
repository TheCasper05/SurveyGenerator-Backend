from sqlalchemy import Column, Integer, String
from app.core.database import Base  # ya está definido ahí

class SurveyModel(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
