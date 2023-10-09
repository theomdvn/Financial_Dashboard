import streamlit as st
import pandas as pd
import datetime as dt
import plotly.graph_objects as go
import plotly_express as px
import numpy as np
import Financial_Dashboard
st.markdown("## OAT France")
st.sidebar.markdown("# OAT France")

Financial_Dashboard.show_index('FRA BENCHMARK 2A','https://www.boursorama.com/bourse/taux/cours/2xFRABM2A/')
Financial_Dashboard.show_index('FRA BENCHMARK 3A','https://www.boursorama.com/bourse/taux/cours/2xFRABM3A/')
Financial_Dashboard.show_index('FRA BENCHMARK 4A','https://www.boursorama.com/bourse/taux/cours/2xFRABM4A/')
Financial_Dashboard.show_index('FRA BENCHMARK 5A','https://www.boursorama.com/bourse/taux/cours/2xFRABM5A/')
Financial_Dashboard.show_index('FRA BENCHMARK 6A','https://www.boursorama.com/bourse/taux/cours/2xFRABM6A/')
Financial_Dashboard.show_index('FRA BENCHMARK 7A','https://www.boursorama.com/bourse/taux/cours/2xFRABM7A/')
Financial_Dashboard.show_index('FRA BENCHMARK 8A','https://www.boursorama.com/bourse/taux/cours/2xFRABM8A/')
Financial_Dashboard.show_index('FRA BENCHMARK 10A','https://www.boursorama.com/bourse/taux/cours/2xFRABM10A/')
Financial_Dashboard.show_index('FRA BENCHMARK 12A','https://www.boursorama.com/bourse/taux/cours/2xFRABM12A/')
Financial_Dashboard.show_index('FRA BENCHMARK 15A','https://www.boursorama.com/bourse/taux/cours/2xFRABM15A/')
Financial_Dashboard.show_index('FRA BENCHMARK 20A','https://www.boursorama.com/bourse/taux/cours/2xFRABM20A/')
Financial_Dashboard.show_index('FRA BENCHMARK 30A','https://www.boursorama.com/bourse/taux/cours/2xFRABM30A/')
Financial_Dashboard.show_index('FRA BENCHMARK 50A','https://www.boursorama.com/bourse/taux/cours/2xFRABM50A/')

