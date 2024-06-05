### Despre

Acest depozit este preluat de la [SunoAI-API](https://github.com/SunoAI-API/Suno-API) și dezvoltat/implementat de [fswair](https://github.com/fswair).

### Documentația de implementare FastAPI

#### Prezentare generală

Această implementare FastAPI oferă diverse puncte finale, cum ar fi crearea de muzică, primirea de feeduri și gestionarea sesiunilor utilizatorilor. Gestionează în siguranță cererile de origine încrucișată și sesiunile utilizatorilor folosind CORS și middleware de sesiune.

## Autentificare manuală

Pentru a vă autentifica manual, trebuie să adăugați un câmp în sarcina utilă în parametrul json cu următorul format:

```
json={
 "date": {
 "cookie": "șir",
 "session_id": "șir"
 },
 "model":{
 „câmp”:valoare
 }
}
```

### Cuprins

- [Prezentare generală](#overview)
- [Configurare middleware](#middleware-configuration)
- [Endpoints](#endpoints)
- [Generează muzică (`/generate`)](https://suno.tomris.dev/docs#/default/generate_generate_post)
- [Generează muzică cu modul de descriere (`/generate/description-mode`)](https://suno.tomris.dev/docs#/default/generate_with_song_description_generate_description_mode_post)
- [Obțineți Feed (`/feed/{aid}`)](https://suno.tomris.dev/docs#/default/fetch_feed_feed__aid__get)
- [Generează versuri (`/generate/lyrics`)](https://suno.tomris.dev/docs#/default/generate_lyrics_post_generate_lyrics__post)
- [Obține versuri (`/lyrics/{lid}`)](https://suno.tomris.dev/docs#/default/fetch_lyrics_lyrics__lid__get)
- [Obține informații despre credit (`/get_credits`)](https://suno.tomris.dev/docs#/default/fetch_credits_get_credits_get)
- [Resetați acreditările (`/reset`)](https://suno.tomris.dev/docs#/default/reset_reset_get)
- [Setare acreditări (GET) (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_get)
- [Setare acreditări (POST) (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_post)

### Configurare middleware

```python
app.add_middleware(
 SessionMiddleware,
 secret_key=SECRET_KEY,
 same_site="niciunul",
 varsta_max=86400 * 30,
 https_only=Adevărat,
 session_cookie="sesiune"
)

app.add_middleware(
 CORSMiddleware,
 allow_origins="*"],
 allow_credentials=Adevărat,
 allow_methods="*"],
 allow_headers="*"],
)
```

Această configurație include `SessionMiddleware` pentru gestionarea sesiunilor și `CORSMiddleware` pentru gestionarea setărilor CORS.

### Puncte extreme

#### Pagina de pornire (`/`)

- **Metodă:** `GET`
- **Descriere:** Mesajul de bun venit și starea sesiunii sunt returnate.
- **Parametri de solicitare:** Nici unul
- **Răspuns:**

```json
{
"message": "Bine ați venit la Suno API",
"status": "în viață",
"utilizator": {
„status”: „conectat la {date}” sau „nu v-ați conectat încă”,
"uuid": "{uuid}",
"session_id": "{session_id}"
}
}
```

#### Generare muzică (`/generate`)

- **Metodă:** `POST`
- **Descriere:** creează muzică pe baza parametrilor de model dat.
- **Organismul cererii:**

```json
{
  "model": {
    //parametrii modelului conform schemelor.CustomModeGenerateParam
  }
}
```

- **Răspuns:** Returnează muzica creată sau mesajul de eroare.

#### Generați muzică cu modul de descriere (`/generate/description-mode`)

- **Metodă:** `POST`
- **Descriere:** creează muzică pe baza descrierii melodiei.
- **Organismul cererii:**

```json
{
  "model": {
    //parametrii modelului conform schemelor.DescriptionModeGenerateParam
  }
}
```

- **Răspuns:** Returnează muzica creată sau mesajul de eroare.

#### Obțineți feed (`/feed/{aid}`)

- **Metodă:** `GET`
- **Descriere:** Preia feedul pentru un anumit „ajutor”.
- **Parametri de solicitare:**
- `aid` (parametru cale): `aid` al fluxului de primit.
- **Răspuns:** returnează datele din feed sau mesajul de eroare.

#### Generați versuri (`/generate/lyrics`)

- **Metodă:** `POST`
- **Descriere:** creează versuri conform solicitării date.
