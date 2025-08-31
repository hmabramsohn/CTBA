# Written by Professor Schlosser

import pandas as pd
import requests

# Query to pull top 10 populous country from Wikidata
query = """
SELECT ?countryLabel ?population WHERE {
  ?country wdt:P31 wd:Q6256 .              # instance of country
  ?country wdt:P1082 ?population .         # population
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?population)
LIMIT 10
"""
# Direct request to correct API site 
endpoint = "https://query.wikidata.org/sparql"
# Add additional information for request
headers = {"User-Agent": "MSBA-class-example/1.0 (hmabramsohn@wm.edu)"}

# Send GET Request to Wikidata
resp = requests.get(endpoint, params={"query": query, "format": "json"}, headers=headers)
# Demand error flag if problem occurs
resp.raise_for_status()
# Select data from json and save into data variable
data = resp.json()["results"]["bindings"]

# Save results into pandas DataFrame
df_api = pd.DataFrame(
    [{"Country": r["countryLabel"]["value"], 
      "Population": int(r["population"]["value"])} for r in data]
)

print(df_api)