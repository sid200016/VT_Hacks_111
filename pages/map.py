import string
import streamlit as st
import time
import numpy as np
from streamlit_folium import st_folium
import folium
import pandas as pd
import string
import streamlit.components.v1 as components
import openai
import os
from PIL import Image

# list of functions
def gpt_Response(input):
    API_KEY = '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'
    openai.api_key = API_KEY
    response = openai.Completion.create(engine = "text-davinci-001", prompt = input, max_tokens = 1000, temperature = 0.3)
    resp = response["choices"][0]["text"]
    return resp
        


def display_map(value):
    gmap='<iframe src="https://maps.eddmaps.org/google/eradication.cfm?notitle&&subjectnumber='+value+'&country=926&lat=39.8283&lng=-98.5795&zoom=5" frameborder="0" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" height="500" width="700" scrolling="no"></iframe>'
    return gmap

#making map data for all the 50 species
# plants
plantmap = {"Purple Loosestrife (Lythrum salicaria)":"3047"}
plantmap["Please choose one"]="1111"
plantmap["Hydrilla (Hydrilla verticillata)"] = "3028"
plantmap["Water Hyacinth (Eichhornia crassipes)"] = "3020"
plantmap["Giant Reed (Arundo donax)"] = "3009"
plantmap["Japanese Knotweed (Reynoutria japonica)"] ="19655"
plantmap["Tamarisk (Tamarix spp.)"] = "3078"
plantmap["English Ivy (Hedera helix)"]="3027"
plantmap["Autumn Olive (Elaeagnus umbellata)"] = "3021"
plantmap["Garlic Mustard (Alliaria petiolata)"] = "3005"
plantmap["Leafy Spurge (Euphorbia esula)"] = "3405"
plantmap["Mile-a-Minute Weed (Persicaria perfoliata)"] = "3065"

# animals
animap = {}
animap["Please choose one"]="1111"
animap["Burmese Python (Python bivittatus)"]="20461"
animap["Zebra Mussel (Dreissena polymorpha)"]="10567"
animap["European Starling (Sturnus vulgaris)"] = "12243"
animap["Cane Toad (Rhinella marina)"] = "12242"
animap["Nutria (Myocastor coypus)"]="4334"

# insects
imap = {}
imap["Please choose one"]="1111"
imap["Brown Stink bug(Euchistus Servus)"] = "2530"
imap["African honey bee(Apis mellifera scutellata)"] = "5000"
imap["Spotted Lanternfly (Lycorma delicatula)"] = "77293"
imap["cheatgrass (downy brome bromus tectorum)"] = "5214"
imap["common buckthorn(Rhamnus cathartica)"] = "3070"
imap["chinese privet(ligustrum sinese)"] = "3035"
imap["Brazillian peppertree(Schinus terebinthifolius)"] = "78819"
imap["Japense Beetle(popilla japonica)"]="213"


#aquatic
aquamap = {}
aquamap["Please choose one"]="1111"
aquamap["Eurasian Watermilfoil"] = "3055"
aquamap["lionfish"] = "12249"
aquamap["Rusty Crayfish (Faxonius rusticus)"] = "87669"
aquamap["Chinese Mystery Snail (Cipangopaludina chinensis)"] = "59309"
aquamap["Goldfish (Carassius auratus)"]="15299"
aquamap["Asian Carp (Hypophthalmichthys spp.)"] = "12248"
aquamap["Asian Swamp Eel"] = "12245"
st.set_page_config(page_title="Streamlit App", page_icon=":world_map:", layout="wide")

i = False
species = ""
temp = ""
# we need to use streamlit using st containers to display the data. on the left side will be the map and on the right side will be the data

st.markdown("<h1 style='text-align: center; color: white;font-size:70px'>Invasive Species Tracker</h1>", unsafe_allow_html=True)



col1,col2 = st.columns(2)
with col1:
    st.markdown("<h1 style='text-align: center; color: #286E15;'>Invasive species Map!</h1>", unsafe_allow_html=True)
    value = "1111"
    another_main_container = st.container()

with col2:
    st.markdown("<h1 style='text-align: center; color: #286E15;'>LETS LEARN!!</h1>", unsafe_allow_html=True)
    choice = st.selectbox(
    'Select the species you want learn about?',
    ('Please choose one','animal','insects','plants','aquatic'))
    st.write('You selected:', choice)
    main_container = st.container()
    part3_container = st.container()
    
    

if choice == 'Please choose one':
    value = "1111"
    tvalue=display_map(value)
    if tvalue != None:
        i = True
        another_main_container.markdown(tvalue, unsafe_allow_html=True)

if choice == 'animal':
    # show all the map keys in the form of a list
    # select the animal you want to learn about
    species = main_container.selectbox(
    'Select the animal you want learn about?',
    ('Please choose one','Burmese Python (Python bivittatus)','Zebra Mussel (Dreissena polymorpha)','European Starling (Sturnus vulgaris)','Cane Toad (Rhinella marina)','Nutria (Myocastor coypus)'))
    # show the animal you selected
    #find the value in the map and then display the map
    value = animap[species]
    tvalue=display_map(value)
    if tvalue != None:
        i = True
        another_main_container.markdown(tvalue, unsafe_allow_html=True)

    
if choice == 'insects':
    species = main_container.selectbox(
    'Select the insect you want learn abomain_containerut?',
    ('Please choose one','Spotted Lanternfly (Lycorma delicatula)','cheatgrass (downy brome bromus tectorum)','common buckthorn(Rhamnus cathartica)','chinese privet(ligustrum sinese)','Brazillian peppertree(Schinus terebinthifolius)','Japense Beetle(popilla japonica)','Brown Stink bug(Euchistus Servus)','African honey bee(Apis mellifera scutellata)'))
    value = imap[species]
    tvalue=display_map(value)
    if tvalue != None:
        i = True
        another_main_container.markdown(tvalue, unsafe_allow_html=True)


if choice == 'plants':
    species = main_container.selectbox(
    'Select the plant you want learn about?',
        ('Please choose one','Purple Loosestrife (Lythrum salicaria)','Hydrilla (Hydrilla verticillata)','Water Hyacinth (Eichhornia crassipes)','Giant Reed (Arundo donax)','Japanese Knotweed (Reynoutria japonica)','Tamarisk (Tamarix spp.)','English Ivy (Hedera helix)','Autumn Olive (Elaeagnus umbellata)','Garlic Mustard (Alliaria petiolata)','Leafy Spurge (Euphorbia esula)','Mile-a-Minute Weed (Persicaria perfoliata)'))
    value = plantmap[species]
    tvalue=display_map(value)
    if tvalue != None:
        i = True
        another_main_container.markdown(tvalue, unsafe_allow_html=True)

if choice == 'aquatic':
    species = main_container.selectbox(
    'Select the fish you want learn about?',
        ('Please choose one','Eurasian Watermilfoil','lionfish','Rusty Crayfish (Faxonius rusticus)','Chinese Mystery Snail (Cipangopaludina chinensis)','Goldfish (Carassius auratus)','Asian Carp (Hypophthalmichthys spp.)','Asian Swamp Eel'))
    value = aquamap[species]
    tvalue=display_map(value)
    if tvalue != None:
        i = True
        another_main_container.markdown(tvalue, unsafe_allow_html=True)



# function to just take the value and display the map         

               

col3,col5 = part3_container.columns(2)

with col3:
    if (species != ""):
        prompt = "Give a brief description of: " + species + " and its impact on the environment"
        answer = gpt_Response(prompt)
        st.write(answer)


    
with col5:
    if(species != "" and species != "Please choose one"):
        # Get the directory of the current script (map.py)
        script_dir = os.path.dirname(os.path.abspath(__file__))


        # Construct the full path to the image
        image_path = os.path.join(script_dir, species)
        temp = image_path+'.jpg'
        print(temp)
        image =Image.open(temp)
        st.image(image, caption="")

    

