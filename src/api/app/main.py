from fastapi import FastAPI,HTTPException
from typing import Optional
from fastapi.testclient import TestClient
from app.utils import malid_scrape as ms
app = FastAPI()

@app.get("/lunch/{name}")
def read_menu(name: str, q: Optional[str] = None):
  b = ("monday", "tuesday", "wednesday", "thursday", "friday")
  if name == "malid":
    menu = ms.get_weekly_menu()
  else:
    raise HTTPException(status_code=404, detail="Unsupported restaurant")
  if q is not None and q in b:
    return menu[name][b.index(q)]
  return {"menu": menu[name]}



