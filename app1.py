import streamlit as st

# Ui Components - Display Elements Text and formatting
st.title("Welcome to the Student Dashboard")
st.header("This is a simple dashboard for students to manage their courses and assignments.")
st.subheader("Student Dashboard Features:")
st.markdown("<h1 style='color: blue;'>Course Management</h1><p> add, remove, and view your courses.</p>", unsafe_allow_html=True)
st.text("Easily add, remove, and view your courses.")

# Data Display Elements - Tables and metrics
st.subheader("Course List")
courses = ["Math 101", "History 202", "Science 303","Computer Science 404"]
st.table(courses,border=True,width="content")
st.subheader("Assignment Metrics")
marks={"Math 101": 85, "History 202": 90, "Science 303": 78,"Computer Science 404":92}
st.table(marks,border="horizontal",width="content",)

student_marks={"Maths":[85, 90, 78], "History":[90, 92, 88], "Science":[78, 80, 82],"Computer Science":[92, 95, 94]}
st.table(student_marks,border="horizontal",width="content",)
st.subheader("Overall Performance")
average_mark = sum(marks.values()) / len(marks)
st.metric("Average Mark", f"{average_mark:.4f}")
st.metric("Total Courses", len(courses))    
st.text(f"Average Mark: {average_mark:.4f}")

# reading and displaying JSON data
data={
    "name": "John Doe",
    "age": 25,
    "email": "john.doe@example.com",
    "courses": ["Math 101", "History 202", "Science 303","Computer Science 404"]
}
st.json(data)

# Interactive Elements - Buttons and forms and input fields
st.subheader("Course Registration")
name = st.text_input("Name")
courses = st.multiselect("Select Courses", ["Math 101", "History 202", "Science 303","Computer Science 404"])
Email = st.text_input("Email")
start_date = st.date_input("Start Date")
schedule_Time = st.time_input("Schedule Time")
Enter_Comments = st.text_area("Enter Comments")
rate_course = st.slider("Rate the Course", 1, 5)
selected_range = st.select_slider("Select a range of marks", options=[0, 50, 60, 70, 80, 90, 100])
terms_accepted = st.checkbox("I accept the terms and conditions to enroll in the course")
if st.button("Submit Registration"):
    if not name or not Email or not courses:
        st.error("Please fill in all required fields (Name, Email, and Courses).")
    elif not terms_accepted:
        st.error("Please accept the terms and conditions to enroll in the course.")
    else:
        st.success(f"Registration submitted for {name} with email {Email} and courses {', '.join(courses)}.")
        st.balloons()
        st.snow()