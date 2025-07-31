import streamlit as st
from PIL import Image
import time
from PIL.ImageFilter import *
from io import BytesIO

# status = st.empty()
 
# status.text("Processing")
# time.sleep(3)
# status.text("Done")

st.set_page_config("Image Editor",layout="wide")
st.markdown("""
<h1 style="text-align:center; color:white; font-size:60px;">
    Image Editor Application📱
</h1>
""", unsafe_allow_html=True)
st.markdown("---")
image = st.file_uploader("Upload Any picture to edit and enhance",type=["jpg","png","svg","jpeg"])

mode = st.empty()
format = st.empty()
size = st.empty()
btn=st.button(" Description of image ")
if image:
    img=Image.open(image)
if btn and image:
    st.markdown(f"""<h6>Format : {img.format}</h6>""",unsafe_allow_html=True)
    st.markdown(f"""<h6>Width : {img.width}</h6>""",unsafe_allow_html=True)
    st.markdown(f"""<h6>Height : {img.height}</h6>""",unsafe_allow_html=True)
    st.markdown(f"""<h6>Mode : {img.mode}</h6>""",unsafe_allow_html=True)
elif btn:
    st.markdown("""<h6 style="margin-left: 5px; color:gray;">Input Image</h6>""",unsafe_allow_html=True) 

if image:
    st.markdown("""<h1 style = text-align:center;>Resizing</h1>""",unsafe_allow_html=True)
    width=st.number_input("Width",value=img.width)
    Height=st.number_input("Height",value=img.height)

    st.markdown("""<h1 style = text-align:center;>Rotation</h1>""",unsafe_allow_html=True)
    degree = st.number_input("Degrees")

    st.markdown("""<h1 style = text-align:center;>Filters</h1>""",unsafe_allow_html=True)
    filters=st.selectbox("Filters",options=("None","Blur","Details","Emboss","Smooth"))

    ebtn =st.button("Apply")
    if ebtn:
        E_image = img.resize((width,Height)).rotate(degree)
        # st.image(E_image, width=600)
        filtered = E_image
        if filters != "None":
            if filters =="Blur":
                filtered=E_image.filter(BLUR)
            elif filters =="Details":
                filtered=E_image.filter(DETAIL)
            elif filters =="Emboss":
                filtered=E_image.filter(EMBOSS)
            elif filters == "Smooth":
                filtered=E_image.filter(SMOOTH)


        col1 ,col2 = st.columns(2)

        with col1:
                st.markdown("**Original Image**")
                st.image(img, width=300)
        

        with col2:
             st.markdown("**Filtererd Image**")
             st.image(filtered, width=300)
        

        buf = BytesIO()
        filtered.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button("Download Edited Image", data=byte_im, file_name="edited.png", mime="image/png")

