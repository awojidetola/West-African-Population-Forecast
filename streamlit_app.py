import streamlit as st
from PIL import Image
import pandas as pd

def overview():
    st.header("Overview")
    st.markdown('''

    This __Web Application__ analyzes the population of the 16 West African Countries. In addition, it forecasts the __population__,
    __crude birth rate__ and __crude death rate__ for each country from 2022 to 2026.
    The data used for this application was collected from [World Bank Open Data](https://data.worldbank.org/), cleaned and uploaded to
    [Kaggle](https://www.kaggle.com/datasets/awojidemargaret/west-african-demograhpics).

    *Check the Sidebar to Navigate*
    
    ''')
    
    image = Image.open('tanzania.jpg')
    st.image(image, caption='Credit: Wallpaper Flare')

def west_africa():
    st.header("West Africa Demograhpics")
    st.markdown('''
    West Africa is located at the western part of the continent. This region of the continent contains over 400 million people in 16 countries. Nigeria, is the most populous country in West Africa with over 200 million occupants.
    Check out the West African Countries [here](https://en.wikipedia.org/wiki/West_Africa)

    ''')
    image = Image.open('westafricamap.gif')
    st.image(image, caption='Image Credit: Appalachian State University')

    st.markdown('''
    Three factors influence the population of a region and they are: Fertility Rate, Mortality Rate and Net Migration. For most countries, especially African countries, Fertility and 
    Mortality are the two most important factors influencing the total population in the country. 
    ''')

    st.markdown('''
    Birth rate significantly influences the population of a country. Nigeria, the most populous country in West Africa, currently has the highest crude birth rate in the World. According to a report by
    __United Nations__, the African continent has the highest birth rate. Africa is currently the fastest [growing population](https://statisticstimes.com/demographics/africa-population.php) and the population size continues to increase.

    ''')

def forecast_analysis():
    st.header("Analysis and Forecast")
    df = pd.read_csv("wa_total_population.csv", index_col = 0, parse_dates = True)
    st.write("Bar Chart showing Total Population of West African Countries in 2021")
    st.bar_chart(df.iloc[-1])
    country = st.selectbox(
     'Select Country',
     ('Benin', 'Burkina Faso', 'Cabo Verde', "Cote d'Ivoire",'Gambia','Ghana','Guinea','Guinea-Bissau','Liberia',
      'Mali','Mauritania','Niger','Nigeria','Senegal','Sierra Leone','Togo'))
    st.line_chart(df[country]) 
    year = st.selectbox('Enter Forecast Year',(2022,2023,2024,2025,2026))

page_names_to_funcs = {
    "General Overview": overview,
    "West African Demographics": west_africa,
    "Analysis & Forecast": forecast_analysis
}


selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
