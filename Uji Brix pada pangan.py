import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# CSS background
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)),
                    url("https://images.unsplash.com/photo-1649783465020-1e0c6f9ced0e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZG9kZGxlcyUyMGJhY2tncm91bmR8ZW58MHx8MHx8fDA%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #111;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar menu
menu = st.sidebar.radio("📂 Menu", ["Informasi Kelompok", "Kalkulator"])

# =========== MENU INFORMASI KEL 4 ===========
if menu == "Informasi Kelompok":
    st.header("Kelompok 4")
    st.markdown("""
**Program Studi:** PMIP  
**Politeknik AKA Bogor**  
**Tahun:** 2025

**Anggota:**
1. Azahra Putrie A  (2420579)
2. Daris Fadillah R (2420585)
3. Muthi'ah Azizah  (2420628)
4. Revan Ar-Rafi    (2420651)
5. Shaqilla Balqies (2420662)
""")
    st.image("https://upload.wikimedia.org/wikipedia/id/8/82/Logo_Politeknik_AKA_Bogor.png")
    st.caption(" Kelompok 4 | Uji Brix, Densitas, dan Gula Larutan")

# =========== MENU KALKULATOR ===========
elif menu == "Kalkulator":
    st.markdown("""
        <marquee behavior="scroll" direction="left" scrollamount="10" style="color:#333; font-size:30px; font-weight:bold;">
            🍫 UJI BRIX PADA BAHAN PANGAN 🍬
        </marquee>
    """, unsafe_allow_html=True)

    st.write("Aplikasi ini menghitung kadar Brix yang telah dikoreksi suhu, estimasi densitas larutan, dan kandungan gula (gram/L).")

    st.header("📥 Masukkan Data")
    brix_awal = st.number_input("Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("🔍 Hitung"):
        suhu_ref = 20.0
        koreksi = (suhu - suhu_ref) * 0.03
        brix_terkoreksi = brix_awal + koreksi

        st.subheader("📌 Koreksi Suhu")
        st.success(f"Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")

        densitas = 0.998 + 0.00385 * (brix_terkoreksi / 10)
        st.subheader("📌 Estimasi Densitas")
        st.info(f"{densitas:.4f} kg/L")

        gula = brix_terkoreksi * densitas * 10
        st.subheader("📌 Estimasi Kandungan Gula")
        st.info(f"{gula:.2f} gram/L")

        st.subheader("📌 Kategori Kadar Gula")
        if brix_terkoreksi < 10:
            st.warning("Rendah (buah belum matang)")
        elif 10 <= brix_terkoreksi <= 15:
            st.warning("Sedang (standar buah segar)")
        else:
            st.warning("Tinggi (madu, sirup, buah sangat manis)")

    with st.expander("📘 Penjelasan Rumus dan Alat"):
        st.markdown("""
### 📌 Rumus Perhitungan

1. **Koreksi Suhu:**
   \nBrix_terkoreksi = Brix_awal + (Suhu - 20) × 0.03

2. **Estimasi Densitas (kg/L):**
   \nDensitas ≈ 0.998 + (Brix / 10 × 0.00385)

3. **Estimasi Kandungan Gula (g/L):**
   \nGula (g/L) = Brix × Densitas × 10

### 🧪 Alat yang Digunakan

- **Refraktometer**: Mengukur Brix secara langsung.
- **Termometer**: Untuk mengetahui suhu larutan.
- **Hidrometer / Piknometer**: Untuk validasi densitas larutan.

### ⚠️ Catatan:
- Rumus ini merupakan pendekatan umum dan dapat bervariasi tergantung jenis larutan.
""")
