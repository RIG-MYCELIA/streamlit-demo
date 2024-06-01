import streamlit as st

from algorithm.free_beer import run_algorithm

st.write("**Hallo welkom!**")

name = st.text_input("Naam:")
age = st.slider("Leeftijd:", 0, 100)
likes_beer = st.checkbox("Bier is lekker")

if name != "":
    if st.button("Kom ik in aanmerking voor gratis bier?"):
        result = run_algorithm(name, age, likes_beer)

        if result:
            st.write("Ja, gefeliciteerd!")
        else:
            st.write("Nee, helaas")
