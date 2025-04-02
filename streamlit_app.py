import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title='태담 행사 신청')
####
st.title("태담 행사 신청 사이트")
####
st.title("신청자 현황 대시보드")

import datetime as dt
current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"**현재 시간:** {current_time}")

if st.button("새로고침"):
    st.cache_data.clear()
    

url1 = st.secrets["googlesheet"]["url1"]
conn = st.connection("gsheets",type = GSheetsConnection)
df = conn.read(spreadsheet=url1)
#st.write(df)
st.write("현재 신청자 수는 총",len(df),"명 입니다.")

dates = df['신청 날짜'].str.split(',').explode()
st.write(dates.value_counts())
st.bar_chart(dates.value_counts())
####
st.info("태담 행사 신청 사이트입니다. 아래 양식에 맞게 기입하여 제출 버튼을 눌러주세요. 현재까지 신청 현황은 아래에서 확인 가능합니다")

iframe_url = 'https://forms.gle/RZcULmSMWXF9ci7K9'
st.components.v1.iframe(src=iframe_url, width=None, height=500, scrolling=True)

#(위험) https://docs.google.com/spreadsheets/d/1ZQfEnX-GLSl4b-OJTWpyynLBygMIfTgWoLFgrp8XIak/edit?usp=sharing


