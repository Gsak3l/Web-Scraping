import requests
import bs4
import multiprocessing

manager = multiprocessing.Manager()
shared_list = manager.list()


def getLinks(scrapeLink, link_list):
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
                    if len(link_list) >= 200:
                        break
            link_list = list(set(link_list))
            if len(link_list) >= 200:
                break


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=getLinks, args=("https://en.wikipedia.org/wiki/Mia_Khalifa", shared_list))
    process2 = multiprocessing.Process(target=getLinks, args=("https://en.wikipedia.org/wiki/Brandy", shared_list))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print(shared_list)
