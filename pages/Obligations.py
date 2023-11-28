import streamlit as st
import pandas as pd
import datetime as dt
import plotly.graph_objects as go
import plotly_express as px
import numpy as np
from Financial_Dashboard import show_indexes

st.title("Obligations")
st.sidebar.markdown("Obligations")

st.markdown('## OAT')
urls_oat = ['https://www.boursorama.com/bourse/taux/cours/2xFRABM2A/', #2A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM3A/', #3A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM4A/', #4A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM5A/', #5A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM6A/', #6A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM7A/', #7A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM8A/', #8A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM10A/', #10A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM12A/', #12A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM15A/', #15A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM20A/', #20A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM30A/', #30A
            'https://www.boursorama.com/bourse/taux/cours/2xFRABM50A/' #50A
            ]



def main():

    show_indexes(urls_oat)

if __name__ == "__main__":
    main()