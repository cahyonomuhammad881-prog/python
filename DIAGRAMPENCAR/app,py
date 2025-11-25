import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# --- 1. Fungsi Pembuat Data (Generasi Data) ---

def generate_data(n_samples, correlation_type):
    """
    Menghasilkan DataFrame dengan korelasi tertentu.
    n_samples: jumlah titik data
    correlation_type: jenis korelasi yang dipilih (misalnya 'Positif Kuat')
    """
    # Base data
    rng = np.random.default_rng(seed=42)
    x = rng.uniform(0, 100, n_samples)
    
    # Koefisien dan Noise berdasarkan Tipe Korelasi
    if correlation_type == 'Positif Kuat':
        coefficient = 1.2
        noise_level = 5  # Noise rendah
        r_label = "r ≈ 0.8 sampai 1.0"
    elif correlation_type == 'Positif Sedang':
        coefficient = 0.8
        noise_level = 15
        r_label = "r ≈ 0.4 sampai 0.7"
    elif correlation_type == 'Negatif Kuat':
        coefficient = -1.2
        noise_level = 5
        r_label = "r ≈ -0.8 sampai -1.0"
    elif correlation_type == 'Negatif Lemah':
        coefficient = -0.5
        noise_level = 20
        r_label = "r ≈ -0.1 sampai -0.4"
    elif correlation_type == 'Nol (Tidak Ada Korelasi)':
        coefficient = 0.05
        noise_level = 50 # Noise sangat tinggi
        r_label = "r ≈ -0.1 sampai 0.1"
    else: # Nol (Tidak Ada Korelasi) - Default
        coefficient = 0
        noise_level = 30
        r_label = "r ≈ 0"

    # Generate y with noise
    y = (coefficient * x) + rng.normal(0, noise_level, n_samples)
    
    # Membuat DataFrame
    df = pd.DataFrame({
        'Variabel X': x,
        'Variabel Y': y
    })
    
    # Hitung koefisien korelasi Pearson aktual
    correlation = df['Variabel X'].corr(df['Variabel Y'])
    
    return df, correlation, r_label

# --- 2. Aplikasi Streamlit Utama ---

def main():
    st.set_page_config(page_title="Virtual Lab Statistika: Korelasi", layout="wide")
    
    st.title("🔬 Virtual Lab: Diagram Pencar & Korelasi")
    st.markdown("Eksplorasi hubungan antara dua variabel secara interaktif.")
    st.markdown("---")
    
    # --- Sidebar Input & Navigasi ---
    st.sidebar.header("Pengaturan Data")
    
    # Pilihan Tipe Korelasi
    correlation_options = [
        'Positif Kuat', 'Positif Sedang', 
        'Negatif Kuat', 'Negatif Lemah', 
        'Nol (Tidak Ada Korelasi)'
    ]
    selected_correlation = st.sidebar.selectbox(
        "Pilih Jenis Hubungan (Korelasi)", 
        correlation_options
    )
    
    # Jumlah Titik Data
    n_samples = st.sidebar.slider(
        "Jumlah Titik Data (N)", 
        min_value=50, max_value=500, value=150
    )
    
    # Generate data
    df, r_actual, r_label_expected = generate_data(n_samples, selected_correlation)
    
    # --- Konten Utama (Dua Kolom) ---
    col_visual, col_interpret = st.columns([3, 2])
    
    with col_visual:
        st.subheader("1️⃣ Diagram Pencar (Scatter Plot)")
        st.info("Setiap titik mewakili pasangan nilai (X, Y).")
        
        # Buat Scatter Plot menggunakan Altair
        scatter_chart = alt.Chart(df).mark_circle(size=60).encode(
            x=alt.X('Variabel X', title='Variabel X (Misal: Jam Belajar)'),
            y=alt.Y('Variabel Y', title='Variabel Y (Misal: Nilai Ujian)'),
            tooltip=['Variabel X', 'Variabel Y']
        ).properties(
            title=f"Diagram Pencar: {selected_correlation}",
            height=400,
            width='container'
        ).interactive() # Tambahkan interaktivitas zoom/pan

        # Tambahkan Garis Regresi (Garis Tren)
        line_fit = scatter_chart.transform_regression(
            'Variabel X', 'Variabel Y', method="linear"
        ).mark_line(color='red')

        st.altair_chart(scatter_chart + line_fit, use_container_width=True)

    with col_interpret:
        st.subheader("2️⃣ Analisis Korelasi")
        st.markdown("### Koefisien Korelasi (r)")
        
        # Menampilkan Koefisien Korelasi
        st.metric(
            label="Nilai $r$ (Korelasi Pearson)", 
            value=f"{r_actual:.4f}",
            delta=r_label_expected # Tampilkan label ekspektasi
        )
        
        st.markdown("---")
        
        st.subheader("3️⃣ Interpretasi Hubungan")
        
        # Logika Interpretasi
        abs_r = abs(r_actual)
        
        if abs_r >= 0.8:
            kekuatan = "Sangat Kuat"
            ikon = "💪"
            penjelasan = "Titik-titik berkerumun sangat dekat membentuk garis lurus. Hubungan antara X dan Y jelas sekali."
        elif abs_r >= 0.6:
            kekuatan = "Kuat"
            ikon = "👍"
            penjelasan = "Titik-titik cenderung membentuk garis lurus, tetapi ada sedikit sebaran."
        elif abs_r >= 0.4:
            kekuatan = "Sedang"
            ikon = "🤏"
            penjelasan = "Titik-titik menyebar, namun tren linear masih terlihat secara umum."
        elif abs_r >= 0.2:
            kekuatan = "Lemah"
            ikon = "🤔"
            penjelasan = "Titik-titik tersebar luas, tren linear hampir tidak terlihat, dan hubungan sangat samar."
        else:
            kekuatan = "Sangat Lemah / Tidak Ada"
            ikon = "🤯"
            penjelasan = "Titik-titik tersebar secara acak (Random), tidak menunjukkan pola linear sama sekali."

        # Arah Korelasi
        if r_actual > 0.1:
            arah = "Positif ↗️"
            arah_desc = "Jika X naik, maka Y cenderung **naik** juga."
        elif r_actual < -0.1:
            arah = "Negatif ↘️"
            arah_desc = "Jika X naik, maka Y cenderung **turun**."
        else:
            arah = "Tidak Ada Arah"
            arah_desc = "Tidak ada hubungan linear yang jelas antara X dan Y."

        st.markdown(f"### Kekuatan Hubungan: {ikon} **{kekuatan}**")
        st.caption(penjelasan)
        
        st.markdown(f"### Arah Hubungan: **{arah}**")
        st.caption(arah_desc)
        
        st.markdown("---")
        st.markdown("Nilai $r$ selalu berada dalam rentang **-1 hingga +1**.")
        st.caption("$r$ mendekati 1 berarti positif kuat; $r$ mendekati -1 berarti negatif kuat; $r$ mendekati 0 berarti tidak ada korelasi.")
         # Trigger gambar untuk memudahkan interpretasi

# --- 3. Run Aplikasi ---
if __name__ == "__main__":
    main()
