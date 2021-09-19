from bs4 import BeautifulSoup
import requests

def get_weekly_menu():
  r = requests.get("http://malid.ru.is")
  soup = BeautifulSoup(r.text, 'html.parser')
  menu = {"monday":{"main": "", "vegan": "", "salat": "", "soup": ""},"tuesday":{"main": "", "vegan": "", "salat": "", "soup": ""},"wednesday":{"main": "", "vegan": "", "salat": "", "soup": ""}, "thursday":{"main": "", "vegan": "", "salat": "", "soup": ""}, "friday":{"main": "", "vegan": "", "salat": "", "soup": ""}}
  menu_titles = soup.find_all("div", class_='restaurant-menu-item')
  menu_title_items = []
  temp = []
  for item in menu_titles:
    for text in item.find_all("span"):
      if len(text.contents) != 0:
        if len(text.contents[0]) > 2:
          temp.append(text.contents[0])
      if len(temp) == 4:
        menu_title_items.append(temp)
        temp = []
  for day, item in zip(menu.keys(), menu_title_items):
    for key, dish in zip(menu[day].keys(), item):
      menu[day][key] = dish
  return menu

def main():
  get_weekly_menu()

if __name__ == "__main__":
  main()