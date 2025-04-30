import streamlit as st

# Link GIF animasi laboratory/kimiawi (GIF BARU dari user)
link_lab_gif = "https://media4.giphy.com/media/l0Iyb2pEevoDThkFW/giphy.gif?cid=6c09b952wi2cy0dz894ts6wn0a47it0u8fwi1vl64uggrtmk&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g"

# Simbol-simbol Kimiawi
CHEM_FLASK = "🧪"
CHEM_MICROSCOPE = "🔬"
CHEM_DNA = "🧬"
CHEM_MOLECULE = "⚛️"
CHEM_TESTTUBE = "🧫"
CHEM_BOOK = "📖"
CHEM_TOOLS = "🛠️"
CHEM_GEAR = "⚙️"
CHEM_STAR = "✨"
CHEM_WARNING = "☣️"

# Bahasa support
bahasa_dict = {
    "Indonesia": {
        "title": "Uji Brix Kimia",
        "nav": ["Beranda", "Uji Brix", "Pengertian Kadar Brix", "Nama-nama Alat Refraktometer", "Pengaturan"],
        "pengertian": "Kadar Brix adalah satuan untuk mengukur konsentrasi zat terlarut (umumnya gula) dalam larutan. Satu derajat Brix (°Bx) setara dengan 1 gram sukrosa dalam 100 gram larutan.",
        "alat": [
            "1. Refraktometer Analog",
            "2. Refraktometer Digital",
            "3. Refraktometer Laboratorium",
            "4. Portable Refraktometer",
            "5. Handheld Refraktometer"
        ],
        "pengaturan": "Pilih bahasa aplikasi:",
        "info_nav": "Gunakan menu navigasi di sebelah kiri untuk memulai eksperimen Brix secara kimiawi!",
        "selamat_datang": "Selamat datang di laboratorium virtual! Aplikasi ini membantu menghitung kadar Brix larutan gula pada bahan pangan, dengan koreksi suhu seperti di laboratorium kimia.",
        "masukkan_param": "Masukkan Parameter Uji",
        "masukkan_brix": "Masukkan nilai Brix dari refraktometer (°Bx):",
        "masukkan_suhu": "Masukkan suhu larutan saat pengukuran (°C):",
        "hitung": "Hitung Koreksi Brix",
        "hasil": "Nilai Brix Terkoreksi",
        "kategori": "Kategori Kadar Gula",
        "langkah": "Langkah Perhitungan:",
        "kategori_gula": "Kategori Kadar Gula:",
        "rendah": "Rendah (contoh: buah belum matang)",
        "sedang": "Sedang (standar industri untuk buah segar)",
        "tinggi": "Tinggi (madu, sirup, atau buah sangat manis)",
        "caption": "Dibuat dengan cinta ilmiah di Laboratorium Virtual"
    }
}

# Sidebar Pengaturan Bahasa
if "bahasa" not in st.session_state:
    st.session_state["bahasa"] = "Indonesia"

with st.sidebar:
    st.markdown(f"### {CHEM_GEAR} Pengaturan / Settings")
    bahasa_pilihan = st.selectbox(
        "Pilih Bahasa / Choose Language",
        options=list(bahasa_dict.keys()),
        index=list(bahasa_dict.keys()).index(st.session_state["bahasa"])
    )
    st.session_state["bahasa"] = bahasa_pilihan

teks = bahasa_dict[st.session_state["bahasa"]]

# Sidebar Navigasi dengan simbol Kimiawi (tanpa "Pengaturan" di menu utama)
st.sidebar.title(f"{CHEM_FLASK} Navigasi")
page = st.sidebar.selectbox(
    "Pilih Halaman / Select Menu",
    [
        f"{CHEM_STAR} {teks['nav'][0]}",
        f"{CHEM_TESTTUBE} {teks['nav'][1]}",
        f"{CHEM_BOOK} {teks['nav'][2]}",
        f"{CHEM_TOOLS} {teks['nav'][3]}"
    ]
)

# HALAMAN BERANDA (GIF hanya di halaman ini)
if page == f"{CHEM_STAR} {teks['nav'][0]}":
    st.markdown(f'<div class="title">{CHEM_FLASK} {teks["title"]} {CHEM_MOLECULE}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{CHEM_MICROSCOPE} {teks["info_nav"]} {CHEM_MICROSCOPE}</div>', unsafe_allow_html=True)
    st.image(link_lab_gif, caption="Laboratorium Kimia Animasi", use_column_width=True)
    st.caption(teks["caption"])

# HALAMAN PENGERTIAN KADAR BRIX
elif page == f"{CHEM_BOOK} {teks['nav'][2]}":
    st.title(f"{CHEM_BOOK} {teks['nav'][2]}")
    
    # Pengertian
    st.markdown(f"### {teks['pengertian']}")
    
    # Rumus
    st.markdown("### Rumus Penghitungan Kadar Brix:")
    st.latex(r"""
    B_{koreksi} = B_{awal} + (T_{larutan} - T_{referensi}) \times K
    """)
    st.markdown("""
    - \( B_{koreksi} \): Nilai Brix yang telah dikoreksi.
    - \( B_{awal} \): Nilai awal Brix sebelum koreksi.
    - \( T_{larutan} \): Suhu larutan saat pengukuran (°C).
    - \( T_{referensi} \): Suhu referensi (umumnya 20°C).
    - \( K \): Faktor koreksi (biasanya 0.03 per °C).
    """)

    # Sejarah
    st.markdown("### Sejarah:")
    st.markdown("""
    Kadar Brix pertama kali diperkenalkan oleh Adolf Ferdinand Wenceslaus Brix, seorang ilmuwan Jerman di abad ke-19. 
    Skala ini digunakan untuk menentukan konsentrasi gula dalam larutan dan sekarang menjadi standar di berbagai industri, 
    termasuk makanan, minuman, dan pertanian.
    """)

    # Jenis-jenis Refraktometer
    st.markdown("### Jenis-jenis Refraktometer:")
    for alat in teks["alat"]:
        st.markdown(f"- {alat}")

    # Tabel Koreksi Brix
    st.markdown("### Tabel Koreksi Brix:")
    st.write("""
    Berikut adalah tabel koreksi kadar Brix berdasarkan suhu larutan:

    | Suhu (°C) | Koreksi (°Bx) |
    |-----------|---------------|
    | 15        | -0.15         |
    | 20        | 0.00          |
    | 25        | +0.15         |
    | 30        | +0.30         |
    | 35        | +0.45         |
    | 40        | +0.60         |

    *Catatan: Koreksi dapat bervariasi tergantung pada jenis larutan.*
    """)
