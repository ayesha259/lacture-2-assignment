import streamlit as st

st.title("Gym Membership Fee Calculator")

# Inputs
registration_fee = st.number_input("Enter registration fee:", min_value=0.0, format="%.2f")
monthly_fee = st.number_input("Enter monthly fee:", min_value=0.0, format="%.2f")
months = st.number_input("Enter number of months to pay for:", min_value=0, step=1)

coupon = st.radio("Do you have a discount coupon?", ("No", "Yes"))

# Calculate button
if st.button("Calculate Total"):
    total_cost = registration_fee + (monthly_fee * months)
    
    if coupon == "Yes":
        total_cost *= 0.90  # 10% discount
    
    st.success(f"Final amount to be paid: {total_cost:.2f}")
