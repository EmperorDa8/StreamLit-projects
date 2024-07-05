from PIL import Image
import requests
from streamlit_lottie import st_lottie
import streamlit as slt

slt.set_page_config(page_title='Dan profile-website', page_icon=':waving_hand:', layout='wide')

# Header
with slt.container():
    slt.subheader('Hello I am Dan Usman :video_game:')
    slt.title('Experienced Junior System Administrator with a Strong Foundation in Google IT Automation and Prompt Engineering')
    slt.write('I am a passionate individual looking to leverage my skillset to pursue a rewarding career in cloud computing and Gen AI')
    slt.write('[Learn more through my LinkedIn >](https://www.linkedin.com/in/dan-usman-b87282134/)')

# Objectives
def lottie_urlget(url):
    rr = requests.get(url)
    if rr.status_code != 200:
        return None
    return rr.json()

def css_file(file_name):
    with open(file_name) as f:
        slt.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

css_file('style/style.css')

lotte_files = lottie_urlget('https://lottie.host/ba90e09a-cb67-427e-86b7-e439e185cddc/rrcxidLaYE.json')
lot_image_IT_auto = Image.open('images/01a.png')
GCp_Img = Image.open('images/G ITwp.jpg')
GCP_gen = Image.open('images/maxres.jpg')
project_gen = Image.open('images/generative_AI.png')

with slt.container():
    slt.write('----')
    left_column, right_column = slt.columns(2)
    with left_column:
        slt.header('My Objectives')
        slt.write('###')
        slt.write('''Seeking a challenging and rewarding internship or entry-level opportunity to apply my IT/cloud skills and contribute to a dynamic cloud team. Open to learning new technologies and eager to make a positive impact.
        
        - Leverage Python scripting to automate routine system administration tasks such as user provisioning, configuration management, and data backup/recovery.
        - Applying automation solutions to scale infrastructure and operations in cloud environments.
        - Utilize Python for cloud infrastructure provisioning, configuration, and maintenance.
        - Troubleshoot and diagnose issues.
        - Strengthen security posture.
        ''')
    with right_column:
        st_lottie(lotte_files, height=300, key='cloud_computing')

with slt.container():
    slt.write('----')
    image_column, text_column = slt.columns((1, 2))
    with text_column:
        slt.header('My Professional Career Google Certification')
        slt.write('###')
        slt.write("""
        My Google IT automation with Python taught me hands-on experience in the following:
        1. Fundamentals of Python syntax, variables, data types, control flow statements, and functions.
           Gain practical experience by writing simple scripts to automate basic tasks like file manipulation, data analysis, and web scraping.
        2. Working with APIs:
           Understanding how APIs work and interacting with them using Python libraries like requests and beautifulsoup4.
           Build scripts that automate interacting with web services, retrieving data, and performing actions.
        3. Managing Cloud Resources with Google Cloud Platform (GCP):
           Introduced to GCP and its core services like Compute Engine, Cloud Storage, and Cloud Functions.
           Write Python scripts to provision and manage virtual machines, upload and download files to cloud storage, and trigger serverless functions.
        4. Automating System Administration Tasks:
           Learnt how to interact with the operating system using Python modules like os and subprocess.
           Automate tasks like managing users and groups, scheduling jobs, and monitoring system resources.
        5. Working with Databases:
           Understand the basics of relational databases and connect to them using Python libraries like MySQL and sqlalchemy.
           Write scripts to query databases, extract data, and perform CRUD operations.
        """)
        slt.write('[Learn more >](https://coursera.org/share/36e937e99bffd61d4cfcd6419d7a7ebe)')
    with image_column:
        slt.image(GCp_Img)

with slt.container():
    slt.write('----')
    img_column, text_column = slt.columns((1, 2))
    with text_column:
        slt.header('My Recent Certification: Getting Started with Generative AI Studio 2023')
        slt.write('###')
        slt.write('''
        Some hands-on experience gained from this certification include the following:
        - Solid understanding of generative AI concepts like text generation, translation, image creation, and code generation.
        - Learnt about the core functionality of Generative AI Studio, including its user interface, pre-trained models, and tools for experimentation.
        Other explorations include:
        - Experimenting with Google's latest AI model Gemini for simple tasks like image extraction, image Q/A, image classification, and others with its pre-trained models for prompt output.
        - Also, I have been able to leverage the platform to create an AI chatbot and enterprise search app that can be deployed with API integration or widget integration to existing applications.
        ''')
        slt.write('[Learn more >](https://coursera.org/share/00162df6e1184066de5b34bf4f2d0b54)')
        slt.write('[Access the enterprise AI search app created and deployed by me using Cloud Run >](https://apptest-cdxrwirz7a-nw.a.run.app/)')
    with img_column:
        slt.image(GCP_gen)

with slt.container():
    slt.write('-----')
    slt.header('My Projects')
    slt.write('##')
    image_column, text_column = slt.columns((1, 2))
    with image_column:
        slt.image(lot_image_IT_auto)
    with text_column:
        slt.subheader('Working Automation Scripts for Tasks')
        slt.write('These are projects that involve extracting data from a supplier_data link, processing the data, and uploading the data in JSON format through an API endpoint.')
        slt.write('[Learn more >](https://github.com/EmperorDa8/automation-scale-projects)')

with slt.container():
    slt.write('-----')
    slt.header('My Projects')
    slt.write('##')
    image_column, text_column = slt.columns((1, 2))
    with image_column:
        slt.image(project_gen)
    with text_column:
        slt.subheader('My Generative AI Projects Attempts')
        slt.write('These projects involve my attempts in using ChatGPT Open API and also AI image tools like Leonardo AI, and finally Generative AI Studio with prompt engineering including the latest multimodal model GEMINI-ultra.')
        slt.write('[Learn more >](https://github.com/EmperorDa8/generativeAI)')
        slt.write('Experience the power of AI semantic search through an AI chatbot I created using Google Vertex AI, which I loaded with my dataset on a cloud storage instance set up in the background. Also, develop AI enterprise search on the same platform.')
    

slt.html(''' 
<script src="https://sf-cdn.coze.com/obj/unpkg-va/flow-platform/chat-app-sdk/0.1.0-beta.4/libs/oversea/index.js"></script>
<script>
    new CozeWebSDK.WebChatClient({
        config: {
            bot_id: '7387920960499810309',
        },
        componentProps: {
            title: 'Coze',
        },
    });
</script> ''')

with slt.container():
    slt.write('-----')
    slt.subheader('Contact Form')
    slt.write('##')

contact_form = '''
    <form action="https://formsubmit.co/uabdul88@gmail.com" method="POST">
        <input type="text" name="name" placeholder='Your name' required>
        <input type="email" name="email" placeholder='Your email' required>
        <textarea name='message' placeholder='Your message here' required></textarea>
        <button type="submit">Send</button>
    </form>
    '''

    left_column, right_column = slt.columns(2)
    with left_column:
        slt.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        slt.empty()


