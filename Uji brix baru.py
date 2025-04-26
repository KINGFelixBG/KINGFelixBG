import streamlit as st

# Link GIF animasi laboratory/kimiawi
link_lab_gif = "https://media.giphy.com/media/3orieQEA4hCz5Q3lYk/giphy.gif"

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
    },
    "English": {
        "title": "Chemical Brix Test",
        "nav": ["Home", "Brix Test", "What is Brix Value?", "Types of Refractometers", "Settings"],
        "pengertian": "Brix is a unit to measure the concentration of dissolved substances (mainly sugar) in a solution. One degree Brix (°Bx) equals 1 gram of sucrose in 100 grams of solution.",
        "alat": [
            "1. Analog Refractometer",
            "2. Digital Refractometer",
            "3. Laboratory Refractometer",
            "4. Portable Refractometer",
            "5. Handheld Refractometer"
        ],
        "pengaturan": "Choose your app language:",
        "info_nav": "Use the navigation menu on the left to start your Brix experiment in a chemical laboratory atmosphere!",
        "selamat_datang": "Welcome to the virtual laboratory! This app helps you calculate the Brix level of sugar solutions in food with temperature correction, just like in a chemistry lab.",
        "masukkan_param": "Enter Test Parameters",
        "masukkan_brix": "Enter Brix value from refractometer (°Bx):",
        "masukkan_suhu": "Enter solution temperature at measurement (°C):",
        "hitung": "Calculate Brix Correction",
        "hasil": "Corrected Brix Value",
        "kategori": "Sugar Level Category",
        "langkah": "Calculation Steps:",
        "kategori_gula": "Sugar Level Category:",
        "rendah": "Low (e.g. unripe fruit)",
        "sedang": "Medium (industry standard for fresh fruit)",
        "tinggi": "High (honey, syrup, or very sweet fruit)",
        "caption": "Made with scientific passion in the Virtual Laboratory"
    },
    "Korea": {
        "title": "화학 브릭스 테스트",
        "nav": ["홈", "브릭스 테스트", "브릭스 값이란?", "굴절계 종류", "설정"],
        "pengertian": "브릭스는 용액 내에 녹아 있는 성분(주로 설탕)의 농도를 측정하는 단위입니다. 1 브릭스(°Bx)는 100g의 용액에 1g의 자당이 들어있는 것을 의미합니다.",
        "alat": [
            "1. 아날로그 굴절계",
            "2. 디지털 굴절계",
            "3. 실험실용 굴절계",
            "4. 휴대용 굴절계",
            "5. 핸드헬드 굴절계"
        ],
        "pengaturan": "앱 언어를 선택하세요:",
        "info_nav": "왼쪽의 탐색 메뉴를 사용해 화학 실험실에서 브릭스 실험을 시작하세요!",
        "selamat_datang": "가상 실험실에 오신 것을 환영합니다! 이 앱은 음식 내 설탕 용액의 브릭스 농도를 온도 보정과 함께 계산하는 데 도움이 됩니다.",
        "masukkan_param": "테스트 매개변수 입력",
        "masukkan_brix": "굴절계에서 측정한 브릭스 값(°Bx)을 입력하세요:",
        "masukkan_suhu": "측정 시 용액 온도(°C)를 입력하세요:",
        "hitung": "브릭스 보정 계산",
        "hasil": "보정된 브릭스 값",
        "kategori": "당도 카테고리",
        "langkah": "계산 단계:",
        "kategori_gula": "당도 카테고리:",
        "rendah": "낮음 (예: 덜 익은 과일)",
        "sedang": "중간 (신선한 과일 산업 표준)",
        "tinggi": "높음 (꿀, 시럽 또는 매우 달콤한 과일)",
        "caption": "과학적 열정으로 만든 가상 실험실"
    },
    "China": {
        "title": "化学布里克斯测试",
        "nav": ["首页", "布里克斯测试", "什么是布里克斯值", "折射仪种类", "设置"],
        "pengertian": "布里克斯是用于测量溶液中溶解物质（主要是糖）浓度的单位。1布里克斯（°Bx）等于100克溶液中含有1克蔗糖。",
        "alat": [
            "1. 模拟折射仪",
            "2. 数字折射仪",
            "3. 实验室折射仪",
            "4. 便携式折射仪",
            "5. 手持折射仪"
        ],
        "pengaturan": "请选择应用语言：",
        "info_nav": "使用左侧导航菜单，在化学实验室氛围中开启布里克斯实验！",
        "selamat_datang": "欢迎来到虚拟实验室！本应用可帮助您计算食品中糖溶液的布里克斯值，并进行温度校正。",
        "masukkan_param": "输入测试参数",
        "masukkan_brix": "请输入折射仪测得的布里克斯值（°Bx）：",
        "masukkan_suhu": "请输入测量时溶液温度（°C）：",
        "hitung": "计算布里克斯校正值",
        "hasil": "校正后的布里克斯值",
        "kategori": "糖度分类",
        "langkah": "计算步骤：",
        "kategori_gula": "糖度分类：",
        "rendah": "低（如未成熟水果）",
        "sedang": "中（新鲜水果行业标准）",
        "tinggi": "高（蜂蜜、糖浆或非常甜的水果）",
        "caption": "以科学热情打造的虚拟实验室"
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
    st.markdown(
        """
        <style>
        .title {
            font-size:50px;
            color:#2184b6;
            text-align:center;
            font-weight:bold;
            text-shadow: 2px 2px #145c82;
        }
        .subtitle {
            font-size:22px;
            text-align:center;
            color: #8a8a8a;
        }
        body {
            background-color: #eef4fa;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f'<div class="title">{CHEM_FLASK} {teks["title"]} {CHEM_MOLECULE}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{CHEM_MICROSCOPE} {teks["info_nav"]} {CHEM_MICROSCOPE}</div>', unsafe_allow_html=True)
    st.image(link_lab_gif, caption="Laboratorium Kimia Animasi", use_column_width=True)
    st.markdown("---")
    st.info(f"{CHEM_DNA} {teks['info_nav']} {CHEM_DNA}")
    st.markdown("---")
    st.caption(teks["caption"])

# HALAMAN UJI BRIX
elif page == f"{CHEM_TESTTUBE} {teks['nav'][1]}":
    st.title(f"{CHEM_TESTTUBE} {teks['nav'][1]} {CHEM_FLASK}")
    st.write(teks["selamat_datang"])
    st.header(f"{CHEM_TOOLS} {teks['masukkan_param']}")
    # GIF TIDAK MUNCUL DI SINI
    brix_awal = st.number_input(f"{CHEM_MOLECULE} {teks['masukkan_brix']}", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input(f"{CHEM_WARNING} {teks['masukkan_suhu']}", min_value=0.0, max_value=100.0, step=0.1)
    if st.button(f"{CHEM_FLASK} {teks['hitung']}"):
        suhu_referensi = 20.0
        koreksi_per_derajat = 0.03
        selisih_suhu = suhu - suhu_referensi
        koreksi = selisih_suhu * koreksi_per_derajat
        brix_terkoreksi = brix_awal + koreksi
        st.success(f"{CHEM_MOLECULE} {teks['hasil']}: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} × {koreksi_per_derajat}) = {brix_terkoreksi:.2f} °Bx")
        # Kategori kadar gula
        if brix_terkoreksi < 10:
            kualitas = f"{CHEM_TESTTUBE} {teks['rendah']}"
        elif 10 <= brix_terkoreksi <= 15:
            kualitas = f"{CHEM_FLASK} {teks['sedang']}"
        else:
            kualitas = f"{CHEM_DNA} {teks['tinggi']}"
        st.info(f"{CHEM_MOLECULE} {teks['kategori']}: {kualitas}")
        st.markdown(f"### {teks['langkah']}")
        st.markdown(f"""
        1. **Selisih Suhu:**<br>
           {suhu:.2f} - 20.00 = {selisih_suhu:.2f} °C

        2. **Koreksi Brix:**<br>
           {selisih_suhu:.2f} × 0.03 = {koreksi:.2f} °Bx

        3. **Brix Terkoreksi:**<br>
           {brix_awal:.2f} + {koreksi:.2f} = {brix_terkoreksi:.2f} °Bx
        """, unsafe_allow_html=True)
        st.markdown(f"#### {teks['kategori_gula']}")
        st.markdown(f"""
        - {CHEM_TESTTUBE} **{teks['rendah']}**
        - {CHEM_FLASK} **{teks['sedang']}**
        - {CHEM_DNA} **{teks['tinggi']}**
        """, unsafe_allow_html=True)

# HALAMAN PENGERTIAN KADAR BRIX
elif page == f"{CHEM_BOOK} {teks['nav'][2]}":
    st.title(f"{CHEM_BOOK} {teks['nav'][2]}")
    st.markdown(f"#### {teks['pengertian']}")

# HALAMAN NAMA ALAT REFRAKTOMETER
elif page == f"{CHEM_TOOLS} {teks['nav'][3]}":
    st.title(f"{CHEM_TOOLS} {teks['nav'][3]}")
    st.markdown("####")
    for alat in teks["alat"]:
        st.markdown(f"- {alat}")
