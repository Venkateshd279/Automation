import streamlit as st

st.set_page_config(page_title="Mark Grade System", page_icon="📚")

# ── Title ──────────────────────────────────────────────────────────────────────
st.title("📚 School Mark Grade System")
st.write("Enter the student's name and marks to find their grade.")
st.divider()

# ── Helper function ────────────────────────────────────────────────────────────
def get_grade(mark):
    # Returns grade and remark based on the mark entered
    if mark >= 90:
        return "A+", "Outstanding 🌟"
    elif mark >= 80:
        return "A", "Excellent 🎉"
    elif mark >= 70:
        return "B", "Good 👍"
    elif mark >= 60:
        return "C", "Average 😊"
    elif mark >= 50:
        return "D", "Below Average ⚠️"
    else:
        return "F", "Fail ❌"

# ── Input Section ──────────────────────────────────────────────────────────────
student_name = st.text_input("Student Name")  # Text box for student name

# Number input — min 0, max 100
mark = st.number_input("Mark (out of 100)", min_value=0, max_value=100, step=1)

# ── Calculate Button ───────────────────────────────────────────────────────────
if st.button("Get Grade", use_container_width=True):

    # Validate that student name is not empty
    if not student_name.strip():
        st.warning("Please enter the student's name.")
    else:
        grade, remark = get_grade(mark)  # Call the function to get grade

        st.divider()

        # Show result
        st.subheader(f"Result for {student_name}")

        # Display mark, grade, remark side by side using 3 columns
        col1, col2, col3 = st.columns(3)
        col1.metric("Mark", f"{mark}/100")
        col2.metric("Grade", grade)
        col3.metric("Remark", remark)

# ── Grade Table ────────────────────────────────────────────────────────────────
st.divider()
st.subheader("📋 Grade Reference Table")

# Dictionary holding grade info — displayed as a table
grade_table = {
    "Marks Range": ["90 – 100", "80 – 89", "70 – 79", "60 – 69", "50 – 59", "0 – 49"],
    "Grade":       ["A+",       "A",        "B",        "C",        "D",        "F"],
    "Remark":      ["Outstanding", "Excellent", "Good", "Average", "Below Average", "Fail"],
}

st.table(grade_table)  # Renders the dictionary as a neat static table
