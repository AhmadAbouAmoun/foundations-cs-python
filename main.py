from bs4 import BeautifulSoup
import os
import requests
import validators
from lxml import html
import json
import pathlib


def tabToDict(Tab):
    return {'name': Tab.name,
            'url': Tab.url,
            'nested_tabs': [tabToDict(nested_tabs) for nested_tabs in Tab.nested_tabs]}
class Tab:
    def __init__(self, name, url, nested_tabs=None):
        self.name = name
        self.url = url
        self.nested_tabs = nested_tabs or []


class Browser:
    def __init__(self):
        self.tabs = []
    def openTab(self):
        name = input("please enter the name of the tab ")
        url = input("please enter the URL of the page ")
        tab = Tab(name, url)
        self.tabs.append(tab)

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

    def switchTabs(self):
        switched_tab = int(input('please enter which tab you want to switch to and display it (press enter to display the last opened tab)') or '-1')
        if switched_tab == -1:
            tab = self.tabs[-1]
            if validators.url(tab.url):
            #https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not this is the link to explain about the validators library and the validate.url function
                page_to_scrape = requests.get(tab.url)
                scraped = html.fromstring(page_to_scrape.content)
                print(scraped)
            else:
                print("the URL provided for this tab is invalid")
        elif switched_tab in range(len(self.tabs)):
            tab = self.tabs[switched_tab]
            if validators.url(tab.url):
                page_to_scrape = requests.get(tab.url)
                scraped = html.fromstring(page_to_scrape.content)
                print(scraped)
        else:
            print("Invalid option")


    def displayAllTabs(self):
        for i in range(len(self.tabs)):
            tab = self.tabs[i]
            print(i, ".", tab.name)
            for j in range(len(tab.nested_tabs)):
                nested_tab = tab.nested_tabs[j]
                print('nested tab ',j,nested_tab.name)

    def openNestedTab(self):
        for i in range(len(self.tabs)-1):
             print(i, ".", self.tabs[i])
        option = int(input('please enter the tab that you want to open a nested tab at '))
        if 0<=option<=len(self.tabs):
            title = input("Enter the title of the nested tab: ")
            url = input("Enter the URL of the nested tab: ")
            self.tabs[option].nested_tabs.append(Tab(title, url))
    def clearAllTabs(self):
         self.tabs = []

    def classToDict(self):
        dict=[tabToDict(tab) for tab in self.tabs]
        return dict
    def saveFile(self):
        browser_dict = self.classToDict()
        file_name = input('enter the name of the file ')

        file_path=input("please enter the path that you want to save the file in ")
        if os.path.exists(file_path):
            #https://bobbyhadz.com/blog/python-input-file-path here is the explanation for the os library and why i used it here
            complete_name = os.path.join(file_path, file_name + ".txt")#https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac this is were i got i learnt about os join
            json_string = json.dumps(browser_dic)
            with open(complete_name, 'w') as file:
                file.write(json.dumps(json_string))
        else:
            print('the path is not valid we will save it in the same directory in the current directory ')
            json_string = json.dumps(browser_dic,encoding='utf-8')#https://youtu.be/jABj-SEhtBc?si=6NuPANZI72Asgz2- this is the video that helped me in options number 7 and 8
            with open(file_name, 'w') as file:
             file.write(json.dumps(json_string,ensure_ascii=False,indent=4))

    def importFiles(self):
        file_name=('please enter the name of the file that you want to open ')
        file_path = input('please enter the files directory ')
        if os.path.exists(file_path):
            with open(file_name,'r') as f:
                browser_dict = json.loads(f.read())
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
        if choice == 2:
            browser.closeTab()
        if choice == 3:
            browser.switchTabs()
        if choice == 4:
            browser.displayAllTabs()
        if choice == 5:
            browser.openNestedTab()
        if choice == 6:
            browser.clearAllTabs()
        if choice == 7:
            browser.saveFile()
        if choice == 8:
            browser.importFile()
        if choice == 9:
            break
main()