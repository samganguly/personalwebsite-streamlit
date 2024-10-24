import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
#from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander
import base64
from streamlit_extras.let_it_rain import rain 


# Set page title
st.set_page_config(page_title="Samrat Ganguly", page_icon = "random", layout = "wide", initial_sidebar_state = "auto")
rain(
    emoji="✨",
    font_size=54,
    falling_speed=5,
    animation_length="1",
)
#test cursor
# Function to encode the local cursor file to base64
def encode_cursor_to_base64(file_path):
    with open(file_path, "rb") as cursor_file:
        cursor_content = cursor_file.read()
        encoded_cursor = base64.b64encode(cursor_content).decode("utf-8")
    return encoded_cursor

# Set the path to your local cursor file
local_cursor_path = "squirtle.cur"

# Encode the cursor file to base64
encoded_cursor_data = encode_cursor_to_base64(local_cursor_path)

# Use HTML and CSS to set the cursor with a data URI
st.markdown(
    f"""
    <style>
        body {{
            cursor: url(data:image/x-icon;base64,{encoded_cursor_data}), auto !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
##test cursor //end


# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Samrat Ganguly';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_p1 = Image.open("images/p1.jpg")
img_p2 = Image.open("images/p2.jpg")

# Assets for education
img_vit = Image.open("images/VIT.png")
img_lbs = Image.open("images/lbs.png")
img_our_own = Image.open("images/our_own.png")
img_gems = Image.open("images/gems.png")

# Assets for experiences
img_crescent = Image.open("images/crescent.png")

# Assets for gallery
#img_lottie_animation = Image.open("images/lottie_animation.gif")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("images/linkedin.png")
img_github = Image.open("images/github.png")
img_email = Image.open("images/email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.jpg')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_p2, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Samrat Ganguly", 
                        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Gallery", "Resume", "Contact", "Socials"],
                         icons=['person fill', 'globe', 'tools', 'book half', 'clipboard', 'image' , 'pencil square', 'envelope','heart'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    linkedin_url = "https://www.linkedin.com/in/samratganguly03/"
    github_url = "https://github.com/samganguly"
    email_url = "mailto:samganguly03@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url , Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Samrat Ganguly")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Aspiring Data Science Engineer | Specializing in Artificial Intelligence and Machine Learning")
            st.write("👋🏻 Hi, I'm Samrat! Currently, I am in my final year of pursuing a degree in Computer Science and Engineering, with a specialization in Artificial Intelligence and Machine Learning.")
            st.write("💻 My interests lie in coding with Python and Java, alongside a deep fascination for Machine Learning and Deep Learning. I am committed to expanding my expertise in these areas and continuously honing my skills.")
            st.write("🚀 With a passion for innovation and technology, I am driven to contribute meaningfully to the AI and software development fields while learning from seasoned professionals. I am eager to apply my knowledge to real-world challenges.")
            st.write("💡 Open-minded and enthusiastic about adapting to emerging technologies, I thrive in environments that encourage learning and growth.")
            st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/1KdLVbCBwzYxDZxzb4KbPC2O4YdEHCy0F/view?usp=sharing)")

            st.write("🛠 Building this portfolio as an extended resume introduced me to Streamlit's versatility. Unlike traditional front-end frameworks like Angular and Bootstrap, Streamlit offers a simpler, more visually engaging way to create interactive web applications, standing out from alternatives like Plotly and Shiny.")

        with middle_column:
            st.empty()
        with right_column:
            st.image(img_p1)

# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1, 5))
        with image_column:
            st.image(img_crescent)
        with text_column:
            st.subheader("AI Intern , **Crescent Petroleum**")
            st.write("Sharjah, United Arab Emirates")
            st.write("*August 2023 to November 2023*")
            st.markdown("""
            - Developed a highly sophisticated custom chatbot leveraging **Azure OpenAI GPT models** to improve internal and external communication processes. This chatbot was integrated with **Power Virtual Agent** and **Power Automate**, automating tasks and creating a more interactive and efficient user experience.
            - Spearheaded the integration of advanced **Convolutional Neural Network (CNN)** models within the **Azure Function App** environment for comprehensive image analysis. This included the successful implementation of the **imagededup library**, significantly enhancing the system's ability to identify and eliminate duplicate images, improving overall data quality.
            - Designed and developed an innovative, user-friendly application using **Power Apps**, enabling users to capture photos from their device's camera or gallery and perform real-time image comparisons. The app compared these photos against a large database of stored images in **SharePoint/Dataverse**, showcasing a creative solution to streamline image management workflows.
            - Worked closely with cross-functional teams, including software engineers and product managers, to implement cutting-edge technology solutions that aligned with the organization's goals.

            **Skills Acquired**:
            - **Azure OpenAI**: Leveraged advanced AI capabilities to build a highly intelligent chatbot.
            - **Power Virtual Agent**: Utilized Power Virtual Agent to create interactive chatbot interfaces.
            - **Power Automate**: Automated workflows and processes to streamline tasks and improve efficiency.
            - **Azure Function**: Developed Python functions within Azure Function for real-time image analysis.
            - **Convolutional Neural Networks (CNN)**: Implemented CNN models for in-depth image analysis.
            - **imagededup Library**: Integrated the imagededup library for effective duplicate image detection.
            - **Power Apps**: Built a user-friendly app to compare images in real-time against a comprehensive database stored in SharePoint/Dataverse.
            """)

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    
    # Programming
    txt3("Programming Languages", "`Java`, `Python`, `C`, `C++`")
    
    # Data Analysis & Reporting
    txt3("Data Analysis & Reporting", "`Data Quality Assessment`, `Power BI Visualizations`, `Excel`, `Data Insights and Presentation`")
    
    # Data Visualization
    txt3("Data Visualization", "`matplotlib`, `seaborn`, `Power BI`")
    
    # Tools and Frameworks
    txt3("Tools and Frameworks", "`Scikit-Learn`, `OpenCV`, `TensorFlow`, `NLTK`, `Face Recognition`, `Firebase`, `Computer Vision`, `Git`, `KNIME`, `Linux`, `Raspberry OS`, `mediapipe`, `blaze`")
    
    # Machine Learning & AI
    txt3("Machine Learning & AI", "`Machine Learning Algorithms`, `Convolutional Neural Networks (CNN)`, `Artificial Intelligence`")
    
    # Cloud Platforms & Automation
    txt3("Cloud Platforms & Automation", "`Azure OpenAI`, `Google Cloud Platform`, `Azure`, `Hugging Face`, `Streamlit`, `Power Apps`, `Power Automate`, `Power Virtual Agent`, `Azure Function App`")
    
    # Natural Language Processing
    txt3("Natural Language Processing", "`NLTK`, `Word2Vec`, `TF-IDF`")
    
    # Computer Vision
    txt3("Computer Vision", "`mediapipe`, `blaze`, `OpenCV`")
    
    # Database Management
    txt3("Database Management", "`Relational Database Design`, `SQL`, `MongoDB`")
    
    # Data Science Techniques
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Random Forest`, `Decision Trees`, `Text Classification`, `Sentiment Analysis`")
    
    # Machine Learning Frameworks
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`")
    
    # Design and Front-end Development
    txt3("Design and Front-end Development", "`Canva`, `Figma`, `HTML`, `CSS`, `Streamlit`")
    
    # Miscellaneous
    txt3("Miscellaneous", "`Canva`, `Cisco Packet Tracer`")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    selected_options = ["Summary", "Modules"
                        ]
    selected = st.selectbox("Which section would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Summary":
        st.subheader("Summary")
        st.write("*Summary of education from primary school till university*")

        # Bachelor's Degree
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_vit, width=290)
            with text_column:
                st.subheader("Bachelor's Degree in CSE with Specialization in Artificial Intelligence and Machine Learning")
                st.write("**Vellore Institute of Technology, Chennai** (2021 - 2025)")
                st.write("7th Semester CGPA: **8.12**")
        
        st.markdown("<br>", unsafe_allow_html=True)

        # Higher Secondary
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_lbs, width=230)
            with text_column:
                st.subheader("Higher Secondary")
                st.write("**Lal Bahadur Shastri Senior Secondary School, Kota** (2019 - 2021)")
                st.write("XII - **92.6%** in AISSCE Examination 2021 (CBSE Board)")
                st.write("XI - **97.6%** in Grade 11 Final Exams")
        
        st.markdown("<br>", unsafe_allow_html=True)

        # High School
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_our_own, width=230)
            with text_column:
                st.subheader("High School")
                st.write("**Our Own English High School, Sharjah, U.A.E** (2017 - 2019)")
                st.write("Grade 10 - **96.8%** in AISSE Examination 2019 (CBSE Board)")
                st.write("- National Rank 1 in International Mathematics Olympiad (International Rank 43), January 2017")
                st.write("- National Rank 4 in International Science Olympiad (International Rank 75), January 2017")
                st.write("- National Rank 9 in International English Olympiad (International Rank 86), January 2017")
        
        st.markdown("<br>", unsafe_allow_html=True)

        # Middle School
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_gems, width=230)
            with text_column:
                st.subheader("Middle School")
                st.write("**GEMS Millennium School, Sharjah, U.A.E** (2016 - 2017)")
                st.write("**Gulf Asian English High School, Sharjah, U.A.E** (2015 - 2016)")

        st.markdown("<br>", unsafe_allow_html=True)

    elif selected == "Modules":
        st.subheader("Modules")
        st.write("*List of courses with course codes and credits*")

        with st.container():
            sem1, mid, sem2 = st.columns((1, 0.1, 1))
            with sem1:
                st.write("**Courses List**")
                st.markdown("""
                | Code      | Module Title                                     | Workload  |
                |-----------|-------------------------------------------------|-----------|
                | BCHY101L  | Engineering Chemistry                           | 3.0 Credits |
                | BCHY101P  | Engineering Chemistry Lab                       | 1.0 Credit |
                | BCSE101E  | Computer Programming: Python                    | 3.0 Credits |
                | BCSE101N  | Introduction to Engineering                     | 1.0 Credit |
                | BEEE101L  | Basic Electrical Engineering                    | 2.0 Credits |
                | BEEE101P  | Basic Electrical Engineering Lab                | 1.0 Credit |
                | BMAT101L  | Calculus                                        | 3.0 Credits |
                | BMAT101P  | Calculus Lab                                    | 1.0 Credit |
                | BSTS101P  | Quantitative Skills Practice I                  | 1.5 Credits |
                | BCSE102L  | Structured and Object-Oriented Programming      | 2.0 Credits |
                | BCSE102P  | Structured and Object-Oriented Programming Lab  | 2.0 Credits |
                | BECE101L  | Basic Electronics                               | 2.0 Credits |
                | BECE101P  | Basic Electronics Lab                           | 1.0 Credit |
                | BENG101L  | Technical English Communication                 | 2.0 Credits |
                | BENG101P  | Technical English Communication Lab             | 1.0 Credit |
                | BHUM101N  | Ethics and Values                               | 2.0 Credits |
                | BMAT102L  | Differential Equations and Transforms           | 4.0 Credits |
                | BPHY101L  | Engineering Physics                             | 3.0 Credits |
                | BPHY101P  | Engineering Physics Lab                         | 1.0 Credit |
                | BSTS102P  | Quantitative Skills Practice II                 | 1.5 Credits |
                | BCSE103E  | Computer Programming: Java                      | 3.0 Credits |
                | BCSE202L  | Data Structures and Algorithms                  | 3.0 Credits |
                | BCSE202P  | Data Structures and Algorithms Lab              | 1.0 Credit |
                | BCSE205L  | Computer Architecture and Organization          | 3.0 Credits |
                | BECE102L  | Digital Systems Design                          | 3.0 Credits |
                | BECE102P  | Digital Systems Design Lab                      | 1.0 Credit |
                | BENG102P  | Technical Report Writing                        | 1.0 Credit |
                | BGER101L  | German I                                        | 2.0 Credits |
                | BMAT205L  | Discrete Mathematics and Graph Theory           | 4.0 Credits |
                | BSTS201P  | Qualitative Skills Practice I                   | 1.5 Credits |
                | BCHY102N  | Environmental Sciences                          | 2.0 Credits |
                | BCSE204L  | Design and Analysis of Algorithms               | 3.0 Credits |
                | BCSE204P  | Design and Analysis of Algorithms Lab           | 1.0 Credit |
                | BCSE303L  | Operating Systems                               | 3.0 Credits |
                | BCSE303P  | Operating Systems Lab                           | 1.0 Credit |
                | BCSE304L  | Theory of Computation                           | 3.0 Credits |
                | BCSE306L  | Artificial Intelligence                         | 3.0 Credits |
                | BECE204L  | Microprocessors and Microcontrollers            | 3.0 Credits |
                | BECE204P  | Microprocessors and Microcontrollers Lab        | 1.0 Credit |
                | BMAT201L  | Complex Variables and Linear Algebra            | 4.0 Credits |
                | BSTS202P  | Qualitative Skills Practice II                  | 1.5 Credits |
                | CFOC308M  | The Joy of Computing using Python               | 3.0 Credits |
                | BCSE209L  | Machine Learning                                | 3.0 Credits |
                | BCSE209P  | Machine Learning Lab                            | 1.0 Credit |
                | BCSE302L  | Database Systems                                | 3.0 Credits |
                | BCSE302P  | Database Systems Lab                            | 1.0 Credit |
                | BCSE308L  | Computer Networks                               | 3.0 Credits |
                | BCSE308P  | Computer Networks Lab                           | 1.0 Credit |
                | BECE351E  | Internet of Things                              | 2.0 Credits |
                | BMAT202L  | Probability and Statistics                      | 3.0 Credits |
                | BMAT202P  | Probability and Statistics Lab                  | 1.0 Credit |
                | BSTS301P  | Advanced Competitive Coding - I                 | 1.5 Credits |
                | BSSC101N  | Essence of Traditional Knowledge                | 2.0 Credits |
                | BCSE309L  | Cryptography and Network Security               | 3.0 Credits |
                | BCSE309P  | Cryptography and Network Security Lab           | 1.0 Credit |
                | BCSE416L  | Game Programming                                | 3.0 Credits |
                | BCSE416P  | Game Programming Lab                            | 1.0 Credit |
                | BCSE417L  | Machine Vision                                  | 3.0 Credits |
                | BCSE417P  | Machine Vision Lab                              | 1.0 Credit |
                | BCSE419L  | Speech and Language Processing                  | 3.0 Credits |
                | BCSE419P  | Speech and Language Processing Lab              | 1.0 Credit |
                | BCSE497J  | Project-I                                       | 3.0 Credits |
                | BHUM103L  | Micro Economics                                 | 3.0 Credits |
                | BCSE301L  | Software Engineering                            | 3.0 Credits |
                | BCSE301P  | Software Engineering Lab                        | 1.0 Credit |
                | BCSE305L  | Embedded Systems                                | 3.0 Credits |
                | BCSE307L  | Compiler Design                                 | 3.0 Credits |
                | BCSE307P  | Compiler Design Lab                             | 1.0 Credit |
                | BCSE332L  | Deep Learning                                   | 3.0 Credits |
                | BCSE332P  | Deep Learning Lab                               | 1.0 Credit |
                | BCSE418L  | Explainable Artificial Intelligence             | 2.0 Credits |
                | BECE352E  | IoT Domain Analyst                              | 2.0 Credits |
                | BSTS302P  | Advanced Competitive Coding - II                | 1.5 Credits |
                | AEXC180N  | Empowering Labours using Social Media           | 2.0 Credits |
                """)
                # Adding total number of credits
                st.markdown("**Total Number of Credits: 150**")


elif choose == "Projects":
    images_projects = {
    0: "images/resume-cf.jpg",  # Example image for AI-Powered Resume Parsing and Career Insights
    1: "images/sva.jpg",    # Example image for Smart Vision Aid for the Visually Impaired
    2: "images/unityaid.png"        # Example image for Unity Aid project
    }
    # Create section for Projects
    st.header("Projects")

    # AI-Powered Resume Parsing and Career Insights
    with st.container():
        text_column, image_column = st.columns((3, 1))
        with text_column:
            st.subheader("AI-Powered Resume Parsing and Career Insights")
            st.write("*Developed for Intel GenAI Hackathon*")
            st.markdown("""
            - Led the development of an AI-driven platform designed to parse resumes and recommend suitable job roles, utilizing **React**, **JavaScript**, and **MongoDB** to build a full-stack web application for optimal performance.
            - Implemented a cutting-edge **BERT deep learning model**, trained on a dataset of resumes to predict the best-fit job roles for candidates, achieving high accuracy in role recommendation through contextual analysis.
            - Applied **BERT tokenizer** to extract and structure key information, including skills, experiences, and qualifications, from resumes, automating the job-matching process.
            - Integrated with the **LinkedIn API** to dynamically fetch and display top job vacancies that aligned with the model's predicted roles, streamlining the job application process for users.
            - Used the **Gemini API** to recommend tailored skill development courses based on the user's resume content, providing a comprehensive career advancement tool that enhanced both job placement and personal growth opportunities.
            - Employed advanced **NLP techniques** to improve the parsing and understanding of resumes, ensuring a nuanced approach to job role recommendations by analyzing the resume's context.
            - Delivered a seamless and user-friendly interface that allowed candidates to apply for jobs directly from the platform, while simultaneously receiving targeted skill development recommendations for ongoing career improvement.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/your-repo-link")
        with image_column:
            st.image(images_projects[0])

    # Smart Vision Aid for the Visually Impaired
    with st.container():
        text_column, image_column = st.columns((3, 1))
        with text_column:
            st.subheader("Smart Vision Aid for the Visually Impaired")
            st.write("*Assistive technology project using Raspberry Pi and Azure*")
            st.markdown("""
            - Spearheaded the development of an **assistive technology device** aimed at enhancing the independence of visually impaired individuals, utilizing **Raspberry Pi**, **OpenCV**, and **Azure Computer Vision API** for real-time image capture and processing.
            - Designed and implemented features for **real-time object recognition**, **scene understanding**, and **text extraction**, transforming visual information into audio feedback using **Text-to-Speech (pyttsx3)** technology to deliver accessible descriptions of surroundings.
            - Ensured high accuracy in object detection and recognition through extensive model training and testing, focusing on usability to provide a reliable navigation aid for users.
            - Integrated customizable audio feedback options to cater to specific user needs, allowing personalized voice guidance and descriptions, enhancing the system's flexibility and user experience.
            - Utilized a combination of **Python**, **OpenCV**, and **Azure’s powerful image analysis tools** to deliver a robust and scalable solution that was capable of adapting to various real-world scenarios.
            - Conducted user testing with individuals from the visually impaired community, gathering feedback and refining the product to ensure it met real-world demands for accessibility and independence.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/your-repo-link")
        with image_column:
            st.image(images_projects[1])

    # Unity Aid: Intelligent Social Event Matching for Crowdfunding
    with st.container():
        text_column, image_column = st.columns((3, 1))
        with text_column:
            st.subheader("Unity Aid: Intelligent Social Event Matching for Crowdfunding")
            st.write("*Web platform for charity designed with HTML, CSS, JavaScript, PHP, and MySQL*")
            st.markdown("""
            - Designed and developed **Unity Aid**, a web platform that facilitates social event matching for charitable fundraising, using a combination of **HTML**, **CSS**, **JavaScript**, **PHP**, and **MySQL** to create a fully functional and optimized application.
            - Focused on building a scalable back-end infrastructure using **PHP/MySQL**, significantly improving system performance by reducing page load times and streamlining database interactions.
            - Developed an intuitive and user-friendly **admin panel**, allowing administrators to efficiently manage fundraising events, track participant activity, and monitor donation flow, increasing operational efficiency.
            - Implemented advanced algorithms for matching social events to potential donors, leveraging the platform’s ability to analyze user preferences and tailor recommendations accordingly, enhancing user engagement and event success rates.
            - Introduced a secure payment gateway and transaction management system to ensure the safety of funds transferred during crowdfunding events, providing transparency and trust for both donors and event organizers.
            - Integrated customizable event pages and user profiles, enabling organizations to personalize their fundraising campaigns and providing donors with detailed insights into the causes they support.
            - Conducted beta testing with several non-profit organizations, gathering feedback and iterating on the platform’s features to improve its overall effectiveness and user satisfaction.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/your-repo-link")
        with image_column:
            st.image(images_projects[2])

    

elif choose == "Gallery":
    st.header("Photography Gallery")
    st.subheader("Capturing moments through my lens!")

    # Update the introduction paragraph
    st.markdown("""
    <div style="font-family: 'Georgia', serif; font-size: 20px; font-style: italic; color: #555;">
        “To me, photography is an art of observation. It’s about finding something interesting in an ordinary place.”
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    Photography has always been more than just a hobby for me—it's a passion, a way of capturing fleeting moments and turning them into everlasting memories. I believe that through my lens, I can preserve not just images, but emotions, experiences, and perspectives.

    As an avid traveler, I’ve been fortunate enough to explore many corners of the world. From the deserts of **Bahrain** and **UAE**, to the breathtaking savannas of **Kenya** and **Tanzania**, to the cultural vibrancy of **Malaysia**, **Singapore**, and **India**—each place has left me with unforgettable experiences that I have captured through photography.

    Whether it's nature, architecture, or wildlife, every photo I take tells a unique story. I’m excited to share with you some of my favorite shots from my travels around the world. I hope you enjoy viewing these snapshots as much as I enjoyed capturing them!
    """)

    selected_options = ["Overview", "Nature", "Architecture", "Wildlife", "Travel", "Portraits", "Abstract"]
    selected = st.selectbox("Choose a category to explore:", options=selected_options)
    st.write("Current selection:", selected)

    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""
        In this gallery, I have compiled some of my favorite photographs across various genres. Each category represents a different aspect of my photography journey, from landscapes to architecture, and from wildlife to portraits.
        
        Enjoy the view!
        """)
    elif selected == "Nature":
        st.subheader("Nature Photography")
        st.write("*Capturing the beauty of the natural world*")
        # Load the nature images
        num_images = 10
        images_nature = [Image.open(f"gallery/nature_{i}.jpg") for i in range(1, num_images + 1)]

        # Display the images in a grid
        num_columns = 3
        num_rows = num_images // num_columns
        remaining_images = num_images % num_columns

        for row in range(num_rows + 1):  # Add 1 to include the last row
            columns = st.columns(num_columns)

            # Calculate the number of columns for the current row
            if row == num_rows:
                num_cols_in_row = remaining_images
            else:
                num_cols_in_row = num_columns

            for col in range(num_cols_in_row):
                index = row * num_columns + col
                with columns[col]:
                    st.image(images_nature[index], use_column_width=True)

    elif selected == "Architecture":
        st.subheader("Architecture Photography")
        st.write("*Showcasing stunning structures from around the world*")
        # Load the architecture images
        num_images = 8
        images_architecture = [Image.open(f"gallery/architecture_{i}.jpg") for i in range(1, num_images + 1)]

        # Display the images in a grid
        num_columns = 3
        num_rows = num_images // num_columns
        remaining_images = num_images % num_columns

        for row in range(num_rows + 1):
            columns = st.columns(num_columns)

            if row == num_rows:
                num_cols_in_row = remaining_images
            else:
                num_cols_in_row = num_columns

            for col in range(num_cols_in_row):
                index = row * num_columns + col
                with columns[col]:
                    st.image(images_architecture[index], use_column_width=True)

    elif selected == "Wildlife":
        st.subheader("Wildlife Photography")
        st.write("*Capturing the wild and free*")
        # Load the wildlife images
        num_images = 7
        images_wildlife = [Image.open(f"gallery/wildlife_{i}.jpg") for i in range(1, num_images + 1)]

        # Display the images in a grid
        num_columns = 3
        num_rows = num_images // num_columns
        remaining_images = num_images % num_columns

        for row in range(num_rows + 1):
            columns = st.columns(num_columns)

            if row == num_rows:
                num_cols_in_row = remaining_images
            else:
                num_cols_in_row = num_columns

            for col in range(num_cols_in_row):
                index = row * num_columns + col
                with columns[col]:
                    st.image(images_wildlife[index], use_column_width=True)

    elif selected == "Travel":
        st.subheader("Travel Photography")
        st.write("*Exploring the world, one shot at a time*")
        # Load the travel images
        num_images = 12
        images_travel = [Image.open(f"gallery/travel_{i}.jpg") for i in range(1, num_images + 1)]

        # Display the images in a grid
        num_columns = 3
        num_rows = num_images // num_columns
        remaining_images = num_images % num_columns

        for row in range(num_rows + 1):
            columns = st.columns(num_columns)

            if row == num_rows:
                num_cols_in_row = remaining_images
            else:
                num_cols_in_row = num_columns

            for col in range(num_cols_in_row):
                index = row * num_columns + col
                with columns[col]:
                    st.image(images_travel[index], use_column_width=True)

    elif selected == "Portraits":
        st.subheader("Portrait Photography")
        st.write("*Capturing emotions and expressions*")
        # Load the portraits images
        num_images = 6
        images_portraits = [Image.open(f"gallery/portraits_{i}.jpg") for i in range(1, num_images + 1)]

        # Display the images in a grid
        num_columns = 2
        num_rows = num_images // num_columns
        remaining_images = num_images % num_columns

        for row in range(num_rows + 1):
            columns = st.columns(num_columns)

            if row == num_rows:
                num_cols_in_row = remaining_images
            else:
                num_cols_in_row = num_columns

            for col in range(num_cols_in_row):
                index = row * num_columns + col
                with columns[col]:
                    st.image(images_portraits[index], use_column_width=True)

    elif selected == "Abstract":
        st.subheader("Abstract Photography")
        st.write("*Playing with light, colors, and textures*")
        # Load the abstract images
        num_images = 5
        images_abstract = [Image.open(f"gallery/abstract_{i}.jpg") for i in range(1, num_images + 1)]

        # Display the images in a grid
        num_columns = 3
        num_rows = num_images // num_columns
        remaining_images = num_images % num_columns

        for row in range(num_rows + 1):
            columns = st.columns(num_columns)

            if row == num_rows:
                num_cols_in_row = remaining_images
            else:
                num_cols_in_row = num_columns

            for col in range(num_cols_in_row):
                index = row * num_columns + col
                with columns[col]:
                    st.image(images_abstract[index], use_column_width=True)

#Resume tab
elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1KdLVbCBwzYxDZxzb4KbPC2O4YdEHCy0F/view?usp=sharing"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (1 page)**"), unsafe_allow_html=True)
    show_pdf("Samrat-Kumar-Gangopadhyay-21BAI1053-resume.pdf")
    with open("Samrat-Kumar-Gangopadhyay-21BAI1053-resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (1 page)",
            data=file,
            file_name="Samrat-Kumar-Gangopadhyay-21BAI1053-resume.pdf",
            mime="application/pdf"
        )

elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,0.5))
        with text_column:
            st.write("Let's connect! You may either reach out to me at samganguly03@gmail.com or use the form below!")
            #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                #st.write('Please help us improve!')
                #Name=st.text_input(label='Your Name',
                                    #max_chars=100, type="default") #Collect user feedback
                #Email=st.text_input(label='Your Email', 
                                    #max_chars=100,type="default") #Collect user feedback
                #Message=st.text_input(label='Your Message',
                                        #max_chars=500, type="default") #Collect user feedback
                #submitted = st.form_submit_button('Submit')
                #if submitted:
                    #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
            def create_database_and_table():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (name TEXT, email TEXT, message TEXT)''')
                conn.commit()
                conn.close()
            create_database_and_table()

            st.subheader("Contact Form")
            if "name" not in st.session_state:
                st.session_state["name"] = ""
            if "email" not in st.session_state:
                st.session_state["email"] = ""
            if "message" not in st.session_state:
                st.session_state["message"] = ""
            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


            column1, column2= st.columns([1,5])
            if column1.button("Submit"):
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                conn.commit()
                conn.close()
                st.success("Your message has been sent!")
                # Clear the input fields
                st.session_state["name"] = ""
                st.session_state["email"] = ""
                st.session_state["message"] = ""
            def fetch_all_contacts():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts")
                rows = c.fetchall()
                conn.close()
                return rows
            
            if "show_contacts" not in st.session_state:
                st.session_state["show_contacts"] = False
            if column2.button("View Submitted Forms"):
                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            
            if st.session_state["show_contacts"]:
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                    st.markdown(markdown_table)
                else:
                    st.write("No contacts found.")


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/samratganguly03/"
            github_url = "https://github.com/samganguly"
            email_url = "https://github.com/samganguly"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
            #st.write("© 2023 Samrat Ganguly")
        with mid:
            st.empty()

elif choose == "Socials":
    st.header("Social Media")
    
    # Personal Instagram Posts
    st.markdown("### Personal Instagram Highlights")
    st.write("Here are some of my favorite personal Instagram posts!")

    # Create a grid with three columns for personal Instagram posts
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <iframe src="https://www.instagram.com/p/DBLQ7EnP1h1/embed" width="320" height="420" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <iframe src="https://www.instagram.com/p/C8kBFpkvy6W/embed" width="320" height="420" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <iframe src="https://www.instagram.com/p/C8ZUe6zPqbq/embed" width="320" height="420" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Photography Instagram Posts
    st.subheader("Photography Instagram Account")
    st.write("Here are some posts from my photography account, showcasing my passion for capturing moments through the lens.")

    # Create a grid with three columns for photography Instagram posts
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <iframe src="https://www.instagram.com/p/C0B6qCVvTUd/embed" width="320" height="420" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <iframe src="https://www.instagram.com/p/Cz3cZs1PJgy/embed" width="320" height="420" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <iframe src="https://www.instagram.com/p/Czk5HbBP0Vf/embed" width="320" height="420" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
        """, unsafe_allow_html=True)





st.markdown("*Copyright © 2023 Samrat Ganguly*")
