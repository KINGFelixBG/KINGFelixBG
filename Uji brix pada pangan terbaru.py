import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Perhitungan Uji Brix",
    layout="centered"
)

# CSS untuk efek geser pada navigasi dan karakter kartun sebagai background
st.markdown(
    """
    <style>
    /* Background dengan karakter zat kimia */
    .stApp {
        background-image: url("https://cdn.pixabay.com/photo/2015/12/22/04/00/molecule-1100683_1280.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Efek geser pada tombol navigasi */
    .button-slide {
        transition: transform 0.3s ease, background-color 0.3s ease;
    }
    .button-slide:hover {
        transform: translateX(10px);
        background-color: #4CAF50;
    }

    /* Teks warna putih agar kontras dengan background */
    .block-container {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigasi
st.sidebar.title("Navigasi")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Beranda", "Pengaturan", "UJI BRIX"],
    key="main_menu"
)

# Beranda
if menu == "Beranda":
    st.title("Selamat Datang di Website Perhitungan Uji Brix")
    st.markdown("---")
    st.write("""
    Website ini dibuat oleh **Kelompok 3 Kimia Terapan** untuk membantu memahami konsep dan perhitungan Uji Brix. 
    Dengan fitur-fitur edukasi dan interaktif, pengguna dapat mempelajari:
    - Pengertian Uji Brix
    - Jenis-jenis Uji Brix
    - Alat-alat pembacaan Uji Brix
    - Rumus dan perhitungan nilai Brix
    
    **Anggota Kelompok:**
    - Felix
    - Rahmat
    - Sinta
    - Diah
    - Bagas
    """)

# Pengaturan
elif menu == "Pengaturan":
    st.title("Pengaturan")
    st.markdown("---")
    bahasa = st.radio("Pilih Bahasa", ["Bahasa Indonesia", "English"], key="language")
    if bahasa == "Bahasa Indonesia":
        st.success("Bahasa diatur ke Bahasa Indonesia.")
    elif bahasa == "English":
        st.success("Language set to English.")

# UJI BRIX
elif menu == "UJI BRIX":
    st.title("UJI BRIX")
    st.markdown("---")
    sub_menu = st.radio(
        "Pilih Sub-Menu:",
        ["Pengertian", "Jenis Uji Brix", "Alat-Alat Pembacaan Uji Brix", "Rumus"],
        key="uji_brix_menu"
    )

    # Sub-menu: Pengertian
    if sub_menu == "Pengertian":
        st.header("Pengertian Uji Brix")
        st.write("""
        Uji Brix adalah metode untuk menentukan kadar gula terlarut dalam suatu larutan. 
        Nilai Brix dinyatakan dalam bentuk persentase (%), yang merepresentasikan jumlah gram gula dalam 100 ml larutan.
        """)

    # Sub-menu: Jenis Uji Brix
    elif sub_menu == "Jenis Uji Brix":
        st.header("Jenis Uji Brix")
        st.write("""
        Uji Brix dapat dibagi menjadi beberapa jenis berdasarkan teknik pengukurannya:
        1. **Refraktometri**: Menggunakan refraktometer untuk mengukur pembiasan cahaya.
        2. **Densitometri**: Mengukur kepadatan larutan menggunakan hydrometer.
        3. **Spektrofotometri**: Menggunakan alat spektrofotometer untuk analisis lebih mendalam.
        """)

    # Sub-menu: Alat-Alat Pembacaan Uji Brix
    elif sub_menu == "Alat-Alat Pembacaan Uji Brix":
        st.header("Alat-Alat Pembacaan Uji Brix")
        st.write("""
        Berikut adalah alat-alat yang umum digunakan untuk pembacaan nilai Brix:
        1. **Refraktometer**:
           - Alat optik yang mengukur indeks bias larutan.
           - Terdiri dari refraktometer manual dan digital.
        2. **Hydrometer Brix**:
           - Mengukur densitas larutan untuk menghitung kadar gula.
           - Umumnya digunakan dalam industri besar.
        3. **Digital Brix Meter**:
           - Alat elektronik presisi tinggi untuk nilai Brix.
           - Cocok untuk analisis cepat dan akurat.
        """)

    # Sub-menu: Rumus
    elif sub_menu == "Rumus":
        st.header("Rumus Menghitung Uji Brix")
        st.write("""
        Rumus dasar untuk menghitung nilai Brix adalah:
        \[
        Brix (\%) = \frac{m_{gula}}{m_{larutan}} \times 100
        \]
        Di mana:
        - \(m_{gula}\) adalah massa gula terlarut (dalam gram).
        - \(m_{larutan}\) adalah massa total larutan (dalam gram).

        ### Rumus Koreksi Suhu
        Koreksi suhu diperlukan untuk memperbaiki nilai Brix sesuai dengan suhu pengukuran:
        \[
        Brix_{koreksi} = Brix_{awal} + (T - T_{referensi}) \times K
        \]
        Di mana:
        - \(T\) adalah suhu pengukuran (°C).
        - \(T_{referensi}\) adalah suhu referensi (biasanya 20°C).
        - \(K\) adalah koefisien koreksi suhu (standar: 0.03 per °C).
        """)
