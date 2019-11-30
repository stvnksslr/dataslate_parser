from fastapi import FastAPI, File, UploadFile
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.utils.battlescribe_meta import check_battlescribe_version
from app.utils.constants import BATTLESCRIBE_VERSION_ERROR
from app.utils.test_utils import get_parser_type_and_parse
import uvicorn
import zipfile
from io import StringIO

app = FastAPI(
    title="Dataslate",
    description="Parsing tool to make more clean and easily printable outputs for battlescribe",
    version="1.0.0",
    redoc_url=None,
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app//static/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/files/")
async def create_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()

    supported_battlescribe_version = check_battlescribe_version(roster=contents)

    if not supported_battlescribe_version:
        return BATTLESCRIBE_VERSION_ERROR

    data = get_parser_type_and_parse(roster=contents)

    parsed_roster = data.get("roster")
    template = data.get("template")

    return templates.TemplateResponse(
        template, {"request": request, "roster": parsed_roster}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
