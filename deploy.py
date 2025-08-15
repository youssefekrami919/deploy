import streamlit as st
import pandas as pd

# ================== DATA STORAGE ==================
# Initialize session state to store data
if "student_data" not in st.session_state:
    st.session_state.student_data = []
if "academic_data" not in st.session_state:
    st.session_state.academic_data = []
# ===================================================

# Sidebar Navigation
page = st.sidebar.selectbox("Navigation", ["Home", "Student", "Academic", "Data"])

# Home Page
if page == "Home":
    st.title("📌 Home Page")
    st.write("Welcome to the Student & Academic Data Collection System.")

# Student Page
elif page == "Student":
    st.title("🧑‍🎓 Student Page")
    name = st.text_input("Enter Student Name")
    student_id = st.text_input("Enter Student ID")

    if st.button("Save Student Data"):
        if name and student_id:
            st.session_state.student_data.append({"Name": name, "ID": student_id})
            st.success("✅ Student data saved successfully!")
        else:
            st.error("⚠️ Please fill both fields.")

# Academic Page
elif page == "Academic":
    st.title("📚 Academic Page")
    name = st.text_input("Enter Student Name")
    student_id = st.text_input("Enter Student ID")

    if st.button("Save Academic Data"):
        if name and student_id:
            st.session_state.academic_data.append({"Name": name, "ID": student_id})
            st.success("✅ Academic data saved successfully!")
        else:
            st.error("⚠️ Please fill both fields.")

# Data Page
elif page == "Data":
    st.title("📊 All Data Records")

    # Combine both Student and Academic into one table
    student_df = pd.DataFrame(st.session_state.student_data)
    academic_df = pd.DataFrame(st.session_state.academic_data)

    if not student_df.empty:
        student_df["Type"] = "Student"
    if not academic_df.empty:
        academic_df["Type"] = "Academic"

    combined_df = pd.concat([student_df, academic_df], ignore_index=True)

    if combined_df.empty:
        st.warning("⚠️ No data available yet.")
    else:
        st.dataframe(combined_df)
