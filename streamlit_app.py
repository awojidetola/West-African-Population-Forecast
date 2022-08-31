import streamlit as st
from PIL import Image
import pandas as pd
from pmdarima.arima import auto_arima

def overview():
    st.header("Overview")
    st.markdown('''

    This __Web Application__ analyzes the population of the 16 West African Countries. In addition, it forecasts the __population__,
    __crude birth rate__ and __crude death rate__ for each country from 2022 to 2026.
    The data used for this application was collected from [World Bank Open Data](https://data.worldbank.org/), cleaned and uploaded to
    [Kaggle](https://www.kaggle.com/datasets/awojidemargaret/west-african-demograhpics).

    *Check the Sidebar to Navigate*
    
    ''')
    
    image = Image.open('images/tanzania.jpg')
    st.image(image, caption='Credit: Wallpaper Flare')

def west_africa():
    st.header("West Africa Demograhpics")
    st.markdown('''
    West Africa is located at the western part of the continent. This region of the continent contains over 400 million people in 16 countries. Nigeria, is the most populous country in West Africa with over 200 million occupants.
    Check out the West African Countries [here](https://en.wikipedia.org/wiki/West_Africa)

    ''')
    image = Image.open('images/westafricamap.gif')
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
    
    df_pop = pd.read_csv("preprocessed files/total_pop.csv", index_col = 0, parse_dates = True)
    df_cbr = pd.read_csv("preprocessed files/crude_birth_rate.csv",index_col = 0, parse_dates = True)
    df_cdr = pd.read_csv("preprocessed files/crude_death_rate.csv",index_col = 0, parse_dates = True)
    df_cdr = df_cdr.iloc[:-1, :]
    
    st.write("Bar Chart showing Total Population of West African Countries in 2021")
    st.bar_chart(df_pop.iloc[-1])
    
    country = st.selectbox(
     'Select Country',
     ('Benin', 'Burkina Faso', 'Cabo Verde', "Cote d'Ivoire",'Gambia','Ghana','Guinea','Guinea-Bissau','Liberia',
      'Mali','Mauritania','Niger','Nigeria','Senegal','Sierra Leone','Togo'))
    year = st.selectbox('Enter Forecast Year',(2022,2023,2024,2025,2026))
    metric = st.selectbox("Select Demographic", ('Total Population', 'Crude Birth Rate','Crude Death Rate'))

    st.write("Line Plot showing the {} for {}".format(metric, country))
    
    if metric == 'Total Population':
        st.line_chart(df_pop[country])
    elif metric == 'Crude Birth Rate':
        st.line_chart(df_cbr[country])
    else:
        st.line_chart(df_cdr[country])

    if st.button('Submit'):
        if metric == "Total Population":
            arima_model = auto_arima(df_pop[country], start_p=0, d=3, start_q=0, max_p=10, max_d=4, max_q=10, seasonal=False,
                        error_action='warn', trace=True, supress_warnings=True, 
                        stepwise=True, random_state=20, n_fits=50)
            prediction = arima_model.predict(n_periods = 5)
            if year == 2022:
                st.write("The population in {} will be approximately {:,} people".format(year, round(prediction[0])))
            elif year == 2023:
                st.write("The population in {} will be approximately {:,} people".format(year, round(prediction[1])))
            elif year == 2024:
                st.write("The population in {} will be approximately {:,} people".format(year, round(prediction[2])))
            elif year == 2025:
                st.write("The population in {} will be approximately {:,} people".format(year, round(prediction[3])))
            else:
                st.write("The population in {} will be approximately {:,} people".format(year, round(prediction[4])))
                
        elif metric == 'Crude Birth Rate':
            arima_model = auto_arima(df_cbr[country], start_p=0, d=2, start_q=0, max_p=10, max_d=3, max_q=10, seasonal=False,
                        error_action='warn', trace=True, supress_warnings=True, 
                        stepwise=True, random_state=20, n_fits=50)
            prediction = arima_model.predict(n_periods = 5)            
            if year == 2022:
                st.write("The Crude Birth Rate for {} will be {}/1000 people".format(year, round(prediction[0])))
            elif year == 2023:
                st.write("The Crude Birth Rate for {} will be {}/1000 people".format(year, round(prediction[1])))
            elif year == 2024:
                st.write("The Crude Birth Rate for {} will be {}/1000 people".format(year, round(prediction[2])))
            elif year == 2025:
                st.write("The Crude Birth Rate for {} will be {}/1000 people".format(year, round(prediction[3])))
            else:
                st.write("The Crude Birth Rate for {} will be {}/1000 people".format(year, round(prediction[4])))
                
        else:
            arima_model = auto_arima(df_cdr[country], start_p=0, d=2, start_q=0, max_p=10, max_d=3, max_q=10, seasonal=False,
                        error_action='warn', trace=True, supress_warnings=True, 
                        stepwise=True, random_state=20, n_fits=50)
            prediction = arima_model.predict(n_periods = 5)            
            if year == 2022:
                st.write("The Crude Death Rate for {} will be {}/1000 people".format(year, round(prediction[0])))
            elif year == 2023:
                st.write("The Crude Death Rate for {} will be {}/1000 people".format(year, round(prediction[1])))
            elif year == 2024:
                st.write("The Crude Death Rate for {} will be {}/1000 people".format(year, round(prediction[2])))
            elif year == 2025:
                st.write("The Crude Death Rate for {} will be {}/1000 people".format(year, round(prediction[3])))
            else:
                st.write("The Crude Death Rate for {} will be {}/1000 people".format(year, round(prediction[4])))
                
    else:
     st.write('Click to forecast!')
    
page_names_to_funcs = {
    "General Overview": overview,
    "West African Demographics": west_africa,
    "Analysis & Forecast": forecast_analysis
}


selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
