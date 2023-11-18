import requests
import streamlit as st
API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}
st.title("App for Image Generation")
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
inputdata=st.text_input("Enter Your Input Data")
bt=st.button("Submit")
if bt :
    image_bytes = query({
        "inputs": inputdata,
    })
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    images = Image.open(io.BytesIO(image_bytes))
    st.image(images)