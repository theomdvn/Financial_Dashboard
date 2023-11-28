import streamlit as st

st.title('Swap')

def display_currency_categories():
    st.markdown("## Conventional rules for asset / base ")

    st.markdown("1. **EUR as Asset Currency:** Evaluate the EUR against all other currencies.")
    
    st.markdown("2. **Commonwealth Currencies:** GBP, AUD, NZD.")
    
    st.markdown("3. **King USD:** Consider USD as the dominant currency.")
    
    st.markdown("4. **Easy 'Swissee' CHF:** Examine CHF for ease of use and stability.")
    
    st.markdown("5. **Other Majors:** CAD, NOK, SEK, DKK.")
    
    st.markdown("6. **Emerging Markets:** BRL, RUB, INR, CNY/CNH, ...")
    
    st.markdown("7. **Respectful JPY:** Analyze JPY thoughtfully, recognizing its significance.")

def display_currency_info():
    X = 1.1061

    st.markdown("## Vocabulary")

    st.markdown(f"X = 1.1<font color='red'>**0**</font>6<font color='yellow'>**1**</font>",unsafe_allow_html=True)

    st.markdown(f"2nd decimal place is called a <font color='red'>**figure**</font>.", unsafe_allow_html=True)
    st.markdown(f"4th decimal place is called a <font color='yellow'>**pip**</font>.", unsafe_allow_html=True)
if __name__ == "__main__":
    display_currency_categories()
    display_currency_info()