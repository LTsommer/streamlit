from distutils.command.upload import upload
import streamlit as st
import cv2
import numpy as np

st.title("iconWiki")
upload_file = st.file_uploader('upload pics', type="jpg")

if upload_file is not None:
    file_bytes = np.asarray(bytearray(upload_file.read()))
    img = cv2.imdecode(file_bytes, 1)
    st.image(img,channels="BGR")

icon_list = ['air conditioner','rice cooker','water heater','zyx']

new_content = st.text_input('add new content',value='')
if st.button('add new content'):
    icon_list.append(new_content)

icon_type = st.sidebar.selectbox(
    "icon content", 
    icon_list
)

if icon_type == 'air conditioner':
    img=cv2.imread('1.png')
    st.image(img,channels="BGR")
elif icon_type == 'rice cooker':
    img=cv2.imread('2.png')
    st.image(img,channels="BGR")
elif icon_type == 'water heater':
    img=cv2.imread('3.png')
    st.image(img,channels="BGR")
elif icon_type == 'zyx':
    img=cv2.imread('1.jpg')
    st.image(img,channels="BGR")


