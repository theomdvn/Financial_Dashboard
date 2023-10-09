import streamlit as st
import pandas as pd
import yfinance as yf  # You can use this library to fetch financial data
import requests
from bs4 import BeautifulSoup

# Create a sidebar for user input
st.sidebar.title("Financial Dashboard")

# Add widgets for user input (e.g., select indexes, date range)
# You can use st.selectbox, st.date_input, etc.

# Create a main area to display financial data
st.title("Financial Indexes Dashboard")

# Fetch and display financial data here

def get_index(url):
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the specific HTML element using the class name
    element = soup.find("span", class_="c-instrument c-instrument--last")

    # Extract the text within the element
    text = element.get_text(strip=True)
    return text
def get_variation(url):
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the specific HTML element using the class name
    element = soup.find("span", class_="c-instrument c-instrument--variation")

    # Extract the text within the element
    text = element.get_text(strip=True)
    return text

def show_index(name,url):
    # Example: Display a line chart
    st.subheader(name)
    st.write(get_index(url),get_variation(url))

#'https://www.boursorama.com/bourse/indices/cours/%24INDU/' DOW JONES
#'https://boursorama.com/bourse/indices/cours/%24INX/' S&P 500


show_index('S&P 500','https://boursorama.com/bourse/indices/cours/%24INX/')
show_index('DOW JONES','https://www.boursorama.com/bourse/indices/cours/%24INDU/')
