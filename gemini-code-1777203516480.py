import streamlit as st
import pandas as pd

# List of major Kenyan hubs for the selector
KENYA_LOCATIONS = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Thika", "Malindi", "Kitale"]

if 'job_database' not in st.session_state:
    st.session_state.job_database = []

st.title("📍 Local Business Network")

# SECTION: POST WITH LOCATION
with st.expander("➕ Post a Job with Location"):
    with st.form("job_form_location"):
        title = st.text_input("Job Title")
        location = st.selectbox("Select Business Location", KENYA_LOCATIONS)
        budget = st.number_input("Budget (KES)", min_value=0)
        details = st.text_area("Requirements")
        
        if st.form_submit_button("Post to Map"):
            new_job = {
                "Title": title,
                "Location": location,
                "Budget": budget,
                "Details": details
            }
            st.session_state.job_database.append(new_job)
            st.success(f"Job posted in {location}!")

# SECTION: SEARCH BY LOCATION
st.subheader("🔎 Find Jobs Near You")
target_city = st.selectbox("Filter by City", ["All"] + KENYA_LOCATIONS)

for job in reversed(st.session_state.job_database):
    if target_city == "All" or job['Location'] == target_city:
        with st.container():
            # Using your Blue and Pink theme for icons
            st.markdown(f"### 🔵 {job['Title']}")
            st.write(f"📍 **Location:** {job['Location']} | 💰 **Budget:** KES {job['Budget']:,}")
            st.write(job['Details'])
            st.button("Contact Business Owner", key=f"{job['Title']}_{job['Location']}")
            st.markdown("---")