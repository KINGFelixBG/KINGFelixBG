import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Perhitungan Uji Brix",
    layout="centered"
)

# CSS untuk tampilan
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://cdn.pixabay.com/photo/2015/12/22/04/00/molecule-1100683_1280.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .button-slide {
        transition: transform 0.3s ease, background-color 0.3s ease;
    }
    .button-slide:hover {
        transform: translateX(10px);
        background-color: #4CAF50;
    }

    .block-container {
        color: black;
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
    Website ini dibuat untuk membantu memahami konsep dan perhitungan Uji Brix. 
    Dengan fitur-fitur edukasi dan interaktif, pengguna dapat mempelajari:
    - Pengertian Uji Brix
    - Jenis-jenis Uji Brix
    - Alat-alat pembacaan Uji Brix
    - Rumus dan perhitungan nilai Brix
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
        ["Pengertian", "Jenis Uji Brix", "Alat-Alat Pembacaan Uji Brix", "Rumus", "Kalkulator & Validasi"],
        key="uji_brix_menu"
    )

    if sub_menu == "Pengertian":
        st.header("Pengertian Uji Brix")
        st.write("""
        Uji Brix adalah metode untuk menentukan kadar gula terlarut dalam suatu larutan. 
        Nilai Brix dinyatakan dalam bentuk persentase (%), yang merepresentasikan jumlah gram gula dalam 100 ml larutan.
        """)

    elif sub_menu == "Jenis Uji Brix":
        st.header("Jenis Uji Brix")
        st.write("""
        Uji Brix dapat dibagi menjadi beberapa jenis berdasarkan teknik pengukurannya:
        1. **Refraktometri**: Menggunakan refraktometer untuk mengukur pembiasan cahaya.
        2. **Densitometri**: Mengukur kepadatan larutan menggunakan hydrometer.
        3. **Spektrofotometri**: Menggunakan alat spektrofotometer untuk analisis lebih mendalam.
        """)

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

    elif sub_menu == "Rumus":
        st.header("Rumus Menghitung Uji Brix")
        st.write(r"""
        Rumus dasar untuk menghitung nilai Brix adalah:
        \[
        	ext{Brix (\%)} = rac{m_{	ext{gula}}}{m_{	ext{larutan}}} 	imes 100
        \]
        Di mana:
        - \(m_{	ext{gula}}\) adalah massa gula terlarut (dalam gram).
        - \(m_{	ext{larutan}}\) adalah massa total larutan (dalam gram).

        ### Rumus Koreksi Suhu
        Koreksi suhu diperlukan untuk memperbaiki nilai Brix sesuai dengan suhu pengukuran:
        \[
        Brix_{	ext{koreksi}} = Brix_{	ext{awal}} + (T - T_{	ext{referensi}}) 	imes K
        \]
        Di mana:
        - \(T\) adalah suhu pengukuran (°C).
        - \(T_{	ext{referensi}}) adalah suhu referensi (biasanya 20°C).
        - \(K\) adalah koefisien koreksi suhu (standar: 0.03 per °C).
        """)

    elif sub_menu == "Kalkulator & Validasi":
        st.header("Kalkulator Brix & Deteksi Anomali")
        st.markdown("Masukkan data sampel di bawah ini:")

        with st.form("form_brix"):
            jenis_sampel = st.selectbox("Jenis Sampel", ["Pilih", "Madu", "Jus Apel", "Sirup Glukosa", "Air Tebu"])
            nilai_brix = st.number_input("Nilai Brix (%)", min_value=0.0, max_value=100.0, step=0.1)
            suhu = st.number_input("Suhu Sampel (°C)", min_value=-10.0, max_value=120.0, step=0.5)
            submit = st.form_submit_button("Cek Hasil")

        if submit:
            def deteksi_anomali(brix, suhu, jenis_sampel):
                warning = []
                if brix > 85:
                    warning.append("⚠️ Nilai Brix terlalu tinggi untuk larutan biasa.")
                elif brix < 0.5:
                    warning.append("⚠️ Nilai Brix terlalu rendah. Pastikan sampel bukan air murni.")
                if suhu < 0 or suhu > 80:
                    warning.append("⚠️ Suhu di luar batas aman untuk pengujian refraktometer.")
                batas_sampel = {
                    "madu": (70, 85),
                    "jus apel": (10, 15),
                    "sirup glukosa": (20, 45),
                    "air tebu": (15, 25),
                }
                js = jenis_sampel.lower()
                if js in batas_sampel:
                    batas_min, batas_max = batas_sampel[js]
                    if brix < batas_min or brix > batas_max:
                        warning.append(f"⚠️ Nilai Brix tidak sesuai untuk {jenis_sampel.title()} ({batas_min}–{batas_max} °Bx).")
                return warning

            if jenis_sampel == "Pilih":
                st.warning("Silakan pilih jenis sampel terlebih dahulu.")
            else:
                st.subheader("📊 Hasil Analisis:")
                st.write(f"- Jenis Sampel: **{jenis_sampel}**")
                st.write(f"- Nilai Brix: **{nilai_brix} °Bx**")
                st.write(f"- Suhu Sampel: **{suhu} °C**")

                hasil = deteksi_anomali(nilai_brix, suhu, jenis_sampel)
                if hasil:
                    st.error("🚨 Ditemukan Anomali:")
                    for peringatan in hasil:
                        st.write(peringatan)
                else:
                    st.success("✅ Data valid. Tidak ada anomali terdeteksi.")
