from pkg_resources import SOURCE_DIST
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
import tensorflow as tf
import requests
import os
from streamlit_option_menu import option_menu

# Libraries for ML model
import numpy as np
import pandas as pd
import tensorflow as tf

from streamlit_lottie import st_lottie


# Tensorflow Libraries
from tensorflow import keras
from tensorflow.keras.applications.xception import preprocess_input

# Code for the home, about, contact
# add a navigation bar on top of teh webpage using streamlit
# Define the pages
def home_page():
    st.markdown('<div style="font-size:60px ;text-align:center;color:white;font-family:Helvetica;">Invasive Insight</div>', unsafe_allow_html=True)
    #st.write("This is the home page of this application.")


def about_page():
    st.title("About Page")
    st.write("This is the about page of this application.")



def contact_page():
    st.title("Contact Page")
    st.write("This is the contact page of this application.")

def load_lottieurl(url):
    r = requests.get(url)
    return r.json()





# Streamlit stuff goes here.
st.set_page_config(page_title="my webpage", page_icon=":house:",layout = "wide")
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)


location_hash = st.experimental_get_query_params().get("nav", None)
if location_hash:
    location_hash = location_hash[0]

if location_hash == 'home':
    home_page()
elif location_hash == 'about':
    about_page()
elif location_hash == 'contact':
    contact_page()
else:
    home_page()  # Default is home








# Lottie
lottie_coding = load_lottieurl('https://lottie.host/515560b6-b5ea-45d4-a8ed-788ef12f64c4/sHcIqQux0Z.json')
# Position the Lottie animation
# Create a Streamlit container

# Place the Lottie animation within the container
# Place the Lottie animation in the right column
# Create columns with custom spacing
# Create columns with custom spacing
# Apply custom CSS to color the container

st.sidebar.success("select")

with st.container():
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.write('#')
        st.markdown('<div style="text-align: left;margin-left:5px; background-color:#042601;">&emsp;&emsp;&emsp;&emsp;Did you know?&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Economists estimate that invasive species cost the United States &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;more than $120 billion in damages</div>', unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding, height=150, key="coding")
st.write("##")

# Partition the stuff
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write("##")
        st.write("##")

        st.write(
            """
An invasive species is an introduced, nonnative organism (disease, parasite, plant, or animal) that begins to spread or expand its range from the site of its original introduction and that has the potential to cause harm to the environment, the economy, or to human health. Invasive species are spread primarily by human activities, often unintentionally. People, and goods transported, travel quickly around the world, and often carry uninvited species with them. The introduction and establishment of invasive species to the U.S. (intentional or unintentional) can pose a significant threat to native and plant communities. Invasive species can lead to the extinction of native plants and animals, destroy biodiversity, and permanently alter habitats.
            """
        )
    with right_column:
        components.html(
            """
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        * {box-sizing: border-box;}
        body {font-family: Verdana, sans-serif;}
        .mySlides {display: none;}
        img {vertical-align: middle;}

        /* Slideshow container */
        .slideshow-container {
          max-width: 1000px;
          position: relative;
          margin: auto;
        }

        /* Caption text */
        .text {
          color: black;
          font-size: 28px;
          padding: 8px 12px;
          position: absolute;
          bottom: 8px;
          width: 100%;
          text-align: center;
        }       
        .text1 {
          color: white;
          font-size: 28px;
          padding: 8px 12px;
          position: absolute;
          bottom: 8px;
          width: 100%;
          text-align: center;
        }

        /* Number text (1/3 etc) */
        .numbertext {
          color: #f2f2f2;
          font-size: 12px;
          padding: 8px 12px;
          position: absolute;
          top: 0;
        }

        /* The dots/bullets/indicators */
        .dot {
          height: 15px;
          width: 15px;
          margin: 0 2px;
          background-color: #bbb;
          border-radius: 50%;
          display: inline-block;
          transition: background-color 0.6s ease;
        }

        .company_name{
            color: white;
            font-family: Helvetica;
            font-size: 40px;
        }

        .tagline{
            color: white;
            font-family: Helvetica;
            font-size: 20px;
        }

        .active {
          background-color: #717171;
        }

        /* Fading animation */
        .fade {
          animation-name: fade;
          animation-duration: 1.5s;
        }

        @keyframes fade {
          from {opacity: .4} 
          to {opacity: 1}
        }

        /* On smaller screens, decrease text size */
        @media only screen and (max-width: 300px) {
          .text {font-size: 11px}
        }
        </style>
        </head>
        <body>

        <p class="tagline">Guarding Nature: Your Guide to Invasive Species</p>

        <div class="slideshow-container">

        <div class="mySlides fade">
          <div class="numbertext">1 / 5</div>
          <img src="https://cals.cornell.edu/sites/default/files/styles/hero_landing_desktop/public/2021-07/0728_lanternfly2.jpeg?h=c74750f6&itok=4lJ5ktcT" style="width:100%">
          <div class="text">Spotted Lanternfly</div>
        </div>

        <div class="mySlides fade">
          <div class="numbertext">2 / 5</div>
          <img src="https://d32ogoqmya1dw8.cloudfront.net/images/eyesinthesky2/week5/small_zebra_mussel_image.jpg" style="width:100%">
          <div class="text">Zebra Mussel</div>
        </div>

        <div class="mySlides fade">
          <div class="numbertext">3 / 5</div>
          <img src="https://entnemdept.ufl.edu/creatures/misc/wasps/Sirex_noctilio01.jpg" style="width:100%">
          <div class="text">Sirex Wood Wasp</div>
        </div>

        <div class="mySlides fade">
          <div class="numbertext">4 / 5</div>
          <img src="https://extension.umn.edu/sites/extension.umn.edu/files/rustycrayfish_inset1.jpg" style="width:100%">
          <div class="text">Rusty Crayfish</div>
        </div>

        <div class="mySlides fade">
          <div class="numbertext">5 / 5</div>
          <img src="https://featuredcreature.com/wp-content/uploads/2012/11/tumblr_mclsu7252N1qzou5ko1_5002.jpg">
          <div class="text1">Chinese Mitten Crab</div>
        </div>

        </div>
        <br>

        <div style="text-align:center">
          <span class="dot"></span> 
          <span class="dot"></span> 
          <span class="dot"></span> 
          <span class="dot"></span> 
          <span class="dot"></span> 
        </div>

        <script>
        let slideIndex = 0;
        showSlides();

        function showSlides() {
          let i;
          let slides = document.getElementsByClassName("mySlides");
          let dots = document.getElementsByClassName("dot");
          for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
          }
          slideIndex++;
          if (slideIndex > slides.length) {slideIndex = 1}    
          for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
          }
          slides[slideIndex-1].style.display = "block";  
          dots[slideIndex-1].className += " active";
          setTimeout(showSlides, 2500); // Change image every 2 seconds
        }
        </script>

        </body>
        </html> 

            """,
            height=600,
        )


try:
    from enum import Enum
    from io import BytesIO, StringIO
    from typing import Union

    import pandas as pd
    import streamlit as st
except Exception as e:
    print(e)

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

def pre_process(uploaded_image):
    uploaded_image = uploaded_image.resize((224, 224))
    uploaded_image = np.array(uploaded_image)
    uploaded_image = preprocess_input(uploaded_image)
    uploaded_image = np.expand_dims(uploaded_image, axis=0)

    return uploaded_image

def classify_img(uploaded_image):
    # Load the .h5 model file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the image
    image_path = os.path.join(script_dir, "my_model.h5")
    model = tf.keras.models.load_model(image_path)

    # Pre Process the uploaded Image
    uploaded_image = pre_process(uploaded_image)

    # Assuming you have obtained predictions from the model
    predictions = model.predict(uploaded_image)

    # Define the threshold value
    threshold = 0.6  # Adjust this threshold as needed

    if np.max(predictions) <= threshold:
        # Classify as "Non-Invasive" (last category)
        return "Non-Invasive"
    else:
        # Classify based on the other categories
        category = predictions.argmax()
        if category == 0:
            return "Chinese Mitten Crab"
        elif category == 1:
            return "Rusty Crayfish"
        elif category == 2:
            return "Sirex Wood Wasp"
        elif category == 3:
            return "Spotted Lanternfly"
        elif category == 4:
            return "Zebra Mussel"



class FileUpload(object):

    def __init__(self):
        self.fileTypes = ["png", "jpg"]

    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        file = st.file_uploader("Upload file", type=self.fileTypes)
        show_file = st.empty()
        if not file:
            show_file.info("Please upload a file of type: " + ", ".join(["png", "jpg"]))

        if isinstance(file, BytesIO):
            # Display the uploaded image
            img = Image.open(file)
            text = classify_img(img)
            show_file.image(img, use_column_width=True)
            st.markdown(f'<div style="text-align: center;font-size:30px;font-family:serif;">{text}</div>', unsafe_allow_html=True)
            st.write("##")
            file.close()


if __name__ == "__main__":
    helper = FileUpload()
    helper.run()




# url = 'https://devpost.com/software/invasive-insight?ref_content=user-portfolio&ref_feature=in_progress'
#
# st.markdown(f'''
# <a href={url}><button style="background-color:GreenYellow; font-size: 20px; border-radius: 30px">Check out our DevPost</button></a>
# ''',unsafe_allow_html=True)

url = 'http://www.iucngisd.org/gisd/'

st.markdown(f'''
<a href={url}><button style="background-color:GreenYellow; font-size: 20px; border-radius: 30px">Know more about Invasive species</button></a>
''', unsafe_allow_html=True)
# Navigation Logic


