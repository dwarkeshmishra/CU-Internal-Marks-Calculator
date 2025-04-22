import streamlit as st

# Page configuration
st.set_page_config(page_title="CU Internal Marks Calculator", layout="wide")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Enhanced CSS for better UI
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        h1, h2, h3 {
            color: #003366;
        }
        .stButton button {
            background-color: #003366;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
        }
        .card {
            padding: 1.5rem;
            border-radius: 10px;
            background-color: rgba(0, 51, 102, 0.03);
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .card:hover {
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        .info-card {
            padding: 1rem;
            border-radius: 8px;
            background-color: #e6f3ff;
            margin-bottom: 1rem;
        }
        .landing-card {
            padding: 2.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin: 2rem 0;
            color: white;
            background-image: url('https://images.shiksha.com/mediadata/images/1737955070phpUHYysj.jpeg');
            background-size: cover;
            background-position: center;
            position: relative;
            min-height: 350px;
        }
        .landing-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
            z-index: 0;
        }
        .landing-card h2, .landing-card p, .landing-card ul {
            position: relative;
            z-index: 1;
            color: white;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
        }
        .landing-card h2 {
            color: white;
            margin-bottom: 1.5rem;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin: 2rem 0;
        }
        .image-container img {
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            max-width: 100%;
        }
        .footer {
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
            color: #003366;
            border-top: 1px solid #e0e0e0;
        }
        /* Input field styling */
        input[type="text"] {
            width: 100%;
            border-radius: 5px;
            border: 1px solid #ccd0d5;
            padding: 8px 12px;
            transition: all 0.3s;
        }
        input[type="text"]:focus {
            border-color: #003366;
            box-shadow: 0 0 0 2px rgba(0, 51, 102, 0.2);
            outline: none;
        }
        /* Card headers */
        .card-header {
            color: #003366;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid rgba(0, 51, 102, 0.1);
        }
        /* Section headers */
        .section-header {
            margin-bottom: 1.5rem;
            color: #003366;
            padding-bottom: 0.5rem;
            width: fit-content;
        }
    </style>
""", unsafe_allow_html=True)

# Helper function to safely convert input to float
def safe_float(value, max_val):
    if not value:
        return 0
    try:
        val = float(value)
        return min(max_val, max(0, val))  # Ensure value is within bounds
    except ValueError:
        return 0

# App title
st.title("🎓 CU Internal Marks Calculator")

# Navigation bar
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Home", use_container_width=True, type="primary" if st.session_state.page == "home" else "secondary"):
        st.session_state.page = "home"
        st.rerun()
with col2:
    if st.button("🔬 Hybrid Subject", use_container_width=True, type="primary" if st.session_state.page == "practical" else "secondary"):
        st.session_state.page = "practical"
        st.rerun()
with col3:
    if st.button("📚 Theory Subject", use_container_width=True, type="primary" if st.session_state.page == "theory" else "secondary"):
        st.session_state.page = "theory"
        st.rerun()

# Home/Landing Page
if st.session_state.page == "home":
    st.markdown("""
        <div class="landing-card">
            <h2>Welcome to CU Internal Marks Calculator</h2>
            <p>This tool helps Chandigarh University students calculate their internal marks for both practical and theory subjects.</p>
            <ul>
                <li>Calculate hybrid subject marks (out of 70)</li>
                <li>Calculate theory subject marks (out of 40)</li>
                <li>Get instant results based on your performance</li>
            </ul>
            <p>Choose from the navigation bar above to get started!</p>
        </div>
    """, unsafe_allow_html=True)

# Practical Subject Calculator (now Hybrid)
elif st.session_state.page == "practical":
    st.markdown('<h2 class="section-header">Hybrid Subject Marks Calculator (Out of 70)</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h3 class="card-header">🔍 Enter Practical Marks</h3>', unsafe_allow_html=True)
    st.markdown('<p>10 Practicals, each out of 30 marks</p>', unsafe_allow_html=True)
    
    cols = st.columns(5)
    practicals = []
    for i in range(10):
        with cols[i % 5]:
            practicals.append(st.text_input(f"Practical {i+1}", key=f"prac_{i}", 
                                        help=f"Enter a value between 0 and 30"))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h3 class="card-header">📊 Other Assessment Components</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        assignment = st.text_input("📄 Assignment (out of 10)", key="p_assignment", help="Enter a value between 0 and 10")
        quiz = st.text_input("🧠 Quiz (out of 4)", key="p_quiz", help="Enter a value between 0 and 4")
        surprise = st.text_input("🎁 Surprise Test (out of 12)", key="p_surprise", help="Enter a value between 0 and 12")
        mst1 = st.text_input("📝 MST 1 (out of 20)", key="p_mst1", help="Enter a value between 0 and 20")
    
    with col2:
        mst2 = st.text_input("📝 MST 2 (out of 20)", key="p_mst2", help="Enter a value between 0 and 20")
        labMST = st.text_input("🔬 Lab MST (out of 10)", key="p_labMST", help="Enter a value between 0 and 10")
        attendance = st.text_input("📅 Attendance (out of 2)", key="p_attendance", help="Enter a value between 0 and 2")
        endTerm = st.text_input("🔚 End Term Practical (out of 40)", key="p_endTerm", help="Enter a value between 0 and 40")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🧮 Calculate Practical Internal Marks", key="calc_practical", use_container_width=True):
            # Convert text inputs to numbers safely
            practical_values = [safe_float(p, 30) for p in practicals]
            assignment_val = safe_float(assignment, 10)
            quiz_val = safe_float(quiz, 4)
            surprise_val = safe_float(surprise, 12)
            mst1_val = safe_float(mst1, 20)
            mst2_val = safe_float(mst2, 20)
            labMST_val = safe_float(labMST, 10)
            attendance_val = safe_float(attendance, 2)
            endTerm_val = safe_float(endTerm, 40)
            
            # Calculate scores
            practicalsScore = sum([(p / 30.0) * 2.0 for p in practical_values])
            assignmentScore = (assignment_val / 10.0) * 6.0
            quizScore = (quiz_val / 4.0) * 4.0
            surpriseScore = (surprise_val / 12.0) * 4.0
            mst1Score = (mst1_val / 20.0) * 5.0
            mst2Score = (mst2_val / 20.0) * 5.0
            labMSTScore = (labMST_val / 10.0) * 4.0
            attendanceScore = (attendance_val / 2.0) * 2.0
            endTermScore = (endTerm_val / 40.0) * 20.0

            total = practicalsScore + assignmentScore + quizScore + surpriseScore + \
                    mst1Score + mst2Score + labMSTScore + attendanceScore + endTermScore

            st.success(f"✅ Total Practical Internal Marks: {total:.2f} / 70")
            
            # Show breakdown
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.subheader("Marks Breakdown")
            breakdown_col1, breakdown_col2 = st.columns(2)
            
            with breakdown_col1:
                st.write(f"Practicals: {practicalsScore:.2f} / 20")
                st.write(f"Assignment: {assignmentScore:.2f} / 6")
                st.write(f"Quiz: {quizScore:.2f} / 4")
                st.write(f"Surprise Test: {surpriseScore:.2f} / 4")
                st.write(f"MST 1: {mst1Score:.2f} / 5")
                
            with breakdown_col2:
                st.write(f"MST 2: {mst2Score:.2f} / 5")
                st.write(f"Lab MST: {labMSTScore:.2f} / 4")
                st.write(f"Attendance: {attendanceScore:.2f} / 2")
                st.write(f"End Term: {endTermScore:.2f} / 20")
                
            st.markdown('</div>', unsafe_allow_html=True)

# Theory Subject Calculator
elif st.session_state.page == "theory":
    st.markdown('<h2 class="section-header">Theory Subject Marks Calculator (Out of 40)</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h3 class="card-header">📊 Assessment Components</h3>', unsafe_allow_html=True)
    st.markdown('<p>Enter your marks for each component to calculate your theory internal marks</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        mst1 = st.text_input("📝 MST 1 (out of 20)", key="t_mst1", help="Enter a value between 0 and 20")
        mst2 = st.text_input("📝 MST 2 (out of 20)", key="t_mst2", help="Enter a value between 0 and 20")
        assignment = st.text_input("📄 Assignment (out of 10)", key="t_assignment", help="Enter a value between 0 and 10")
        
    with col2:
        quiz = st.text_input("🧠 Quiz (out of 4)", key="t_quiz", help="Enter a value between 0 and 4")
        surprise = st.text_input("🎁 Surprise Test (out of 12)", key="t_surprise", help="Enter a value between 0 and 12")
        attendance = st.text_input("📅 Attendance (out of 2)", key="t_attendance", help="Enter a value between 0 and 2")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🧮 Calculate Theory Internal Marks", key="calc_theory", use_container_width=True):
            # Convert text inputs to numbers safely
            mst1_val = safe_float(mst1, 20)
            mst2_val = safe_float(mst2, 20)
            assignment_val = safe_float(assignment, 10)
            quiz_val = safe_float(quiz, 4)
            surprise_val = safe_float(surprise, 12)
            attendance_val = safe_float(attendance, 2)
            
            # Calculate scores
            mst1Score = (mst1_val / 20.0) * 10.0
            mst2Score = (mst2_val / 20.0) * 10.0
            assignmentScore = assignment_val
            quizScore = quiz_val
            surpriseScore = (surprise_val / 12.0) * 4.0
            attendanceScore = attendance_val

            total = mst1Score + mst2Score + assignmentScore + quizScore + surpriseScore + attendanceScore

            st.success(f"✅ Total Theory Internal Marks: {total:.2f} / 40")
            
            # Show breakdown
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.subheader("Marks Breakdown")
            breakdown_col1, breakdown_col2 = st.columns(2)
            
            with breakdown_col1:
                st.write(f"MST 1: {mst1Score:.2f} / 10")
                st.write(f"MST 2: {mst2Score:.2f} / 10")
                st.write(f"Assignment: {assignmentScore:.2f} / 10")
                
            with breakdown_col2:
                st.write(f"Quiz: {quizScore:.2f} / 4")
                st.write(f"Surprise Test: {surpriseScore:.2f} / 4")
                st.write(f"Attendance: {attendanceScore:.2f} / 2")
                
            st.markdown('</div>', unsafe_allow_html=True)

# Footer text
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("© 2025 Chandigarh University Internal Marks Calculator. Developed with ❤️ for CU students.", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
