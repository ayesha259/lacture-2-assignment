import streamlit as st
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Expiry Date Tracker", page_icon="📦", layout="centered")

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #333;
    }
    .card {
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(135deg, #36d1dc, #5b86e5);
        color: white;
        text-align: center;
        font-size: 20px;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>📦 Expiry Date Tracker</div>", unsafe_allow_html=True)
st.write("Check whether your product is expired or still valid.")

# Input Section
st.subheader("📝 Enter Product Details")

manufacture_date = st.date_input("Select Manufacture Date")
validity_days = st.number_input("Enter Validity (in days)", min_value=1, step=1)

# Button
if st.button("🔍 Check Expiry Status"):
    
    # Calculate Expiry Date
    expiry_date = manufacture_date + timedelta(days=validity_days)
    today = datetime.today().date()

    is_expired = today > expiry_date

    # Display Result Card
    st.markdown(f"""
        <div class="card">
            <p><strong>Manufacture Date:</strong> {manufacture_date.strftime("%d %B %Y")}</p>
            <p><strong>Expiry Date:</strong> {expiry_date.strftime("%d %B %Y")}</p>
            <p><strong>Today's Date:</strong> {today.strftime("%d %B %Y")}</p>
        </div>
    """, unsafe_allow_html=True)

    if is_expired:
        st.error("❌ The product has EXPIRED!")
    else:
        st.success("✅ The product is still VALID!")
