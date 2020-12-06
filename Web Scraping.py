import requests
from bs4 import BeautifulSoup


# besically we get all the data in html

# we use requests library to collect the data form html 
# and for parse html data we use BeautifulSoup

# we have generally use two types of request
# like
    # get=in this we requesing for a special data from a specific server or page 
    # post= and in this we post our data in any specific server or any page


flipkart=requests.get("https://www.flipkart.com")
# print(flipkart)


# when we print flipkart we get 200 that means succcess.
# but if we get status code is 400 its a error likw 401 and 403 etc  so 401--- unauthonticate and 403--- for permission denied 
# and 404 for page not found and 500 series error for server side error 500----- internal server error by fult of website
# we scrap he data only when we use 200 as status Code 


# print(flipkart.status_code)

# we creat a object in whic we paerse all the html data 
# so we creat a soup object. here soup is a object we use any one of them 
soup=BeautifulSoup(flipkart.content,"html.parser") #here we use 2 parser like html.parser another one is lxml.parser so here we use html.parser
# if we prit soup then se get the content from the requset which we get


flipkart_mobile=requests.get("https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# now by abob=ve request we get about mobile details from flipkart

# print(flipkart_mobile.status_code)
soup=BeautifulSoup(flipkart_mobile.content,"html.parser")

# now we collect data from above html parser by using beautifulsoup
# here we have some method of BeautifulSoup to fetch the data from the web pages
#                         like find("tag name"):- its fetch the 1st one from the html page
                        # find('div',attrs={'id':132,'class':'abc'},text='abc')
#                         and find_all("tag name"):- its fetch the all at one time from html page
# this both are use for top-buttom

# find_parent('tag_name'):-its fetch the 1st one from the html page
# find_parents('tag_name'):- its fetch the all at one time from html page
# this above are work from buttom-top

# # sideways
# find_sibling('tag_name')
# find_sibling('tag_name')
# mobile_name=soup.find("div",attrs={'class':"_3wU53n"})
# # print(mobile_name)
# # if we want only text of this div or class then we use only .text
# # print(mobile_name.text)
# # if we now need all the name of mobile of proper div 
# mobile_names=soup.find_all("div",attrs={'class':"_3wU53n"})
# print(mobile_names) this is give a list of mobile name with there div and class name
# so now
# for name in mobile_names:
#     print(name.text)
    # by doing this we get the name of mobiile by line by line

# price=soup.find("div",attrs={'class':"_1vC4OE _2rQ-NK"})
# # print(price.text)


# all_price=soup.find_all("div",attrs={'class':"_1vC4OE _2rQ-NK"})

# when we need all the details of similar thing then we use looops?
# so

# for price in all_price:
#     print(price.text)


# card=soup.find("div",attrs={'class':"_1UoZlX"})

# name=card.find("div",attrs={'class':"_3wU53n"})
# price=card.find("div",attrs={'class':"_1vC4OE _2rQ-NK"})
# rating=card.find("div",attrs={'class':"hGSR34"})
# print(name.text,price.text,rating.text)
# this above are for only one card that gives only gives one mobile details


# cards=soup.find_all("div",attrs={'class':"_1UoZlX"})

# for card in cards:
#     name=card.find("div",attrs={'class':"_3wU53n"})
#     price=card.find("div",attrs={'class':"_1vC4OE _2rQ-NK"})
#     rating=card.find("div",attrs={'class':"hGSR34"})
#     print(f'{name.text},{price.text},{rating.text}')

# next_link=soup.find('a',text='Next')
# print(next_link.text)

                                                        # for geting something from this next_link

# next_link=soup.find('a',text='Next').get("href")
# home_page_link="https://www.flipkart.com"
# next_page_link=home_page_link+next_link
# page_two=requests.get(next_page_link)
# print(page_two.status_code)

# soup=BeautifulSoup(page_two.content,"html.parser")
# cards=soup.find_all("div",attrs={'class':"_1UoZlX"})

# for card in cards:
#     name=card.find("div",attrs={'class':"_3wU53n"})
#     price=card.find("div",attrs={'class':"_1vC4OE _2rQ-NK"})
#     rating=card.find("div",attrs={'class':"hGSR34"})
#     print(f'{name.text},{price.text},{rating.text}')


# next_link=soup.find('a',text="4").get("href")
# home_page_link="https://www.flipkart.com"
# next_page_link=home_page_link+next_link
# page_two=requests.get(next_page_link)
# print(page_two.status_code)

# soup=BeautifulSoup(page_two.content,"html.parser")
# cards=soup.find_all("div",attrs={'class':"_1UoZlX"})

# for card in cards:
#     name=card.find("div",attrs={'class':"_3wU53n"})
#     price=card.find("div",attrs={'class':"_1vC4OE _2rQ-NK"})
#     rating=card.find("div",attrs={'class':"hGSR34"})
#     if name:
#         name_text=name.text
#     else:
#         name_text=None
#     if price:
#         price_text=price.text
#     else:
#         price_text=None
#     if rating:
#         rating_text=rating.text
#     else:
#         rating_text=None
#     print(f'{name.text},{price.text},{rating.text}')


import requests
from bs4 import BeautifulSoup
# for j in range(1,):
#     i=''
#     i+=str(j)

# next_link=soup.find('a',text='5').get("href")

# home_page_link="https://www.flipkart.com"
# next_page_link=home_page_link+next_link
# page_two=requests.get(next_page_link)
# print(page_two.status_code)

# soup=BeautifulSoup(page_two.content,"html.parser")
# cards=soup.find_all("div",attrs={'class':"_1UoZlX"})

# for card in cards:
#     name=card.find("div",attrs={'class':"_3wU53n"})
#     price=card.find("div",attrs={'class':"_1vC4OE _2rQ-NK"})
#     rating=card.find("div",attrs={'class':"hGSR34"})
#     if name:
#         name_text=name.text
#     else:
#         name_text=None
#     if price:
#         price_text=price.text
#     else:
#         price_text=None
#     if rating:
#         rating_text=rating.text
#     else:
#         rating_text=None
#     print(f'{name.text},{price.text},{rating.text}')




