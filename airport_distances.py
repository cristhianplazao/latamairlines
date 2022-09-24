import requests
import pandas as pd

base_url = "https://aerodatabox.p.rapidapi.com/airports/icao/SCEL/distance-time/"

headers = {
    "X-RapidAPI-Key": "f7efb1d66emsh4ccdecff1b21ac2p1ca4d5jsn3cdaf219814c",
    "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

def importing_distances(df):
  try: 
    TIEMPO_ESTIMADO = []
    DISTANCIA = []

    for destino in df["Des-O"].unique().tolist():
      response = requests.request("GET", f"{base_url}{destino}", headers=headers)
      TIEMPO_ESTIMADO.append(response.json()["approxFlightTime"])
      DISTANCIA.append(response.json()["greatCircleDistance"]["km"])

    distances = {
      "DISTANCIA": DISTANCIA,
      "TIEMPO_ESTIMADO": TIEMPO_ESTIMADO,
      "DESTINO_ID": df["Des-O"].unique().tolist()
    }
  except:
    print("Error en el proceso")

  return distances


if __name__ == "__main__":
  df = pd.read_csv("data/dataset_SCL.csv")
  distances = importing_distances(df)
  df_distances = pd.DataFrame(distances)
  df_distances.to_csv("data/airports-distances.csv")

  

  

  

  