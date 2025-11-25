import streamlit as st
import math

# --- 1. Fungsi Perhitungan Kombinatorika ---

def hitung_faktorial(n):
    """Menghitung n!"""
    if n < 0:
        return 0
    return math.factorial(n)

def hitung_permutasi(n, k):
    """Menghitung Permutasi P(n, k)"""
    if n < k or n < 0 or k < 0:
        return 0
    try:
        # Menggunakan math.perm
        return math.perm(n, k)
    except ValueError:
        return 0 # Error handling jika input tidak valid

def hitung_kombinasi(n, k):
    """Menghitung Kombinasi C(n, k)"""
    if n < k or n < 0 or k < 0:
        return 0
    try:
        # Menggunakan math.comb
        return math.comb(n, k)
    except ValueError:
        return 0 # Error handling jika input tidak valid

# --- 2. Aplikasi Streamlit Utama ---

def main():
    st.set_page_config(page_title="Virtual Lab Kombinatorika & Peluang", layout="wide")
    
    st.title("🔬 Virtual Lab: Kombinatorika & Peluang")
    st.markdown("Aplikasi interaktif untuk memahami Permutasi, Kombinasi, dan Peluang.")
    st.markdown("---")
    
    # --- Sidebar Navigasi dan Input Global ---
    
    menu = ["Permutasi", "Kombinasi", "Peluang (Probability)", "Perbandingan Konsep"]
    pilihan = st.sidebar.selectbox("Pilih Topik Utama", menu)
    
    st.sidebar.header("Input Variabel Utama (n dan k)")
    n = st.sidebar.number_input("Total Elemen (n)", min_value=1, value=5, step=1)
    k = st.sidebar.number_input("Elemen yang Dipilih (k)", min_value=0, value=2, step=1)
    
    if n < k:
        st.sidebar.error("⚠️ **n** harus lebih besar atau sama dengan **k**.")
        
    # --- Konten Utama Berdasarkan Pilihan ---

    if pilihan == "Permutasi":
        st.header("1️⃣ Permutasi: Urutan Diperhatikan")
        st.info("Permutasi adalah cara menyusun objek di mana **urutan susunan sangat penting**.")
        
        col_rumus, col_output = st.columns(2)
        
        with col_rumus:
            st.subheader("📝 Rumus Permutasi $P(n, k)$")
            st.latex(r'''P(n, k) = \frac{n!}{(n-k)!}''')
            st.markdown("*n* = total elemen, *k* = elemen yang disusun.")
            
        with col_output:
            st.subheader(f"⚙️ Hasil Perhitungan P({n}, {k})")
            if n >= k:
                hasil_p = hitung_permutasi(n, k)
                st.success(f"Ada **{hasil_p}** cara penyusunan.")
                st.markdown(f"**Contoh Kasus:** Menyusun {k} posisi (Ketua, Wakil, dll.) dari {n} kandidat.")
            else:
                st.error("Input n dan k tidak valid. Koreksi di sidebar.")
            
    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Kombinasi":
        st.header("2️⃣ Kombinasi: Urutan Tidak Penting")
        st.info("Kombinasi adalah cara memilih/mengambil objek di mana **urutan pemilihan tidak penting** (hanya pengelompokan).")

        col_rumus, col_output = st.columns(2)

        with col_rumus:
            st.subheader("📝 Rumus Kombinasi $C(n, k)$")
            st.latex(r'''C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}''')
            st.markdown("*n* = total elemen, *k* = elemen yang dipilih.")
            
        with col_output:
            st.subheader(f"⚙️ Hasil Perhitungan C({n}, {k})")
            if n >= k:
                hasil_c = hitung_kombinasi(n, k)
                st.success(f"Ada **{hasil_c}** cara pengelompokan/pemilihan.")
                st.markdown(f"**Contoh Kasus:** Memilih {k} anggota tim (tanpa jabatan spesifik) dari {n} kandidat.")
            else:
                st.error("Input n dan k tidak valid. Koreksi di sidebar.")

    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Peluang (Probability)":
        st.header("3️⃣ Peluang (Probability)")
        st.info("Peluang adalah rasio antara hasil yang diinginkan *n(A)* dengan total hasil yang mungkin *n(S)*.")
        
        st.subheader("📝 Rumus Dasar Peluang")
        st.latex(r'''P(A) = \frac{n(A)}{n(S)}''')
        
        st.markdown("---")
        
        st.subheader("Contoh Interaktif: Peluang Menggunakan Kombinasi")
        
        nS_opsi = st.selectbox(
            "Pilih Total Ruang Sampel (n(S))",
            ["Gunakan Kombinasi (Kasus Kompleks)", "Input Manual"]
        )
        
        if nS_opsi == "Gunakan Kombinasi (Kasus Kompleks)":
            st.markdown("Misal: Mengambil **k** bola dari total **n** bola (n(S) = C(n, k))")
            
            n_tot = st.number_input("Total Objek (n)", min_value=1, value=10, key='n_tot')
            k_ambil = st.number_input("Jumlah yang Diambil (k)", min_value=1, value=3, key='k_ambil')
            
            if n_tot >= k_ambil:
                nS = hitung_kombinasi(n_tot, k_ambil)
                st.markdown(f"Total Ruang Sampel $n(S) = C({n_tot}, {k_ambil})$ adalah **{nS}**")
            else:
                st.error("Total Objek harus lebih besar dari jumlah yang diambil.")
                nS = 1 # Hindari division by zero
                
            nA = st.number_input("Jumlah Kejadian yang Diinginkan (n(A))", min_value=0, value=1, key='nA_input')
            
        else: # Input Manual
            nS = st.number_input("Input Manual Total Ruang Sampel n(S)", min_value=1, value=6, key='nS_manual')
            nA = st.number_input("Input Manual Jumlah Kejadian yang Diinginkan n(A)", min_value=0, value=1, key='nA_manual')
            
        # Perhitungan Peluang
        if nS > 0 and nA <= nS:
            P_A = nA / nS
            st.markdown("---")
            st.subheader("💡 Hasil Peluang")
            st.success(f"Peluang $P(A) = \\frac{{{nA}}}{{{nS}}} \\approx$ **{P_A:.4f}**")
            
            # Visualisasi Bar
            st.progress(P_A, text=f"Peluang sebesar {P_A*100:.2f}%")
        elif nA > nS:
             st.error("Jumlah kejadian yang diinginkan n(A) tidak boleh melebihi total ruang sampel n(S).")


    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Perbandingan Konsep":
        st.header("⚖️ Perbandingan Konsep Utama")
        st.warning("**Kunci Utama:** Apakah **Urutan** Penting? (Permutasi vs Kombinasi)")
        
        st.markdown(f"Input saat ini: $n={n}, k={k}$")
        
        col1, col2 = st.columns(2)
        
        # --- Kolom Permutasi ---
        with col1:
            st.subheader("Permutasi")
            st.markdown("* **Urutan Penting** (misal: posisi Juara 1 $\\ne$ Juara 2)")
            st.markdown("* **Hasil:** Selalu lebih besar.")
            if n >= k:
                 P_val = hitung_permutasi(n, k)
                 st.metric(label=f"P({n}, {k})", value=P_val)
            
        # --- Kolom Kombinasi ---
        with col2:
            st.subheader("Kombinasi")
            st.markdown("* **Urutan Tidak Penting** (misal: tim {A, B} $=$ tim {B, A})")
            st.markdown("* **Hasil:** Selalu lebih kecil.")
            if n >= k:
                C_val = hitung_kombinasi(n, k)
                st.metric(label=f"C({n}, {k})", value=C_val)
                
        # --- Penjelasan Peluang ---
        st.markdown("---")
        st.subheader("Peluang dalam Konteks Kombinatorika")
        st.markdown("Peluang seringkali menggunakan Kombinasi atau Permutasi untuk menghitung $n(A)$ (hasil yang diinginkan) dan $n(S)$ (total ruang sampel).")
        st.markdown("> **Peluang = (Hasil yang Diinginkan) / (Total Kemungkinan)**")

if __name__ == "__main__":
    main()
