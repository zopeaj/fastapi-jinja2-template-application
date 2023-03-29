import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import api_router
from app.core.settings.settingsConfiguration import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title=settings.appName, openapi_url=f"/{settings.appName}", servers=[{"url":"https://stag.example.com", "description":"Staging environment"}, {"url": "https://prod.example.com", "description": "Production environment"}], root_path="/api/v1", root_path_in_servers=False,)
@app.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}


# # In the docs UI at http://127.0.0.1:9999/api/v1/docs
# it would look like:

# {
#     "openapi": "3.0.2",
#     # // More stuff here
#     "servers": [
#         {
#             "url": "/api/v1"
#         },
#         {
#             "url": "https://stag.example.com",
#             "description": "Staging environment"
#         },
#         {
#             "url": "https://prod.example.com",
#             "description": "Production environment"
#         }
#     ],
#     "paths": {
#             # // More stuff here
#     }
# }


subapi = FastAPI()

@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    with open("log.txt", mode="a") as log:
        log.write("Application Startup Successfully")

@app.on_event("shutdown")
def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application Shutdown Successfully")


app.include_router(api_router, prefix="/main")



staticFiles = StaticFiles(directory="templates/static")
app.mount("/static", staticFiles, name="static")
app.mount("/subapi", subapi)
# 127.0.0.1:8080/subapi/sub


