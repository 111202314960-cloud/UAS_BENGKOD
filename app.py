import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('model.pkl')

st.title("Prediksi Customer Churn")
st.write("Aplikasi ini memprediksi apakah seorang pelanggan akan Churn atau Tidak.")

# Membuat form input interaktif untuk fitur yang paling penting
age = st.number_input('Umur Pelanggan', min_value=10, max_value=100, value=30)
total_spent = st.number_input('Total Belanja ($)', min_value=0.0, value=500.0)
support_tickets = st.number_input('Jumlah Tiket Bantuan', min_value=0, max_value=20, value=1)
gender = st.selectbox('Jenis Kelamin', ['Male', 'Female'])

if st.button("Prediksi"):
    # Menyusun dataframe dengan SEMUA 26 kolom yang digunakan saat training
    input_data = pd.DataFrame([{
        'gender': gender,
        'age': age,
        'total_spent': total_spent,
        'support_tickets': support_tickets,
        'country': 'USA',
        'city': 'New York',
        'acquisition_channel': 'Google Ads',
        'device_type': 'Tablet',
        'subscription_type': 'Monthly',
        'is_premium_user': 0,
        'total_visits': 8,
        'avg_session_time': 9.99585673373457,
        'pages_per_session': 2.2909877458028,
        'email_open_rate': 0.99,
        'email_click_rate': 0.42,
        'avg_order_value': 78.2129256719875,
        'discount_used': 0,
        'coupon_code': 'NONE',
        'refund_requested': 0,
        'delivery_delay_days': 2,
        'payment_method': 'PayPal',
        'satisfaction_score': 1.0,
        'nps_score': 4,
        'marketing_spend_per_user': 19.26,
        'lifetime_value': 1340.17184911385,
        'last_3_month_purchase_freq': 14
    }])
    
    try:
        # Melakukan prediksi
        prediction = model.predict(input_data)
        
        # Menampilkan hasil
        if prediction[0] == 1:
            st.error("⚠️ Hasil: Customer BERPOTENSI CHURN (akan berhenti berlangganan)!")
        else:
            st.success("✅ Hasil: Customer TIDAK CHURN (loyal).")
            
    except Exception as e:
        st.error(f"Terdapat kesalahan pada input model. Error: {e}")
