### 説明

このソースでは、[SunoAI-API](https://github.com/SunoAI-API/Suno-API) と [fswair](https://github.com/fswair) がサポートされています/詳細はこちら。

### FastAPI ドキュメントの翻訳

#### 一般的な翻訳

FastAPI ドキュメントの翻訳、音楽の翻訳、およびオーディオの翻訳は、通常、ユーザーが自分のコンピュータで実行している操作です。 CORS は、読者が自分のブログやウェブサイトをいつでも無料で閲覧できるようにするために作成されました。

## 手動認証

手動で認証するには、次の形式で json パラメータのペイロードにフィールドを追加する必要があります。

「」
json={
"データ"： {
"クッキー": "文字列",
"セッション ID": "文字列"
}、
"モデル"：{
「フィールド」:値
}
}
「」

### コンテンツ

- [一般的な投稿](#一般的な投稿)
- [現在の投稿設定](#現在の投稿設定)
- [現在の投稿設定](#現在の投稿設定)
- [音楽生成 (`/generate`)](https://suno.tomris.dev/docs#/default/generate_generate_post)
- [音楽生成モード (`/generate/description-) の使用] mode`)](https://suno.tomris.dev/docs#/default/generate_with_song_description_generate_description_mode_post)
- [Feed by AID (`/feed/{aid}`)](https://suno.tomris.dev/docs#/default/fetch_feed_feed__aid__get)
- [Create Lyrics (`/generate/lyrics`)](https://suno. tomris.dev/docs#/default/generate_lyrics_post_generate_lyrics\_\_post)
- [`/lyrics/{lid}` をアップロード](https://suno.tomris.dev/docs#/default/fetch_lyrics_lyrics__lid__get)
- [クレジット カード(`/get_credits`)](https://suno.tomris.dev/docs#/default/fetch_credits_get_credits_get)
- [クレジットを投稿する(`/reset`)](https://suno.tomris.dev/docs#/default/reset_reset_get)
- [Setup Creds (GET) (`/setup`)](https://suno.tomris.dev /docs#/default/setup_setup_get)
- [POST ドキュメント (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_post)

### 次ページ 設定

```python
app.add_middleware(
SessionMiddleware、
secret_key=SECRET_KEY、
same_site="none",
max_age=86400 * 30、
https_only=True、
session_cookie="session"
)

app.add_middleware(
CORSMiddleware、
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)
```

この構成では、`SessionMiddleware` と CORS ミドルウェアの両方がサポートされています。また、`CORSMiddleware` もサポートされています。 .

### 無効にする

#### ホーム (`/`)

- **実行:** `GET`
- **実行:** メッセージを再度送信して、しばらくお待ちください。
- ** パラメーター:** 有効
- ** 有効:**

```json
{
"message": "Suno API へようこそ",
"status": "alive",
"user": {
"status": " {date} にログインしました" または "まだログインしていません",
"uuid": "{uuid}",
"session_id": "{session_id}"
}
}
```

#### 音楽生成 (`/generate` )

- **タグ:** `POST`
- **タグ:** 音楽再生用のパラメーター付きモデル。
- **出力:**

```json
{
  "model": {
    // schemas.CustomModeGenerateParam はモデル パラメーターです
  }
}
```

- **出力:** 出力には、このメッセージが含まれている必要があります。

#### 音楽出力モード (`/generate/description-mode`)

- **生成:** `POST`
- **出力:** 音楽出力モードを無効にします。
- **出力:**

```json
{
  "model": {
    // schemas.DescriptionModeGenerateParam はモデル パラメーターです
  }
}
```

- **出力:** 出力には、このメッセージが含まれている必要があります。

#### 承認済み (`/feed/{aid}`)

- **承認済み:** `GET`
- **承認済み:** 承認済みの `aid` をアップロードしてください。
- ** パスパラメータ:**
- `aid` (パスパラメータ): `aid` を指定します。
- **コメント:** 必ずこのメッセージを送ってください。

#### 歌詞を生成する (`/generate/lyrics`)

- **管理者:** `POST`
- **アクション:** 歌詞を生成するプロンプトが表示されます。
