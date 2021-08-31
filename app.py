import streamlit as st
import requests
import base64
import json
from PIL import Image
from io import BytesIO


def send_request(text, num_images):
    headers = {
        'Content-Type': 'application/json',
    }

    data = {"text": text, "num_images": num_images}

    response = requests.post('https://main-dalle-server-scy6500.endpoint.ainize.ai/generate', headers=headers,
                             data=json.dumps(data))
    status_code = response.status_code

    return status_code, response

st.title("DALL-E Pytorch Demo")
st.header("Creating Images from Text")

num_images = st.sidebar.slider("Number of images you want", 1, 4)

text = st.text_input("Text for the image you want to create", "snow located on the grand canyon.")
if st.button("Generate"):
    t = st.empty()
    result = []
    t.markdown("Generating...")
    status_code, response = send_request(text, num_images)
    if status_code == 200:
        prediction = response.json()
        for base64_image in prediction:
            result.append(Image.open(BytesIO(base64.b64decode(base64_image))))
        st.image(result, width=300)
    else:
        st.error(str(status_code) + " Error")
    t.markdown("")
