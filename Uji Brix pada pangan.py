import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Tambahkan CSS untuk background cerah dan teks jelas
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

# Sidebar navigasi
menu = st.sidebar.radio("📂 Menu", ["Kalkulator", "Informasi Kelompok"])

# --- Menu: Kalkulator ---
if menu == "Kalkulator":
    # Judul animasi
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

        suhu_referensi = 20.0
        faktor_koreksi = 0.03
        selisih_suhu = suhu - suhu_referensi
        koreksi = selisih_suhu * faktor_koreksi
        brix_terkoreksi = brix_awal + koreksi

        st.subheader("📌 Koreksi Suhu")
        st.success(f"Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Perhitungan: {brix_awal:.2f} + ({suhu:.2f} - {suhu_referensi}) × {faktor_koreksi} = {brix_terkoreksi:.2f} °Bx")

        densitas = 0.998 + (0.00385 * (brix_terkoreksi / 10))

        st.subheader("📌 Estimasi Densitas")
        st.info(f"Densitas larutan (perkiraan): {densitas:.4f} kg/L")
        st.caption(f"Perhitungan: 0.998 + (0.00385 × ({brix_terkoreksi:.2f} ÷ 10)) = {densitas:.4f} kg/L")

        gula_per_liter = brix_terkoreksi * densitas * 10

        st.subheader("📌 Estimasi Kandungan Gula")
        st.info(f"Kandungan gula: {gula_per_liter:.2f} gram/L")
        st.caption(f"Perhitungan: {brix_terkoreksi:.2f} × {densitas:.4f} × 10 = {gula_per_liter:.2f} g/L")

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

- **Refraktometer**: Mengukur Brix.
- **Termometer**: Untuk suhu larutan.
- **Hidrometer / Piknometer**: Validasi densitas.

### ⚠️ Catatan:
- Pendekatan kasar, hasil bisa bervariasi tergantung jenis larutan.
""")

# --- Menu: Informasi Kelompok ---
elif menu == "Informasi Kelompok":
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
    st.image("https://upload.wikimedia.org/wikipedia/id/6/67/Logo_Politeknik_AKA_Bogor.png", width=200, caption="Politeknik AKA Bogor")
    st.caption("© Kelompok 4 | Uji Brix, Densitas, dan Gula Larutan")
