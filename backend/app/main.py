

from fastapi import FastAPI
from app.interfaces import survey_router

app = FastAPI()

app.include_router(survey_router.router)
