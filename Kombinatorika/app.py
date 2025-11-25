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

# --- 2. Aplikasi Streamlit Utama ---

def main():
    st.set_page_config(page_title="Virtual Lab Kombinatorika & Peluang", layout="wide")
    
    st.title("🔬 Virtual Lab: Kombinatorika & Peluang")
    st.markdown("Aplikasi interaktif untuk memahami Permutasi, Kombinasi, dan Peluang.")
    st.markdown("---")
    
    # --- Sidebar Navigasi dan Input Global ---
    
    menu = ["Permutasi", "Kombinasi", "Peluang (Probability)", "Perbandingan Konsep"]
    pilihan = st.sidebar.selectbox("Pilih Topik Utama", menu)
    
    # Input n dan k hanya untuk bagian Permutasi/Kombinasi
    if pilihan in ["Permutasi", "Kombinasi", "Perbandingan Konsep"]:
        st.sidebar.header("Input Variabel Utama (n dan k)")
        n = st.sidebar.number_input("Total Elemen (n)", min_value=1, value=5, step=1, key='n_global')
        k = st.sidebar.number_input("Elemen yang Dipilih (k)", min_value=0, value=2, step=1, key='k_global')
        
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
            
        with col_output:
            st.subheader(f"⚙️ Hasil Perhitungan P({n_global}, {k_global})")
            if n_global >= k_global:
                hasil_p = hitung_permutasi(n_global, k_global)
                st.success(f"Ada **{hasil_p}** cara penyusunan.")
                st.markdown(f"**Contoh:** Menyusun {k_global} posisi dari {n_global} kandidat.")
            else:
                st.error("Input n dan k tidak valid. Koreksi di sidebar.")
            
    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Kombinasi":
        st.header("2️⃣ Kombinasi: Urutan Tidak Penting")
        st.info("Kombinasi adalah cara memilih/mengambil objek di mana **urutan pemilihan tidak penting**.")

        col_rumus, col_output = st.columns(2)

        with col_rumus:
            st.subheader("📝 Rumus Kombinasi $C(n, k)$")
            st.latex(r'''C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}''')
            
        with col_output:
            st.subheader(f"⚙️ Hasil Perhitungan C({n_global}, {k_global})")
            if n_global >= k_global:
                hasil_c = hitung_kombinasi(n_global, k_global)
                st.success(f"Ada **{hasil_c}** cara pengelompokan/pemilihan.")
                st.markdown(f"**Contoh:** Memilih {k_global} anggota tim dari {n_global} kandidat.")
            else:
                st.error("Input n dan k tidak valid. Koreksi di sidebar.")

    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Peluang (Probability)":
        st.header("3️⃣ Peluang (Probability): Menghubungkan Konsep")
        st.info("Peluang adalah rasio antara banyaknya kejadian yang diinginkan ($n(A)$) dengan total semua kemungkinan ($n(S)$).")
        
        st.subheader("📝 Rumus Dasar Peluang")
        st.latex(r'''P(A) = \frac{n(A)}{n(S)}''')
        
        st.markdown("---")
        
        st.subheader("⚙️ Kalkulator Peluang")
        
        # Input n(S)
        st.markdown("**Langkah 1: Tentukan Ruang Sampel ($n(S)$)**")
        opsi_nS = st.radio(
            "Cara Menentukan $n(S)$:",
            ["Input Manual", "Menggunakan Kombinasi C(n,k)"]
        )

        if opsi_nS == "Input Manual":
            nS = st.number_input("Masukkan Nilai $n(S)$", min_value=1, value=10, key='nS_manual')
        else:
            st.markdown("**(Contoh:** Total kemungkinan mengambil *k* bola dari *n* bola.**)**")
            nS_n = st.number_input("Total Objek (n)", min_value=1, value=10, key='nS_n')
            nS_k = st.number_input("Jumlah Objek yang Diambil (k)", min_value=1, value=3, key='nS_k')
            
            if nS_n >= nS_k:
                nS = hitung_kombinasi(nS_n, nS_k)
                st.code(f"n(S) = C({nS_n}, {nS_k}) = {nS}", language='markdown')
            else:
                st.error("n(S) tidak dapat dihitung: $n < k$")
                nS = 1 # Safety value
                
        st.markdown("---")

        # Input n(A)
        st.markdown("**Langkah 2: Tentukan Banyaknya Kejadian ($n(A)$)**")
        opsi_nA = st.radio(
            "Cara Menentukan $n(A)$:",
            ["Input Manual", "Menggunakan Kombinasi C(n,k)", "Menggunakan Permutasi P(n,k)"]
        )
        
        if opsi_nA == "Input Manual":
            nA = st.number_input("Masukkan Nilai $n(A)$", min_value=0, value=1, key='nA_manual')
        elif opsi_nA == "Menggunakan Kombinasi C(n,k)":
            st.markdown("**(Contoh:** Peluang terambil *k* bola **merah** dari *n* bola merah.**)**")
            nA_n = st.number_input("Total Objek Kejadian (n_A)", min_value=0, value=4, key='nA_n_c')
            nA_k = st.number_input("Jumlah Objek yang Diinginkan (k_A)", min_value=0, value=2, key='nA_k_c')
            
            if nA_n >= nA_k:
                nA = hitung_kombinasi(nA_n, nA_k)
                st.code(f"n(A) = C({nA_n}, {nA_k}) = {nA}", language='markdown')
            else:
                st.error("n(A) tidak dapat dihitung: $n < k$")
                nA = 0 # Safety value
        else: # Menggunakan Permutasi P(n,k)
            st.markdown("**(Contoh:** Peluang terambilnya *k* susunan kartu urut.**)**")
            nA_n = st.number_input("Total Objek Kejadian (n_A)", min_value=0, value=4, key='nA_n_p')
            nA_k = st.number_input("Jumlah Objek yang Diinginkan (k_A)", min_value=0, value=2, key='nA_k_p')
            
            if nA_n >= nA_k:
                nA = hitung_permutasi(nA_n, nA_k)
                st.code(f"n(A) = P({nA_n}, {nA_k}) = {nA}", language='markdown')
            else:
                st.error("n(A) tidak dapat dihitung: $n < k$")
                nA = 0 # Safety value

        st.markdown("---")
        
        # --- Hasil Peluang ---
        st.subheader("✅ Hasil Peluang ($P(A)$)")
        
        col_res, col_vis = st.columns(2)
        
        with col_res:
            st.markdown(f"**Ruang Sampel ($n(S)$):** `{nS}`")
            st.markdown(f"**Banyaknya Kejadian ($n(A)$):** `{nA}`")
            
            if nS > 0 and nA <= nS:
                P_A = nA / nS
                st.success(f"$$P(A) = \\frac{{{nA}}}{{{nS}}} \\approx {P_A:.4f}$$")
            elif nA > nS:
                 st.error("⚠️ n(A) tidak boleh melebihi n(S).")
            else:
                st.error("⚠️ n(S) tidak boleh nol.")

        with col_vis:
            if nS > 0 and nA <= nS:
                st.metric(label="Peluang (Persentase)", value=f"{P_A*100:.2f}%")
                # Visualisasi Bar
                st.progress(P_A, text="Representasi Peluang")

    # --------------------------------------------------------------------------------------------------
    
    elif pilihan == "Perbandingan Konsep":
        st.header("⚖️ Perbandingan Konsep Utama")
        st.warning("**Kunci Utama:** Apakah **Urutan** Penting? (Permutasi vs Kombinasi)")
        
        n, k = st.session_state.n_global, st.session_state.k_global
        st.markdown(f"Input dari sidebar: $n={n}, k={k}$")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Permutasi")
            st.markdown("* **Urutan Penting**")
            if n >= k:
                 P_val = hitung_permutasi(n, k)
                 st.metric(label=f"P({n}, {k})", value=P_val)
            
        with col2:
            st.subheader("Kombinasi")
            st.markdown("* **Urutan Tidak Penting**")
            if n >= k:
                C_val = hitung_kombinasi(n, k)
                st.metric(label=f"C({n}, {k})", value=C_val)
                
        st.markdown("---")
        st.subheader("Peluang")
        st.markdown("Peluang menggunakan Permutasi atau Kombinasi untuk menentukan jumlah $n(A)$ (kejadian) dan $n(S)$ (ruang sampel). Peluang adalah **rasio** dari keduanya.")


if __name__ == "__main__":
    main()
