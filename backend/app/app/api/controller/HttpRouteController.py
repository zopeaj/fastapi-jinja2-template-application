from dataclasses import dataclass, field
from typing import Optional, List
from pydantic.dataclasses import dataclass as pydanticDataClass

from fastapi import APIRouter

@dataclass
class Item:
    name: str
    price: float
    description: Optional[str] = None
    tax: Optional[float] = None

@dataclass
class ItemResult:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)
    description: Optional[str] = None
    tax: Optional[float] = None


itemApi = APIRouter()

@itemApi.post("/items/")
async def create_item(item: Item):
    return item

@itemApi.get("/items/next/", response_mode=ItemResult)
async def read_next_item():
    return {
        "name":"Island In The Moon",
        "price": 12.99,
        "description":"A place to be playing' and havin' fun",
        "tags": ["breater"],
        "tax":231.2
    }

@pydanticDataClass
class Items:
    name: str
    description: Optional[str] = None

@pydanticDataClass
class Author:
    name: str
    items: List[Item] = field(default_factory=list)


structClass = APIRouter(prefix="/authors", tags=["author"], responses={404: {"resource-not-found": "I'm a teapot"}})

@structClass.post("/{author_id}/items/", response_model=Author)
async def create_author_items(author_id: str, items: List[Item]):
    return {"name": author_id, "items": items}


@structClass.get("/", response_model=List[Author])
def get_authors():
    return [
        {
            "name": "Breaters",
            "items": [
                {
                    "name": "Island In The Moon",
                    "description": "A place to be be playin' and havin' fun",
                },
                {"name": "Holy Buddies"},
            ],
        },
        {
            "name": "System of an Up",
            "items": [
                {
                    "name": "Salt",
                    "description": "The kombucha mushroom people's favorite",
                },
                {"name": "Pad Thai"},
                {
                    "name": "Lonely Night",
                    "description": "The mostests lonliest nightiest of allest",
                },
            ],
        },
    ]


