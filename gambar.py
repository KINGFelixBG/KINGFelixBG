# Backup version - Minecraft-inspired homepage
import streamlit as st

# Configure page
st.set_page_config(page_title="Minecraft Brix Adventure", layout="centered")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Home", "Uji Brix"])

# Home Page
if page == "Home":
    # Custom CSS for Minecraft theme
    st.markdown(
        """
        <style>
        .title {
            font-size:50px;
            color:#228B22;
            text-align:center;
            font-weight:bold;
            font-family: 'Courier New', Courier, monospace;
            text-shadow: 2px 2px 4px #000000;
        }
        .subtitle {
            font-size:22px;
            text-align:center;
            color: #8B4513;
            font-family: 'Courier New', Courier, monospace;
        }
        body {
            background-color: #87CEEB;
            background-image: url('https://i.ibb.co/5kZtqJ3/minecraft-background.png');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title
    st.markdown('<div class="title">Minecraft Brix Adventure</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Explore the world of Brix with pixelated fun!</div>', unsafe_allow_html=True)

    # Display pixelated images side by side
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("https://i.ibb.co/5Lw09VJ/minecraft-character.png", caption="Pixel Scientist", use_column_width=True)

    st.markdown("---")

    st.info("Use the navigation menu on the left to start your Brix Adventure!")

    st.markdown("---")
    st.caption("Made with ❤️ in Streamlit Pixel Minecraft Adventure")

# Uji Brix Page
elif page == "Uji Brix":
    st.title("🧪 Uji Brix - Minecraft Edition")

    st.write("""
    This application helps calculate the Brix level of sugar solutions in food ingredients, with temperature correction.
    """)

    # Input parameters
    st.header("Enter Test Parameters (Minecraft Style)")

    brix_awal = st.number_input("Enter Brix value from refractometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Enter solution temperature during measurement (°C):", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("Calculate Brix Correction"):
        suhu_referensi = 20.0
        koreksi_per_derajat = 0.03

        selisih_suhu = suhu - suhu_referensi
        koreksi = selisih_suhu * koreksi_per_derajat
        brix_terkoreksi = brix_awal + koreksi

        st.success(f"Corrected Brix Value: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Calculation: {brix_awal:.2f} + ({selisih_suhu:.2f} × {koreksi_per_derajat}) = {brix_terkoreksi:.2f} °Bx")

        # Quality assessment of food ingredients
        if brix_terkoreksi < 10:
            kualitas = "Low (e.g., unripe fruit)"
        elif 10 <= brix_terkoreksi <= 15:
            kualitas = "Medium (industry standard for fresh fruit)"
        else:
            kualitas = "High (honey, syrup, or very sweet fruit)"

        st.info(f"Sugar Level Category: {kualitas}")
