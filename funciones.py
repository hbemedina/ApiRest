import time
import json
from selenium import webdriver

def extract_countries():
    page = 0    
    country_id = 0
    countriesArr = []
    flag = True
    driver = webdriver.Chrome('./chromedriver.exe')   
    while flag:
        try:
            driver.get('http://example.webscraping.com/places/default/index/'+str(page))
            countries = driver.find_elements_by_id('results')[0].find_elements_by_tag_name('td')
            size = len(countries)
            if size > 0:
                for country in countries:
                        country_id += 1
                        country_name = country.text

                        countryObject = {
                            "Id": country_id,
                            "Name": country_name
                        }
                        countriesArr.append(countryObject)
                page +=1
                time.sleep(0.4)
            else:
                flag = False
        except:
            pass
    return countriesArr

def extract_countries_detail(id):
    try:
        driver = webdriver.Chrome('./chromedriver.exe')
        driver.get('http://example.webscraping.com/places/default/view/'+str(id))
        countryDetailArr = []
        neighboursArr = []
        flag = driver.find_element_by_tag_name("img")
        flag_src = flag.get_attribute("src")
        area = driver.find_element_by_xpath('//*[@id="places_area__row"]/td[2]').text
        population = driver.find_element_by_xpath('//*[@id="places_population__row"]/td[2]').text
        iso = driver.find_element_by_xpath('//*[@id="places_iso__row"]/td[3]').text
        country = driver.find_element_by_xpath('//*[@id="places_country__row"]/td[2]').text
        capital = driver.find_element_by_xpath('//*[@id="places_capital__row"]/td[2]').text
        continent = driver.find_element_by_xpath('//*[@id="places_continent__row"]/td[2]').text
        tld = driver.find_element_by_xpath('//*[@id="places_tld__row"]/td[2]').text
        currencyCode = driver.find_element_by_xpath('//*[@id="places_currency_code__row"]/td[2]').text
        currencyName = driver.find_element_by_xpath('//*[@id="places_currency_name__row"]/td[2]').text
        phone = driver.find_element_by_xpath('//*[@id="places_phone__row"]/td[2]').text
        postalCodeFormat = driver.find_element_by_xpath('//*[@id="places_postal_code_format__row"]/td[2]').text
        postalCodeRegex = driver.find_element_by_xpath('//*[@id="places_postal_code_regex__row"]/td[2]').text
        languages = driver.find_element_by_xpath('//*[@id="places_languages__row"]/td[2]').text
        neighbours = driver.find_elements_by_id('places_neighbours__row')[0].find_elements_by_tag_name('a')

        for neighbour in neighbours:
            neighbour_name = neighbour.text         
            neighboursArr.append(neighbour_name)

        countryObjectDetail = {
            "NationalFlag": flag_src, 
            "Area": area,
            "Population": population,
            "Iso": iso,
            "Country": country,
            "Capital": capital,
            "Continent": continent,
            "Tld": tld,
            "CurrencyCode": currencyCode,
            "CurrencyName": currencyName,
            "Phone": phone,
            "PostalCodeFormat": postalCodeFormat,
            "Languages": languages,
            "Neighbours": neighboursArr
        }
        countryDetailArr.append(countryObjectDetail)   
    except:
        pass
    return countryDetailArr