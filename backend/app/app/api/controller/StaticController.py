from typing import Any, Optional
from fastapi import APIRouter, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: Optional[str] = None
    age: int = None
    business: Optional[str] = None

class ItemCreateResponse(BaseModel):
    name: str
    age: int


staticRouter = APIRouter()


items = {
    1: {
       "id": 1,
       "name": "text 1",
       "description": "Hello Data 1",
    },
    2: {
       "id": 2,
       "name": "text 2",
       "description": "Hello Text 2"
    }
}

itemdata = [
    {
     "id": 1,
     "name": "text-1",
    },
    {
     "id": 2,
     "name": "text-2",
    },
    {
     "id": 3,
     "name": "text-3",
    },
    {
     "id": 4,
     "name": "text-4",
    },
    {
     "id": 5,
     "name": "text-5",
    }
]


templates = Jinja2Templates(directory="templates")

@staticRouter.get("/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: int = Path(..., title="The item details")):
    item = None
    if item_id in items:
        item = items[item_id]
    else:
        item = None
    return templates.TemplateResponse("item_details.html", {"request": request, "item": item})


@staticRouter.get("/", response_class=HTMLResponse)
async def read_items(request: Request) -> Any:
    return templates.TemplateResponse("item_list.html", {"request": request, "itemdata": itemdata})

@staticRouter.get("/create/", response_class=HTMLResponse)
async def post_items(request: Request) -> Any:
    return templates.TemplateResponse("item.html", {"request": request})

@staticRouter.post("/create/item/")
async def post_data_item(item: ItemCreate):
    return {"name": item.name, "age": item.age}

# @staticRouter.get("/index1", response_class=HTMLResponse)
# def index(request: Request):
#    return templates.TemplateResponse("demo.html",{"request":request,
#         "title":"Kaustubh Demo", "body_content":
#         "This is the deom fastAPI with Jinja templates"})


# @staticRouter.get("/index2", response_class=HTMLResponse)
# def index(request: Request):
#     return templates.TemplateResponse("demo.html", {"request":request,
#         "title":"Kaustubh Demo",
#         "body_content":"This is the demo for using FastAPI with Jinja templates"})

