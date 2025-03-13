import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Koshal Kumar - Data Scientist", page_icon="🧑‍💻", layout="wide")

# Header Section
st.title("Koshal Kumar")
st.subheader("Data Scientist | Machine Learning | Optimization | NLP")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("📍 Chennai, IN")
    st.write("📧 koshalsingh0921@gmail.com")
    st.write("📞 +91 8210004520")
    st.write("[LinkedIn](https://www.linkedin.com/in/koshalsingh/) | [GitHub](https://github.com/koshalsingh)")

with col2:
    profile_img = Image.open("profile_pic.jpg")  # Replace with actual profile image
    st.image(profile_img, width=150)

st.markdown("---")

# Summary Section
st.header("Summary")
st.write(
    "Data Scientist with 3+ years of experience in data preprocessing, EDA, data modeling, and Machine Learning."
    " Skilled in Python, data wrangling, data structures, inferential statistics, and various data science packages."
    " Worked on projects across multiple industries, including automation, data modeling, price optimization,"
    " data science package development, and backend development."
)

st.markdown("---")

# Experience Section
st.header("Professional Experience")
st.subheader("Data Scientist @ Tiger Analytics")
st.write("📆 March 2022 – Present | Chennai, IN")

with st.expander("Retail Price Optimization - FMCG (Python, PySpark, PyOMO, ML, Regression)"):
    st.write("• Developed an algorithm for revenue forecasting using the concept of price elasticity of demand for FMCG client.")
    st.write("• Deployed multiple loss minimization & optimization techniques to run examine models and simulation.")
    st.write("• Applied pricing models and conducted pricing simulations to evaluate the impact of pricing decisions on revenue and profitability.")
    st.write("• Created a method to resolve the infeasible solution problem and issue of constrained results.")    

with st.expander("Data Cleaning Pipelines - FMCG (Python, PySpark, Feature Engineering)"):
    st.write("• Developed data cleaning pipelines for several different retailers' datasets using DataBricks, ensuring consistency and accuracy in data processing for a FMCG client.s.")
    st.write("• Implemented quality control measures at each stage of the data cleaning process to validate data integrity and completeness.")
    st.write("• Standardized data formats across all retailers by mapping to a common column (EAN), facilitating seamless data consolidation.")
    st.write("• Orchestrated the consolidation of cleaned data and its subsequent transfer to SQL Pipeline, streamlining data management and analysis processes.")

st.subheader("Associate Data Scientist @ Alunoz Technologies")
st.write("📆 Dec 2021 – Feb 2022")
st.write("• Designed & developed a facial recognition system using OpenCV’s one-shot learning technique with 93% accuracy.")

st.markdown("---")

# Education Section
st.header("Education")
st.write("**M.Sc. Data Science** - Central University of Rajasthan (2019-2021) | GPA: 7.83/10")
st.write("**B.Sc. Information Technology** - Magadh University (2016-2019) | 75.1%")

st.markdown("---")

# Skills Section
st.header("Key Skills")
st.write("Machine Learning | Optimization | NLP | Data Wrangling | Predictive Analytics | Pricing Optimization | Python | PySpark")
st.write("SQL | Data Mining | Text Mining | LLMs | Gen AI | Data Analysis | Debugging | Cloud Computing (Azure, DataBricks)")

st.markdown("---")

# Projects Section
st.header("Key Data Science Projects")
with st.expander("Intelligent Document Retrieval & RAG Pipeline (Python, LangChain, FAISS, Hugging Face, NLP)"):
    st.write("• Developed a Retrieval-Augmented Generation (RAG) pipeline to enhance LLMs with real-time document retrieval.")
    st.write("• Built a vector search system using FAISS and Hugging Face Embeddings for semantic search.")
    st.write("• Integrated Ollama LLM for AI-driven insights, improving response accuracy and reducing hallucinations.")

with st.expander("Duplicate Question Detection - Quora (Python, NLP)"):
    st.write("• Built a model to identify duplicate questions on Quora, improving answer efficiency.")
    st.write("• Used TF-IDF, Word2Vec, Cosine similarity, and Jaccard similarity for feature engineering.")
    st.write("• Achieved 98% accuracy, reducing redundancy in Quora’s question database.")

st.markdown("---")

# Certifications Section
st.header("Certifications")
st.write("• **Insurance Domain Certification** - Tiger Analytics (Oct 2023)")
st.write("• **CPG Domain Certification** - Tiger Analytics (Jan 2023)")
st.write("• **Applied NLP** - NPTEL (Dec 2020)")
st.write("• **Data Structure Certification** - CDAC (Sep 2017)")

st.markdown("---")
