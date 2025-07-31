import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Data Remover app",layout="wide")
st.title("📁File converter and Data Filter")
st.write("Upload your CSV and Excel files to Filter data and convert format")

File = st.file_uploader("Upload CSV or Excel files",type=["csv","xlsx"],accept_multiple_files=True)

if File:
    for files in File:
        extension = files.name.split(".")[-1]
        df = pd.read_csv(files) if extension == "csv" else pd.read_excel(files)


        st.subheader(f"{files.name} Preview Incoming")
        st.dataframe(df.head())
         

        if st.checkbox(f"Fill Missing values of {files.name}",help="Use if u have numeric values as Nan"):
            df.fillna(df.select_dtypes(include="number").mean(),inplace=True)
            st.success("Missed Numeric Values succesfully filled")
            st.dataframe(df.head())

        selected_cols = st.multiselect(f"Select Columns of file {files.name}",df.columns,default=df.columns)
        df=df[selected_cols]
        st.dataframe(df.head())

        if st.checkbox(f"Show chart",help="Works only if there are 2 colums or rows of numbers")and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])
        

        choice=st.radio(f"convert{files.name} to",["csv","Excel"],key=files.name)

        if st.button(f"Download {files.name} as {choice}"):
            output=BytesIO()
            #In-memory file to temporarily store CSV/Excel data
            if choice=="csv":
                df.to_csv(output,index=False)
                mime = "text/csv"
                new_name = files.name.replace(extension,"csv")
            else:
                df.to_excel(output,index=False)
                mime="application/vnd.openxmlformats-officedocument.spreadsheet.sheet"
                #Multipurpose Internet Mail Extensions
                new_name = files.name.replace(extension,"xlsx")
            
                output.seek(0)
                # Points at beginning
                st.write("Click The button to Download")
                sucess=st.download_button("Download",file_name=new_name,data=output,mime=mime)

                if sucess:
                    st.success("Download Succesfully done")

                