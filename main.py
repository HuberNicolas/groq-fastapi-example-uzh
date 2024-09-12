from fastapi import FastAPI
from fastapi import __version__ as fastapi_version
from fastapi.middleware.cors import CORSMiddleware


import logging
from app.routes import llm



log = logging.getLogger(__name__)

app = FastAPI(
    title='Groq Example',
    version='0.1.0',
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
    )
app.include_router(llm.router)


# CORS (development only)
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/version")
def version():
    return {"version": app.version}


@app.get("/fastapi-version")
def version():
    return {"version": fastapi_version}
