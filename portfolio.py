import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Koshal Kumar - Portfolio", page_icon="💼", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Poppins', sans-serif;
        }
        .title {
            font-size: 3rem;
            text-align: center;
            font-weight: bold;
        }
        .btn-container {
            display: flex;
            justify-content: center;
            gap: 1rem;
        }
        .btn {
            padding: 1rem;
            border-radius: 2rem;
            font-weight: 600;
        }
        .nav-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            font-size: 1.5rem;
        }
        .nav-links a {
            color: black;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation Menu
st.markdown("""
<nav class='nav-links'>
    <a href='#about'>About</a>
    <a href='#experience'>Experience</a>
    <a href='#projects'>Projects</a>
    <a href='#education'>Education & Certifications</a>
    <a href='#contact'>Contact</a>
</nav>
<hr>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([1, 2])
with col1:
    profile_img = Image.open("profile_pic.jpg")  # Replace with actual profile image
    st.image(profile_img, width=250)
with col2:
    st.markdown("<p class='title'>Koshal Kumar</p>", unsafe_allow_html=True)
    st.subheader("Data Scientist | Machine Learning | Optimization | NLP")
    st.write("📍 Chennai, IN")
    st.write("📧 koshalsingh0921@gmail.com")
    st.write("📞 +91 8210004520")
    
    st.markdown("""
    <div class='btn-container'>
        <a href='#contact' class='btn btn-color-1'>Contact Me</a>
        <a href='#projects' class='btn btn-color-2'>My Projects</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# About Section
st.markdown("<h1 id='about' class='title'>About Me</h1>", unsafe_allow_html=True)
st.write(
    "Data Scientist with 3+ years of experience in data preprocessing, EDA, data modeling, and Machine Learning."
    " Skilled in Python, data wrangling, data structures, inferential statistics, and various data science packages."
)

st.markdown("---")

# Experience Section
st.markdown("<h1 id='experience' class='title'>Experience</h1>", unsafe_allow_html=True)
st.subheader("Data Scientist @ Tiger Analytics")
st.write("📆 March 2022 – Present | Chennai, IN")
with st.expander("Retail Price Optimization - Automobile"):
    st.write("• Built a pricing engine optimizing store-item prices based on demand, cost, inventory, and promotions.")
    st.write("• Developed a simulation tool to evaluate price impact on KPIs (net sales, margins, revenue).")
    st.write("• Achieved 3x-4x faster model performance.")
with st.expander("Data Cleaning Pipelines - FMCG"):
    st.write("• Automated data cleaning pipelines for retailer datasets using Databricks.")
    st.write("• Standardized data formats and integrated with SQL pipeline.")

st.markdown("---")

# Projects Section
st.markdown("<h1 id='projects' class='title'>Projects</h1>", unsafe_allow_html=True)
with st.expander("Intelligent Document Retrieval & RAG Pipeline"):
    st.write("• Developed a RAG pipeline using LangChain, FAISS, and Hugging Face Embeddings.")
    st.write("• Built a vector search system and integrated Ollama LLM for AI-driven insights.")
with st.expander("Duplicate Question Detection - Quora"):
    st.write("• Built a model to identify duplicate questions on Quora, improving answer efficiency.")
    st.write("• Achieved 98% accuracy, reducing redundancy in Quora’s question database.")

st.markdown("---")

# Education & Certifications Section
st.markdown("<h1 id='education' class='title'>Education & Certifications</h1>", unsafe_allow_html=True)
st.subheader("🎓 Academic Degrees")
st.write("**Master in Data Science & Big Data** - Central University of Rajasthan (2019 – 2021)")
st.write("**Bachelor of Science in Computer Science** - Magadh University (2016 – 2019)")

st.subheader("📜 Professional & Technical Certifications")
with st.expander("Deep Learning & AI"):
    st.write("• **Neural Networks and Deep Learning** - DeepLearning.AI / Coursera (Mar 2020)")
    st.write("• **Improving Deep Neural Networks: Hyperparameter Tuning, Regularization & Optimization** - DeepLearning.AI / Coursera (May 2020)")
    st.write("• **Convolutional Neural Networks in TensorFlow** - DeepLearning.AI / Coursera (May 2020)")
    st.write("• **Introduction to TensorFlow for AI, Machine Learning, and Deep Learning** - DeepLearning.AI / Coursera (Mar 2020)")
    st.write("• **Natural Language Processing in TensorFlow** - DeepLearning.AI / Coursera (Jun 2020)")
    st.write("• **Applied NLP** - NPTEL (Dec 2020)")
    st.write("• **Deep Learning** - NPTEL (2020)")

with st.expander("Machine Learning & Data Science"):
    st.write("• **Applied Machine Learning in Python** - University of Michigan / Coursera (Mar 2020)")
    st.write("• **Introduction to Data Science in Python** - University of Michigan / Coursera (Mar 2020)")
    st.write("• **Machine Learning with Python: Build Real-World ML Models** - IBM / Coursera (Feb 2020)")
    st.write("• **Data Visualization with Python: Hands-On Projects** - IBM / Coursera (Feb 2020)")
    st.write("• **Data Structure Certification** - CDAC (Sep 2017)")

with st.expander("Industry & Domain Expertise"):
    st.write("• **Insurance Domain Certification** - Tiger Analytics (Oct 2023)")
    st.write("• **CPG Domain Certification** - Tiger Analytics (Jan 2023)")

st.markdown("---")

# Contact Section
st.markdown("<h1 id='contact' class='title'>Contact Me</h1>", unsafe_allow_html=True)
st.write("📧 [Email](mailto:koshalsingh0921@gmail.com)")
st.write("[LinkedIn](#) | [GitHub](#)")
st.write("📍 Chennai, IN")

st.markdown("---")
st.write("Developed with ❤️ using Streamlit")
