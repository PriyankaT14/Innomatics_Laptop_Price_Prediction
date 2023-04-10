import streamlit as st
import pickle
import numpy as np
import pandas as pd


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
# import the model
# pipe = pickle.load(open('pipe.pkl','rb'))
# df = pickle.load(open('df1.pkl','rb'))
# df = pickle.load(open('predictor.pickle','rb'))
df = pd.read_csv("df.csv")
pipe = pickle.load(open("pipe.pkl", "rb"))

# def main():

st.title("Laptop Price Predictor")

# brand
brand = st.selectbox('Brand',df['Brand'].unique())
# brand = st.selectbox('Brand', [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16])
# brand = st.selectbox('Brand',df.columns[0].unique())

#cpu
cpubrand = st.selectbox('CPU',df['Cpu Brand'].unique())
# cpubrand = st.selectbox('CPU', [ 3,  1,  2,  5,  6,  8,  4,  7, 10,  9])
# cpubrand = st.selectbox('CPU',df.columns[1].unique())

processorbrand = st.selectbox('Processor',df['Processor Brand'].unique())
# processorbrand = st.selectbox('Processor',df.columns[2].unique())

operatingsystem = st.selectbox('Operating System',df['Operating System'].unique())
# operatingsystem = st.selectbox('Operating System',[1, 2, 4, 3])
#operatingsystem = st.selectbox('Operating System',df.columns[3].unique())


displayinch = st.selectbox('Display(in INCH)',[11.6,13.0,13.3,13.4,13.5,13.6,14.0,14.1,14.2,14.96,15,15.6,16.0,16.1,16.2,16.6,17.3,35.0])
# displayinch = int(st.number_input('Display Size of the Laptop'))

# Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

ramtype = st.selectbox('RAM Type',df['RAM Type'].unique())
# ramtype = st.selectbox('RAM Type',[1, 2, 3, 4, 5, 6, 7])
# ramtype = st.selectbox('RAM Type',df.columns[6].unique())

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

emmc = st.selectbox('EMMC(in GB)',[0,8,128,256,512,1024])

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

if st.button('Predict Price'):
    # query
    # ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    query = np.array([brand,cpubrand,processorbrand,operatingsystem,displayinch,ram,ramtype,ssd,hdd,emmc,touchscreen])
    # output = prediction(brand,cpubrand,processorbrand,operatingsystem,displayinch,ram,ramtype,ssd,hdd,emmc,touchscreen)
    query = query.reshape(1,11)
    # output = output.reshape(1,11)
    st.header("The predicted price of this configuration is: " + str(int(np.exp(pipe.predict(query)[0]))))
    st.header(':sunglasses:')


# if __name__=='__main__':
#     main()