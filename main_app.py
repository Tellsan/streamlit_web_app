import streamlit as st
import PIL.Image as pi
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

import datetime


st.title('株価グラフ表示テスト')
st.caption('指定した期間の株価を取得し、折れ線グラフを表示します。')

with st.form(key='stock_form'):   
  stock_code = st.text_input('株コード')
  #print(stock_code)   
   
  start_date = st.date_input(
    '開始日',
    datetime.date(2023,1,1)
  )
   
  end_date = st.date_input(
    '終了日',
    datetime.date(2024,1,1)
  )
   
  submit_btn = st.form_submit_button('検索')
  #cancel_btn = st.form_submit_button('キャンセル')
       
   
  if submit_btn:
    #yfinanceのライブラリで指定した条件でデータを取得
    yf.pdr_override() 
    df_save = pdr.get_data_yahoo(stock_code + '.T', start_date, end_date)
     
    folder_path = '.\\data\\'
    file_path = folder_path + stock_code + '.csv'
     
    #csvで保存
    #ファイル名は上記tickerで指定した文字列_daily_data.csvとして保存されます
    df_save.to_csv(file_path, encoding='utf8')
     
    # データ分析関連
    df = pd.read_csv(file_path, index_col='Date')
    #df['Date'] = pd.to_datetime(df['Date'])

    #st.dataframe(df)
    st.line_chart(df['Close'])
     

  #print(f'submit_btn: {submit_btn}')
  #print(f'cancel_btn: {cancel_btn}')

#st.subheader('自己紹介')
#st.text('ここに自己紹介を記載。\n改行挟む')

#code = '''
#import streamlit as st

#st.title('タイトル')
#st.caption('キャプション')
#
#'''

#st.code(code, language='python')


# 画像
#image = pi.open('graph.png')
#st.image(image, width=500)

# 動画
#video_file = open('XXXX.mov', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)

#  age_category = st.selectbox(
#    '年齢層',
#    ('10代','20代')
#  )

