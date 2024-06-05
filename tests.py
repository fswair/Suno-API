import json
import os
import time
import requests
import pathlib

base_endpoint: str = "http://127.0.0.1:8000"

def test_generate_music():
    data = {
        "prompt": "[Verse]\nWake up in the morning, feeling brand new\nGonna shake off the worries, leave 'em in the rearview\nStep outside, feeling the warmth on my face\nThere's something 'bout the sunshine that puts me in my place\n\n[Verse 2]\nWalking down the street, got a spring in my step\nThe rhythm in my heart, it just won't forget\nEverywhere I go, people smiling at me\nThey can feel the joy, it's contagious, can't you see?\n\n[Chorus]\nI got sunshine in my pocket, happiness in my soul\nA skip in my stride, and I'm ready to go\nNothing gonna bring me down, gonna keep on shining bright\nI got sunshine in my pocket, this world feels so right",
        "tags": "heartfelt anime",
        "mv": "chirp-v3-0",
        "title": "Sunshine in your Pocket",
        "continue_clip_id": None,
        "continue_at": None,
    }

    r = requests.post(
        f"{base_endpoint.strip('/')}/generate/description-mode", data=json.dumps(data)
    )

    resp = r.text
    print(resp)
    return resp


def test_generate_music_with_description():
    data = {
        "gpt_description_prompt": "A Blues song about a person who is feeling happy and optimistic about the future.",
        "make_instrumental": False,
        "mv": "chirp-v3-0",
    }

    r = requests.post(f"{base_endpoint.strip('/')}/generate", data=json.dumps(data))

    resp = r.text
    print(resp)
    return resp


def test_generate_lyrics():
    data = {"prompt": ""}

    r = requests.post(f"{base_endpoint.strip('/')}/generate/lyrics/", data=json.dumps(data))
    print(r.text)
    return r.text


def get_lyrics(lid: str):
    r = requests.get(f"{base_endpoint.strip('/')}/lyrics/{lid}")
    print(r.text)


def get_info(aid: str):
    response = requests.get(f"{base_endpoint.strip('/')}/feed/{aid}")

    data = json.loads(response.text)[0]

    return data["audio_url"], data["metadata"]


def save_song(aid: str, output_path: str = "output"):
    start_time = time.time()
    while True:
        audio_url, metadata = get_info(aid)
        if audio_url:
            break
        elif time.time() - start_time > 90:
            raise TimeoutError("Failed to get audio_url within 90 seconds")
        time.sleep(30)
    response = requests.get(audio_url, allow_redirects=False, stream=True)
    if response.status_code != 200:
        raise Exception("Could not download song")
    index = 0
    while os.path.exists(os.path.join(output_path, f"suno_{index}.mp3")):
        index += 1
    path = os.path.join(output_path, f"suno_{index}.mp3")
    with open(path, "wb") as output_file:
        for chunk in response.iter_content(chunk_size=1024):
            # If the chunk is not empty, write it to the file.
            if chunk:
                output_file.write(chunk)
    return pathlib.Path(output_path)