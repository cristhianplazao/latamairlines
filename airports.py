import requests
import pandas as pd

url = "https://flight-radar1.p.rapidapi.com/airports/list"

headers = {
	"X-RapidAPI-Key": "f7efb1d66emsh4ccdecff1b21ac2p1ca4d5jsn3cdaf219814c",
	"X-RapidAPI-Host": "flight-radar1.p.rapidapi.com"
}

if __name__ == "__main__":
  response = requests.request("GET", url, headers=headers)
  df_airports = pd.DataFrame(response.json()["rows"])
  df_airports.to_csv("data/airports.csv")