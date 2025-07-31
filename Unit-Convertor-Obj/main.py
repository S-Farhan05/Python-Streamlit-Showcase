import streamlit as st
def convert(value ,From ,To):
    conversions = {

        "Meter_KiloMeter" : 0.001,
        "KiloMeter_Meter" :1000,
        "Gram_KiloGram" : 0.001,
        "KiloGram_Gram" :1000,
    }

    key = f"{From}_{To}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    
    else:
        return "Sorry not Supported !! "

st.markdown(
    """
    <style>
  
    div[data-testid="stAppViewContainer"] h1 {
        color: red;
        text-align: center;
        font-size: 50px; /* example size */
        padding-bottom :20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title ("Unit Converter 📱")    


value =  st.number_input("Enter The Value to convert : ")
From = st.selectbox("Convert from",["Meter","KiloMeter","Gram","KiloGram"])
To = st.selectbox("Convert To",["KiloMeter","Meter","Gram","KiloGram"])


if st.button("Convert"):
    result = convert(value , From ,To)
    st.success(f"The converted value is  : {result}")


# st.markdown(
#     """
#     <style>
#     div[data-baseweb="select"] {  // test id for larger deeds / testbase for seelctbox
#       border: 2px solid green;
#       border-radius: 8px;
#       padding: 4px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )