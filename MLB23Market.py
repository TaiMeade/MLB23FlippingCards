"""
Tai Meade
Create a program that showcases best cards to flip on MLB 23 using their API
"""

import requests
from tabulate import tabulate
import streamlit as st

# profitWant = int(input("Enter minimum profit from flip: "))
# series = int(input("Please enter the series you'd like to check:\n (1) Live Series\n (2) Rookie\n (3) Breakout\n (4) Veteran\n (5) All-Star\n (6) Awards\n (7) Postseason\n (8) Future Stars\n (9) Signature\n (10) Topps Now\n (11) Finest\n (12) 2nd Half Heroes\n (13) Milestone\n (14) Captain\n (15) Charisma\n (16) World Baseball Classic\n"))

seriesOptions = ['Live Series', 'Rookie', 'Breakout', 'Veteran','All-Star','Awards','Postseason','Future Stars','Signature','Topps Now','Finest','2nd Half Heroes','Milestone','Captain','Charisma','World Baseball Classic','Sanford Greene','Home Run Derby','All-Star Game','Mexico City']

# Streamlit sidebar elements
with st.sidebar:

    st.title("Options:")

    profitWant = st.number_input("Minimum Profit: ", 100, 1000000, 250, step=50)

    seriesOption = st.selectbox("Series:", seriesOptions)


if seriesOption == 'Live Series':
    series = 1337
elif seriesOption == 'Rookie':
    series = 10001
elif seriesOption == 'Breakout':
    series = 10002
elif seriesOption == 'Veteran':
    series = 10003
elif seriesOption == 'All-Star':
    series = 10004
elif seriesOption == 'Awards':
    series = 10005
elif seriesOption == 'Postseason':
    series = 10006
elif seriesOption == 'Future Stars':
    series = 10008
elif seriesOption == 'Signature':
    series = 10009
elif seriesOption == 'Topps Now':
    series = 10017
elif seriesOption == 'Finest':
    series = 10018
elif seriesOption == '2nd Half Heroes':
    series = 10020
elif seriesOption == 'Milestone':
    series = 10022
elif seriesOption == 'Captain':
    series = 10026
elif seriesOption == 'Charisma':
    series = 10027
elif seriesOption == 'World Baseball Classic':
    series = 10028
elif seriesOption == 'Sanford Greene':
    series = 10025
elif seriesOption == 'Home Run Derby':
    series = 10030
elif seriesOption == 'All-Star Game':
    series = 10029
elif seriesOption == 'Mexico City':
    series = 10033
else:
    with st.sidebar:
        st.write("INVALID...CHECKING FOR LIVE SERIES.")
    series = 1337
    

cardListings = requests.get(f"https://mlb23.theshow.com/apis/listings.json?type=mlb_card&series_id={series}")
cardListings = cardListings.json()

numPages = cardListings['total_pages']

listingNames = []
buyNowPrices = []
sellNowPrices = []

for pageNumber in range(13):
    cardListings = requests.get(f"https://mlb23.theshow.com/apis/listings.json?type=mlb_card&series_id={series}&page={pageNumber+1}")
    cardListings = cardListings.json()
    for listing in cardListings['listings']:
        if not ((listing['best_sell_price'] == 0) or (listing['best_buy_price'] == 0)):
            buyNowPrices.append(listing['best_sell_price'])
            sellNowPrices.append(listing['best_buy_price'])
            listingNames.append(listing['listing_name'])

table = {}

for i in range(len(listingNames)):
    profit = ((buyNowPrices[i] * 0.9) - sellNowPrices[i])
    if profit > profitWant:
        table[listingNames[i]] = profit

table = sorted(table.items(),key=lambda x:x[1], reverse=True)

col1, col2 = st.columns(2)

with col1:
   st.header("Name:")
   for item in table:
       st.write(item[0])

with col2:
   st.header("Profit:")
   for item in table:
       st.write(item[1])