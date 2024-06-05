### Hakkında

Bu depo, [SunoAI-API](https://github.com/SunoAI-API/Suno-API)'dan çatallanmıştır ve [fswair](https://github.com/fswair) tarafından geliştirilmiş/konuşlanmıştır.

### FastAPI Uygulama Dokümantasyonu

#### Genel Bakış

Bu FastAPI uygulaması, müzik oluşturma, beslemeleri alma ve kullanıcı oturumlarını yönetme gibi çeşitli uç noktalar sağlar. CORS ve oturum ara yazılımı kullanarak çapraz kaynak taleplerini ve kullanıcı oturumlarını güvenli bir şekilde yönetir.

### İçindekiler

- [Genel Bakış](#genel-bakış)
- [Ara Yazılım Konfigürasyonu](#ara-yazılım-konfigürasyonu)
- [Uç Noktalar](#uç-noktalar)
  - [Ana Sayfa (`/`)](#ana-sayfa-)
  - [Müzik Oluştur (`/generate`)](https://suno.tomris.dev/docs#/default/generate_generate_post)
  - [Açıklama Modu ile Müzik Oluştur (`/generate/description-mode`)](https://suno.tomris.dev/docs#/default/generate_with_song_description_generate_description_mode_post)
  - [Besleme Al (`/feed/{aid}`)](https://suno.tomris.dev/docs#/default/fetch_feed_feed__aid__get)
  - [Şarkı Sözü Oluştur (`/generate/lyrics`)](https://suno.tomris.dev/docs#/default/generate_lyrics_post_generate_lyrics__post)
  - [Şarkı Sözlerini Getir (`/lyrics/{lid}`)](https://suno.tomris.dev/docs#/default/fetch_lyrics_lyrics__lid__get)
  - [Kredi Bilgilerini Al (`/get_credits`)](https://suno.tomris.dev/docs#/default/fetch_credits_get_credits_get)
  - [Kimlik Bilgilerini Sıfırla (`/reset`)](https://suno.tomris.dev/docs#/default/reset_reset_get)
  - [Kimlik Bilgilerini Ayarla (GET) (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_get)
  - [Kimlik Bilgilerini Ayarla (POST) (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_post)

### Ara Yazılım Konfigürasyonu

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

Bu konfigürasyon, oturumları yönetmek için `SessionMiddleware` ve CORS ayarlarını yönetmek için `CORSMiddleware` içerir.

### Uç Noktalar

## Manuel Kimlik Doğrulama

Manuel olarak kimlik doğrulamak için json parametresindeki payloadda aşağıdaki biçimde bir field eklemelisiniz:

```
json={
  "data": {
    "cookie": "string",
    "session_id": "string"
  },
  "model": {
    "field": value
  }
}
```

#### Ana Sayfa (`/`)

- **Yöntem:** `GET`
- **Açıklama:** Hoş geldiniz mesajı ve oturum durumu döner.
- **İstek Parametreleri:** Yok
- **Yanıt:**
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

#### Müzik Oluştur (`/generate`)

- **Yöntem:** `POST`
- **Açıklama:** Verilen model parametrelerine göre müzik oluşturur.
- **İstek Gövdesi:**
  ```json
  {
    "model": {
      // schemas.CustomModeGenerateParam'a göre model parametreleri
    }
  }
  ```
- **Yanıt:** Oluşturulan müziği veya hata mesajını döner.

#### Açıklama Modu ile Müzik Oluştur (`/generate/description-mode`)

- **Yöntem:** `POST`
- **Açıklama:** Şarkı açıklamasına göre müzik oluşturur.
- **İstek Gövdesi:**
  ```json
  {
    "model": {
      // schemas.DescriptionModeGenerateParam'a göre model parametreleri
    }
  }
  ```
- **Yanıt:** Oluşturulan müziği veya hata mesajını döner.

#### Besleme Al (`/feed/{aid}`)

- **Yöntem:** `GET`
- **Açıklama:** Belirli bir `aid` için beslemeyi alır.
- **İstek Parametreleri:**
  - `aid` (path parametresi): Alınacak beslemenin `aid`'i.
- **Yanıt:** Besleme verilerini veya hata mesajını döner.

#### Şarkı Sözü Oluştur (`/generate/lyrics`)

- **Yöntem:** `POST`
- **Açıklama:** Verilen prompt'a göre şarkı sözleri oluşturur.
