class Tab:
    def __init__(self ,name , url):
        self.name = name
        self.url = url

class Browser:
    def __init__(self):
        self.tabs = []
    def open(self):
        name = input("please enter the name of the tab ")
        url = input("please enter the URL of the page ")
        tab = Tab(name,url)
        self.tabs.append(tab)

def main():
    browser = Browser()
    browser.open()
main()