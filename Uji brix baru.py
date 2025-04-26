import streamlit as st

# Link GIF animasi Steve Minecraft yang Anda berikan
link_steve_gif = "https://media4.giphy.com/media/OUUnxL2NbwNuX16EfK/giphy.gif?cid=6c09b952woyzjs8sgsv2fjy3nl229cu65fl6ilj6l1dl4my7&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g"

# Link stiker langsung ke gambar
link_stiker = "https://i.ibb.co/987t0F9/minecraft-scientist-strawberry.png"

# Simbol-simbol Minecraft
MINECRAFT_PICKAXE = "⛏️"
MINECRAFT_APPLE = "🍏"
MINECRAFT_DIAMOND = "💎"
MINECRAFT_CREEPER = "🟩"
MINECRAFT_BLOCK = "🟫"
MINECRAFT_HEART = "❤️"
MINECRAFT_GOLD = "🟨"
MINECRAFT_REDSTONE = "🔴"

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix Adventure", layout="centered")

# Sidebar Navigasi dengan simbol Minecraft
st.sidebar.title(f"{MINECRAFT_BLOCK} Navigasi Dunia Minecraft")
page = st.sidebar.selectbox("Pilih Halaman", [f"{MINECRAFT_DIAMOND} Beranda", f"{MINECRAFT_PICKAXE} Uji Brix"])

# Halaman Beranda
if page == f"{MINECRAFT_DIAMOND} Beranda":
    # Custom CSS
    st.markdown(
        """
        <style>
        .title {
            font-size:50px;
            color:#5e9c36;
            text-align:center;
            font-weight:bold;
            text-shadow: 2px 2px #3c6218;
        }
        .subtitle {
            font-size:22px;
            text-align:center;
            color: #8a8a8a;
        }
        body {
            background-color: #f3f4f6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Judul dengan simbol Minecraft
    st.markdown(f'<div class="title">{MINECRAFT_PICKAXE} Uji Brix Adventure {MINECRAFT_CREEPER}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{MINECRAFT_APPLE} Bersama Ilmuwan Kecil & Creeper Buah! {MINECRAFT_APPLE}</div>', unsafe_allow_html=True)

    # Tampilkan animasi GIF Steve Minecraft
    st.image(link_steve_gif, caption="Steve si maniz", use_container_width=True)
    
    st.image(link_stiker, caption="Minecraft Scientist Strawberry", use_container_width=True)
    st.markdown("---")

    st.info(f"{MINECRAFT_GOLD} Gunakan menu navigasi di sebelah kiri untuk memulai petualangan Uji Brix di dunia Minecraft! {MINECRAFT_PICKAXE}")

    st.markdown("---")
    st.caption(f"Made with {MINECRAFT_HEART} in Minecraft Pixel Adventure")

# Halaman Uji Brix
elif page == f"{MINECRAFT_PICKAXE} Uji Brix":
    st.title(f"{MINECRAFT_PICKAXE} Uji Brix pada Bahan Pangan {MINECRAFT_APPLE}")

    st.write(f"""
    Selamat datang di dunia Minecraft! Aplikasi ini membantu menghitung kadar Brix larutan gula pada bahan pangan,
    dengan koreksi suhu. Cobalah uji kadar gula pada madu Creeper atau buah Blokmanis! {MINECRAFT_CREEPER}
    """)

    # Input parameter
    st.header(f"{MINECRAFT_BLOCK} Masukkan Parameter Uji")

    # Input nilai Brix awal dan suhu pengukuran
    brix_awal = st.number_input(f"{MINECRAFT_DIAMOND} Masukkan nilai Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input(f"{MINECRAFT_REDSTONE} Masukkan suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

    if st.button(f"{MINECRAFT_PICKAXE} Hitung Koreksi Brix"):
        # Parameter tetap
        suhu_referensi = 20.0
        koreksi_per_derajat = 0.03

        # Perhitungan
        selisih_suhu = suhu - suhu_referensi
        koreksi = selisih_suhu * koreksi_per_derajat
        brix_terkoreksi = brix_awal + koreksi

        st.success(f"{MINECRAFT_DIAMOND} Nilai Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} × {koreksi_per_derajat}) = {brix_terkoreksi:.2f} °Bx")

        # Penilaian kualitas bahan pangan
        if brix_terkoreksi < 10:
            kualitas = f"{MINECRAFT_BLOCK} Rendah (contoh: buah belum matang)"
        elif 10 <= brix_terkoreksi <= 15:
            kualitas = f"{MINECRAFT_APPLE} Sedang (standar industri untuk buah segar)"
        else:
            kualitas = f"{MINECRAFT_GOLD} Tinggi (madu, sirup, atau buah sangat manis)"

        st.info(f"{MINECRAFT_HEART} Kategori Kadar Gula: {kualitas}")

        # Penjelasan lengkap langkah perhitungan
        st.markdown("### Langkah Perhitungan:")
        st.markdown(f"""
        1. **Hitung Selisih Suhu:**
           <br>
           Selisih Suhu = Suhu Pengukuran - Suhu Referensi  
           Dalam kasus ini:  
           **{suhu:.2f} - {suhu_referensi:.2f} = {selisih_suhu:.2f} °C**

        2. **Hitung Koreksi Brix:**  
           Koreksi = Selisih Suhu × Koreksi per Derajat Celsius  
           Dalam kasus ini:  
           **{selisih_suhu:.2f} × {koreksi_per_derajat:.2f} = {koreksi:.2f} °Bx**

        3. **Hitung Brix Terkoreksi:**  
           Brix Terkoreksi = Brix Awal + Koreksi  
           Dalam kasus ini:  
           **{brix_awal:.2f} + {koreksi:.2f} = {brix_terkoreksi:.2f} °Bx**
        """, unsafe_allow_html=True)

        st.markdown("#### Kategori Kadar Gula:")
        st.markdown(f"""
        - {MINECRAFT_BLOCK} **Rendah**: Jika nilai Brix terkoreksi &lt; 10 (contoh: buah belum matang).
        - {MINECRAFT_APPLE} **Sedang**: Jika nilai Brix terkoreksi antara 10 hingga 15 (standar industri untuk buah segar).
        - {MINECRAFT_GOLD} **Tinggi**: Jika nilai Brix terkoreksi &gt; 15 (contoh: madu, sirup, atau buah sangat manis).
        """, unsafe_allow_html=True)
