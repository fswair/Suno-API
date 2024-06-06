İşte JSON yükünde manuel kimlik doğrulaması hakkında ek bilgi içeren Türkçe README:

````markdown
# Suno API

Bu, FastAPI ile oluşturulmuş Suno API'sidir. API, müzik oluşturma, besleme alma, şarkı sözleri oluşturma ve kullanıcı kimlik bilgilerini oturumlar (çerezler) veya doğrudan yük aracılığıyla işleme sonlanımlarını içerir.

## Manuel Kimlik Doğrulama

JSON yükünü kullanarak manuel kimlik doğrulaması yapmak için aşağıdaki alanları ekleyin:

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

## Gereksinimler

- Python 3.8+
- FastAPI
- Uvicorn
- `requirements.txt` dosyasında listelenen diğer bağımlılıklar

## Kurulum

1. Depoyu klonlayın:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Bir sanal ortam oluşturun ve etkinleştirin:

   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows'ta `venv\Scripts\activate` kullanın
   ```

3. Bağımlılıkları yükleyin:
   ```sh
   pip install -r requirements.txt
   ```

## Uygulamayı Çalıştırma

FastAPI uygulamasını Uvicorn ile çalıştırın:

```sh
uvicorn main:app --reload
```

Uygulama `http://127.0.0.1:8000` adresinde erişilebilir olacaktır.

## Endpoints

### Ana Endpoint

- **GET `/`**
  - Hoş geldiniz mesajı ve mevcut kullanıcı durumu döner.

### Müzik Oluştur

- **GET `/generate`**
  - Parametreler: `model: schemas.CustomModeGenerateParam`
  - Oturum kimlik bilgileri gerektirir.
- **POST `/generate`**
  - Parametreler: `model: schemas.CustomModeGenerateParam`, `data: schemas.Credentials`
  - Yükte kimlik bilgilerini kabul eder.

### Açıklama ile Müzik Oluştur

- **GET `/generate/description-mode`**
  - Parametreler: `model: schemas.DescriptionModeGenerateParam`
  - Oturum kimlik bilgileri gerektirir.
- **POST `/generate/description-mode`**
  - Parametreler: `model: schemas.DescriptionModeGenerateParam`, `data: schemas.Credentials`
  - Yükte kimlik bilgilerini kabul eder.

### Besleme Al

- **GET `/feed/{aid}`**
  - Yol Parametresi: `aid` (string)
  - Oturum kimlik bilgileri gerektirir.
- **POST `/feed/{aid}`**
  - Yol Parametresi: `aid` (string)
  - Yükte kimlik bilgilerini kabul eder.

### Şarkı Sözleri Oluştur

- **GET `/generate/lyrics/`**
  - Parametreler: `model: schemas.LyricsGenerateParam`
  - Oturum kimlik bilgileri gerektirir.
- **POST `/generate/lyrics/`**
  - Parametreler: `model: schemas.LyricsGenerateParam`, `data: schemas.Credentials`
  - Yükte kimlik bilgilerini kabul eder.

### Şarkı Sözlerini Al

- **GET `/lyrics/{lid}`**
  - Yol Parametresi: `lid` (string)
  - Oturum kimlik bilgileri gerektirir.
- **POST `/lyrics/{lid}`**
  - Yol Parametresi: `lid` (string)
  - Yükte kimlik bilgilerini kabul eder.

### Kredileri Al

- **GET `/get_credits`**
  - Oturum kimlik bilgileri gerektirir.
- **POST `/get_credits`**
  - Yükte kimlik bilgilerini kabul eder.

### Kimlik Bilgilerini Sıfırla

- **GET `/reset`**
  - Oturumda depolanan kimlik bilgilerini temizler.

### Kimlik Bilgilerini Ayarla

- **GET `/setup`**
  - Çerez ve oturum kimliğini girmek için bir form görüntüler.
- **POST `/setup`**
  - Sağlanan kimlik bilgilerini oturumda depolar.

## Kullanım

API'yi kullanmak için önce `/setup` yoluna giderek gerekli alanları doldurarak kimlik bilgilerini ayarlayın. Alternatif olarak, POST isteklerini destekleyen son noktalar için kimlik bilgileri doğrudan yükte geçilebilir.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

```

Projeye özgü detayları eklemek isterseniz bu README'yi daha fazla özelleştirebilirsiniz.
```
