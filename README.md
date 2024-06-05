### About

This repo forked from [SunoAI-API](https://github.com/SunoAI-API/Suno-API) and developed/deployed by [fswair](https://github.com/fswair)

### FastAPI Application Documentation

#### Overview

This FastAPI application provides several endpoints for generating music, fetching feeds, and handling user sessions. It utilizes CORS and session middleware to manage cross-origin requests and user sessions securely.

## Manual Authentication

To authenticate manually, you must add a field in the payload in the json parameter with the following format:

```
json={
 "data": {
 "cookie": "string",
 "session_id": "string"
 },
 "model":{
 "field":value
 }
}
```

### Table of Contents

- [Overview](#overview)
- [Middleware Configuration](#middleware-configuration)
- [Endpoints](#endpoints)
- [Home Page (`/`)](#home-page-)
- [Generate Music (`/generate`)](https://suno.tomris.dev/docs#/default/generate_generate_post)
- [Generate Music with Description Mode (`/generate/description-mode`)](https://suno.tomris.dev/docs#/default/generate_with_song_description_generate_description_mode_post)
- [Get Feed (`/feed/{aid}`)](https://suno.tomris.dev/docs#/default/fetch_feed_feed__aid__get)
- [Generate Lyrics (`/generate/lyrics`)](https://suno.tomris.dev/docs#/default/generate_lyrics_post_generate_lyrics__post)
- [Get Lyrics (`/lyrics/{lid}`)](https://suno.tomris.dev/docs#/default/fetch_lyrics_lyrics__lid__get)
- [Get Credit Information (`/get_credits`)](https://suno.tomris.dev/docs#/default/fetch_credits_get_credits_get)
- [Reset Credentials (`/reset`)](https://suno.tomris.dev/docs#/default/reset_reset_get)
- [Set Credentials (GET) (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_get)
- [Set Credentials (POST) (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_post)

### Middleware Configuration

```python
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
```

This configuration includes `SessionMiddleware` for managing sessions and `CORSMiddleware` to handle Cross-Origin Resource Sharing (CORS) settings.

### Endpoints

#### Root (`/`)

- **Method:** `GET`
- **Description:** Returns a welcome message and session status.
- **Request Parameters:** None
- **Response:**
  ```json
  {
    "message": "Welcome to Suno API",
    "status": "alive",
    "user": {
      "status": "logged in at {date}" or "not logged in yet",
      "uuid": "{uuid}",
      "session_id": "{session_id}"
    }
  }
  ```

#### Generate Music (`/generate`)

- **Method:** `POST`
- **Description:** Generates music based on the provided model parameters.
- **Request Body:**
  ```json
  {
    "model": {
      // Model parameters as per schemas.CustomModeGenerateParam
    }
  }
  ```
- **Response:** Returns the generated music or an error message.

#### Generate Music with Description (`/generate/description-mode`)

- **Method:** `POST`
- **Description:** Generates music based on song description.
- **Request Body:**
  ```json
  {
    "model": {
      // Model parameters as per schemas.DescriptionModeGenerateParam
    }
  }
  ```
- **Response:** Returns the generated music or an error message.

#### Fetch Feed (`/feed/{aid}`)

- **Method:** `GET`
- **Description:** Fetches the feed for a specific `aid`.
- **Request Parameters:**
  - `aid` (path parameter): The aid of the feed to fetch.
- **Response:** Returns the feed data or an error message.

#### Generate Lyrics (`/generate/lyrics`)

- **Method:** `POST`
- **Description:** Generates lyrics based on the provided prompt.
- **Request Body:**
  ```json
  {
    "model": {
      "prompt": "Lyrics prompt text"
    }
  }
  ```
- **Response:** Returns the generated lyrics or an error message.

#### Fetch Lyrics (`/lyrics/{lid}`)

- **Method:** `GET`
- **Description:** Fetches lyrics for a specific `lid`.
- **Request Parameters:**
  - `lid` (path parameter): The ID of the lyrics to fetch.
- **Response:** Returns the lyrics data or an error message.

#### Fetch Credits (`/get_credits`)

- **Method:** `GET`
- **Description:** Fetches the user's credits.
- **Response:** Returns the credits data or an error message.

#### Reset Credentials (`/reset`)

- **Method:** `GET`
- **Description:** Clears stored credentials from the session.
- **Response:** HTML response indicating that credentials have been cleared.

#### Setup Credentials (GET) (`/setup`)

- **Method:** `GET`
- **Description:** Displays a form to setup credentials.
- **Response:** HTML form for entering credentials.

#### Setup Credentials (POST) (`/setup`)

- **Method:** `POST`
- **Description:** Stores the provided credentials in the session.
- **Request Body:** Form data containing `cookie` and `session_id`.
- **Response:** HTML response indicating that credentials have been stored.
