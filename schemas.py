# -*- coding:utf-8 -*-

from typing import Any, Optional
from pydantic import BaseModel, Field

class Response(BaseModel):
    code: Optional[int] = 0
    msg: Optional[str] = "success"
    data: Optional[Any] = None

class CustomModeGenerateParam(BaseModel):
    """Generate with Custom Mode"""

    prompt: str = Field(..., description="lyrics")
    mv: str = Field(
        ...,
        description="model version, default: chirp-v3-0",
        examples=["chirp-v3-0"],
    )
    title: str = Field(..., description="song title")
    tags: str = Field(..., description="style of music")
    continue_at: Optional[int] = Field(
        default=None,
        description="continue a new clip from a previous song, format number",
        examples=[120],
    )
    continue_clip_id: Optional[str] = None

class DescriptionModeGenerateParam(BaseModel):
    """Generate with Song Description"""

    gpt_description_prompt: str
    make_instrumental: bool = False
    mv: str = Field(
        default='chirp-v3-0',
        description="model version, default: chirp-v3-0",
        examples=["chirp-v3-0", "chirp-v3-5"],
    )
    
    prompt: str = Field(
        default="",
        description="Placeholder, keep it as an empty string, do not modify it",
    )

class LyricsGenerateParam(BaseModel):
    """Generate Lyrics"""

    prompt: str = Field(..., description="lyrics")

class Credentials(BaseModel):
    """Credentials"""

    cookie: Optional[str] = Field(default=None, description="cookie")
    session_id: Optional[str] = Field(default=None, description="session_id")