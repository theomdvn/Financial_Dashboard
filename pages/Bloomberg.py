import streamlit as st
import pandas as pd

st.title('Bloomberg cheat-sheet')

# Existing data
existing_data = {
    'Command Code': [
        'BU', 'SMNR', 'GRAB', 'HELP', 'DOCS', 'MSG', 'BIO/PEOPLE', 'TOP',
        'MAG', 'NSUB', 'JOBS', 'BRIEF', 'POSH', 'YAS', 'BXT', 'SXT', 'DES',
        'SPDL', 'CDS', 'IRS', 'RFR'
    ],
    'Description': [
        'Bloomberg University – Formations à distance',
        'Seminars (in-person or retransmitted)',
        'Faire une copie d’écran de sa page Bloomberg',
        'Links you to a Bloomberg representative',
        'Cheat Sheets',
        'DM Bloomberg users',
        'Find Bloomberg users',
        'News',
        'High level magazine, must read',
        'News Subscription directly to your inbox',
        'Craigslist equivalent',
        'Revues',
        'Leboncoin equivalent',
        'Yield and Spread Analysis',
        'Buy',
        'Sell',
        'Description du produit',
        'Speed Dial',
        'Single name look-up',
        'Interest Rate Swap',
        'Risk Free Rate'
    ]
}

# Additional data
additional_data = {
    'Command Code': ['ECO', 'WEI', 'HS', 'FA', 'SAID', 'CRVD', 'MISA', 'RELS', 'PEOP', 'FFM', 'YAS', 'READ/TRENDS', 'NIM', 'NI CHART', 'RATC/RATD', 'COMB', 'ECB/FED/BOE'],
    'Description': [
        'Nouvelles économiques.',
        'World Equity Indices analysis function.',
        'Historical spread avec analyse des corrélations.',
        'ESG Analyse ESG performance of a single company.',
        'Citations, proverbes.',
        'Base neg, Base po. Relative value of an issuer\'s bonds/CDS.',
        'Titres les plus échangés.',
        'Related securities.',
        'Find people, filter by school is possible.',
        'Functions for the Market: Examples showing how Bloomberg functions can be applied to current market events.',
        'Asset swap d’un bond.',
        'News les plus lues.',
        'Nouvelles émissions d’obligations (marché européen : NIM 4).',
        'Nouvelles avec un graphique commenté.',
        'Rating definition et rating change.',
        'Comparative bonds.',
        'Banques centrales'
    ]
}

# Combine data
data = {k: existing_data[k] + additional_data[k] for k in existing_data}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame in Streamlit
st.table(df)
