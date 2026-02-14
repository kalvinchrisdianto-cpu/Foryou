import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="Happy Valentine's Day!", page_icon="🧸")

# Custom CSS untuk tema pink & font yang lucu
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #ff1493;
        color: white;
    }
    h1, h2, h3 {
        color: #d02090;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Judul Utama
st.title("🧸 Special Message for You!")

# Dekorasi Sidebar
with st.sidebar:
    st.header("Valentine's Corner")
    st.write("Dibuat khusus dengan penuh ❤️")
    st.write("---")
    st.image("https://img.icons8.com/bubbles/200/teddy-bear.png", width=150)

# Bagian Konten Utama
col1, col2 = st.columns([1, 2])

with col1:
    # Ilustrasi Teddy Bear (Menggunakan URL gambar publik)
    st.image("https://img.icons8.com/clouds/200/love-message.png", width=150)

with col2:
    st.header("Haloo Jes maap gabut ! ✨")
    st.write("""
    Kangen. oh iya smgt ya seminggunya see you lagi besok kamis hehehehe. slmat valentine. alay gak seh le misal ngene???.
    """)

# Interaksi Tombol
if st.button("Klik di sini untuk kejutan! 🎁"):
    st.balloons()
    st.snow() # Dalam streamlit, efek salju bisa terlihat seperti partikel putih yang lembut
    
    st.markdown("### 💌 Pesan Spesial:")
    message = st.empty()
    text = "Happy Valentine's Day! 🌹\n\nCOKLAT E NYUSUL HEHEHEHE! 🧸"
    
    # Efek mengetik sederhana
    full_text = ""
    for char in text:
        full_text += char
        message.markdown(f"**{full_text}**")
        time.sleep(0.05)
        
    st.success("You are loved! ❤️")

# Footer dekoratif
st.write("---")
st.write("🌷 *Beda agama peduli apa😜😜😜😜!*")
