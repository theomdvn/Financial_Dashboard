import streamlit as st
from Financial_Dashboard import show_indexes


st.title('Commodities')

urls_commo = ['https://www.boursorama.com/bourse/matieres-premieres/cours/_GC/', #GOLD
              'https://www.boursorama.com/bourse/matieres-premieres/cours/_SI/', #SILVER
              'https://www.boursorama.com/bourse/matieres-premieres/cours/7xCAUSD/', #COPPER
              'https://www.boursorama.com/bourse/matieres-premieres/cours/_HR/', #ACIER
              'https://www.boursorama.com/bourse/matieres-premieres/cours/8xBRN/', #BRENT
              'https://www.boursorama.com/bourse/matieres-premieres/cours/8xWBS/', #WTI
              'https://www.boursorama.com/bourse/matieres-premieres/cours/6xWWY/', #Blé
              'https://www.boursorama.com/bourse/matieres-premieres/cours/_CJ/'

]

show_indexes(urls_commo)