import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import APIRouter
from app.api.controller.StaticController import staticRouter

api_router = APIRouter()

api_router.include_router(staticRouter, prefix="/items", tags=["data"])
