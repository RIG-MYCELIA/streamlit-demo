import altair as alt
import pandas as pd
import streamlit as st

from algorithm.free_beer import run_algorithm

NAME = "Naam"
NAME_LENGTH = "Lengte naam"
AGE = "Leeftijd"
LIKES_BEER = "Vindt bier lekker"
QUALIFIES = "Komt in aanmerking"
QUALIFIES_PERCENTAGE = "Percentage dat in aanmerking komt"
SELECT = "-- Selecteer --"


def run_algorithm_on_row(row):
    return 1.0 if run_algorithm(row[NAME], row[AGE], row[LIKES_BEER]) else 0.0


def name_length(row):
    return len(row[NAME])


def calculate_percentage_per_group(df, group_by):
    series_grouped_mean = df[[group_by, QUALIFIES]].copy().groupby([group_by])[QUALIFIES].mean()
    df_grouped = pd.DataFrame(series_grouped_mean)
    df_grouped[group_by] = df_grouped.index
    df_grouped[QUALIFIES_PERCENTAGE] = 100 * df_grouped[QUALIFIES]
    return df_grouped


st.write("**Welkom onderzoeker!**")
st.write("Upload een csv met kolommen 'Naam', 'Leeftijd' en 'Vindt bier lekker (Ja/Nee)'")

uploaded_file = st.file_uploader("Selecteer bestand", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=";")
    df[LIKES_BEER] = df[LIKES_BEER] == "Ja"
    df[QUALIFIES] = df.apply(run_algorithm_on_row, axis=1)

    st.write(df)

    research_subject = st.selectbox("Onderzoek", options=[SELECT, LIKES_BEER, AGE, NAME])

    if research_subject == LIKES_BEER:
        df_likes = calculate_percentage_per_group(df, LIKES_BEER)
        c = (alt.Chart(df_likes).mark_bar().encode(x=LIKES_BEER, y=QUALIFIES_PERCENTAGE))
        st.altair_chart(c, use_container_width=True)

    elif research_subject == AGE:
        df_age = calculate_percentage_per_group(df, AGE)
        c = (alt.Chart(df_age).mark_circle().encode(x=AGE, y=QUALIFIES_PERCENTAGE))
        st.altair_chart(c, use_container_width=True)

    elif research_subject == NAME:
        df[NAME_LENGTH] = df.apply(name_length, axis=1)
        df_name_length = calculate_percentage_per_group(df, NAME_LENGTH)
        c = (alt.Chart(df_name_length).mark_line().encode(x=NAME_LENGTH, y=QUALIFIES_PERCENTAGE))
        st.altair_chart(c, use_container_width=True)
