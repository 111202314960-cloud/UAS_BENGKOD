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
    # Fitur dari form dimasukkan, sisanya diisi dengan nilai default/dummy
    input_data = pd.DataFrame([{
        'gender': gender,
        'age': age,
        'country': 'UK',
        'city': 'London',
        'acquisition_channel': 'Email',
        'device_type': 'Desktop',
        'subscription_type': 'Monthly',
        'is_premium_user': 1,
        'total_visits': 10,
        'avg_session_time': 5.0,
        'pages_per_session': 3.0,
        'email_open_rate': 0.5,
        'email_click_rate': 0.2,
        'total_spent': total_spent,
        'avg_order_value': 50.0,
        'discount_used': 0,
        'coupon_code': 'NONE',
        'support_tickets': support_tickets,
        'refund_requested': 0,
        'delivery_delay_days': 0,
        'payment_method': 'Card',
        'satisfaction_score': 4,
        'nps_score': 8,
        'marketing_spend_per_user': 15.0,
        'lifetime_value': 1000.0,
        'last_3_month_purchase_freq': 3
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
