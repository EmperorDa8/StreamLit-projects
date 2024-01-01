from PIL import Image
import requests
from streamlit.components.v1 import html
from streamlit_lottie import st_lottie
import streamlit as slt

slt.set_page_config(page_title = 'Dan profile-website', page_icon=':waving_hand:', layout ='wide')

#header

with slt.container():
    slt.subheader('Hello i am Dan Usman :video_game:')
    slt.title('i am an aspiring junior system administrator / junior cloud engineer currently located in Nigeria')
    slt. write('i am a passionate individual looking to leverage my skillset to pursue a rewarding career in cloud computing')
    slt.write('[learn more through my Linkedin >](https://www.linkedin.com/in/dan-usman-b87282134/)')
#---objectives
def lottie_urlget(url):
    rr= requests.get(url)
    if rr.status_code!=200:
        return None
    return rr.json()

def css_file(file_name):
    with open(file_name) as f:
        slt.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

css_file('style/style.css')

lotte_files=lottie_urlget('https://lottie.host/ba90e09a-cb67-427e-86b7-e439e185cddc/rrcxidLaYE.json')
lot_image_IT_auto=Image.open('images/01a.png')
GCp_Img=Image.open('images/G ITwp.jpg')
GCP_gen=Image.open('images/maxres.jpg')
project_gen=Image.open('images/generative_AI.png')

with slt.container():
    slt.write('----')
    left_column, right_column = slt.columns(2)
    with left_column:
        slt.header('my objectives ')
        slt.write('###')
        slt.write('''Seeking a challenging and rewarding internship or entry-level opportunity to apply my Python skills and contribute to a dynamic cloud team. Open to learning new technologies and eager to make a positive impact.
        
        -Leverage Python scripting to automate routine system administration tasks such as user provisioning, configuration management, and data backup/recovery.
        -Applying automation solutions to scale infrastructure and operations in cloud environments.
        
        -Utilize Python for cloud infrastructure provisioning, configuration, and maintenance.
        
        -Troubleshoot and diagnose issues.
        
        -Strengthen security posture:.
        
        ''')
    with right_column:
        st_lottie(lotte_files, height=300, key='cloud computing')

with slt.container():
    slt.write('----')
    image_column, text_column = slt.columns((1,2))
    with text_column:
        slt.header('my professional career google certification ')
        slt.write('###')
        slt.write("""
        My Google IT automation with Python taught me hands-on experience in the following :
1. fundamentals of Python syntax, variables, data types, control flow statements, and functions.
Gain practical experience by writing simple scripts to automate basic tasks like file manipulation, data analysis, and web scraping.

2. Working with APIs:
Understanding how APIs work and interacting with them using Python libraries like requests and beautifulsoup4.
Build scripts that automate interacting with web services, retrieving data, and performing actions.

3. Managing Cloud Resources with Google Cloud Platform (GCP):
introduced to GCP and its core services like Compute Engine, Cloud Storage, and Cloud Functions.
Write Python scripts to provision and manage virtual machines, upload and download files to cloud storage, and trigger serverless functions.

4. Automating System Administration Tasks:
Learnt how to interact with the operating system using Python modules like os and subprocess.
Automate tasks like managing users and groups, scheduling jobs, and monitoring system resources.

5. Working with Databases:
Understand the basics of relational databases and connect to them using Python libraries like pymysql and sqlalchemy.
Write scripts to query databases, extract data, and perform CRUD operations.
 
           """)
        slt.write('[learn more >](https://coursera.org/share/36e937e99bffd61d4cfcd6419d7a7ebe)')
    with image_column:
        slt.image(GCp_Img)


with slt.container():
    slt.write('----')
    img_column, text_column = slt.columns((1,2))
    with text_column:
        slt.header('my recent certification > getting started with generative AI studio 2023')
        slt.write('###')
        slt.write('''
        some hands on experience gained from this certification include the following
        
-solid understanding of generative AI concepts like text generation, translation, image creation, and code generation.
-learnt about the core functionality of Generative AI Studio, including its user interface, pre-trained models, and tools for experimentation.
other exploration include :

-experimenting Google latest AI model gemini for simple task like image extraction, image Q/A, image classificaton , and others with its pre-trained models for
prompt output
         
-also I have been able to leverage the platform to create AI chatbot , enterprize search app which can be deployed with API integration or widget integration to existing application      
        ''')
        slt.write('[learn more >](https://coursera.org/share/00162df6e1184066de5b34bf4f2d0b54)')
    with img_column:
        slt.image(GCP_gen)



with slt.container():
    slt.write('-----')
    slt.header('My_Projects')
    slt.write('##')
    image_column, text_column= slt.columns((1,2))
    with image_column:
        slt.image(lot_image_IT_auto)
    with text_column:
        slt.subheader('working automation scripts for tasks')
        slt.write('they are projects that involves extracting data from a supplier_data link , process the data and upload the data in json format through api endpoint')
        slt.write('[learn more >](https://github.com/EmperorDa8/automation-scale-projects)')

with slt.container():
    slt.write('-----')
    slt.header('My_Projects')
    slt.write('##')
    image_column, text_column= slt.columns((1,2))
    with image_column:
        slt.image(project_gen)
    with text_column:
        slt.subheader('My Generative AI projects attempts')
        slt.write('this projects involves my attempts in using chatgpt Open API and also AI image tools like lenardo AI, and finally generative AI studio with prompt generating including latest multimodal model GEMINI')
        slt.write('[learn more >](https://github.com/EmperorDa8/generativeAI)')
        slt.write('Experience the power Ai semantic search through enterprise search app i created by Google vertex AI which i loaded with BBC-News public dataset on bigquery instance set up in background ')
        slt.subheader('widget_search')
        slt.write('##')

        widget_search= '''

                <!-- Widget JavaScript bundle -->
        <script src="https://cloud.google.com/ai/gen-app-builder/client?hl=en_US"></script>
        
        <!-- Search widget element is not visible by default -->
        <gen-search-widget
          configId="89e9c1be-87fb-4524-b314-6be96f357a94"
          triggerId="searchWidgetTrigger">
        </gen-search-widget>
        
        <!-- Element that opens the widget on click. It does not have to be an input -->
        <input placeholder="Search here" id="searchWidgetTrigger" />

         '''

        html( widget_search)
        
        
        

with slt.container():
    slt.write('-----')
    slt.subheader('Contact_form')
    slt.write('##')

    contact_form= '''
            <form action="https://formsubmit.co/uabdul88@gmail.com" method="POST">
     <input type="text" name="name"  placeholder ='Your name' required>
     <input type="email" name="email" placeholder ='Your email' required>
     <textarea name='message' placeholder='Your message here'  required></textarea>
     <button type="submit">Send</button>
</form>   
    
    '''

    left_column, right_column= slt.columns(2)
    with left_column:
        slt.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        slt.empty()

