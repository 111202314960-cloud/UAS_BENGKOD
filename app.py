import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('model.pkl')

st.title("Prediksi Customer Churn")
st.write("Aplikasi ini memprediksi apakah seorang pelanggan akan Churn atau Tidak.")

# Membuat form input sederhana (Sesuaikan isiannya jika ada kolom spesifik)
age = st.number_input('Umur Pelanggan', min_value=10, max_value=100, value=30)
total_spent = st.number_input('Total Belanja', min_value=0.0, value=500.0)
support_tickets = st.number_input('Jumlah Tiket Bantuan', min_value=0, max_value=20, value=1)
# Untuk demo, kita harus men-supply dataframe sesuai input fitur (Pipeline otomatis mengisi/imputasi sisanya)

if st.button("Prediksi"):
    # Karena kita membuat pipeline utuh, kita butuh DataFrame dummy yang merepresentasikan satu baris penuh
    # (Pastikan di real application semua input dikumpulkan)
    # Ini merupakan implementasi tiruan untuk contoh
    input_data = pd.DataFrame([{
        'age': age,
        'total_spent': total_spent,
        'support_tickets': support_tickets,
        'gender': 'Female', # Sisanya diset dummy/default
        'country': 'UK',
        'is_premium_user': 1
        # Dan fitur-fitur lain yang diminta oleh pipeline
    }])
    
    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.error("Hasil: Customer berpotensi churn!")
        else:
            st.success("Hasil: Customer tidak churn.")
    except Exception as e:
        st.write("Terdapat kesalahan input kolom yang belum terpenuhi untuk pipeline. Error: ", e)
