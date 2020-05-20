"""
This script performs the equivalent of going to https://covid19.ncdhhs.gov/dashboard#zip-code-map
zooming in, and then clicking on your zip code to retrieve the number of cases
"""
import requests
import time
import sys
import argparse
import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

parser = argparse.ArgumentParser()
parser.add_argument('-z', '--zip', type=int, help='NC ZIP CODE', required=False)

args = parser.parse_args()

if not args.zip:
      zip_code = input("Enter your zip code: ")
else:
      zip_code = args.zip

# The below url was determined by first going here:
# https://www.arcgis.com/sharing/rest/content/items/39d1cab54b33496db848905e728e2204/data
# The 39d1... is the ID, which was found by searching Dev Tools for "webmap"

url = f"https://services.arcgis.com/iFBq2AW9XO0jYYF7/" \
      f"arcgis/rest/services/Covid19byZIPnew/FeatureServer" \
      f"/0/query?where=ZIPCode={zip_code}&outFields=*&f=json"

headers = {'Accept':'application/json'}

try:
      resp = requests.get(url, headers=headers)
except Exception as e:
      print(f"Error making connection: {e}")
      print("Exiting!")
      sys.exit(1)

today = time.strftime("%Y-%m-%d %H:%M:%S %Z",time.localtime())

if resp.status_code == 200 and resp.json()['features']:
      cases = resp.json()['features'][0]['attributes']['Cases']
      pop = resp.json()['features'][0]['attributes']['TotalPop']
      place = resp.json()['features'][0]['attributes']['Place']
      case_avg = round_up(cases/pop, 4) * 100
      print("\n*-------------------------------------------------------------------*")
      print(f"Number of cases on {today} in zip code {zip_code} is: {cases}")
      print(f"This is about {case_avg}% of the {pop} residents in {place}")
      print("*-------------------------------------------------------------------*\n")
else:
      print(f"Query failed for zip code {zip_code}")
      print("Did you enter a valid NC zip code?  Please try again.")

