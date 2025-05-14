import streamlit as st

def hitung_kebutuhan_kalori(umur, tb, bb, jenis_kelamin, aktivitas):
    if jenis_kelamin == "Pria":
        bmr = 66 + (13.7 * bb) + (5 * tb) - (6.8 * umur)
    else:
        bmr = 655 + (9.6 * bb) + (1.8 * tb) - (4.7 * umur)

    faktor_aktivitas = {
        "Sedentari (minim aktivitas)": 1.2,
        "Ringan (olahraga ringan)": 1.375,
        "Sedang (olahraga 3-5 hari/minggu)": 1.55,
        "Berat (olahraga intens)": 1.725,
    }

    return bmr * faktor_aktivitas[aktivitas]

def tampilkan_tentang_aplikasi():
    st.header("Tentang Aplikasi 🌞")
    st.write("""
    Aplikasi ini membantu menghitung kebutuhan kalori dan konsumsi gula ideal berdasarkan
    data pribadi dan tingkat aktivitas harian. Cocok untuk kamu yang ingin hidup lebih sehat! 🍏💪
    Meningkatkan Kesadaran Gizi dan Pola Makan Sehat. Banyak orang belum menyadari berapa banyak gula yang mereka konsumsi setiap hari.
    Aplikasi ini membantu pengguna memahami batas konsumsi gula maksimal dan ideal berdasarkan kondisi tubuh dan aktivitas mereka.
    """)

def tampilkan_pengenalan_kelompok():
    st.header("Pengenalan Kelompok 👩‍💻👨‍💻")
    st.write("""
    Aplikasi ini dikembangkan oleh kelompok 12:

    - *Allyshia Rahma Putri*: 2420570  💻
    - *I Gede Hilmi Krisna Hadinata*: 2420604 🎨
    - *Khaesa Shafa Nuraini*: 2420608 📝
    - *Pramudya Bayu Perkasa*: 2420640  🩵
    - *Rahmawati Syafitri*: 2420645 💻

    Kelompok Kami hadir untuk membantu kamu lebih peduli terhadap pola makan! 😄
    """)

def main():
    # Background Gambar
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                        url("https://images.unsplash.com/photo-1634612831148-03a8550e1d52?w=1200&auto=format&fit=crop&q=60&ixlib=rb-4.1.0");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
        }

        h1, h2, h3, h4, h5, h6, p, label, .css-1cpxqw2, .css-qrbaxs {
            color: white !important;
        }

        .kalkulator-container {
            background-color: rgba(0, 0, 0, 0.75);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .kalkulator-container label, .kalkulator-container span, .kalkulator-container p {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Kalkulator Kebutuhan Gula Harian 🍭")

    menu = st.sidebar.radio("Pilih Menu 🤔", ["Kalkulator Kebutuhan Kalori 🧮", "Tentang Aplikasi 🌞", "Pengenalan Kelompok 👩‍💻👨‍💻"])

    if menu == "Kalkulator Kebutuhan Kalori 🧮":
        st.markdown('<div class="kalkulator-container">', unsafe_allow_html=True)

        umur = st.number_input("Umur (tahun) 🎂", min_value=1, max_value=100, value=25)
        tb = st.number_input("Tinggi Badan (cm) 📏", min_value=50, max_value=250, value=170)
        bb = st.number_input("Berat Badan (kg) ⚖️", min_value=10, max_value=200, value=65)
        jenis_kelamin = st.selectbox("Jenis Kelamin 👦👧", ["Pria", "Wanita"])
        aktivitas = st.selectbox("Tingkat Aktivitas 🏃", [
            "Sedentari (minim aktivitas)",
            "Ringan (olahraga ringan)",
            "Sedang (olahraga 3-5 hari/minggu)",
            "Berat (olahraga intens)"
        ])

        if st.button("Hitung Kebutuhan Gula 🍬"):
            kebutuhan_kalori = hitung_kebutuhan_kalori(umur, tb, bb, jenis_kelamin, aktivitas)
            gula_maks_10 = kebutuhan_kalori * 0.10 / 4
            gula_ideal_5 = kebutuhan_kalori * 0.05 / 4

            st.success(f"Estimasi kebutuhan kalori: {kebutuhan_kalori:.0f} kkal/hari 💪")
            st.info(f"Konsumsi gula maksimal (10% energi): {gula_maks_10:.1f} gram/hari 🍭")
            st.info(f"Saran konsumsi ideal (5% energi): {gula_ideal_5:.1f} gram/hari 🍬")

        st.markdown('</div>', unsafe_allow_html=True)

    elif menu == "Tentang Aplikasi 🌞":
        tampilkan_tentang_aplikasi()

    elif menu == "Pengenalan Kelompok 👩‍💻👨‍💻":
        tampilkan_pengenalan_kelompok()

if __name__ == "__main__":
    main()
