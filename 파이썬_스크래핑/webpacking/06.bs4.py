import requests
from bs4 import BeautifulSoup

# url = "https://www.kpop-radar.com/RedVelvet"
# url = "https://comic.naver.com/webtoon/weekday.nhn"
url = "https://comic.naver.com/webtoon/list.nhn?titleId=758150"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# print(title)

# link = cartoons[0].a["href"]
# print("https://comic.naver.com" + link)
# 만화 제목과 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 가져오기
totla_rates = 0
scores = soup.find_all("div", attrs={"class":"rating_type"})
for score in scores:
    rate = score.find("strong").get_text()
    print(rate)
    totla_rates += float(rate)
print("전체 점수 : ", totla_rates)
print("평균 점수 : ", totla_rates / len(scores) )