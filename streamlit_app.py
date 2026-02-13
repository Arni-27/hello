import streamlit as st
import math

st.title("_hitung_ is :blue[luas lingkaran] :rocket:")

r = st.number_input("Masukan Jari-Jari (cm):",0)
t = st. numbet_input("Masukan Tinggi (cm) : ", 0) 

if st.button("hitung luas lingkaran", type="primary"):
   v = math.pi*(r**2)
st.succes(f'Volume tabung adalah {v:2f}')
