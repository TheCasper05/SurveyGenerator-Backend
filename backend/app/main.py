from fastapi import FastAPI
from app.interfaces import survey_router

app = FastAPI(title="Encuestador de Opinión")

# Incluir routers
app.include_router(survey_router.router, prefix="/api/surveys", tags=["Surveys"])
