import time
import os
from dotenv import load_dotenv
import redis
import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

load_dotenv()
app = FastAPI()
app.mount("/static", StaticFiles(directory="../templates"), name="static")
templates = Jinja2Templates(directory="../templates")
r=redis.Redis(host=os.getenv('REDIS_HOST'),port=os.getenv('REDIS_PORT'))


webh=0
@app.get("/home",include_in_schema=False)
def index(request: Request):
    global webh
    webh=webh+1
    return templates.TemplateResponse("redirecthome.html", {"request": request , "wb" : webh})

@app.get("/new",include_in_schema=False)
def index(request:Request):
    return templates.TemplateResponse("maplinks.html" , {"request" : request})

# @app.get("/r/{key}")
# def redirect(key : str):
    # if(key=="g"):
        # return RedirectResponse("https://www.google.com")
        
Allowed_domain=["google.com", "stackoverflow.com"]
        

@app.get("/r/{key}", response_class=RedirectResponse, status_code=302)
async def redirect_short_links(key : str):
    start=time.time()*1000
    if(key=="alive"):
        return "https://www.google.com" #this is test redirect , let it be to check if the service is up and running
    else:
        link=r.get(key)
        print(link)
        end=time.time()*1000
        print("Total redirect time : ",end-start)
        return link.decode('ascii')
        if link:
            url = link.decode('ascii')
            domain = urlparse(url).hostname.split(".")[-2] + "." + urlparse(url).hostname.split(".")[-1]
            if domain in Allowed_domain:
                if urlparse(url).scheme == "https":
                    return url
                else:
                    return "This website does not use HTTPS"
            else:
                return "This website is blocked"
        else:
            return "Invalid entry"


if __name__ == "__main__":
    tot_webhits = 0
    uvicorn.run(app, host='0.0.0.0', port=8080, log_level="debug")
