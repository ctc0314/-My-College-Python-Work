import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title("matplotlib畫圖")
st.markdown(r"畫一個 $\draft{sin(x)}{x}$")

x = np.linspace(-10,10,200)
y = np.sinc(x)
plt.plot(x,y)
st.pyplot()