＃＃＃ 关于

该存储库是从 [SunoAI-API](https://github.com/SunoAI-API/Suno-API) 分叉出来的，并由 [fswair](https://github.com/fswair) 开发/部署。

### FastAPI 实施文档

＃＃＃＃ 概述

此 FastAPI 实现提供了各种端点，例如创建音乐、接收源和管理用户会话。使用 CORS 和会话中间件安全地管理跨源请求和用户会话。

＃＃＃ 内容

## 手动验证

要手动进行身份验证，您必须在 json 参数的有效负载中添加一个字段，格式如下：

```
json={
 “数据”： {
 “cookie”：“字符串”，
 “session_id”：“字符串”
 },
 “模型”：{
 “字段”：值
 }
}
```

- [概述](#概述)
- [中间件配置](#middleware-configuration)
- [端点](#endpoints)
- [生成音乐 (`/generate`)](https://suno.tomris.dev/docs#/default/generate_generate_post)
- [使用描述模式生成音乐 (`/generate/description-mode`)](https://suno.tomris.dev/docs#/default/generate_with_song_description_generate_description_mode_post)
- [获取 Feed (`/feed/{aid}`)](https://suno.tomris.dev/docs#/default/fetch_feed_feed__aid__get)
- [生成歌词 (`/generate/lyrics`)](https://suno.tomris.dev/docs#/default/generate_lyrics_post_generate_lyrics__post)
- [获取歌词 (`/lyrics/{lid}`)](https://suno.tomris.dev/docs#/default/fetch_lyrics_lyrics__lid__get)
- [获取信用信息(`/get_credits`)](https://suno.tomris.dev/docs#/default/fetch_credits_get_credits_get)
- [重置凭证 (`/reset`)](https://suno.tomris.dev/docs#/default/reset_reset_get)
- [设置凭据 (GET) (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_get)
- [设置凭据 (POST) (`/setup`)](https://suno.tomris.dev/docs#/default/setup_setup_post)

### 中间件配置

```蟒蛇
应用程序.add_middleware(
 会话中间件，
 秘密密钥=秘密密钥，
 Same_site =“无”，
 最大年龄=86400 * 30,
 https_only=真，
 session_cookie=“会话”
）

应用程序.add_middleware(
 CORS中间件，
 允许起源=["*"],
 允许凭据=真，
 允许方法=["*"],
 允许标头=["*"],
）
```

此配置包括用于管理会话的“SessionMiddleware”和用于管理 CORS 设置的“CORSMiddleware”。

### 极值点

#### 主页 (`/`)

- **方法：** `GET`
- **描述：** 返回欢迎消息和会话状态。
- **请求参数：** 无
- **回答：**

```json
{
"message": "欢迎使用 Suno API",
“状态”：“活着”，
“用户”：{
"status": "已于 {date} 登录" 或 "尚未登录",
"uuid": "{uuid}",
"session_id": "{session_id}"
}
}
```

#### 生成音乐（`/generate`）

- **方法：** `POST`
- **描述：** 根据给定的模型参数创建音乐。
- **请求正文：**

```json
{
“模型”： {
//根据schemas.CustomModeGenerateParam模型参数
}
}
```

- **响应：** 返回创建的音乐或错误消息。

#### 使用描述模式生成音乐（`/generate/description-mode`）

- **方法：** `POST`
- **描述：** 根据歌曲描述创建音乐。
- **请求正文：**

```json
{
“模型”：{
//根据schemas.DescriptionModeGenerateParam模型参数
}
}
```

- **响应：** 返回创建的音乐或错误消息。

#### 获取 Feed (`/feed/{aid}`)

- **方法：** `GET`
- **描述：** 检索给定“aid”的提要。
- **请求参数：**
- `aid`（路径参数）：要接收的 feed 的 `aid`。
- **响应：** 返回提要数据或错误消息。

#### 生成歌词 (`/generate/lyrics`)

- **方法：** `POST`
- **描述：** 根据给定的提示创建歌词。
