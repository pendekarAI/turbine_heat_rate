# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Turbine Heat Rate</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>Indonesia Power</h1>", unsafe_allow_html=True)
st.markdown('---'*10)

# Load model
my_model = pickle.load(open('model_regresi_turbine_heat_rate.pkl', 'rb'))

# Pilihan utama

pilihan = st.selectbox('Apa yang ingin Anda lakukan?',['Prediksi dari PyVision', 'Input Manual'])

if pilihan == 'Prediksi dari PyVision':
    # Mengupload file
    st.write('Sedang tahap pengembangan')
    
else:
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            load_mw = st.number_input('Load (MW)', value= 221.0)
        with col2:
            load = st.number_input('Load', value= 221)
        with col3:
            ms_temp = st.number_input('MS Temp, degc', value= 540.67)

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            rh_temp = st.number_input('RH Temp, degc', value= 542.12)
        with col2:
            ms_press = st.number_input('MS Press, bar', value= 122.31)
        with col3:
            rh_press = st.number_input('RH Press, mpa', value= 2.33)
    
    data = {
        'MS Temp': ms_temp,
        'RH Temp': rh_temp,
        'MS Press': ms_press
        }
    
    kolom = list(data.keys())
    
    df_final = pd.DataFrame([data.values()],columns=kolom)
    
    # Predict
    result = round(float(my_model.predict(df_final)),2)
    
    st.write('<center><b><h3>Turbine Heat Rate= ', str(result),'</b></h3>', unsafe_allow_html=True)