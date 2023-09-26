from pathlib import Path
import streamlit as st
from PIL import Image

current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file= "E:/StreamLit/styles/main.css"
resume_file=current_dir/"assets"/"YASH S Resume.pdf"
profile_pic=current_dir/"assets"/"IMG_20230926_200253-fotor-202309270811.png"

#-----general setting----#
PAGE_TITLE ="Digital CV | Yash Singh"
PAGE_ICON  =":wave:"
NAME      ="Yash Singh"
DESCRIPTION="""
I'm skilled and certified Data Scientist with competence in statistical modelling,data mining and data extraction.Looking for a
responsible full-time career opportunity in a reputable organization where I can work with experienced professionals and reach my full
potential.
"""

EMAIL  ="singhyash9009@gmail.com"
SOCIAL_MEDIA={
    'LinkedIn':"https://www.linkedin.com/in/yash-singh-02b7341a3/",
    'GitHub'  :"https://github.com/Singhyash9009/GIT-HUB"
}

PROJECTS ={
    "🏆 Capstone_Amazon_Project":"https://github.com/Singhyash9009/GIT-HUB/tree/main/Capstone%20Amazon%20Project",
    "🏆 Kaggle_Walmart_Project" :"https://github.com/Singhyash9009/GIT-HUB/tree/main/Kaggle%20dataset",
    "🏆Classification_model_mini_project":"https://github.com/Singhyash9009/GIT-HUB/blob/main/MINI%20PROJECT/MINI%20PROJECT%20%202%20(CLASSIFICATION%20MODEL)%20YASH%20SINGH.ipynb",
    "🏆 Clustering_model_mini_project"    :"https://github.com/Singhyash9009/GIT-HUB/blob/main/MINI%20PROJECT/MINI%20PROJECT%203%20(CLUSTERING%20MODEL)%20YASH%20SINGH.ipynb",
    "🏆 Summary_app_tool":"https://github.com/Singhyash9009/GIT-HUB/tree/main/Summary%20App%20Tool",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """  
- ✔️ Strong hands on experience and knowledge in Python,MySQL and Excel
- ✔️ Having good experience on visualization software such as Tableau and PowerBI
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Having 3 months internships experience at Bugendaitech
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy), SQL
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Supervised Models: Logistic and Linear regression, Decision tree, Naive Bayes,Stacking Models
- 📚 Unsupervised Models: K-Means Clustering , DBSCAN , Hierarchical Clustering
- 🗄️ Databases: Postgres, MongoDB, MySQL
- 📊 UI : StreamLit, Django, Flasks
"""
)

st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Science Intern | Bugendaitech**")
st.write("05/2023 - 05/2023")
st.write(
    """
- ► Worked on Machine Learning Models created model for AirBnB Dataset
- ► Used Tableau and PowerBI  to redeﬁne and track KPIs on sales of superstore and  recommendations to boost their sales in future
- ► Done LDA on Speech of Narendra Modi
- ► Build a Web Summary Application Tool and made it interactive with help of StreamLit
"""
)


st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")