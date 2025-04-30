import streamlit as st

# Link GIF animasi laboratory/kimiawi
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

# Sidebar Navigasi dengan simbol Kimiawi
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

# HALAMAN BERANDA
if page == f"{CHEM_STAR} {teks['nav'][0]}":
    st.markdown(f'<div class="title">{CHEM_FLASK} {teks["title"]} {CHEM_MOLECULE}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{CHEM_MICROSCOPE} {teks["info_nav"]} {CHEM_MICROSCOPE}</div>', unsafe_allow_html=True)
    st.image(link_lab_gif, caption="Laboratorium Kimia Animasi", use_column_width=True)
    st.caption(teks["caption"])

# HALAMAN UJI BRIX
elif page == f"{CHEM_TESTTUBE} {teks['nav'][1]}":
    st.title(f"{CHEM_TESTTUBE} {teks['nav'][1]} {CHEM_FLASK}")
    st.write(teks["selamat_datang"])
    st.header(f"{CHEM_TOOLS} {teks['masukkan_param']}")
    brix_awal = st.number_input(f"{CHEM_MOLECULE} {teks['masukkan_brix']}", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input(f"{CHEM_WARNING} {teks['masukkan_suhu']}", min_value=0.0, max_value=100.0, step=0.1)
    if st.button(f"{CHEM_FLASK} {teks['hitung']}"):
        suhu_referensi = 20.0
        koreksi_per_derajat = 0.03
        selisih_suhu = suhu - suhu_referensi
        koreksi = selisih_suhu * koreksi_per_derajat
        brix_terkoreksi = brix_awal + koreksi
        st.success(f"{CHEM_MOLECULE} {teks['hasil']}: {brix_terkoreksi:.2f} °Bx")
        if brix_terkoreksi < 10:
            kualitas = f"{CHEM_TESTTUBE} {teks['rendah']}"
        elif 10 <= brix_terkoreksi <= 15:
            kualitas = f"{CHEM_FLASK} {teks['sedang']}"
        else:
            kualitas = f"{CHEM_DNA} {teks['tinggi']}"
        st.info(f"{CHEM_MOLECULE} {teks['kategori']}: {kualitas}")

# HALAMAN PENGERTIAN KADAR BRIX
elif page == f"{CHEM_BOOK} {teks['nav'][2]}":
    st.title(f"{CHEM_BOOK} {teks['nav'][2]}")
    st.markdown(f"### {teks['pengertian']}")
    st.markdown("### Rumus Penghitungan Kadar Brix:")
    st.latex(r"B_{koreksi} = B_{awal} + (T_{larutan} - T_{referensi}) \times K")
    st.markdown("### Sejarah:")
    st.markdown("Diperkenalkan oleh Adolf Ferdinand Wenceslaus Brix.")

# HALAMAN NAMA ALAT REFRAKTOMETER
elif page == f"{CHEM_TOOLS} {teks['nav'][3]}":
    st.title(f"{CHEM_TOOLS} {teks['nav'][3]}")
    for alat in teks["alat"]:
        st.markdown(f"- {alat}")
