import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("""<h1 style=text-aligned:centered;color:red>Web Scrapper Application</h1> """,unsafe_allow_html=True)
# st.image("https://images.unsplash.com/photo-1704340142770-b52988e5b6eb")

with st.form("Searching"):
    Input=st.text_input("Search the Web")
    submit= st.form_submit_button("Search")
    if submit:
        res = requests.get(f"https://unsplash.com/s/photos/{Input}")
        soup=BeautifulSoup(res.content ,"lxml")
        rows = soup.find_all("img")
        print(len(rows))
        st.write(res.status_code)
        st.code(soup.prettify())
       