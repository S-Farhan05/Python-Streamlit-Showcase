import streamlit as st
import re

st.set_page_config("Seo optimizer",layout="wide")
st.markdown("""
<h1 style="text-align:center; color:gray; font-size:60px;">
    Density Checker
</h1>
""", unsafe_allow_html=True)
st.markdown("""<hr style='border: 1px solid gray; width: 70%; margin: auto;'>""", unsafe_allow_html=True)


st.subheader("An online Application used to detact keywords and optimize paragraphs for best using seo optimizing and practicing")

text = st.text_area("Paragraph",width=500)
word_dict = dict()
col1,col2,col3 = st.columns(3)
if text:
    
    col1.markdown("""<h3>Words</h3>""",unsafe_allow_html=True)
    col2.markdown("""<h3>Value</h3>""",unsafe_allow_html=True)
    col3.markdown("""<h3>Percentage</h3>""",unsafe_allow_html=True)
    sim_text = re.sub("[!@$%,.?&*()-=+_/';:\|@`]","",text)
    words=sim_text.lower().split(" ")
    t_word = len(words)
    for word in words:
        if word in word_dict:
            word_dict[word]=word_dict[word]+1
        else:
            word_dict[word]=1

    keys = list(word_dict.keys())
    values = list(word_dict.values())

    
    for i in range(len(keys)):
        col1.markdown(f"""<h5>{keys[i]}</h5>""",unsafe_allow_html=True)
        col2.markdown(f"""<h5>{values[i]}</h5>""",unsafe_allow_html=True)
        col3.markdown(f"""<h5>{round((values[i]/ t_word)*100)}%</h5>""",unsafe_allow_html=True)
