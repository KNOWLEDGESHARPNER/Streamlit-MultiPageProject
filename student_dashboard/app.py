import streamlit as st
import pandas as pd
import numpy as np
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Student Dashboard",
    page_icon=":mortar_board:", 
    initial_sidebar_state="collapsed",
    layout="centered"
)

# --- HELPER: Path Resolution ---
# This ensures images are found on Streamlit Cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "images", "student.jpg")

# --- HEADER ---
st.title("Student Dashboard")
st.header("Welcome, Ashwath!") 
st.subheader("Access your academic resources and personal profile below.")

st.divider()

# --- PERSONAL INFORMATION SECTION ---
st.markdown("### 👤 Personal Information")

col1, col2 = st.columns([1, 1.5], gap="medium")

with col1:
    # Display Profile Image
    if os.path.exists(image_path):
        st.image(image_path, caption="Profile Photo", width=250)
    else:
        st.info("Upload 'student.jpg' to the images folder to see your profile photo.")
    
with col2:
    st.write("**Name:** Ashwath M Shetty")
    st.write("**Role:** Master Trainer (Full Stack)")
    st.write("**Location:** Karnataka, India")
    
    # Voice Inputs
    st.info("Voice Registration")
    name_audio = st.audio_input("Verify Name via Voice")
    roll_audio = st.audio_input("Verify Roll Number", key="roll_number")

st.divider()

# --- MEDIA SECTION ---
st.markdown("### 📹 Multimedia Resources")

tab1, tab2, tab3 = st.tabs(["Intro Video", "External Reference", "Audio Message"])

with tab1:
    # Using local video path
    video_path = os.path.join(current_dir, "videos", "Ashwath M.mp4")
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.warning("Local video file not found.")

with tab2:
    st.video("https://youtu.be/D1eL1EnxXXQ?si=sjiUhctRx-8oQig6")

with tab3:
    audio_path = os.path.join(current_dir, "audios", "sample.mp3")
    if os.path.exists(audio_path):
        st.audio(audio_path, start_time=0)
    else:
        st.write("Audio sample unavailable.")

st.divider()

# --- FILE UPLOADS ---
st.markdown("### 📂 Upload Center")

# Video Submission
intro_video = st.file_uploader(
    "Submit your Introduction Video",
    type=["mp4", "mov", "avi"],
    key="intro_video"
)
if intro_video:
    st.video(intro_video)

# CSV Data Handling
student_details = st.file_uploader("Upload Academic Records (CSV)", type=["csv"], key="student_details")
if student_details is not None:
    df = pd.read_csv(student_details)
    st.success("Data loaded successfully!")
    
    with st.expander("View Full Records"):
        st.dataframe(df, use_container_width=True)
    
    # Simple Visualization if data exists
    if not df.empty:
        st.write("**Data Preview:**")
        st.line_chart(df.select_dtypes(include=[np.number]))