import streamlit as st
import pandas as pd
import yfinance as yf  # You can use this library to fetch financial data
import requests
from bs4 import BeautifulSoup, SoupStrainer

st.sidebar.title("AFIBoard")

st.title("AFIBoard")


# def get_info(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")

#     name = soup.find('a', class_='c-faceplate__company-link')
#     name = name.get_text(strip=True)
#     value = soup.find("span", class_="c-instrument c-instrument--last")
#     value = value.get_text(strip=True)
#     denom = soup.find("span",class_="c-faceplate__price-currency")
#     denom = denom.get_text(strip=True)
#     variation = soup.find("span", class_="c-instrument c-instrument--variation")
#     variation = variation.get_text(strip=True)

#     return name,value,denom,variation

@st.cache_resource()

def get_info(url):
    with requests.Session() as session:
        response = session.get(url)
        only_tags = SoupStrainer(['a', 'span'])
        soup = BeautifulSoup(response.content, "html.parser", parse_only=only_tags)

    name = soup.find('a', class_='c-faceplate__company-link').get_text(strip=True)
    value = soup.find("span", class_="c-instrument c-instrument--last").get_text(strip=True)
    denom = soup.find("span", class_="c-faceplate__price-currency").get_text(strip=True)
    variation = soup.find("span", class_="c-instrument c-instrument--variation").get_text(strip=True)

    return name, value, denom, variation


def show_indexes(urls):
    data = {
        'Name': [],
        'Values': [],
        'Daily Variation': []

    }

    for url in urls:
        name = get_info(url)[0]
        index_value = get_info(url)[1]
        denom = get_info(url)[2]
        variation_str = get_info(url)[3]
        variation = float(variation_str.replace('%', ''))

        # Set the color based on the sign of the variation
        color = "green" if variation >= 0 else "red"

        data['Name'].append(name)
        data['Values'].append(index_value + ' ' + denom)
        data['Daily Variation'].append(variation_str)


        # Create a DataFrame
    df = pd.DataFrame(data)

    def color_change(val):
        variation = float(val.rstrip('%'))
        if variation > 0:
            color = 'green'
        elif variation < 0:
            color = 'red'
        else:
            color = 'grey'
        return f'color: {color}'
        # Apply the style to the 'Variation' column
    styled_df = df.style.map(color_change, subset=['Daily Variation'])
        # Display the DataFrame in Streamlit

    st.table(styled_df)





def main():
    st.markdown("## Indexes")
    urls = ['https://boursorama.com/bourse/indices/cours/%24INX/', #SNP500
            'https://www.boursorama.com/bourse/indices/cours/%24INDU/', #DOWJONES
            'https://www.boursorama.com/bourse/indices/cours/%24COMPX/', #NASDAQ
            'https://www.boursorama.com/bourse/indices/cours/2cSX5E/', #EUROSTOXX 50
            'https://www.boursorama.com/bourse/indices/cours/1rPCAC/', #CAC40
            'https://www.boursorama.com/bourse/indices/cours/5pDAX/', #DAX
            'https://www.boursorama.com/bourse/indices/cours/UKX.L/', #FTSE100

            ]
    show_indexes(urls)
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
    show_indexes(urls_oat)

    st.markdown("Commodities")
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



if __name__ == "__main__":
    main()