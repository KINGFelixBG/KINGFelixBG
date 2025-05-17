import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# CSS & JS: Ganti ikon panah dengan tombol "Menu"
st.markdown("""
    <style>
    /* Background terang atau gelap menyesuaikan */
    .stApp {
        background: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)),
                    url("https://images.unsplash.com/photo-1649783465020-1e0c6f9ced0e?w=800&auto=format&fit=crop&q=60");
        background-size: cover;
        background-position: center;
        color: #111;
        font-weight: bold;
    }

    /* Sembunyikan panah default sidebar */
    [data-testid="collapsedControl"] {
        visibility: hidden;
    }

    /* Tombol Menu kustom */
    #custom-menu-button {
        position: fixed;
        top: 10px;
        left: 10px;
        background-color: #4CAF50;
        color: white;
        padding: 6px 14px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        z-index: 9999;
        font-weight: bold;
    }
    </style>

    <script>
    function toggleSidebar() {
        const sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
        const toggleBtn = window.parent.document.querySelector('[data-testid="collapsedControl"]');
        if (sidebar && toggleBtn) {
            toggleBtn.click();  // Klik tombol panah default
        }
    }

    // Tambahkan tombol kustom jika belum ada
    window.addEventListener('DOMContentLoaded', (event) => {
        const existingButton = window.parent.document.getElementById("custom-menu-button");
        if (!existingButton) {
            const btn = document.createElement("button");
            btn.innerHTML = "📂 Menu";
            btn.id = "custom-menu-button";
            btn.onclick = toggleSidebar;
            window.parent.document.body.appendChild(btn);
        }
    });
    </script>
""", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    menu = st.radio("Pilih Menu:", ["Tentang", "Kalkulator Brix"])

# Judul animasi di atas halaman
st.markdown("""
    <marquee behavior="scroll" direction="left" scrollamount="10" style="color:#333; font-size:30px; font-weight:bold;">
        🍫 UJI BRIX PADA BAHAN PANGAN 🍬
    </marquee>
""", unsafe_allow_html=True)

# Halaman 1: Tentang
elif menu == "Tentang":
    st.header("KELOMPOK 4")
    st.markdown("""
    ### PRODI PMIP  
    **POLITEKNIK AKA BOGOR - 2025**

    #### Anggota Kelompok:
1. Azahra Putrie A  (2420579)
2. Daris Fadillah R (2420585)
3. Muthi'ah Azizah  (2420628)
4. Revan Ar-Rafi    (2420651)
5. Shaqilla Balqies (2420662)
 st.image("https://upload.wikimedia.org/wikipedia/id/8/82/Logo_Politeknik_AKA_Bogor.png")
    
# Footer
st.caption("📗 Dibuat oleh Kelompok 4 | PMIP POLITEKNIK AKA BOGOR 2025")


# Halaman 2: Kalkulator
if menu == "Kalkulator Brix":
    st.write("Aplikasi ini menghitung kadar Brix yang telah dikoreksi suhu, estimasi densitas larutan, dan kandungan gula (gram/L).")
    
    st.header("📥 Masukkan Data")
    brix_awal = st.number_input("Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("🔍 Hitung"):

        # Koreksi Suhu
        suhu_referensi = 20.0
        faktor_koreksi = 0.03
        selisih_suhu = suhu - suhu_referensi
        koreksi = selisih_suhu * faktor_koreksi
        brix_terkoreksi = brix_awal + koreksi

        st.subheader("📌 Koreksi Suhu")
        st.success(f"Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Perhitungan: {brix_awal:.2f} + ({suhu:.2f} - {suhu_referensi}) × {faktor_koreksi} = {brix_terkoreksi:.2f} °Bx")

        # Estimasi Densitas
        densitas = 0.998 + (0.00385 * (brix_terkoreksi / 10))

        st.subheader("📌 Estimasi Densitas")
        st.info(f"Densitas larutan (perkiraan): {densitas:.4f} kg/L")
        st.caption(f"Perhitungan: 0.998 + (0.00385 × ({brix_terkoreksi:.2f} ÷ 10)) = {densitas:.4f} kg/L")

        # Estimasi Gula
        gula_per_liter = brix_terkoreksi * densitas * 10

        st.subheader("📌 Estimasi Kandungan Gula")
        st.info(f"Kandungan gula: {gula_per_liter:.2f} gram/L")
        st.caption(f"Perhitungan: {brix_terkoreksi:.2f} × {densitas:.4f} × 10 = {gula_per_liter:.2f} g/L")

        # Kategori Kadar Gula
        st.subheader("📌 Kategori Kadar Gula")
        if brix_terkoreksi < 10:
            kualitas = "Rendah (buah belum matang)"
        elif 10 <= brix_terkoreksi <= 15:
            kualitas = "Sedang (standar buah segar)"
        else:
            kualitas = "Tinggi (madu, sirup, buah sangat manis)"
        st.warning(f"Kategori: {kualitas}")

    with st.expander("📘 Penjelasan Rumus dan Alat"):
        st.markdown("""
        ### 📌 Rumus Perhitungan

        1. **Koreksi Suhu:**  
        Brix_terkoreksi = Brix_awal + (Suhu - 20) × 0.03

        2. **Estimasi Densitas (kg/L):**  
        Densitas ≈ 0.998 + (Brix / 10 × 0.00385)

        3. **Estimasi Kandungan Gula (g/L):**  
        Gula (g/L) = Brix × Densitas × 10

        ### 🧪 Alat yang Digunakan

        - **Refraktometer**: Mengukur Brix secara langsung.  
        - **Termometer**: Untuk mengetahui suhu larutan.  
        - **Hidrometer / Piknometer**: Untuk validasi densitas larutan.

        ### ⚠️ Catatan:
        Rumus ini merupakan pendekatan umum dan dapat bervariasi tergantung jenis larutan.
        """) 

