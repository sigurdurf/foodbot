import requests
import datetime
import json

URL = "https://prod-10.westeurope.logic.azure.com/workflows/661a8f1211d34ed98db39ea8c6caa52f/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=BpkZO2O35IlCXBbLQ7xzM75G0GWbx7D-enVq6I8b7F8"
MAIN = "🍴 "
VEGAN = "🥬 "
SOUP = "🥣 "


def get_todays_menu():
    r = requests.get(URL)
    meals = json.loads(r.text)

    weekday = datetime.datetime.now()

    for i in meals:
        if i["Date"] == weekday.strftime("%Y-%m-%d"):
            m = i

    weekday = weekday.strftime("%A")

    menu = [ {"day": weekday, "main": MAIN+m["Title"], "vegan": VEGAN+m["VeganMenu"], "salat": "", "soup": SOUP+m["SoupOfTheDay"]}]

    return {"malid": menu}


def get_weekly_menu():
    r = requests.get(URL)
    meals = json.loads(r.text)
    menu = []

    for meal in meals:
        weekday = datetime.datetime.strptime(meal["Date"], "%Y-%m-%d").strftime("%A")
        menu.append({"day": weekday, "main": MAIN+meal["Title"], "vegan": VEGAN+meal["VeganMenu"], "salat": "", "soup": SOUP+meal["SoupOfTheDay"]})

    return {"malid": menu}


def main():
    print(get_weekly_menu())


if __name__ == "__main__":
    main()
