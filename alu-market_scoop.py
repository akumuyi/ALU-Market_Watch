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
