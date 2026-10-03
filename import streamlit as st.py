import streamlit as st

st.title("User Details Form")

name = st.text_input("Enter Name")
roll_no = st.text_input("Enter Roll Number")
branch = st.text_input("Enter Branch")
age = st.text_input("Enter Age")

if st.button("Submit"):
    if not name or not roll_no or not branch or not age:
        st.error("Please fill all the details.")
    elif not age.isdigit() or int(age) <= 0:
        st.warning("Please enter a valid age.")
    else:
        st.success("Details submitted successfully!")

        st.write("### User Details")
        st.write("Name:", name)
        st.write("Roll Number:", roll_no)
        st.write("Branch:", branch)
        st.write("Age:", age)