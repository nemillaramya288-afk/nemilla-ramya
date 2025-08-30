import streamlit as st
from backend import generate_audio

# Page config
st.set_page_config(page_title="Echoverse - Text to Speech", page_icon="🎙️", layout="centered")

# Custom CSS with modern design
st.markdown("""
    <style>
        body {
            background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #fbc2eb);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            font-family: 'Poppins', sans-serif;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .title {
            text-align: center;
            font-size: 52px;
            font-weight: 900;
            color: #2d3436;
            margin-bottom: -10px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #2d3436;
            margin-bottom: 40px;
            font-style: italic;
        }
        .stTextArea textarea {
            border-radius: 20px !important;
            border: none !important;
            font-size: 16px !important;
            padding: 18px !important;
            background: rgba(255, 255, 255, 0.75) !important;
            backdrop-filter: blur(10px) !important;
            box-shadow: inset 5px 5px 10px #d1d9e6,
                        inset -5px -5px 10px #ffffff;
            color: #2d3436 !important;
        }
        .stButton button {
            background: #ff7675;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 25px;
            padding: 12px 28px;
            border: none;
            transition: all 0.3s ease-in-out;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.2),
                        -5px -5px 15px rgba(255,255,255,0.5);
        }
        .stButton button:hover {
            background: #d63031;
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
            cursor: pointer;
        }
        .audio-box {
            background: rgba(255, 255, 255, 0.55);
            border-radius: 20px;
            padding: 30px;
            margin-top: 40px;
            box-shadow: 8px 8px 20px rgba(0,0,0,0.15),
                        -8px -8px 20px rgba(255,255,255,0.6);
            text-align: center;
            font-weight: 600;
            font-size: 20px;
            color: #2d3436;
        }
    </style>
""", unsafe_allow_html=True)

# Title & subtitle
st.markdown('<p class="title">🎙️ Echoverse</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Turn your words into magical speech ✨</p>', unsafe_allow_html=True)

# Input text
user_input = st.text_area("✍️ Write something beautiful:", "")

# Button
if st.button("🎧 Generate Speech"):
    if user_input.strip():
        output_file = generate_audio(user_input, "speech.mp3")
        st.markdown('<div class="audio-box">✅ Your audio is ready! Enjoy your voice output 🎶</div>', unsafe_allow_html=True)
        st.audio(output_file)
        with open(output_file, "rb") as f:
            st.download_button("⬇️ Download MP3", f, file_name="speech.mp3")
    else:
        st.error("⚠️ Please enter some text before generating audio.")
