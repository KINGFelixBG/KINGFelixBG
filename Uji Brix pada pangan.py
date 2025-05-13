import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Sidebar input
with st.sidebar:
    st.header("Input Parameter")
    brix_awal = st.number_input("Masukkan nilai Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Masukkan suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)
    show_dark_mode = st.checkbox("Aktifkan Mode Gelap")

# Terapkan background
if show_dark_mode:
    # Mode gelap
    st.markdown("""
        <style>
            .stApp {
                background-color: #1e1e1e;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    # Background merah
    st.markdown("""
        <style>
            .stApp {
                background-color: #ff4c4c;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# Judul dan deskripsi
st.title("😚 Uji Brix pada Bahan Pangan 🍕🍟")
st.write("Aplikasi ini membantu menghitung kadar Brix dari larutan gula pada bahan pangan, dengan koreksi suhu.")

# Kalkulasi
if st.button("Hitung Koreksi Brix"):
    suhu_referensi = 20.0
    koreksi_per_derajat = 0.03

    selisih_suhu = suhu - suhu_referensi
    koreksi = selisih_suhu * koreksi_per_derajat
    brix_terkoreksi = brix_awal + koreksi

    st.success(f"Nilai Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
    st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} x {koreksi_per_derajat}) = {brix_terkoreksi:.2f} °Bx")

    # Penilaian kualitas
    if brix_terkoreksi < 10:
        kualitas = "Rendah (contoh: buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (standar industri untuk buah segar)"
    else:
        kualitas = "Tinggi (madu, sirup, atau buah sangat manis)"

    st.info(f"Kategori Kadar Gula: {kualitas}")

# Footer
st.markdown("---")
st.caption("📘 Dibuat dengan Streamlit untuk edukasi uji Brix pada pangan.")



