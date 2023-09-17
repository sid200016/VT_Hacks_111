import streamlit as st
import time
import numpy as np
from streamlit_folium import st_folium
import folium
import pandas as pd

#making map data for all the 50 species
# plants
animap = {"Purple Loosestrife (Lythrum salicaria)":"3047"}
animap["Hydrilla (Hydrilla verticillata)"] = "3028"
animap["Water Hyacinth (Eichhornia crassipes)"] = "3020"
animap["Giant Reed (Arundo donax)"] = "3009"
animap["Japanese Knotweed (Reynoutria japonica)"] ="19655"
animap["Tamarisk (Tamarix spp.)"] = "3078"
animap["English Ivy (Hedera helix)"]="3027"
animap["Autumn Olive (Elaeagnus umbellata)"] = "3021"
animap["Garlic Mustard (Alliaria petiolata)"] = "3005"
animap["Leafy Spurge (Euphorbia esula)"] = "3405"
animap["Mile-a-Minute Weed (Persicaria perfoliata)"] = "3065"

# animals
animap["Burmese Python (Python bivittatus)"]="20461"
animap["Zebra Mussel (Dreissena polymorpha)"]="10567"
animap["European Starling (Sturnus vulgaris)"] = "12243"
animap["Cane Toad (Rhinella marina)"] = "12242"
animap["Nutria (Myocastor coypus)"]="4334"
st.set_page_config(page_title="Streamlit App", page_icon=":smiley:")




st.markdown('<iframe src="https://maps.eddmaps.org/google/eradication.cfm?notitle&&subjectnumber=19660&country=926&lat=39.8283&lng=-98.5795&zoom=5" frameborder="0" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" height="500" width="960" scrolling="no"></iframe>', unsafe_allow_html=True)
                     
                         
                         
                         
                          # # center on Liberty Bell, add marker
# m = folium.Map(location=[39.949610, -75.150282], zoom_start=19)
# folium.Marker(
#     [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)


