from bs4 import BeautifulSoup
import requests

def get_weekly_menu():
  r = requests.get("http://malid.ru.is")
  soup = BeautifulSoup(r.text, 'html.parser')
  menu = [
    {"day": "monday", "main": "", "vegan": "", "salat": "", "soup": ""},
    {"day": "tuesday", "main": "", "vegan": "", "salat": "", "soup": ""},
    {"day":"wednesday", "main": "", "vegan": "", "salat": "", "soup": ""}, 
    {"day":"thursday", "main": "", "vegan": "", "salat": "", "soup": ""},
    {"day": "friday", "main": "", "vegan": "", "salat": "", "soup": ""}
  ]
  menu_titles = soup.find_all("div", class_='restaurant-menu-item')
  menu_title_items = []
  temp = [" "]
  for item in menu_titles:
    for text in item.find_all("span"):
      if len(text.contents) != 0:
        if len(text.contents[0]) > 2:
          temp.append(text.contents[0])
      if len(temp) == 5:
        menu_title_items.append(temp)
        temp = [" "]
  for day, item in zip(menu, menu_title_items):
    for key, dish in zip(day.keys(), item):
      print(key, dish)
      if key != "day":
        day[key] = dish
  return {"malid": menu}

def main():
  print(get_weekly_menu())

if __name__ == "__main__":
  main()