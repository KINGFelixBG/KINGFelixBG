import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Uji Brix Adventure", layout="centered")

st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Uji Brix"])

if page == "Beranda":
    # Setup refresh otomatis tiap 3 detik
    count = st_autorefresh(interval=3000, limit=None, key="slide_refresh")

    # Daftar gambar karakter
    images = [
        {
            "url": "https://i.ibb.co/QdJ6KHZ/pixel-scientist.png",
            "caption": "Ilmuwan Kecil - Si Peneliti Brix"
        },
        {
            "url": "https://i.ibb.co/whR1Zn7/pixel-fruit-man.png",
            "caption": "Orang Buah - Sang Pembawa Manis"
        }
    ]

    # Pilih gambar sesuai counter
    current_image = images[count % len(images)]

    # CSS untuk styling
    st.markdown(
        """
        <style>
        .title {
            font-size:50px;
            color:#00bcd4;
            text-align:center;
            font-weight:bold;
        }
        .subtitle {
            font-size:22px;
            text-align:center;
            color: #666;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Tampilan Title dan Subtitle
    st.markdown('<div class="title">Uji Brix Adventure</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Petualangan Dimulai!</div>', unsafe_allow_html=True)

    # Gambar pixel karakter
    st.image(current_image["url"], caption=current_image["caption"], use_column_width=True)

    st.markdown("---")

    # Tombol mulai (redirect ke Uji Brix manual pakai sidebar)
    st.info("Gunakan navigasi di sebelah kiri untuk memulai Uji Brix!")

    st.markdown("---")
    st.caption("Made with ❤️ in Streamlit Pixel Retro Adventure")

# Halaman Uji Brix
elif page == "Uji Brix":
    st.title("🧪 Uji Brix pada Bahan Pangan")

    st.write("""
    Aplikasi ini membantu menghitung kadar Brix dari larutan gula pada bahan pangan, dengan koreksi suhu.
    """)

    # Sidebar Input
    st.header("Masukkan Parameter Uji")

    brix_awal = st.number_input("Masukkan nilai Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Masukkan suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("Hitung Koreksi Brix"):
        suhu_referensi = 20.0
        koreksi_per_derajat = 0.03

        selisih_suhu = suhu - suhu_referensi
        koreksi = selisih_suhu * koreksi_per_derajat
        brix_terkoreksi = brix_awal + koreksi

        st.success(f"Nilai Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} × {koreksi_per_derajat}) = {brix_terkoreksi:.2f} °Bx")

        # Penilaian kualitas bahan pangan
        if brix_terkoreksi < 10:
            kualitas = "Rendah (contoh: buah belum matang)"
        elif 10 <= brix_terkoreksi <= 15:
            kualitas = "Sedang (standar industri untuk buah segar)"
        else:
            kualitas = "Tinggi (madu, sirup, atau buah sangat manis)"

        st.info(f"Kategori Kadar Gula: {kualitas}")

    st.markdown("---")
    st.caption("📘 Dibuat dengan Streamlit untuk edukasi uji Brix pada pangan.")
    
