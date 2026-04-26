import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Business Hub", page_icon="💼", layout="wide")

# --- CUSTOM STYLING (Pink, Blue, White) ---
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    .stButton>button { background-color: #0000FF; color: white; border-radius: 10px; }
    .stTextInput>div>div>input { border-color: #FFC0CB; }
    h1 { color: #0000FF; }
    </style>
    """, unsafe_allow_code=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Login", "Job Board", "Business Calculator", "Map View"])

# --- LOGIN PAGE ---
if page == "Login":
    st.title("🔑 Business Login")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success(f"Welcome back, {user}!")

# --- JOB BOARD ---
elif page == "Job Board":
    st.title("💼 Job Marketplace")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Post a Job")
        job_title = st.text_input("Job Title")
        job_desc = st.text_area("Description")
        if st.button("Post Job"):
            st.balloons()
            st.write("Job posted successfully!")

    with col2:
        st.subheader("Available Jobs")
        st.info("Project Manager needed for Nairobi startup")
        st.info("Cybersecurity Consultant - Remote")

# --- MATH CALCULATOR ---
elif page == "Business Calculator":
    st.title("🧮 Profit Calculator")
    revenue = st.number_input("Total Revenue", min_value=0)
    expenses = st.number_input("Total Expenses", min_value=0)
    if st.button("Calculate Profit"):
        profit = revenue - expenses
        st.write(f"### Your Net Profit: {profit}")

# --- MAP VIEW ---
elif page == "Map View":
    st.title("📍 Business Map")
    st.write("Finding business partners near you...")
    # Placeholder for actual map data
    st.map()