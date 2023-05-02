"""
Tai Meade
Create a program that showcases best cards to flip on MLB 23 using their API
"""

import requests
from tabulate import tabulate

profitWant = int(input("Enter minimum profit from flip: "))
series = int(input("Please enter the series you'd like to check:\n (1) Live Series\n (2) Rookie\n (3) Breakout\n (4) Veteran\n (5) All-Star\n (6) Awards\n (7) Postseason\n (8) Future Stars\n (9) Signature\n (10) Topps Now\n (11) Finest\n (12) 2nd Half Heroes\n (13) Milestone\n (14) Captain\n (15) Charisma\n (16) World Baseball Classic\n"))

if series == 1:
    series = 1337
elif series == 2:
    series = 10001
elif series == 3:
    series = 10002
elif series == 4:
    series = 10003
elif series == 5:
    series = 10004
elif series == 6:
    series = 10005
elif series == 7:
    series = 10006
elif series == 8:
    series = 10008
elif series == 9:
    series = 10009
elif series == 10:
    series = 10017
elif series == 11:
    series = 10018
elif series == 12:
    series = 10020
elif series == 13:
    series = 10022
elif series == 14:
    series = 10026
elif series == 15:
    series = 10027
elif series == 16:
    series = 10028
else:
    print("INVALID...CHECKING FOR LIVE SERIES.")
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

print(tabulate(table.items(), headers=("Name:", "Profit:")))