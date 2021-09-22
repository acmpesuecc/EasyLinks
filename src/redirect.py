import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="../templates"), name="static")
templates = Jinja2Templates(directory="../templates")


@app.get("/home")
async def index(request: Request):
    return templates.TemplateResponse("redirecthome.html", {"request": request})
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080, debug=True)
