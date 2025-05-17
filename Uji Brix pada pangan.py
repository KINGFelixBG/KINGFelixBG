import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Pilihan mode terang/gelap
mode = st.sidebar.radio("🌓 Pilih Mode Tampilan:", ["Terang", "Gelap"])

# CSS berdasarkan mode
if mode == "Gelap":
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
                        url("https://images.unsplash.com/photo-1533628635777-112b2239b1c7?w=600&auto=format&fit=crop&q=60");
            background-size: cover;
            background-position: center;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
    teks_warna = "white"
else:
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)),
                        url("https://images.unsplash.com/photo-1649783465020-1e0c6f9ced0e?w=600&auto=format&fit=crop&q=60");
            background-size: cover;
            background-position: center;
            color: #111;
        }
        </style>
    """, unsafe_allow_html=True)
    teks_warna = "#111"

# Navigasi menu
menu = st.sidebar.radio("📂 Navigasi", ["Informasi Kelompok", "Kalkulator"])

# --- INFORMASI KELOMPOK (halaman 1) ---
if menu == "Informasi Kelompok":
    st.markdown(f"<h1 style='color:{teks_warna}; text-align:center;'>👥 Informasi Kelompok</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <p style="color:{teks_warna}; font-size:18px; font-weight:bold;">
    Kelompok 4<br>
    PRODI PMIP POLITEKNIK AKA BOGOR 2025
    </p>
    <ul style="color:{teks_warna}; font-size:16px;">
1. Azahra Putrie A  (2420579)
2. Daris Fadillah R (2420585)
3. Muthi'ah Azizah  (2420628)
4. Revan Ar-Rafi    (2420651)
5. Shaqilla Balqies (2420662)
    </ul>
    """, unsafe_allow_html=True)

# --- KALKULATOR (halaman 2) ---
elif menu == "Kalkulator":
    st.markdown(f"""
        <marquee behavior="scroll" direction="left" scrollamount="10" style="color:{teks_warna}; font-size:30px; font-weight:bold;">
            🍫 UJI BRIX PADA BAHAN PANGAN 🍬
        </marquee>
    """, unsafe_allow_html=True)

    st.write(f'<p style="color:{teks_warna}; font-weight:bold;">Aplikasi ini menghitung kadar Brix yang telah dikoreksi suhu, estimasi densitas larutan, dan kandungan gula (gram/L).</p>', unsafe_allow_html=True)

    st.header("📥 Masukkan Data")
    brix_awal = st.number_input("Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("🔍 Hitung"):
        # Koreksi suhu
        suhu_referensi = 20.0
        faktor_koreksi = 0.03
        selisih_suhu = suhu - suhu_referensi
        brix_terkoreksi = brix_awal + selisih_suhu * faktor_koreksi

        st.subheader("📌 Koreksi Suhu")
        st.success(f"Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Perhitungan: {brix_awal:.2f} + ({suhu:.2f} - {suhu_referensi}) × {faktor_koreksi} = {brix_terkoreksi:.2f} °Bx")

        # Estimasi densitas (kg/L)
        densitas = 0.998 + (0.00385 * (brix_terkoreksi / 10))
        st.subheader("📌 Estimasi Densitas")
        st.info(f"Densitas larutan (perkiraan): {densitas:.4f} kg/L")
        st.caption(f"Perhitungan: 0.998 + (0.00385 × ({brix_terkoreksi:.2f} ÷ 10)) = {densitas:.4f} kg/L")

        # Estimasi kandungan gula (g/L)
        gula_per_liter = brix_terkoreksi * densitas * 10
        st.subheader("📌 Estimasi Kandungan Gula")
        st.info(f"Kandungan gula: {gula_per_liter:.2f} gram/L")
        st.caption(f"Perhitungan: {brix_terkoreksi:.2f} × {densitas:.4f} × 10 = {gula_per_liter:.2f} g/L")

        # Kategori kadar gula
        st.subheader("📌 Kategori Kadar Gula")
        if brix_terkoreksi < 10:
            kualitas = "Rendah (buah belum matang)"
        elif 10 <= brix_terkoreksi <= 15:
            kualitas = "Sedang (standar buah segar)"
        else:
            kualitas = "Tinggi (madu, sirup, buah sangat manis)"
        st.warning(f"Kategori: {kualitas}")

    with st.expander("📘 Penjelasan Rumus dan Alat"):
        st.markdown(f"""
### 📌 Rumus Perhitungan

1. **Koreksi Suhu:**
   \nBrix_terkoreksi = Brix_awal + (Suhu - 20) * 0.03

2. **Estimasi Densitas (kg/L):**
   \nDensitas = 0.998 + (Brix / 10 * 0.00385)

3. **Estimasi Kandungan Gula (g/L):**
   \nGula (g/L) = Brix × Densitas × 10

### 🧪 Alat yang Digunakan

- **Refraktometer**: Mengukur Brix secara langsung.
- **Termometer**: Untuk mengetahui suhu larutan.
- **Hidrometer / Piknometer**: Untuk validasi densitas larutan.

### ⚠️ Catatan:
- Rumus ini merupakan pendekatan umum dan dapat bervariasi tergantung jenis larutan.
        """, unsafe_allow_html=True)

# Footer
st.caption("📗 Dibuat oleh Kelompok 4 - PMIP POLITEKNIK AKA BOGOR 2025")
