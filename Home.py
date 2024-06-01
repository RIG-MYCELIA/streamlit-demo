import streamlit as st

with st.sidebar:
    st.image("img/free_beer.jpg")

st.title("Algoritme n.a.v. motie 'Gratis Bier'")

st.markdown("_Een dummy-applicatie om de werking van Streamlit te demonstreren_")

st.page_link("pages/Gebruik.py", label="Komt u in aanmerking?")
st.page_link("pages/Onderzoek.py", label="Onderzoek het algoritme")
