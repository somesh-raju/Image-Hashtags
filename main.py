import streamlit as st
import numpy as np

from PIL import Image
from cv2 import resize
from models import getHashtags

st.header("Get #ashtags from any image")
st.write("Choose any image and get hastags that you can use in your social network:")

uploaded_file = st.file_uploader("Choose an image...")

img_size = 200


if uploaded_file is not None:
    # src_image = load_image(uploaded_file)
    image = Image.open(uploaded_file)
    image = np.array(image, dtype=np.uint8)
    image = resize(image, (img_size, img_size))
    # image = np.expand_dims(image, 0)
    image = image / 255.0

    st.image(uploaded_file, caption='Input Image', use_column_width=True)

    st.write('Predicted Hashtags')
    with st.spinner('Wait for it...'):
        st.write(['#'+hashtag for hashtag in getHashtags(image)])
    st.success('Done!')

