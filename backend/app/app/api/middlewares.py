import time

from fastapi import FastAPI, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware


middlewares = FastAPI()
middlewares.add_middleware(GZipMiddleware, minimum_size=100)
middlewares.add_middleware(HTTPSRedirectMiddleware)
middlewares.add_middleware(TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "example.com", "*.example.com"]) #"example.com", "*.example.com", "127.0.0.1"


@middlewares.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


middlewares.get("/")
async def main():
    return {"message": "Hello world"}


@middlewares.get("/")
async def main():
    return {"message": "Hello World"}


@middlewares.get("/")
async def main():
    return "somebig-content"

