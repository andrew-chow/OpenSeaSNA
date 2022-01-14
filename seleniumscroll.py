import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://opensea.io/collection/loomlock?tab=activity")

counter_to_start = 0
file = open('openseanfts7.csv', 'w',newline='')
writer = csv.writer(file)
writer.writerow(['Transaction', 'Asset Url', 'Asset Name', 'Price', 'From Name', 'From Url', 'To Name', 'To Url'])

time.sleep(6)  # Allow 2 seconds for the web page to open
scroll_pause_time = 3 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1
# soup = BeautifulSoup(driver.page_source, "html.parser")
#initiallize arrays
transaction_type = []
asset_url_arr = []
asset_name_arr = []
#etherium_urls_arr =[]
price_arr = []
#quantity_arr =[]
from_arr = []
from_url_arr =[]
to_arr = []
to_url_arr = []
times_arr =[]



while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break
    if counter_to_start > 0:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        ### Scraping data with beautifulsoup###
        list = soup.find_all('div', {'role': 'listitem'})
        for asset in list:
            #transaction_type
            sale_type = asset.find('h6', {'class': 'Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ehCsVi ibqWjk'})
            sale_type = sale_type.text.strip()
            #transaction_type.append(sale_type)
            #asset_url_arr
            asset_url = asset.find('a', {'class' : 'styles__StyledLink-sc-l6elh8-0 ekTmzq styles__CoverLink-sc-nz4knd-1 givILt'})
            base = "https://opensea.io/"
            link = asset_url.attrs['href']
            url_asset = urljoin(base, link)
            #asset_url_arr.append(url_asset)
            #asset_name_arr
            asset_name = asset.find('div', {'class': 'Overflowreact__OverflowContainer-sc-10mm0lu-0 kohuDY'})
            asset_name = asset_name.text.strip()
            #asset_name_arr.append(asset_name)
            #price_arr
            price = asset.find('div', {'class':'Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--fiat-amount'})
            price = price.text.strip()
            #price_arr.append(price)
            #etherium_urls_arr
            #i will code later might be important to track things on the blockchain

            #quantity_arr
            #quantity = asset.find('div', {'class': 'Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf'})
            #quantity = quantity.text.strip()
            #quantity_arr.append(quantity)
            #from_arr & from_url_arr
            from_data = asset.find_all('a', {'class': 'styles__StyledLink-sc-l6elh8-0 ikuMIO AccountLink--ellipsis-overflow'})
            from_data = from_data[0]
            from_name = from_data.find('span')
            from_name = from_name.text.strip()
            #from_arr.append(from_name)
            base = "https://opensea.io/"
            link_from = from_data.attrs['href']
            url_from = urljoin(base, link_from)
            #from_url_arr.append(url_from)

            #to_arr & to_url_arr
            to_data = asset.find_all('a', {'class': 'styles__StyledLink-sc-l6elh8-0 ikuMIO AccountLink--ellipsis-overflow'})
            to_data= to_data[1]
            to_name = to_data.find('span')
            to_name = to_name.text.strip()
            #to_arr.append(to_name)
            base ="https://opensea.io/"
            link_to = to_data.attrs['href']
            url_to = urljoin(base, link_to)
            #to_url_arr.append(url_to)

            #hover over timestamp
            #element_to_hover_over = driver.find_element_by_class_name('styles__StyledLink-sc-l6elh8-0 ekTmzq EventTimestamp--link')
            #hover = ActionChains(driver).move_to_element(element_to_hover_over)
            #hover.perform()

            #times_arr
            #time_data = asset.find('div', {'class':'tippy-content'})
            #time_data= time_data.text.strip()
            #print(time_data)




            writer.writerow([sale_type, url_asset, asset_name, price, from_name, url_from, to_name, url_to])

            #print(transaction_type)
            print(counter_to_start)
    if counter_to_start > 500:
        break
    else:
        counter_to_start += 1
#print('pooooop')
file.close()








        #testing
        #print(transaction_type)
        #print(asset_url_arr)





        #sale_types_arr = soup.find_all('h6', {'class': 'Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ehCsVi ibqWjk'})
        #for type in sale_types_arr:
            #type= type.text.strip()
