# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:15:01 2021

@author: tobias
"""
import streamlit as st
import pandas as pd
from datetime import datetime, date
import plotly.graph_objs as go
from PIL import Image
import yfinance as yf
import base64

#put in a path with a picture you want to show in the background. Musst be jpg format.
main_bg = "your background-picture"
main_bg_ext = "jpg"



st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)




#header
st.markdown ("""
          Data overview for Stocks and Cryptos
          """)
          
#image = Image.open("C:/Users/tobia/iCloudDrive/Desktop/Python/Dashboard/Download.jpg")

#st.image(image, use_column_width = True)

# iniate sidebar for user input
st.sidebar.header("User Input")

# ipnut allowed: ticker and date range
tickers = st.sidebar.text_input ("Ticker" , "MSFT" )
start_date = st.sidebar.text_input ("Start Date" , "2020-01-01")  
end_date = st.sidebar.text_input ("End Date" , "2021-06-01")

@st.cache


def get_ticker_name(ticker):
    ticker= ticker.upper()
    return ticker


def load_data(tickers):
    df2 = yf.Ticker(tickers).financials
    return df2

#tickers, start_date, end_date = get_input()

ticker_name = get_ticker_name(tickers)



df = yf.download(tickers, start = start_date, end = end_date , progress = False)
df2 = load_data(tickers)


#df = get_data ( tickers , start , end)

#initiate candlestick chart, statistics and financials
fig = go.Figure(
    data = [go.Candlestick(
        x = df.index,
        open = df["Open"],
        high = df["High"],
        low = df["Low"],
        close = df["Close"],
        increasing_line_color = "green" ,
        decreasing_line_color = "red"
    )
  ]
)

st.header(ticker_name + " Data")
st.write(df)

st.header(ticker_name + " Data Statistics")
st.write(df.describe())

st.header(ticker_name + " Data Statistics")
st.line_chart(df["Close"])

st.header(ticker_name + " Data Statistics")
st.bar_chart(df["Volume"])

st.header(ticker_name + " Candle Stick")
st.plotly_chart(fig)

st.subheader(tickers + ' Financials')
st.write(df2)




        
   
        