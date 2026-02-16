import streamlit as st
from datetime import datetime, timedelta
import random
import time

# Page Config
st.set_page_config(page_title="Lecture 2 Assignment", page_icon="📚", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: #333;
        margin-bottom: 30px;
    }
    .balance-box {
        padding: 20px;
        border-radius: 15px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
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
    .otp-card {
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        text-align: center;
        font-size: 20px;
        margin-top: 20px;
    }
    .stButton>button {
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<div class='main-title'>📚 Lecture 2 Assignment</div>", unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "💳 E-Wallet",
    "💪 Gym Calculator",
    "📦 Expiry Tracker",
    "🔐 OTP Verification"
])

# ==================== TAB 1: E-WALLET ====================
with tab1:
    st.markdown("<h2 style='color: #333;'>💳 Simple E-Wallet</h2>", unsafe_allow_html=True)
    st.write("Manage your recharge and expenses easily!")
    
    wallet_balance = 0.0
    
    with st.container():
        st.subheader("💰 Recharge & Expenses")
        
        add_money = st.number_input("🔹 Add Money", min_value=0.0, step=1.0, key="wallet_add")
        
        col1, col2 = st.columns(2)
        with col1:
            food_expense = st.number_input("🍔 Food Expense", min_value=0.0, step=1.0, key="wallet_food")
            transport_expense = st.number_input("🚌 Transport Expense", min_value=0.0, step=1.0, key="wallet_transport")
        with col2:
            shopping_expense = st.number_input("🛍 Shopping Expense", min_value=0.0, step=1.0, key="wallet_shopping")
    
    if st.button("💳 Calculate Balance", key="wallet_calc"):
        wallet_balance += add_money
        wallet_balance -= food_expense
        wallet_balance -= transport_expense
        wallet_balance -= shopping_expense
        
        is_valid_balance = wallet_balance > 500 and wallet_balance < 5000
        
        st.markdown(f"""
            <div class="balance-box">
                Final Wallet Balance: ₹ {wallet_balance:.2f}
            </div>
        """, unsafe_allow_html=True)
        
        if is_valid_balance:
            st.success("✅ Balance is between 500 and 5000")
        else:
            st.error("❌ Balance is NOT between 500 and 5000")

# ==================== TAB 2: GYM MEMBERSHIP ====================
with tab2:
    st.markdown("<h2 style='color: #333;'>💪 Gym Membership Fee Calculator</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        registration_fee = st.number_input("Enter registration fee:", min_value=0.0, format="%.2f", key="gym_reg")
        monthly_fee = st.number_input("Enter monthly fee:", min_value=0.0, format="%.2f", key="gym_month")
    
    with col2:
        months = st.number_input("Enter number of months to pay for:", min_value=0, step=1, key="gym_months")
        coupon = st.radio("Do you have a discount coupon?", ("No", "Yes"), key="gym_coupon")
    
    if st.button("Calculate Total", key="gym_calc"):
        total_cost = registration_fee + (monthly_fee * months)
        
        if coupon == "Yes":
            discount_amount = total_cost * 0.10
            total_cost *= 0.90  # 10% discount
            st.markdown(f"""
                <div class="card" style='background: linear-gradient(135deg, #f093fb, #f5576c);'>
                    <p><strong>Registration Fee:</strong> ₹{registration_fee:.2f}</p>
                    <p><strong>Monthly Fee:</strong> ₹{monthly_fee:.2f} × {months} months = ₹{monthly_fee * months:.2f}</p>
                    <p><strong>Discount (10%):</strong> -₹{discount_amount:.2f}</p>
                    <hr style='border: 1px solid white;'>
                    <p><strong>Final Amount to be Paid: ₹{total_cost:.2f}</strong></p>
                </div>
            """, unsafe_allow_html=True)
            st.success("✅ 10% discount applied!")
        else:
            st.markdown(f"""
                <div class="card" style='background: linear-gradient(135deg, #4CAF50, #45a049);'>
                    <p><strong>Registration Fee:</strong> ₹{registration_fee:.2f}</p>
                    <p><strong>Monthly Fee:</strong> ₹{monthly_fee:.2f} × {months} months = ₹{monthly_fee * months:.2f}</p>
                    <hr style='border: 1px solid white;'>
                    <p><strong>Final Amount to be Paid: ₹{total_cost:.2f}</strong></p>
                </div>
            """, unsafe_allow_html=True)

# ==================== TAB 3: EXPIRY DATE TRACKER ====================
with tab3:
    st.markdown("<h2 style='color: #333;'>📦 Expiry Date Tracker</h2>", unsafe_allow_html=True)
    st.write("Check whether your product is expired or still valid.")
    
    st.subheader("📝 Enter Product Details")
    
    col1, col2 = st.columns(2)
    with col1:
        manufacture_date = st.date_input("📅 Select Manufacture Date", key="expiry_mfg")
    with col2:
        validity_days = st.number_input("📅 Enter Validity (in days)", min_value=1, step=1, key="expiry_valid")
    
    if st.button("🔍 Check Expiry Status", key="expiry_check"):
        expiry_date = manufacture_date + timedelta(days=validity_days)
        today = datetime.today().date()
        
        is_expired = today > expiry_date
        
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
            days_left = (expiry_date - today).days
            st.success(f"✅ The product is still VALID! ({days_left} days remaining)")

# ==================== TAB 4: OTP VERIFICATION ====================
with tab4:
    st.markdown("<h2 style='color: #333;'>🔐 OTP Verification System</h2>", unsafe_allow_html=True)
    st.write("Secure your transaction with OTP verification.")
    
    # Initialize session state
    if "generated_otp" not in st.session_state:
        st.session_state.generated_otp = None
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    
    col1, col2 = st.columns(2)
    
    with col1:
        amount = st.number_input("💰 Enter Amount to Send", min_value=0.0, step=1.0, key="otp_amount")
        
        if st.button("📩 Generate OTP", key="otp_gen"):
            st.session_state.generated_otp = random.randint(100000, 999999)
            st.session_state.start_time = time.time()
            
            st.markdown(f"""
                <div class="otp-card">
                    🔐 Your OTP is: <strong>{st.session_state.generated_otp}</strong><br>
                    ⏳ Valid for 10 seconds
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        user_otp = st.text_input("🔢 Enter OTP", key="otp_input")
        
        if st.button("✅ Verify OTP", key="otp_verify"):
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
