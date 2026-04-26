import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize a 'database' in the app's memory to store jobs
if 'job_database' not in st.session_state:
    st.session_state.job_database = []

st.title("💼 Professional Job Exchange")
st.markdown("---")

# SECTION 1: POST A JOB
with st.expander("➕ Post a New Job Opening"):
    with st.form("job_form"):
        title = st.text_input("Job Title (e.g., Marketing Consultant)")
        category = st.selectbox("Industry", ["Technology", "Agriculture", "Finance", "Retail", "Construction"])
        budget = st.number_input("Budget/Salary (KES)", min_value=0)
        description = st.text_area("Job Requirements & Details")
        
        submit_button = st.form_submit_button("Broadcast to Network")
        
        if submit_button:
            if title and description:
                new_job = {
                    "Date": datetime.now().strftime("%Y-%m-%d"),
                    "Title": title,
                    "Category": category,
                    "Budget": budget,
                    "Description": description
                }
                # Add to our memory
                st.session_state.job_database.append(new_job)
                st.success("Your job post is live!")
            else:
                st.error("Please fill in the Title and Description.")

# SECTION 2: FIND A JOB
st.subheader("🔍 Available Opportunities")

# Filtering Logic
search_query = st.text_input("Search by keyword...")
filter_cat = st.multiselect("Filter by Industry", ["Technology", "Agriculture", "Finance", "Retail", "Construction"])

# Displaying the Jobs
if not st.session_state.job_database:
    st.info("No jobs posted yet. Be the first to post!")
else:
    # Reverse the list so the newest jobs are at the top
    for job in reversed(st.session_state.job_database):
        # Apply filters
        if search_query.lower() in job['Title'].lower() or not search_query:
            if not filter_cat or job['Category'] in filter_cat:
                with st.container():
                    st.markdown(f"### {job['Title']}")
                    col1, col2, col3 = st.columns(3)
                    col1.write(f"📅 **Date:** {job['Date']}")
                    col2.write(f"🏷️ **Category:** {job['Category']}")
                    col3.write(f"💰 **Budget:** KES {job['Budget']:,}")
                    st.write(job['Description'])
                    if st.button(f"Apply for {job['Title']}", key=job['Title']+job['Date']):
                        st.success("Application sent to the employer!")
                    st.markdown("---")