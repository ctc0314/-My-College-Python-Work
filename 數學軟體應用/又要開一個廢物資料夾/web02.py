import streamlit as st
import pandas as pd

st.ittle("我沒有用的網頁")

df = pd.DataFrame({
    "A":[33,99,88],
    "B":[94,87,1000]
})

st.write(df)