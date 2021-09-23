import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="../templates"), name="static")
templates = Jinja2Templates(directory="../templates")

webh=0
@app.get("/home",include_in_schema=False)
def index(request: Request):
    global webh
    webh=webh+1
    return templates.TemplateResponse("redirecthome.html", {"request": request , "wb" : webh})

# @app.get("/r/{key}")
# def redirect(key : str):
    # if(key=="g"):
        # return RedirectResponse("https://www.google.com")
@app.get("/r/{key}", response_class=RedirectResponse, status_code=302)
async def redirect_short_links(key : str):
    if(key=="test"):
        return "https://www.google.com"

if __name__ == "__main__":
    tot_webhits = 0
    uvicorn.run(app, host='0.0.0.0', port=8080, debug=True)
