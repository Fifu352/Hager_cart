import urllib3
from bs4 import BeautifulSoup

class product():
        def __init__(self,url):

            self.url=url
            self.http = urllib3.PoolManager()
            self.content= self.http.request('GET',url)
            self.soup = BeautifulSoup(self.content.data)
            self.name = self.soup.find(class_='blockwithgridheadline').text
            self.features = self.soup.find(class_="product__details__featuregroups")
            self.headlines = self.features.findAll(class_="panel__headline open")
            self.contents = self.features.findAll( 'tr')

            self.headline = []
            self.content=[]



            for wrapper in self.headlines:
                self.headline.append(wrapper.text)


            for wrapper in self.contents:
                self.content.append(wrapper.text)





if __name__== "__main__":
    switch = product("http://www.hager.pl/katalog-produktow/rozdzial-energii/aparatura-modulowa/mcb-wylaczniki-nadpradowe/mcb-wylaczniki-nadpradowe-icn-6000a-0-5-63a/mbn116e/40249.htm?Suchbegriffe=mbn116e")


    print("Produkt: " +  switch.name + "\n \nParamatry:")


    for i in range(len(switch.content)-1):


        print(switch.content[i + 1])
