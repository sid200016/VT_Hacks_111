from pkg_resources import SOURCE_DIST
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
from tensorflow.keras.applications.xception import preprocess_input
import tensorflow as tf

st.set_page_config(page_title="my webpage", page_icon=":smiley:")
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
# add a navigation bar on top of teh webpage using streamlit
# Define the pages
def home_page():
    st.title("Invasive Insight")
    st.write("This is the home page of this application.")

def about_page():
    st.title("About Page")
    st.write("This is the about page of this application.")

def contact_page():
    st.title("Contact Page")
    st.write("This is the contact page of this application.")




# Define the navigation bar
navbar = '''
    <div style="position: fixed; z-index: 999; top: 40px; left: 50px;width: 90%;background-color: #AEF971;padding:10px;font-family:sans-serif; font-size: 28px">
        <a href="#home" style= "color: black; font-size: 25px">Home</a> |
        <a href="#about" style= "color: black; font-size: 25px">Map Data</a> |
        <a href="#contact" style= "color: black; font-size: 25px">Identify Invasive species</a>|
         <a href="#contact" style= "color: black; font-size: 25px">Know more </a>|
    </div>
'''




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

<h2 class="company_name">Invasive Insight</h2>
<p class="tagline">Guarding Nature: Your Guide to Invasive Species Awareness</p>

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
  <img src="https://www.researchgate.net/publication/338661038/figure/fig1/AS:848488678035456@1579306873511/Chinese-mitten-crab-Eriocheir-japonica-sinensis.png">
  <div class="text">Chinese Mitten Crab</div>
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
 
 
class FileUpload(object):
 
    def __init__(self):
        self.fileTypes = ["csv", "png", "jpg"]
 
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
            show_file.info("Please upload a file of type: " + ", ".join(["csv", "png", "jpg"]))
            return
        content = file.getvalue()
        if isinstance(file, BytesIO):
            # Display the uploaded image
            img = Image.open(file)
            show_file.image(img, caption="Uploaded Image", use_column_width=True)
        else:
            data = pd.read_csv(file)
            st.dataframe(data.head(10))
        file.close()
 
 
if __name__ ==  "__main__":
    helper = FileUpload()
    helper.run()

def Classify_img(uploaded_image):
    # Load the .h5 model file
    model = tf.keras.models.load_model('./my_model.h5')

    # Pre Process the uploaded Image
    uploaded_image = pre_process(uploaded_image)

    # Assuming you have obtained predictions from the model
    predictions = model.predict(uploaded_image)

    # Define the threshold value
    threshold = 0.5  # Adjust this threshold as needed

    if np.max(predictions) <= threshold:
        # Classify as "Non-Invasive" (last category)
        print("Non-Invasive")
    else:
        # Classify based on the other categories
        category = predictions.argmax()
        if category == 0:
            print("Spotted Lanternfly")
        elif category == 1:
            print("Zebra Mussel")
        elif category == 2:
            print("Sirex Wood Wasp")
        elif category == 3:
            print("Rusty Crayfish")
        elif category == 4:
            print("Chinese Mitten Crab")



def pre_process(uploaded_img):
    uploaded_image = uploaded_image.resize((224, 224))
    uploaded_image = np.array(uploaded_image)
    uploaded_image = preprocess_input(uploaded_image)
    uploaded_image = np.expand_dims(uploaded_image, axis=0)

    return uploaded_img
    



url = 'https://stackoverflow.com'

st.markdown(f'''
<a href={url}><button style="background-color:GreenYellow; font-size: 30px; border-radius: 30px">Check out Map Data</button></a>
''',
unsafe_allow_html=True)

url = 'https://stackoverflow.com'

st.markdown(f'''
<a href={url}><button style="background-color:GreenYellow; font-size: 30px; border-radius: 30px">Know more about Invasive species</button></a>
''',
unsafe_allow_html=True)
st.markdown(navbar, unsafe_allow_html=True)
# Navigation Logic

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
with open("style.css") as source:
    st.markdown(f"<style>{source.read()}</style>", unsafe_allow_html=True)

