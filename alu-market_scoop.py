#!/usr/bin/python3
import csv
import requests
import os
import time


class ALUMarketScoop:

  def __init__(self):
    self.base_url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/get-movers"
    self.headers = {
        "X-RapidAPI-Key": "da2be58476msh45c6b4882ab4411p1cc2cdjsnc02fb4696657",
        "X-RapidAPI-Host":
        "bloomberg-market-and-financial-news.p.rapidapi.com",
        "user-agent": "bloomberg_app/1.0"
    }

  def clear_terminal(self):
    os.system('clear')

  def regional_location(self):
    self.clear_terminal()
    print(
        "Welcome to the ALU Market Scoop!\n\n"
        "Your one-stop portal to real-time market information and financial insights.\n"
        "Market enthusiasts can explore movers and stay updated on trends worldwide."
    )
    time.sleep(8)
    self.clear_terminal()
    print("Select from available regions:\n",
          "Americas\n",
          "EMEA\n",
          "APAC",
          sep="")
    region = input("Enter region: ").lower()
    while region not in {"americas", "emea", "apac"}:
      region = input("Enter region: ").lower()
    time.sleep(1)
    self.clear_terminal()
    return region

  def index_name(self, region):
    if region == "americas":
      print("Here is a list of available indexes in the Americas\n",
            "Enter 1 for DOW JONES INDUS. AVG\n",
            "Enter 2 for S&P 500 INDEX\n", "Enter 3 for NASDAQ COMPOSITE\n",
            "Enter 4 for NYSE COMPOSITE INDEX\n",
            "Enter 5 for S&P/TSX COMPOSITE INDEX")
    elif region == "emea":
      print(
          "Here is a list of available indexes in Europe, Middle East & Africa\n",
          "Enter 1 for Euro Stoxx 50 Pr\n", "Enter 2 for FTSE 100 INDEX\n",
          "Enter 3 for DAX INDEX\n", "Enter 4 for CAC 40 INDEX\n",
          "Enter 5 for IBEX 35 INDEX")
    else:
      print("Here is a list of available indexes in Asia Pacific\n",
            "Enter 1 for NIKKEI 225\n", "Enter 2 for TOPIX INDEX (TOKYO)\n",
            "Enter 3 for HANG SENG INDEX\n", "Enter 4 for CSI 300 INDEX\n",
            "Enter 5 for S&P/ASX 200 INDEX\n",
            "Enter 6 for MSCI AC ASIA PACIFIC")

    index_name = input("Your pick: ").lower()
    while index_name not in {"1", "2", "3", "4", "5", "6"}:
      index_name = input("Enter an index_number: ").lower()
    # time.sleep(1)
    self.clear_terminal()
    return region, index_name

  def index_region_mapping(self, region, index_number):
    index_mapping = {
        "americas": {
            "1": "indu:ind",
            "2": "spx:ind",
            "3": "ccmp:ind",
            "4": "nya:ind",
            "5": "sptsx:ind"
        },
        "emea": {
            "1": "sx5e:ind",
            "2": "ukx:ind",
            "3": "dax:ind",
            "4": "cac:ind",
            "5": "ibex:ind"
        },
        "apac": {
            "1": "nky:ind",
            "2": "tpx:ind",
            "3": "hsi:ind",
            "4": "shsz300:ind",
            "5": "as51:ind",
            "6": "mxap:ind"
        }
    }
    return index_mapping[region][index_number]

