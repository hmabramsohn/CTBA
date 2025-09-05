# Author: Harrison Abramsohn
# Attempt to pull the top 10 U.S. states by population from relevant Wikipedia article.

# First, import necessary libraries.
import pandas as pd
import requests

# Q = Encoding in Wikidata
# Write a query to pull human population (P1082, Q33829) from US states (Q35657)
query = """
SELECT ?state ?stateLabel ?population 
WHERE {
    ?state wdt:P31 wd:Q35657 .
    ?state wdt:P1082 ?population .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

# Direct request to wikidata in SPARQL
endpoint = "https://query.wikidata.org/sparql"
# Add additional information for request
headers = {"User-Agent": "Experiment (hmabramsohn@wm.edu)"}

resp = requests.get(url = endpoint, params = {"query": query, "format": "json"}, headers = headers)
resp.raise_for_status()
data = resp.json()['results']['bindings']

states = []

for state in data:
    states.append(
        {"State": state['stateLabel']['value'],
          "Population": int(state['population']['value'])}
    )

states_df = pd.DataFrame(states)
states_df = states_df.sort_values('Population', ascending=False)
states_df = states_df[:10]
print(states_df)