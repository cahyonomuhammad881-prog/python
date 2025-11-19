import streamlit as st

def hitung_luas(panjang, lebar):
    """Menghitung Luas = Panjang * Lebar"""
    luas = panjang * lebar
    return luas

# --- Streamlit UI ---
st.title("Aplikasi Penghitung Luas Persegi Panjang")
st.markdown("Masukkan nilai panjang dan lebar dalam satuan yang sama.")

# Input Panjang
panjang_input = st.number_input(
    "Masukkan nilai **Panjang**:",
    min_value=0.0,
    value=10.0, # Nilai default
    step=0.1,
    format="%.2f"
)

# Input Lebar
lebar_input = st.number_input(
    "Masukkan nilai **Lebar**:",
    min_value=0.0,
    value=5.0, # Nilai default
    step=0.1,
    format="%.2f"
)

# Tombol untuk menghitung
if st.button("Hitung Luas"):
    if panjang_input <= 0 or lebar_input <= 0:
        st.error("Panjang dan lebar harus bernilai positif.")
    else:
        # Panggil fungsi
        hasil_luas = hitung_luas(panjang_input, lebar_input)
        
        # Output Hasil
        st.success(f"**Luas Persegi Panjang** adalah: **{hasil_luas:.2f}**")
        st.balloons() # Efek visual setelah perhitungan