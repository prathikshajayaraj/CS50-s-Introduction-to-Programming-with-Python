import sys
import requests
import json
def main():
  value = check_float()
  amount(value)

def amount(value):
  try:
    if value is not None:
      response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
      data= response.json()
      bitcoin_value = data["bpi"]['USD']['rate_float']
      amount= bitcoin_value*value
      print(f"${amount:,.4f}")

  except requests.RequestException as e:
      print(f"An error occurred: {e}")



def check_float():
  try:
    if len(sys.argv)!=2:
     sys.exit("Missing command-line argument")
    else:
      value =sys.argv[1]
      return float(value)
  except ValueError:
    sys.exit("Command-line argument is not a number")



if __name__ == "__main__":
    main()
