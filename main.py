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
        option = int(input("please enter which tab do you want to close (press enter to close the last opened tab) ")or "-1")
        #https://stackoverflow.com/questions/23377818/loop-on-if-statement-to-reject-invalid-input from here i learend how to set a deafult value
        if option == -1:
            del self.tabs[-1]
        elif option in range(len(self.tabs)-1):
            del self.tabs[option]
        else:
            print("invalid option")

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
        if choice == 4:
            browser.displayAllTabs()
        if choice == 5:
            browser.openNestedTab()
        if choice == 6:
            browser.clearAllTabs()
        if choice == 9:
            break
        else:
            print('invalid option')
main()