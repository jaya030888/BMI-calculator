import streamlit as st

st.title("Calculate Your BMI")

# n= st.number_input("enter")
# for i in range(1,11):
#   st.write(n,"x",i,"=",n*i)     

weight = st.number_input("Enter your weight in kilograms:")
height = st.number_input("Enter your height in meter")

if st.button('calculate'):
  BMI=weight/height**2
  st.write("Your BMI is",BMI)   