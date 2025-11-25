import streamlit as st
import math

# --- 1. Fungsi Perhitungan Kombinatorika ---

def hitung_permutasi(n, k):
    """Menghitung Permutasi P(n, k)"""
    if n < k or n < 0 or k < 0:
        return 0
    return math.perm(n, k)

def hitung_kombinasi(n, k):
    """Menghitung Kombinasi C(n, k)"""
    if n < k or n < 0 or k < 0:
        return 0
    return math.comb(n, k)

# --- 2. Fungsi untuk Menghasilkan Ilustrasi Teks ---

def ilustrasi_permutasi(n, k):
    """Menghasilkan teks ilustrasi dinamis untuk Permutasi."""
    if n < k: return "Masukkan nilai n ≥ k yang valid."
    
    return f"""
    ### 🏃 Ilustrasi: Perlombaan Lari
    Bayangkan ada **{n}** pelari yang berkompetisi. Kita ingin tahu ada berapa cara mereka bisa menempati **{k}** posisi juara (Juara 1, Juara 2, dan seterusnya).

    **Urutan penting!**
    * Jika Pelari A di Juara 1 dan B di Juara 2, **itu berbeda** dengan B di Juara 1 dan A di Juara 2.
    * Setiap susunan posisi dihitung berbeda.
    """

def ilustrasi_kombinasi(n, k):
    """Menghasilkan teks ilustrasi dinamis untuk Kombinasi."""
    if n < k: return "Masukkan nilai n ≥ k yang valid."
    
    return f"""
    ### 🤝 Ilustrasi: Jabat Tangan / Pembentukan Tim
    Bayangkan ada **{n}** orang di sebuah ruangan. Kita ingin membentuk tim beranggotakan **{k}** orang, atau memilih {k} orang untuk saling berjabat tangan.

    **Urutan tidak penting!**
    * Jika Anda memilih Orang A dan Orang B untuk tim, **itu sama** dengan memilih Orang B dan Orang A.
    * Dalam jabat tangan, A menjabat B sama dengan B menjabat A.
    """

def ilustrasi_peluang(nS, nA):
    """Menghasilkan teks ilustrasi dinamis untuk Peluang."""
    if nS == 0: return "Ruang Sampel tidak boleh nol."
    
    P_A = nA / nS if nS > 0 else 0
    
    return f"""
    ### 🎲 Ilustrasi: Kotak Keberuntungan
    Bayangkan sebuah kotak berisi total **{nS}** kelereng (Ruang Sampel).
    Anda tertarik pada **{nA}** kelereng berwarna emas (Kejadian yang Diinginkan).

    **Peluang $P(A)$** adalah seberapa mungkin Anda mengambil kelereng emas tersebut dalam satu kali pengambilan.
    * Jika $P(A) \approx 0.0$ (0%), kejadian itu sangat jarang.
    * Jika $P(A) \approx 1.0$ (100%), kejadian itu pasti terjadi.
    """


# --- 3. Aplikasi Streamlit Utama ---

def main():
    st.set_page_config(page_title="Virtual Lab Kombinatorika & Peluang", layout="wide")
    
    st.title("🔬 Virtual Lab: Kombinatorika & Peluang")
    st.markdown("Aplikasi interaktif dengan **visualisasi** untuk memahami Permutasi, Kombinasi, dan Peluang.")
    st.markdown("---")
    
    # --- Sidebar Navigasi ---
    
    menu = ["Permutasi", "Kombinasi", "Peluang (Probability)", "Perbandingan Konsep"]
    pilihan = st.sidebar.selectbox("Pilih Topik Utama", menu)
    
    
    # Input Global n dan k di Sidebar (hanya untuk Permutasi/Kombinasi)
    if pilihan in ["Permutasi", "Kombinasi", "Perbandingan Konsep"]:
        st.sidebar.header("Input Variabel Utama (n dan k)")
        n_global = st.sidebar.number_input("Total Elemen (n)", min_value=1, value=5, step=1, key='n_global')
        k_global = st.sidebar.number_input("Elemen yang Dipilih (k)", min_value=0, value=2, step=1, key='k_global')
        
        if n_global < k_global:
            st.sidebar.error("⚠️ **n** harus lebih besar atau sama dengan **k**.")
            
    # --- Konten Utama Berdasarkan Pilihan (Menggunakan 2 Kolom) ---

    if pilihan == "Permutasi":
        st.header("1️⃣ Permutasi: Urutan Diperhatikan")
        col_calc, col_illust = st.columns(2)
        
        with col_calc:
            st.info("Permutasi adalah **susunan** di mana urutan penting.")
            st.subheader("📝 Rumus & Perhitungan")
            st.latex(r'''P(n, k) = \frac{n!}{(n-k)!}''')
            
            if n_global >= k_global:
                hasil_p = hitung_permutasi(n_global, k_global)
                st.success(f"P({n_global}, {k_global}) = **{hasil_p}**")
            else:
                st.error("Input n dan k tidak valid.")
            
        with col_illust:
            st.markdown(ilustrasi_permutasi(n_global, k_global))
            # Tag visual yang relevan
            st.image("https://i.imgur.com/u8d8d3H.png", caption="Urutan dalam Permutasi (A,B,C ≠ B,A,C)", use_column_width='auto')


    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Kombinasi":
        st.header("2️⃣ Kombinasi: Urutan Tidak Penting")
        col_calc, col_illust = st.columns(2)

        with col_calc:
            st.info("Kombinasi adalah **pemilihan/pengelompokan** di mana urutan tidak penting.")
            st.subheader("📝 Rumus & Perhitungan")
            st.latex(r'''C(n, k) = \frac{n!}{k!(n-k)!}''')
            
            if n_global >= k_global:
                hasil_c = hitung_kombinasi(n_global, k_global)
                st.success(f"C({n_global}, {k_global}) = **{hasil_c}**")
            else:
                st.error("Input n dan k tidak valid.")
        
        with col_illust:
            st.markdown(ilustrasi_kombinasi(n_global, k_global))
            # Tag visual yang relevan
            st.image("https://i.imgur.com/g9XnF7b.png", caption="Jabat Tangan (Tim {A,B} = {B,A})", use_column_width='auto')
            

    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Peluang (Probability)":
        st.header("3️⃣ Peluang (Probability): Menghubungkan Konsep")
        col_calc, col_illust = st.columns(2)
        
        with col_calc:
            st.info("Peluang = $n(A)$ dibagi $n(S)$.")
            st.subheader("⚙️ Kalkulator Peluang")
            st.latex(r'''P(A) = \frac{n(A)}{n(S)}''')
            
            st.markdown("**Langkah 1: Tentukan Ruang Sampel ($n(S)$)**")
            nS = st.number_input("Masukkan Nilai $n(S)$", min_value=1, value=10, key='nS_manual_p')
                
            st.markdown("**Langkah 2: Tentukan Banyaknya Kejadian ($n(A)$)**")
            nA = st.number_input("Masukkan Nilai $n(A)$", min_value=0, value=1, key='nA_manual_p')
            
            st.markdown("---")
            st.subheader("✅ Hasil Peluang ($P(A)$)")
            
            if nS > 0 and nA <= nS:
                P_A = nA / nS
                st.markdown(f"**$n(S)$ (Total Kemungkinan):** `{nS}`")
                st.markdown(f"**$n(A)$ (Hasil Diinginkan):** `{nA}`")
                st.success(f"$$P(A) = \\frac{{{nA}}}{{{nS}}} \\approx {P_A:.4f}$$")
                st.progress(P_A, text=f"Peluang sebesar {P_A*100:.2f}%")
            elif nA > nS:
                 st.error("⚠️ $n(A)$ tidak boleh melebihi $n(S)$.")
            else:
                st.error("⚠️ $n(S)$ harus lebih besar dari 0.")

        with col_illust:
            st.markdown(ilustrasi_peluang(nS, nA))
            # Tag visual yang relevan
            st.image("https://i.imgur.com/X4yD1L2.png", caption="Peluang (Kelereng yang Diinginkan / Total Kelereng)", use_column_width='auto')
            

    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Perbandingan Konsep":
        st.header("⚖️ Perbandingan Konsep Utama")
        st.warning("Kunci: Fokus pada apakah **URUTAN** menentukan hasilnya.")
        
        n, k = st.session_state.n_global, st.session_state.k_global
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Permutasi P(n, k)")
            st.markdown("* **Urutan Penting** (misal: kode kunci, Juara 1)")
            if n >= k:
                 st.metric(label=f"P({n}, {k})", value=hitung_permutasi(n, k))
            
        with col2:
            st.subheader("Kombinasi C(n, k)")
            st.markdown("* **Urutan Tidak Penting** (misal: jabat tangan, anggota tim)")
            if n >= k:
                st.metric(label=f"C({n}, {k})", value=hitung_kombinasi(n, k))
                
        st.markdown("---")
        st.subheader("Peluang $P(A)$")
        st.markdown("Peluang adalah rasio yang menggunakan Permutasi atau Kombinasi untuk menentukan **jumlah kemungkinannya**.")


if __name__ == "__main__":
    main()
