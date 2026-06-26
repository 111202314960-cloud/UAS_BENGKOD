import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('model.pkl')

st.title("Prediksi Customer Churn")
st.write("Aplikasi ini memprediksi apakah seorang pelanggan akan Churn atau Tidak secara dinamis.")
st.markdown("---")

# Membagi layar menjadi 2 kolom agar form terlihat rapi dan profesional
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Demografi")
    age = st.number_input('Umur Pelanggan', min_value=10, max_value=100, value=30)
    gender = st.selectbox('Jenis Kelamin', ['Male', 'Female'])
    is_premium = st.selectbox('Status Premium?', ['Tidak', 'Ya'])
    # Mengubah teks menjadi angka (1 untuk Ya, 0 untuk Tidak)
    is_premium_user = 1 if is_premium == 'Ya' else 0

with col2:
    st.subheader("Data Transaksi & Interaksi")
    total_spent = st.number_input('Total Belanja ($)', min_value=0.0, value=500.0)
    satisfaction_score = st.slider('Skor Kepuasan (1-5)', min_value=1.0, max_value=5.0, value=3.0)
    support_tickets = st.number_input('Jumlah Tiket Komplain', min_value=0, max_value=20, value=1)
    last_3_month_freq = st.number_input('Transaksi 3 Bulan Terakhir', min_value=0, max_value=50, value=5)

st.markdown("---")

if st.button("Prediksi Status Pelanggan", use_container_width=True):
    # Menyusun dataframe dengan SEMUA 26 kolom
    # Nilai tersembunyi diset "Netral" agar form input mendominasi keputusan model
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
        'is_premium_user': is_premium_user,
        'total_visits': 10,
        'avg_session_time': 5.0,
        'pages_per_session': 3.0,
        'email_open_rate': 0.5,
        'email_click_rate': 0.2,
        'avg_order_value': 50.0,
        'discount_used': 0,
        'coupon_code': 'NONE',
        'refund_requested': 0,
        'delivery_delay_days': 0,
        'payment_method': 'PayPal',
        'satisfaction_score': satisfaction_score,
        'nps_score': 5, # Skor Netral
        'marketing_spend_per_user': 15.0,
        'lifetime_value': 1000.0,
        'last_3_month_purchase_freq': last_3_month_freq
    }])
    
    try:
        # Melakukan prediksi
        prediction = model.predict(input_data)
        
        # Menampilkan hasil
        if prediction[0] == 1:
            st.error("⚠️ HASIL: Customer BERPOTENSI CHURN (Kemungkinan besar akan berhenti berlangganan)!")
        else:
            st.success("✅ HASIL: Customer TIDAK CHURN (Pelanggan loyal dan aktif).")
            
    except Exception as e:
        st.error(f"Terdapat kesalahan pada input model. Error: {e}")
