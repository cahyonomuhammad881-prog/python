import streamlit as st
import math

# --- Data Ilustrasi (Penting: Ganti URL dengan Link GIF/Gambar Anda) ---

# URL untuk GIF atau gambar statis yang relevan
# PENTING: Jika menggunakan GIF, pastikan ukurannya kecil agar cepat loading.
# (Contoh URL ini hanyalah placeholder)
ILUSTRASI_DATA = {
    "permutasi_utama": "https://i.imgur.com/Qk9sZ7p.gif",  # Placeholder: GIF susunan objek berurut
    "kombinasi_utama": "https://i.imgur.com/hGj9pWd.gif",  # Placeholder: GIF pemilihan tim/jabat tangan
    "peluang_dadu": "https://i.imgur.com/r8O0eCq.gif",     # Placeholder: GIF dadu dilempar
    "peluang_kelereng": "https://i.imgur.com/X4yD1L2.png"  # Placeholder: Gambar kotak kelereng
}

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

# --- 2. Fungsi untuk Menghasilkan Ilustrasi Teks Dinamis ---

def ilustrasi_permutasi_text(n, k):
    """Menghasilkan teks ilustrasi dinamis untuk Permutasi."""
    if n < k: return "Masukkan nilai n ≥ k yang valid."
    
    kasus = "kunci loker 4 digit" if k == 4 else "posisi ketua, wakil, bendahara" if k == 3 else "medali emas dan perak"
    
    return f"""
    ### 🔑 Contoh Kasus: Susunan Kode Kunci
    Bayangkan Anda memiliki **{n}** angka unik, dan Anda harus membuat kode kunci sepanjang **{k}** digit.

    **Urutan sangat penting!** Jika Anda menukar dua digit, kode kuncinya sudah berbeda.
    * **Kasus:** Ada berapa cara {n} objek dapat disusun menjadi {k} tempat?
    """

def ilustrasi_kombinasi_text(n, k):
    """Menghasilkan teks ilustrasi dinamis untuk Kombinasi."""
    if n < k: return "Masukkan nilai n ≥ k yang valid."

    kasus = "jabat tangan" if k == 2 else "pemilihan anggota tim"
    
    return f"""
    ### 🤝 Contoh Kasus: {kasus.capitalize()}
    Bayangkan ada **{n}** orang. Kita ingin memilih **{k}** orang di antaranya untuk:
    * **Jika k=2:** Saling berjabat tangan.
    * **Jika k>2:** Membentuk sebuah tim tanpa jabatan khusus.

    **Urutan tidak penting!** Tim {chr(65)} dan {chr(66)} sama dengan tim {chr(66)} dan {chr(65)} ({chr(65)} adalah A, {chr(66)} adalah B).
    """

def ilustrasi_peluang_text(nS, nA):
    """Menghasilkan teks ilustrasi dinamis untuk Peluang."""
    if nS == 0: return "Ruang Sampel tidak boleh nol."
    
    P_A = nA / nS if nS > 0 else 0
    
    return f"""
    ### 🎯 Contoh Kasus: Peluang
    Peluang seringkali menggunakan konsep kombinatorika. Misalnya:
    1.  **$n(S)$ (Ruang Sampel):** Total semua kemungkinan yang ada.
    2.  **$n(A)$ (Kejadian Diinginkan):** Total kemungkinan untuk kejadian yang spesifik (misalnya, mendapat angka 6 pada dadu, atau terpilihnya 3 kelereng merah).

    **Visualisasi:**
    Peluang Anda $P(A) = {P_A:.2f}$ adalah rasio dari kejadian yang Anda inginkan terhadap total kejadian.
    """


# --- 3. Aplikasi Streamlit Utama ---

def main():
    st.set_page_config(page_title="Virtual Lab Kombinatorika & Peluang", layout="wide")
    
    st.title("🔬 Virtual Lab: Kombinatorika & Peluang")
    st.markdown("Aplikasi interaktif dengan **visualisasi bergerak** untuk memahami Permutasi, Kombinasi, dan Peluang.")
    st.markdown("---")
    
    # --- Sidebar Navigasi dan Input Global ---
    menu = ["Permutasi", "Kombinasi", "Peluang (Probability)", "Perbandingan Konsep"]
    pilihan = st.sidebar.selectbox("Pilih Topik Utama", menu)
    
    # Input Global n dan k di Sidebar
    if pilihan in ["Permutasi", "Kombinasi", "Perbandingan Konsep"]:
        st.sidebar.header("Input Variabel Utama (n dan k)")
        n_global = st.sidebar.number_input("Total Objek (n)", min_value=1, value=5, step=1, key='n_global')
        k_global = st.sidebar.number_input("Objek yang Dipilih/Disusun (k)", min_value=0, value=2, step=1, key='k_global')
        
        if n_global < k_global:
            st.sidebar.error("⚠️ **n** harus lebih besar atau sama dengan **k**.")
            
    # --- Konten Utama Berdasarkan Pilihan (Menggunakan 2 Kolom) ---

    if pilihan == "Permutasi":
        st.header("1️⃣ Permutasi: Urutan Diperhatikan (Ordered Arrangement)")
        col_calc, col_illust = st.columns(2)
        
        with col_calc:
            st.info("Permutasi = $P(n, k)$. Hasilnya adalah **susunan** di mana urutan sangat penting.")
            st.subheader("📝 Rumus & Perhitungan")
            st.latex(r'''P(n, k) = \frac{n!}{(n-k)!}''')
            
            if n_global >= k_global:
                hasil_p = hitung_permutasi(n_global, k_global)
                st.metric(label=f"P({n_global}, {k_global})", value=hasil_p)
                st.success(f"Ada **{hasil_p}** cara penyusunan berbeda.")
            else:
                st.error("Input n dan k tidak valid.")
            
        with col_illust:
            st.markdown(ilustrasi_permutasi_text(n_global, k_global))
            st.image(ILUSTRASI_DATA["permutasi_utama"], caption=f"Visualisasi susunan {k_global} objek dari {n_global} total", use_column_width='auto')


    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Kombinasi":
        st.header("2️⃣ Kombinasi: Urutan Tidak Penting (Unordered Selection)")
        col_calc, col_illust = st.columns(2)

        with col_calc:
            st.info("Kombinasi = $C(n, k)$. Hasilnya adalah **pemilihan** atau **pengelompokan**.")
            st.subheader("📝 Rumus & Perhitungan")
            st.latex(r'''C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}''')
            
            if n_global >= k_global:
                hasil_c = hitung_kombinasi(n_global, k_global)
                st.metric(label=f"C({n_global}, {k_global})", value=hasil_c)
                st.success(f"Ada **{hasil_c}** cara pemilihan/pengelompokan berbeda.")
            else:
                st.error("Input n dan k tidak valid.")
        
        with col_illust:
            st.markdown(ilustrasi_kombinasi_text(n_global, k_global))
            st.image(ILUSTRASI_DATA["kombinasi_utama"], caption=f"Visualisasi pemilihan {k_global} objek dari {n_global} total", use_column_width='auto')
            

    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Peluang (Probability)":
        st.header("3️⃣ Peluang (Probability): Rasio Kejadian")
        col_calc, col_illust = st.columns(2)
        
        with col_calc:
            st.info("Peluang $P(A)$ adalah rasio antara $n(A)$ (hasil diinginkan) dengan $n(S)$ (total kemungkinan).")
            st.subheader("⚙️ Kalkulator Peluang")
            st.latex(r'''P(A) = \frac{n(A)}{n(S)}''')
            
            st.markdown("**1. Ruang Sampel $n(S)$**")
            nS = st.number_input("Total Kemungkinan (n(S))", min_value=1, value=6, key='nS_manual_p')
                
            st.markdown("**2. Banyaknya Kejadian $n(A)$**")
            nA = st.number_input("Hasil yang Diinginkan (n(A))", min_value=0, value=1, key='nA_manual_p')
            
            st.markdown("---")
            st.subheader("✅ Hasil Peluang ($P(A)$)")
            
            if nS > 0 and nA <= nS:
                P_A = nA / nS
                st.markdown(f"**$n(S)$:** `{nS}`")
                st.markdown(f"**$n(A)$:** `{nA}`")
                st.success(f"$$P(A) = \\frac{{{nA}}}{{{nS}}} \\approx {P_A:.4f}$$")
                st.progress(P_A, text=f"Peluang sebesar {P_A*100:.2f}%")
            elif nA > nS:
                 st.error("⚠️ $n(A)$ tidak boleh melebihi $n(S)$.")
            else:
                st.error("⚠️ $n(S)$ harus lebih besar dari 0.")

        with col_illust:
            st.markdown(ilustrasi_peluang_text(nS, nA))
            
            # Ilustrasi dinamis berdasarkan input nS (Contoh sederhana)
            if nS == 6:
                st.image(ILUSTRASI_DATA["peluang_dadu"], caption="Contoh: Melempar Dadu (n(S)=6)", use_column_width='auto')
            else:
                 st.image(ILUSTRASI_DATA["peluang_kelereng"], caption=f"Contoh: Mengambil objek dari {nS} total kemungkinan", use_column_width='auto')
            

    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Perbandingan Konsep":
        st.header("⚖️ Perbandingan Konsep Utama")
        st.warning("Fokus: Apakah **URUTAN** menentukan hasilnya? Jika YA, gunakan Permutasi.")
        
        n, k = st.session_state.n_global, st.session_state.k_global
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Permutasi P(n, k)")
            st.markdown("* **Urutan Penting** (Kode, Juara, Jabatan)")
            if n >= k:
                 st.metric(label=f"P({n}, {k})", value=hitung_permutasi(n, k))
            
        with col2:
            st.subheader("Kombinasi C(n, k)")
            st.markdown("* **Urutan Tidak Penting** (Tim, Jabat Tangan, Kumpulan)")
            if n >= k:
                st.metric(label=f"C({n}, {k})", value=hitung_kombinasi(n, k))
                
        st.markdown("---")
        st.subheader("Peluang $P(A)$")
        st.markdown("Peluang adalah hasil bagi dari banyaknya kejadian yang dihitung (menggunakan Permutasi/Kombinasi) dengan total ruang sampel.")


if __name__ == "__main__":
    main()
