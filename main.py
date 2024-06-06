# -*- coding:utf-8 -*-

import base64, time, datetime

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse

import schemas
from cookie import set_cookie
from utils import Suno, SECRET_KEY

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    same_site="none",
    max_age=86400 * 30,
    https_only=True,
    session_cookie="session"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_root(request: Request):
    credentials = dict(request.session)
    sid = credentials.get("session_id")
    if sid:
        sid = sid[:12] + ("*" * 22) + sid[34:]
    return {"message": "Welcome to Suno API", "status": "alive", "user": {
        "status": f"logged in at {credentials.get('date')}" if credentials.get("uuid") else "not logged in yet",
        "uuid": credentials.get("uuid"),
        "session_id": sid
    }}

@app.get("/generate")
async def generate(
    request: Request,
    prompt: str,
    mv: str,
    title: str,
    tags: str,
    continue_at: int = None,
    continue_clip_id: str = None
):
    credentials = dict(request.session)
    if credentials.get("cookie") is None:
        return RedirectResponse(url="/setup", headers={"error": "Credentials not found in cookie. Please setup credentials."})
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.generate_music(dict(prompt=prompt, mv=mv, title=title, tags=tags, continue_at=continue_at, continue_clip_id=continue_clip_id))
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        

@app.post("/generate")
async def generate(
    model: schemas.CustomModeGenerateParam,
    request: Request,
    data: schemas.Credentials = None,
):
    credentials = data.dict() if data and isinstance(data, schemas.Credentials) else {}
    if credentials.get("cookie") is None:
        return {"error": "No credentials found in payload."}
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.generate_music(model.dict())
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.get("/generate/description-mode")
async def generate_with_song_description(
    request: Request,
    gpt_description_prompt: str
    make_instrumental: bool = False,
    mv: str = "chirp-v3-0",
    prompt: str = ""
):
    credentials = dict(request.session)
    if credentials.get("cookie") is None:
        return RedirectResponse(url="/setup", headers={"error": "Credentials not found in cookie. Please setup credentials."})
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.generate_music(dict(gpt_description_prompt=gpt_description_prompt, make_instrumental=make_instrumental, mv=mv, prompt=prompt))
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/generate/description-mode")
async def generate_with_song_description(
    model: schemas.DescriptionModeGenerateParam,
    request: Request, data: schemas.Credentials = None,
):
    credentials = data.dict() if data and isinstance(data, schemas.Credentials) else {}
    if credentials.get("cookie") is None:
        return {"error": "No credentials found in payload."}
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.generate_music(model.dict())
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.get("/feed/{aid}")
async def fetch_feed(aid: str, request: Request):
    credentials = dict(request.session)
    if credentials.get("cookie") is None:
        return RedirectResponse(url="/setup", headers={"error": "Credentials not found in cookie. Please setup credentials."})
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.get_feed(aid)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/feed/{aid}")
async def fetch_feed(aid: str, request: Request, data: schemas.Credentials = None):
    credentials = data.dict() if data and isinstance(data, schemas.Credentials) else {}
    if credentials.get("cookie") is None:
        return {"error": "No credentials found in payload."}
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.get_feed(aid)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.get("/generate/lyrics/")
async def generate_lyrics_post(prompt: str, request: Request):
    credentials = dict(request.session)
    if credentials.get("cookie") is None:
        return RedirectResponse(url="/setup", headers={"error": "Credentials not found in cookie. Please setup credentials."})
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    if not prompt.strip():
        return HTTPException(
            detail="Prompt can't be empty!", status_code=status.HTTP_400_BAD_REQUEST
        )
    try:
        resp = await suno.generate_lyrics(prompt)
        resp.update({"lyrics": f"{request.base_url}lyrics/{resp['id']}"})
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/generate/lyrics/")
async def generate_lyrics_post(model: schemas.LyricsGenerateParam, request: Request, data: schemas.Credentials = None):
    credentials = data.dict() if data and isinstance(data, schemas.Credentials) else {}
    if credentials.get("cookie") is None:
        return {"error": "No credentials found in payload."}
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    if not model.prompt.strip():
        return HTTPException(
            detail="Prompt can't be empty!", status_code=status.HTTP_400_BAD_REQUEST
        )
    try:
        resp = await suno.generate_lyrics(model.prompt)
        resp.update({"lyrics": f"{request.base_url}lyrics/{resp['id']}"})
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.get("/lyrics/{lid}")
async def fetch_lyrics(lid: str, request: Request):
    credentials = dict(request.session)
    if credentials.get("cookie") is None:
        return RedirectResponse(url="/setup", headers={"error": "Credentials not found in cookie. Please setup credentials."})
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.get_lyrics(lid)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/lyrics/{lid}")
async def fetch_lyrics(lid: str, request: Request, data: schemas.Credentials = None):
    credentials = data.dict() if data and isinstance(data, schemas.Credentials) else {}
    if credentials.get("cookie") is None:
        return {"error": "No credentials found in payload."}
    else:
        auth = await set_cookie(credentials)
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.get_lyrics(lid)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.get("/get_credits")
async def fetch_credits(request: Request):
    credentials = request.session
    if not credentials:
        return {"error": "Credentials not found in cookie. Please setup or pass credentials as json data."}
    else:
        try:
            auth = await set_cookie(credentials)
        except Exception as e:
            return HTTPException(500, f"An error occured: {e!r}")
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.get_credits()
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.post("/get_credits")
async def fetch_credits(request: Request, data: schemas.Credentials = None):
    credentials = dict(request.session) or data.dict() if data else {}
    if not credentials:
        return {"error": "Credentials not found in cookie. Please setup or pass credentials as json data."}
    else:
        try:
            auth = await set_cookie(credentials)
        except Exception as e:
            return HTTPException(500, f"An error occured: {e!r}")
        token = auth.get_token()
        suno = Suno(token)
    try:
        resp = await suno.get_credits()
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@app.get("/reset")
async def reset(request: Request):
    request.session.clear()
    return HTMLResponse("Credentials cleared from cookie. To setup credentials, click <a href='/setup'><b>here</b></a>.")

@app.get("/setup")
async def setup(request: Request):
    credentials = dict(request.session)
    if credentials.get("uuid"):
            return HTMLResponse("There is already a UUID stored in the cookie. To reset credentials, click <a href='/reset'><b>here</b></a>.")
    return HTMLResponse(
        """
        <h2> Setup Credentials </h2>
        Enter your cookie and session ID to reach the API:
        <hr>
        <form method="post" action='/setup'>
            <input type="text" name="cookie" placeholder="Cookie" required>
            <input type="text" name="session_id" placeholder="Session ID" required>
            <button type="submit">Submit</button>
        </form>
        """
    )

@app.post("/setup")
async def setup(request: Request):
        form = await request.form()
        uid = int(int(time.time() + id(request)))
        credentials = dict(request.session)
        if credentials.get("uuid"):
            return HTMLResponse("There is already a UUID stored in the cookie. To reset credentials, click <a href='/reset'><b>here</b></a>.")
        if (
            form.get("cookie") is None or form.get("session_id") is None
        ):
            return HTMLResponse("Cookie and Session ID are required.")
        
        cookie, session_id = form.get("cookie"), form.get("session_id")
        
        if not cookie or not session_id:
            return HTMLResponse("Cookie and Session ID are required as filled.")
        
        request.session["uuid"] = uid
        request.session["cookie"] = base64.b64encode(cookie.encode()).decode()
        request.session["session_id"] = base64.b64encode(session_id.encode()).decode()
        request.session["timestamp"] = time.time()
        request.session["date"] = datetime.datetime.fromtimestamp(request.session["timestamp"]).strftime("%d/%m/%Y %H:%M %p")
        return {"status": f"Credentials stored into cookie for author has {uid!r} UUID."}
