from bs4 import BeautifulSoup
import os
import requests
import validators
from bs4 import BeautifulSoup
import json


def tabToDict(Tab):
    return {'name': Tab.name,
            'url': Tab.url,
            'nested_tabs': [tabToDict(nested_tabs) for nested_tabs in Tab.nested_tabs]}
#the tabToDict function is used to convert a tab into a dictionary



class Tab:
    def __init__(self, name, url, nested_tabs=None):
        self.name = name
        self.url = url
        self.nested_tabs = nested_tabs or []
#the Tab class is to create a tab that consist of a name a url and a list of nested tabs

class Browser:
    def __init__(self):
        self.tabs = []

#the Browser class is made up of a list of tabs

    def openTab(self):
        name = input("please enter the name of the tab ")
        url = input("please enter the URL of the page ")
        tab = Tab(name, url)
        self.tabs.append(tab)
#the openTab method asks for  the name and the url link and create a tab then inserts the created tab in the browser object which is a list of tabs
    def closeTab(self):
        for i in range(len(self.tabs)-1):
             print(i, ".", self.tabs[i])
        option = int(input("please enter which tab do you want to close (press enter to close the last opened tab) ") or "-1")
        #https://stackoverflow.com/questions/23377818/loop-on-if-statement-to-reject-invalid-input from here i learned how to set a default value
        if option == -1:
            del self.tabs[-1]
        elif option in range(len(self.tabs)-1):
            del self.tabs[option]
        else:
            print("invalid option")
#the closeTab method takes an input from the user for the index that he wants to close if no index has been given the last index shall be closed by using the default value -1 that i assigned

    def switchTabs(self):
        switched_tab = int(input('please enter which tab you want to switch to and display it (press enter to display the last opened tab)') or '-1')
        if switched_tab == -1:
            tab = self.tabs[-1]
            if validators.url(tab.url):
            #https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not this is the link to explain about the validators library and the validate.url function
                page_to_scrape = requests.get(tab.url)
                #https://youtu.be/hlSR0JAKpeQ?si=gjUaudGJgkd_sz4W from here i learnt how to scrape the html content of a page
                scraped = BeautifulSoup(page_to_scrape.content,'html.parser')
                print(scraped.prettify())

            else:
                print("the URL provided for this tab is invalid")
        elif switched_tab in range(len(self.tabs)):
            tab = self.tabs[switched_tab]
            if validators.url(tab.url):
                page_to_scrape = requests.get(tab.url)
                scraped = BeautifulSoup(page_to_scrape.content, 'html.parser')
                print(scraped.prettify())
        else:
            print("Invalid option")

#the switchTabs method asks the user what tab he wants to switch to and display its content if no value is given an default value is assigned so i can automatically display the last opened tab's html content
#then i used the validate.url to verify if the url given is valid or not (the link explains where i got it) then i used the request.get() and the BeautifulSoup functions to scrape the html content (the link is where i got this code and it explains what everything does)

    def displayAllTabs(self):
        for i in range(len(self.tabs)):
            tab = self.tabs[i]
            print(i, ".", tab.name)
            for j in range(len(tab.nested_tabs)):
                nested_tab = tab.nested_tabs[j]
                print('nested tab ',j,nested_tab.name)

#the displayAllTabs method is used to display the name of every tab by looping on the object (which is a list of tabs) then looping on the nested tabs list so that it can also display the nested tabs

    def openNestedTab(self):
        option = int(input('please enter the tab that you want to open a nested tab at '))
        if 0<=option<=len(self.tabs):
            title = input("Enter the title of the nested tab: ")
            url = input("Enter the URL of the nested tab: ")
            self.tabs[option].nested_tabs.append(Tab(title, url))
        else:
            print('invalid option')

#the openNestedTab method asks the user to input a  the index of the tab to open a nested tab  then if this index exist the it will ask the user to give the name and url for the opened tab

    def clearAllTabs(self):
         self.tabs = []
#the clearAllTabs method only deletes the opened tabs
    def objToDict(self):
        dict=[tabToDict(tab) for tab in self.tabs]
        return dict

#the objToDict method converts the browser object into a dictionary by using the tabToDict function as much as tabs are created in the object browser

    def saveFile(self):
        browser_dict = self.objToDict()
        file_name = input('enter the name of the file ')

        file_path=input("please enter the path that you want to save the file in ")
        if os.path.exists(file_path):
            #https://bobbyhadz.com/blog/python-input-file-path here is the explanation for the os library and why i used it here
            complete_name = os.path.join(file_path, file_name )#https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac this is were i got i learnt about os join
            json_string = json.dumps(browser_dict,indent=4)#https://youtu.be/jABj-SEhtBc?si=6NuPANZI72Asgz2- this is the video that helped me in understanding the json
            with open(complete_name, 'w') as file:
                file.write(json.dumps(json_string))
        else:
            print('the path is not valid we will save it in the same directory in the current directory ')
            json_string = json.dumps(browser_dict,indent=4)
            with open(file_name, 'w') as file:
             file.write(json.dumps(json_string))

#the saveFile method uses the function objToDict to turn the object browser into a dictionary so it can be written in json format in the file
#then asks the user for the name of the file and the path that he wants to save the file in the os.path.exists checks if this file exists (more details in the link) if not it will be created in the current directory
#if the path exists it will use the json.dump function so that the json_string will contain the new information then open a new file with the w aspect so that it could write in it the json_string(more details about the functions used in there respective links)



    def importFile(self):
        file_name=input('please enter the name of the file that you want to open ')
        file_path = input("please enter file's directory ")
        if(os.path.exists(file_path)):
            complete_name=os.path.join(file_path, file_name)#https://www.geeksforgeeks.org/python-os-path-join-method/ i read more about this function from this site so i can use it this way
            with open(complete_name,'r') as f:
                browser_dict = json.loads(f.read())#https://youtu.be/jABj-SEhtBc?si=6NuPANZI72Asgz2- again this video taught me about json
            print(browser_dict)
#the importFile method will ask the user to give the name of the file that he wants to open and its path then it will check if the path exists then open it and extract the details from it
def main():
    browser = Browser()
    while True:
        print('1- Open tab')
        print('2- Close tab')
        print('3- Switch tab')
        print('4- Display all tabs')
        print('5- Open nested tabs')
        print('6- Clear all tabs')
        print('7- Save tabs')
        print("8- Import tabs")
        print('9-Exit')
        choice = int(input('please enter your choice '))
        if choice == 1:
            browser.openTab()
        elif choice == 2:
            browser.closeTab()
        elif choice == 3:
            browser.switchTabs()
        elif choice == 4:
            browser.displayAllTabs()
        elif choice == 5:
            browser.openNestedTab()
        elif choice == 6:
            browser.clearAllTabs()
        elif choice == 7:
            browser.saveFile()
        elif choice == 8:
            browser.importFile()
        elif choice == 9:
            break
        else:
            print('invalid option')
main()