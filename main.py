from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # ----------------- setting page item and style -----------------
    navbarItems = {
        "Title": "程式代寫",
        "Home": "Home",
        "About": "About",
        "Contact": "Contact",
    }


    return templates.TemplateResponse(
        "index.html", {"request": request, "navbarItems": navbarItems}
    )
