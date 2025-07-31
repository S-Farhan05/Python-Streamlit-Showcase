import streamlit as st
def convert_unit(C , U ,V):
  if C == "Temperature":
      if U == "Celsius to Fahrenheit":
          ans = (V *(9/5))+32
          return ans
      elif U == "Celsius to Kelvin" :
          ans = V + 273.15
          return ans
      
      elif U == "Fahrenheit to Celsius" :
       ans = (V -32) *(5/9)
       return ans
        

        
      elif U == "Kelvin to celsius" :  
       ans = V - 273.15
      return ans
       

  if C == "Length":
     if U=="Kilometer to Meter":
        ans = V*1000
        return ans
     elif U == "Meter to Kilometer ":
        ans = V/1000
        return ans
     
    #  if i has array passed from function i can use strip

  if C == "Time":
     if U== "Days into Hours":
        ans = V* 60 
        return ans
     
     elif U== "Hours into Min":
        ans = V* 60 
        return ans
     
     elif U== "Min into Seconds":
        ans = V* 60 
        return ans
     
     elif U== "Hours into Sec":
        ans = V*60*60 
        return ans
 
  
      
 

st.title("📲 Unit Convertor Applicaton")
st.markdown("#### Convert Temperature , Length and Time units instantly")
st.write("🔨 Choose a Category ,enter the values and get converted numbers in real time ")
Category = st.selectbox("Choose a Category", ["Temperature" , "Length" ,"Time"])

if Category == "Temperature" :
    Unit = st.selectbox("Select the unit ❄",["Celsius to Fahrenheit","Celsius to Kelvin","Fahrenheit to Celsius" ,"Kelvin to celsius"])

elif Category =="Length" :
    Unit = st.selectbox("Select the unit 🧵" , ["Kilometer to Meter","Meter to Kilometer "])   
elif Category =="Time" :
    Unit = st.selectbox("Select the unit ⌛" , ["Days into Hours","Hours into Min","Min into Seconds","Hours into Sec"]) 

Value = st.number_input("Enter The Desired Value to convert")

if st.button("Convert") :
    Result = convert_unit(Category,Unit,Value)
    st.success(f"The result is : {Result:.3f}")



