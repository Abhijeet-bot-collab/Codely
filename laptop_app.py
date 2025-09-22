import streamlit as st
import pickle
df=pickle.load(open('df.pkl','rb'))
pipe=pickle.load(open('pipe.pkl','rb'))
st.title("Laptop Price Predictor App")
st.text("This app is using only a select few laptops(around 1200 laptops), so it may not align exactly with real world data")

company=st.selectbox("Manufacturer of the Laptop",df['Company'].unique(),index=4)
typename=st.radio("Type of the Laptop",df['TypeName'].unique(),horizontal=True,index=1)
cpu=st.selectbox("Processor",df['Cpu'].unique())
ram=st.pills("RAM on the system(in GB)",[4,8,12,16,24,32,64,128])
gpu=st.radio("Graphics Card",df['Gpu'].unique(),index=1,horizontal=True)
os=st.selectbox("Operating System",df['OpSys'].unique(),index=2)
weight=st.slider("Weight of the laptop(in kg)",min_value=0.7,max_value=4.8,step=0.1,value=2.1)
touchscreen=st.pills("Does the laptop have touchscreen?",['Yes','No'])
ips=st.pills("Does the laptop have an IPS display?",['Yes','No'])
cpu_speed=st.slider("Clock Speed of CPU(in GHz)",min_value=0.9,max_value=3.6,step=0.1,value=2.3)
hdd=st.pills("Hard disk size on the system(in GB). If only SSD is present, select this is as 0",
             [0,512,1024,2000])
ssd=st.pills("SSD storage on the system(in GB).",[0,256,512,1024,2000])
screen_size=st.slider("Screen size(measured diagonally, in inches)",min_value=10.0,max_value=18.4,value=15.6,step=0.1)
screen_resolution=st.selectbox("Laptop Screen Resolution (in pixels)",
 ["2560x1600","1440x900","1920x1080","2880x1800","1366x768","2304x1440","3200x1800","1920x1200","2256x1504",
  "3840x2160","2160x1440","2560x1440","1600x900","2736x1824","2400x1600"],index=2)

if st.button("PREDICT PRICE"):
    if touchscreen == 'Yes':
        touchscreen=1
    else:
        touchscreen=0
    if ips == 'Yes':
        ips=1
    else:
        ips=0
    X_res=int(screen_resolution.split('x')[0])
    Y_res=int(screen_resolution.split('x')[1])
    ppi = ((X_res**2)+(Y_res**2))**0.5/screen_size
    query=[[company,typename,cpu,ram,gpu,os,weight,touchscreen,ips,cpu_speed,hdd,ssd,ppi]]
    op=pipe.predict(query)
    st.subheader("The estimated price of the laptop with the above mentioned specs is ₹"+str(int(round(op[0],-2)))+".")
