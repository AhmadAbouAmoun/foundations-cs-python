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
main()