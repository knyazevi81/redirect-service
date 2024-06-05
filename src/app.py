from fastapi import FastAPI, Header, Response
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import uvicorn
from pyngrok import ngrok

from fastapi.responses import HTMLResponse
import os

current_directory = os.getcwd()

file_path = os.path.join(current_directory, "wind_installer.bat")

#import nest_asyncio

#nest_asyncio.apply()

app = FastAPI()

data = {
    "apple": 0,
    "android":0,
    "windows":0
}


@app.get("/")
async def read_user_agent(user_agent: str = Header(None)):
    target_android = "https://play.google.com/store/apps/details?id=com.colizeumarena.colizeum"
    target_apple = "https://apps.apple.com/ru/app/%D1%81-world/id6459059878"

    windows = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    apple = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    android = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
    mac = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15"

    if "Windows" in user_agent:
        data["windows"] += 1
        return RedirectResponse(url=target_apple)

    if "iPhone" in user_agent:
        data["apple"] += 1
        return RedirectResponse(url=target_apple)

    if "Android" in user_agent:
        data["android"] += 1
        return HTMLResponse(
            """<!DOCTYPE html>
                <html lang='en'>
                <head>
                    <meta charset='UTF-8'>
                    <meta http-equiv='refresh' content='0;url=market://details?id=com.cworld'>
                    <title>Redirecting...</title>
                </head>
                <body>
                    <p>Redirecting to colizeum app in 1 seconds...</p>
                </body>
                </html>
            """
        )
    else:
        return RedirectResponse(url=target_apple)
        #return HTMLResponse(
        #    "<a href='market://details?id=com.colizeumarena.colizeum'>Открыть приложение в Google Play Store</a>"
        #)

@app.get("/user_data/all")
async def read_user_agent():
    return data

@app.get("/pc_activator")
async def download_bat_file(response: Response):
    response.headers["Content-Disposition"] = "attachment; filename=my_script.bat"
    response.headers["Content-Type"] = "application/octet-stream"
    # Открываем bat-файл и записываем его содержимое в response
    print(os.listdir())
    with open(file_path, "rb") as file:
        content = file.read()
        
    return Response(content)

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
