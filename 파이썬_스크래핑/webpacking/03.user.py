## 유저 에이전트(USER - AGENT)

import requests
url="https://www.kpop-radar.com/RedVelvet"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

# res = requests.get("https://www.kpop-radar.com/RedVelvet")
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("redvelvet_two.html", "w", encoding="utf8") as f:
    f.write(res.text)

