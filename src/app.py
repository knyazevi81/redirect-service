from fastapi import FastAPI, Header
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import uvicorn
from pyngrok import ngrok
from tinyurl import UrlShortenTinyurl


app = FastAPI()


@app.get("/get_my_pussy")
async def read_user_agent(user_agent: str = Header(None)):
    target_android = "https://play.google.com/store/apps/details?id=com.colizeumarena.colizeum"
    target_apple = "https://apps.apple.com/us/app/colizeum/id6444331712"

    windows = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    apple = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    android = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"

    if user_agent == windows:
        return RedirectResponse(url=target_apple)

    if user_agent == apple:
        return RedirectResponse(url=target_apple)

    if user_agent == android:
        return RedirectResponse(url=target_android)


HOST = "0.0.0.0"
PORT = int("8000")

# https://dashboard.ngrok.com/get-started/your-authtoken
ngrok.set_auth_token(TOKEN)
public_url = ngrok.connect(PORT).public_url
print(f"ngrok tunnel {UrlShortenTinyurl().shorten(public_url)}")


#app.include_router(auth_route)
#app.include_router(admin_route)

if __name__ == '__main__':
    print(f"API rinnung {HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)