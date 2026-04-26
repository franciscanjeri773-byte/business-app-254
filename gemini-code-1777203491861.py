import streamlit as st

# --- SECTION: TRANSACTION LINK ---
st.header("💸 Secure Business Payments")
with st.container():
    st.markdown("""
        <div style="background-color: #FFC0CB; padding: 15px; border-radius: 10px;">
            <h4 style="color: #0000FF;">Lipa na M-Pesa Gateway</h4>
        </div>
    """, unsafe_allow_code=True)
    
    phone = st.text_input("Enter M-Pesa Phone Number (e.g., 0712...)", placeholder="07XXXXXXXX")
    amount = st.number_input("Amount to Send (KES)", min_value=1)
    
    if st.button("Initiate Transaction"):
        if len(phone) >= 10:
            st.info(f"Sending STK Push to {phone} for KES {amount}...")
            st.success("✔ Request Sent! Please enter your PIN on your phone.")
        else:
            st.error("Please enter a valid phone number.")

st.markdown("---")

# --- SECTION: BUSINESS MATH CALCULATOR ---
st.header("🧮 Commander's Profit Tools")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Profit Margin Calc")
    buying_price = st.number_input("Buying/Production Cost", min_value=0.0)
    selling_price = st.number_input("Selling Price", min_value=0.0)
    
    if selling_price > 0:
        profit = selling_price - buying_price
        margin = (profit / selling_price) * 100
        st.write(f"**Net Profit:** KES {profit}")
        st.write(f"**Profit Margin:** {margin:.2f}%")

with col2:
    st.subheader("Tax Estimator (VAT)")
    total_bill = st.number_input("Total Bill Amount", min_value=0.0)
    vat_rate = 16  # Standard Kenyan VAT
    
    if st.button("Calculate Tax"):
        tax_amount = total_bill * (vat_rate / 100)
        final_total = total_bill + tax_amount
        st.write(f"**VAT (16%):** KES {tax_amount}")
        st.write(f"**Final Total:** KES {final_total}")