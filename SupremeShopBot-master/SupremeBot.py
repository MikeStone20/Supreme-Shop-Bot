from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class userInfo: # object for user information

    def __init__(self, name, creditCard, email, phone, address, zipCode, city, apt, state, country): # the typical user object

        self.name = name
        self.creditCard = creditCard
        self.email = email
        self.phone = phone
        self.address = address
        self.zipCode = zipCode
        self.city = city
        self.apt = apt
        self.state = state
        self.country = country

class Products: # object to keep track of all of the product properties

    def __init__(self, link, size, style, quantity):
        
        self.link = link
        self.size = size
        self.style = style
        self.quantity = quantity


users = {} # dictionary to hold all the profiles

items = [] # list to hold items

 # allows the manipulation of the browser

def getItemInfo(): #gets any sizes, quanitites, styles that the person may want
    
    link = str(input("Please input the link of the object"))
    style = str(input("Please select a style you want. Leave empty if you dont care"))
    size = str(input("Please select a size. Leave empty if NA or you dont care"))
    quantity = str(input("Please select the quantity desired, leave empty if NA"))
    
    items.append(Products(link,size,style,quantity))

def checkOut(): # goes through the process of checking out
    
    #driver.get("https://www.supremenewyork.com/mobile/?fbclid=IwAR2FkD1Reu9_CqBci2RxQFywWLjDO5ObzPdI8fi31dw64a9wYv4kNTk955w#products/172394") #head to the website
    #time.sleep(1)
    #elem = driver.find_element_by_xpath('//*[@id="cart-update"]/span') # find the element
    #temp = elem.get_attribute("class") #get the class name
    
    #if(temp == "cart-button sold-out"):
        #print("This item is sold out")
    driver = webdriver.Chrome("chromedriver") # open up the browser
    
    for item in items: # loop through all the items in the list
        
       driver.get(item.link) # go to the items link
       time.sleep(1)
       elem = driver.find_element_by_xpath('//*[@id="cart-update"]/span')# look at the add to cart button
       checkOutStatus = elem.get_attribute("class")
       
       if(checkOutStatus == "cart-button sold-out"): # if sold out then skip item
           print("This item is sold out.")
    
       else:
           
           #try: #check to see if a style can be selected
              # styleOption = driver.find_element_by_xpath('//*[@id="style-selector"]')
               #driver.find_element_by_xpath('//*[@id="style-%s"]'%(item.style)).click()
               #time.sleep(1)
           #except NoSuchElementException:
               #print("Specified Style not avilable")
           
           try: #check to see if an item can select a quantity
               quantityOption = driver.find_element_by_xpath('//*[@id="qty-options"]')
               driver.find_element_by_xpath('//*[@id="qty-options"]/option[%s]'%(item.quantity)).click()
               
           except NoSuchElementException:
               print("This quantity isnt avilabe")
        
           try:# check to see if an item can select a size
               sizeOption = driver.find_element_by_xpath('//*[@id="size-options"]')
               driver.find_element_by_xpath('//*[@id="size-options"]/option[%s]'%(item.size)).click()
           except NoSuchElementException:
               print("Size not avilable")
               
           driver.find_element_by_xpath('//*[@id="cart-update"]/span').click()
           
    driver.find_element_by_xpath('//*[@id="checkout-now"]').click()         
           

        

def newUser(): # make a new profile

    proName = input("Please select a name for this profile ")
    name = input("What is your name ")
    creditCard = input("Input your credit card number ")
    email = input("What is your email ")
    phone = input("What is your phone number ")
    address = input("Please input your address ")
    zipCode = input("What is your zip code")
    city = input("What is your city ")
    apt = input("What is your apartment ")
    state = input("What is your state ")
    country = ("What is your country ")

    if proName not in users: #trying to avoid duplicates

        users[proName] = userInfo(name, creditCard, email, phone, address, zipCode, city, apt, state, country)
        return

    while proName not in users:

        proName = input("That profile Name already exists please choose another name")

        if proName not in users:

            users[proName] = userInfo(name, creditCard, email, phone, address, zipCode, city, apt, state, country)

if __name__ == "__main__":
   
   for i in range(0,3):
       getItemInfo() 
   checkOut()          
   
    
