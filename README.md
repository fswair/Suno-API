Here's the updated README with the additional information on manual authentication using JSON payload:

````markdown
# Suno API

This is the Suno API built with FastAPI. The API includes endpoints for generating music, fetching feeds, generating lyrics, and handling user credentials through sessions (cookies) or direct payload.

## Manual Authentication

To manually authenticate using JSON payload, include the following fields:

```json
{
  "data": {
    "cookie": "string",
    "session_id": "string"
  },
  "model": {
    "field": "value"
  }
}
```
````

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

Run the FastAPI application with Uvicorn:

```sh
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Endpoints

### Root Endpoint

- **GET `/`**
  - Returns a welcome message and the current user status.

### Generate Music

- **GET `/generate`**
  - Parameters: `model: schemas.CustomModeGenerateParam`
  - Requires session credentials.
- **POST `/generate`**
  - Parameters: `model: schemas.CustomModeGenerateParam`, `data: schemas.Credentials`
  - Accepts credentials in the payload.

### Generate Music with Description

- **GET `/generate/description-mode`**
  - Parameters: `model: schemas.DescriptionModeGenerateParam`
  - Requires session credentials.
- **POST `/generate/description-mode`**
  - Parameters: `model: schemas.DescriptionModeGenerateParam`, `data: schemas.Credentials`
  - Accepts credentials in the payload.

### Fetch Feed

- **GET `/feed/{aid}`**
  - Path Parameter: `aid` (string)
  - Requires session credentials.
- **POST `/feed/{aid}`**
  - Path Parameter: `aid` (string)
  - Accepts credentials in the payload.

### Generate Lyrics

- **GET `/generate/lyrics/`**
  - Parameters: `model: schemas.LyricsGenerateParam`
  - Requires session credentials.
- **POST `/generate/lyrics/`**
  - Parameters: `model: schemas.LyricsGenerateParam`, `data: schemas.Credentials`
  - Accepts credentials in the payload.

### Fetch Lyrics

- **GET `/lyrics/{lid}`**
  - Path Parameter: `lid` (string)
  - Requires session credentials.
- **POST `/lyrics/{lid}`**
  - Path Parameter: `lid` (string)
  - Accepts credentials in the payload.

### Get Credits

- **GET `/get_credits`**
  - Requires session credentials.
- **POST `/get_credits`**
  - Accepts credentials in the payload.

### Reset Credentials

- **GET `/reset`**
  - Clears the credentials stored in the session.

### Setup Credentials

- **GET `/setup`**
  - Displays a form to input cookie and session ID.
- **POST `/setup`**
  - Stores the provided credentials into the session.

## Usage

To use the API, set up the credentials first by navigating to `/setup` and filling in the required fields. Alternatively, credentials can be passed directly in the payload for endpoints that support POST requests.

## License

This project is licensed under the MIT License.

```

Feel free to further customize this README to match the specifics of your project.
```
