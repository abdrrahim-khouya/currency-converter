import requests
import re
from bs4 import BeautifulSoup
def curr_convert(txt):
    patcur=r"\b[A-Za-z]{3}\b"
    patnb=r"[^0-9\.]"
    fro=re.findall(patcur,txt)[0]
    to=re.findall(patcur,txt)[1]
    n=float(re.sub(patnb,"",txt))
    url=f"https://www.xe.com/currencyconverter/convert/?Amount=31&From={fro}&To={to}"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    res=soup.find_all("div",{"class":"unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx"})[0]
    resolto=str(res).replace('<div class="unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx"><p>',"").replace("</p></div>","").split("</p><p>")[0].replace(",","")
    print(str(resolto))
