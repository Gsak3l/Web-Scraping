# this takes a given page, and basically stores every Wikipedia link
# available in a Text file. Max number of links = 2100
import requests
import bs4

links = []
soup = bs4.BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Mia_Khalifa").text, 'html.parser')
for link in soup.find_all('a', href=True):
    if link['href'][0:6] == "/wiki/" and (link['href'].find('#') == -1 and (link['href'][-4:] != ".jpg")):
        links.append("https://en.wikipedia.org" + link['href'])
        soup2 = bs4.BeautifulSoup(requests.get("https://en.wikipedia.org" + link['href']).text, 'html.parser')
        for link2 in soup2.find_all('a', href=True):
            if link2['href'][0:6] == "/wiki/" and (link2['href'].find('#') == -1 and (link2['href'][-4:] != ".jpg")):
                links.append("https://en.wikipedia.org" + link2['href'])
                links = list(set(links))
                if len(links) >= 2100:
                    break
        links = list(set(links))
        if len(links) >= 200:
            break
f = open("links.txt", "w+")
for i in links:
    f.write(i + "\n")
f.close()
