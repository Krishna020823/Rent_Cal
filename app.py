# filepath: c:\Users\krishna.4.yadav\OneDrive - Coforge Limited\Desktop\Krishna Code\Rent_Cal-main\app.py
import streamlit as st

st.title("Rent Calculator")
st.write("If you see this text, Streamlit is working!")

rent = st.number_input("Hostel/flat rent", min_value=0)
food = st.number_input("Food expenses", min_value=0)
electricity_spend = st.number_input("Electricity units", min_value=0)
charge_per_unit = st.number_input("Charge per unit", min_value=0)
persons = st.number_input("Number of persons", min_value=1)

if st.button("Calculate"):
    total_bill = electricity_spend * charge_per_unit
    output = (food + rent + total_bill) // persons
    st.success(f"Each person's share is: {output}")