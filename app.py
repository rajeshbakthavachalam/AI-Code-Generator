import streamlit as st
import subprocess
import os
import json
from streamlit_lottie import st_lottie

# ✅ Set path to Ollama executable
OLLAMA_PATH = "C:\\Users\\rajes\\AppData\\Local\\Programs\\Ollama\\ollama.exe" #<your ollama path>

# Page config
st.set_page_config(page_title="AI Code Generator", page_icon="💻", layout="wide")

# Load animation from file
def load_lottie_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

animation2 = load_lottie_file("Animation2.json")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .hero-section {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 3rem;
        padding: 2rem 4rem 1rem 4rem;
        flex-wrap: wrap;
    }
    .hero-animation {
        flex: 1;
        min-width: 280px;
        max-width: 350px;
    }
    .hero-text {
        flex: 2;
        min-width: 300px;
    }
    .hero-text h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .hero-text p {
        font-size: 1.1rem;
        color: #555;
        line-height: 1.6;
    }
    .input-section {
        padding: 0 4rem;
        margin-top: 2rem;
    }
    .input-label {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
        display: flex;
        align-items: center;
    }
    .input-label::before {
        content: "📝";
        margin-right: 0.5rem;
    }
    .stTextArea textarea {
        border-radius: 10px !important;
        border: 1px solid #dcdcdc !important;
        padding: 0.75rem !important;
        font-size: 1rem !important;
    }
    .stButton {
        margin-top: 1.2rem;
    }
    .stButton button {
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        font-weight: 500;
        background-color: #ffffff;
        border: 1px solid #ccc;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #f0f0f0;
        border-color: #aaa;
    }
    hr {
        border: none;
        border-top: 1px solid #ddd;
        margin: 3rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# 🧠 Hero Section: Animation Left, Title Right
st.markdown('<div class="hero-section">', unsafe_allow_html=True)

# Left side - Animation
st.markdown('<div class="hero-animation">', unsafe_allow_html=True)
st_lottie(animation2, height=250, key="hero_anim")
st.markdown('</div>', unsafe_allow_html=True)

# Right side - Text
st.markdown('''
    <div class="hero-text">
        <h1>💻 AI Code Generator</h1>
        <p>This AI assistant helps you generate code from natural language using the <strong>CodeGemma</strong> model via <strong>Ollama</strong>. Whether it’s a Python function or an entire script — just describe what you need and let AI handle the rest.</p>
    </div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close hero-section

# Divider
st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
        Generate code from natural language using the **CodeGemma** model via Ollama.
        
        💡 *Example:*  
        `"Write a Python function to check if a number is prime."`
    """)

# ✅ Ollama check
if not os.path.exists(OLLAMA_PATH):
    st.error(f"Ollama executable not found at: `{OLLAMA_PATH}`")
    st.stop()

# Code generation logic
def generate_code(prompt):
    try:
        result = subprocess.run(
            [OLLAMA_PATH, "run", "codegemma"],
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        if result.returncode != 0:
            return f"⚠️ Error: {result.stderr.strip()}"
        return result.stdout.strip()
    except Exception as e:
        return f"⚠️ Exception occurred: {str(e)}"

# Prompt input
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown('<div class="input-label">Enter your code prompt:</div>', unsafe_allow_html=True)
st.caption("Describe what code you need:")
code_prompt = st.text_area("E.g., Create a Python class for a bank account.", height=150)
st.markdown('</div>', unsafe_allow_html=True)

# Generate code button
if st.button("🚀 Generate Code"):
    if code_prompt.strip():
        with st.spinner("🧠 Thinking and generating code..."):
            generated = generate_code(code_prompt)
        st.success("✅ Code generated below!")
        st.code(generated, language="python")
    else:
        st.warning("Please enter your code prompt above.")
