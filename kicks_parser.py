import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
for i in range(1,4,1):
    my_url = 'https://www.kicksonfire.com/app/upcoming?page=' + str(i)
    #reads html page and stores it into 
    stuff = uReq(my_url)
    html_page = stuff.read()
    stuff.close()
    # Parses the html file on the page
    page_soup = soup(html_page, "html.parser")
    #grabs each product
    containers = page_soup.findAll("div",{"class":"col-xs-12 col-sm-6 col-md-4 release-date-item-continer clear-padding"})
    for j in range(len(containers)):
        shoe_url = containers[j].div.div.a['href']
        shoe_title = containers[j].div.div.div.img['alt']
        shoe_img = containers[j].div.div.div.img['src']
        shoe_date = str(containers[j].find("div",{"class":"event-date first-event"}).div).strip("</div>")
        print('Shoe name:', shoe_title)
        print('URL:', shoe_url)
        print('Date:', shoe_date)
        print('Image URL:', shoe_img)
        print()