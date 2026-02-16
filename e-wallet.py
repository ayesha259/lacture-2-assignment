import streamlit as st

# Page Config
st.set_page_config(page_title="E-Wallet App", page_icon="💳", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
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
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #333;'>💳 Simple E-Wallet</h1>", unsafe_allow_html=True)
st.write("Manage your recharge and expenses easily!")

# Initialize balance
wallet_balance = 0.0

# Card-style input section
with st.container():
    st.subheader("💰 Recharge & Expenses")

    add_money = st.number_input("🔹 Add Money", min_value=0.0, step=1.0)
    
    col1, col2 = st.columns(2)
    with col1:
        food_expense = st.number_input("🍔 Food Expense", min_value=0.0, step=1.0)
        transport_expense = st.number_input("🚌 Transport Expense", min_value=0.0, step=1.0)
    with col2:
        shopping_expense = st.number_input("🛍 Shopping Expense", min_value=0.0, step=1.0)

# Button
if st.button("💳 Calculate Balance"):
    # Using assignment operators
    wallet_balance += add_money
    wallet_balance -= food_expense
    wallet_balance -= transport_expense
    wallet_balance -= shopping_expense

    # Logical condition
    is_valid_balance = wallet_balance > 500 and wallet_balance < 5000

    # Display Result
    st.markdown(f"""
        <div class="balance-box">
            Final Wallet Balance: ₹ {wallet_balance:.2f}
        </div>
    """, unsafe_allow_html=True)

    if is_valid_balance:
        st.success("✅ Balance is between 500 and 5000")
    else:
        st.error("❌ Balance is NOT between 500 and 5000")
