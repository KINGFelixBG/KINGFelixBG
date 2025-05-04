import streamlit as st

# Set up the title and theme
st.title("Kalkulator Uji Brix")
st.subheader("Tema: Kimia - Perhitungan Uji Brix")
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Opsi", ["Pengertian", "Jenis Alat", "Rumus", "Kalkulator", "Penjelasan Hasil"])

# Pengertian Uji Brix
if menu == "Pengertian":
    st.header("Pengertian Uji Brix")
    st.write("""
    Uji Brix adalah metode untuk mengukur kadar gula terlarut dalam suatu larutan, 
    biasanya digunakan dalam industri makanan dan minuman, seperti jus buah, minuman ringan, dan lainnya. 
    Nilai Brix dinyatakan dalam bentuk persentase (%), yang merepresentasikan jumlah gram gula dalam 100 ml larutan.
    """)

# Jenis-Jenis Alat Uji Brix
elif menu == "Jenis Alat":
    st.header("Jenis-Jenis Alat Uji Brix")
    st.write("""
    Beberapa jenis alat yang digunakan untuk uji Brix adalah:
    1. **Refraktometer**: Alat optik yang menggunakan prinsip pembiasan cahaya.
    2. **Hydrometer Brix**: Alat yang mengukur densitas larutan untuk mengestimasi kadar gula.
    3. **Digital Brix Meter**: Alat elektronik yang memberikan hasil lebih presisi dan cepat.
    """)

# Rumus Perhitungan Uji Brix
elif menu == "Rumus":
    st.header("Rumus Perhitungan Uji Brix")
    st.write("""
    Rumus dasar untuk uji Brix adalah:
    \[
    Brix (\%) = \frac{m_{gula}}{m_{larutan}} \times 100
    \]
    Di mana:
    - \(m_{gula}\) adalah massa gula terlarut (dalam gram).
    - \(m_{larutan}\) adalah massa total larutan (dalam gram).
    """)

# Kalkulator Uji Brix
elif menu == "Kalkulator":
    st.header("Kalkulator Uji Brix")
    st.write("Masukkan data untuk menghitung nilai Brix:")
    
    # Input data
    mass_gula = st.number_input("Masukkan massa gula terlarut (gram):", min_value=0.0, step=0.1)
    mass_larutan = st.number_input("Masukkan massa total larutan (gram):", min_value=0.1, step=0.1)
    
    if st.button("Hitung Brix"):
        # Perhitungan
        brix = (mass_gula / mass_larutan) * 100
        st.success(f"Nilai Brix: {brix:.2f} %")

# Penjelasan Hasil Perhitungan
elif menu == "Penjelasan Hasil":
    st.header("Penjelasan Hasil Perhitungan Uji Brix")
    st.write("""
    Hasil perhitungan Brix memberikan informasi tentang kadar gula dalam suatu larutan.
    - **Nilai Brix tinggi** menunjukkan bahwa larutan tersebut memiliki kadar gula yang tinggi, seperti sari buah murni atau sirup.
    - **Nilai Brix rendah** menunjukkan bahwa larutan tersebut memiliki kadar gula rendah, seperti air minum atau jus yang diencerkan.
    """)
    st.write("""
    **Contoh Aplikasi**:
    - Dalam industri makanan dan minuman, nilai Brix digunakan untuk memastikan konsistensi rasa dan kualitas produk.
    - Dalam bidang pertanian, nilai Brix digunakan untuk mengevaluasi kualitas hasil panen, seperti buah dan sayuran.
    """)
