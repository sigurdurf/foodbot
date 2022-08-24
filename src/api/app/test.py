
from bs4 import BeautifulSoup
import requests
import json
import datetime


r = requests.get("https://prod-10.westeurope.logic.azure.com/workflows/661a8f1211d34ed98db39ea8c6caa52f/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=BpkZO2O35IlCXBbLQ7xzM75G0GWbx7D-enVq6I8b7F8")
n = json.loads(r.text)

weekday = datetime.datetime.now()

for i in n:
    if i["Date"] == weekday.strftime("%Y-%m-%d"):
        m = i

weekday = weekday.strftime("%A")

menu = [ {"day": weekday, "main": m["Title"], "vegan": m["VeganMenu"], "salat": "", "soup": m["SoupOfTheDay"]}]
print(menu)
