import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="OTP Verification", page_icon="🔐", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        color: #333;
    }
    .card {
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        text-align: center;
        font-size: 20px;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🔐 OTP Verification System</div>", unsafe_allow_html=True)
st.write("Secure your transaction with OTP verification.")

# Initialize session state
if "generated_otp" not in st.session_state:
    st.session_state.generated_otp = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Step 1: Enter Amount
amount = st.number_input("💰 Enter Amount to Send", min_value=0.0, step=1.0)

# Generate OTP Button
if st.button("📩 Generate OTP"):
    st.session_state.generated_otp = random.randint(100000, 999999)
    st.session_state.start_time = time.time()

    st.markdown(f"""
        <div class="card">
            🔐 Your OTP is: <strong>{st.session_state.generated_otp}</strong><br>
            ⏳ Valid for 10 seconds
        </div>
    """, unsafe_allow_html=True)

# OTP Input
user_otp = st.text_input("🔢 Enter OTP")

# Verify Button
if st.button("✅ Verify OTP"):

    if st.session_state.generated_otp is None:
        st.warning("⚠️ Please generate OTP first!")
    else:
        current_time = time.time()
        elapsed_time = current_time - st.session_state.start_time

        if elapsed_time > 10:
            st.error("❌ OTP Expired!")
        elif user_otp == str(st.session_state.generated_otp):
            st.success(f"✅ Amount ₹{amount} Sent Successfully!")
        else:
            st.error("❌ OTP Incorrect!")
