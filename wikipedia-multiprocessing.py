import requests
import bs4
import multiprocessing


def getLinks(scrapeLink, text_file):
    link_list = []
    soup = bs4.BeautifulSoup(requests.get(scrapeLink).text, 'html.parser')
    for link in soup.find_all('a', href=True):
        if link['href'][0:6] == "/wiki/" and (link['href'].find('#') == -1 and (link['href'][-4:] != ".jpg")):
            link_list.append("https://en.wikipedia.org" + link['href'])
            soup2 = bs4.BeautifulSoup(requests.get("https://en.wikipedia.org" + link['href']).text, 'html.parser')
            for link2 in soup2.find_all('a', href=True):
                if link2['href'][0:6] == "/wiki/" and (
                        link2['href'].find('#') == -1 and (link2['href'][-4:] != ".jpg")):
                    link_list.append("https://en.wikipedia.org" + link2['href'])
                    link_list = list(set(link_list))
                    if len(link_list) >= 20000:
                        break
            link_list = list(set(link_list))
            if len(link_list) >= 20000:
                break
    for i in link_list:
        text_file.write(i + "\n")
    text_file.close()


if __name__ == '__main__':
    f = open("links.txt", "w+")
    process1 = multiprocessing.Process(target=getLinks, args=("https://en.wikipedia.org/wiki/Mia_Khalifa", f))
    process2 = multiprocessing.Process(target=getLinks, args=("https://en.wikipedia.org/wiki/Brandy", f))
    process3 = multiprocessing.Process(target=getLinks, args=("https://en.wikipedia.org/wiki/Jordan", f))
    process4 = multiprocessing.Process(target=getLinks, args=("https://en.wikipedia.org/wiki/Leonardo_da_Vinci", f))
    process5 = multiprocessing.Process(target=getLinks, args=("https://en.wikipedia.org/wiki/Joker_(2019_film)", f))
    process6 = multiprocessing.Process(target=getLinks, args=("https://en.wikipedia.org/wiki/Frank_Zappa", f))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()

    f.close()
    g = open("links.txt", "r")
    line = g.read().split('\n')
    line = list(set(line))
    f = open("links.txt", "w+")
    for i in line:
        f.write(i + "\n")
    f.close()
    g.close()
    print("done")
