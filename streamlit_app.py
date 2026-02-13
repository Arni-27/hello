import streamlit as st 

st.title("_hitung_ is :blue[luas lingkaran] :rocket:")
r = st.number_input("masukan jari-jari (cm):",0)
if st.button("hitung luas lingkaran", type="primary"):
   v = math.pi*(r**2)
