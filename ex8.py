#We will be experimenting with usa.gov API's to familiarize ourselves with JSON values.
1. Find the number of people visiting a U.S. government website right now using this website.



import requests

r = requests.get("https://analytics.usa.gov/data/live/realtime.json")
#r = requests.get("https://analytics.usa.gov/data/live/browsers.json")

print(r.json()["data"])

#print(r.json()["totals"]["browser"])
