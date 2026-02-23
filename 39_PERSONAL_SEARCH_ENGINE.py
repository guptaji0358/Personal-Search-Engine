from tkinter import *
import webbrowser 
import os 

Dir_Base_Path = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpng"

Google = os.path.join(Dir_Base_Path,"GOOGLE.png")
Youtube = os.path.join(Dir_Base_Path,"YOUTUBE.png")
Facebook =os.path.join(Dir_Base_Path,"FACEBOOK.png")
Instagram = os.path.join(Dir_Base_Path,"INSTAGRAM.png")
Edge = os.path.join(Dir_Base_Path,"BING.png")
Github = os.path.join(Dir_Base_Path,"GITHUB.png")
Wikipedia = os.path.join(Dir_Base_Path,"WIKIPEDIA.png")

class PersonalSearchEngine:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("550x350")
        self.window.title("Personal Search Engine")

        self.TittleLabel = Label(text="Personal Search Engine",font=("Arial Black",15,"italic"))
        self.TittleLabel.grid(row=0,column=1)

        self.SearchLabel = Label(text="Search ->")
        self.SearchLabel.grid(row=1,column=0)

        self.SearchBox = Entry(width=30)
        self.SearchBox.focus()
        self.SearchBox.grid(row=1,column=1,columnspan=1)

        self.browser_var = StringVar()
        self.browser_var.set("Default")  # default selected value
        self.Browser_Dropdown = OptionMenu(self.window,self.browser_var,"Default","Edge","Chrome")
        self.Browser_Dropdown.grid(row=5, column=0,pady=20)

        self.Google_Img = PhotoImage(file=Google).subsample(9,9)
        self.Google_Img_Button = Button(image=self.Google_Img,borderwidth=1,highlightthickness=0,command=self.Google_Button_Logic)
        self.Google_Img_Button.grid(row=3,column=0,padx=40,pady=10)

        self.YouTube_Img = PhotoImage(file=Youtube).subsample(7,7)
        self.YouTube_Img_Button = Button(image=self.YouTube_Img,borderwidth=1,highlightthickness=0,command=self.Youtube_Button_Logic)
        self.YouTube_Img_Button.grid(row=3,column=1,padx=15)

        self.Facebook_Img = PhotoImage(file=Facebook).subsample(7,7)
        self.Facebook_Img_Button = Button(image=self.Facebook_Img,borderwidth=1,highlightthickness=0,command=self.Facebook_Button_Logic)
        self.Facebook_Img_Button.grid(row=4,column=0,padx=15)

        self.Instagram_Img = PhotoImage(file=Instagram).subsample(7,7)
        self.Instragram_Img_Button = Button(image=self.Instagram_Img,borderwidth=1,highlightthickness=0,command=self.Instagram_Button_Logic)
        self.Instragram_Img_Button.grid(row=4,column=1,padx=15)

        self.Edge_Img = PhotoImage(file=Edge).subsample(7,7)
        self.Edge_Img_Button = Button(image=self.Edge_Img,borderwidth=1,highlightthickness=0,command=self.Bing_Button_Logic)
        self.Edge_Img_Button.grid(row=3,column=2,padx=15)

        self.Github_Img = PhotoImage(file=Github).subsample(7,7)
        self.Github_Img_Button = Button(image=self.Github_Img,borderwidth=1,highlightthickness=0,command=self.GitHub_Button_Logic)
        self.Github_Img_Button.grid(row=4,column=2,padx=15,pady=5)

        self.Wikipedia_Img = PhotoImage(file=Wikipedia).subsample(7,7)
        self.Wikipedia_Img_Button = Button(image=self.Wikipedia_Img,borderwidth=1,highlightthickness=0,command=self.Wikipedia_Button_Logic)
        self.Wikipedia_Img_Button.grid(row=5,column=1,padx=15)

        self.ClearButton = Button(text="❌",bg="red",fg="#FFFFFF",command=self.Clear_Searchbox_History)
        self.ClearButton.grid(row=1,column=2,sticky="w")

        self.window.mainloop()

    def open_browser(self, url):
        selected = self.browser_var.get()
        if selected == "Default":
            webbrowser.open(url)
        elif selected == "Edge":
            EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            webbrowser.get(f'"{EDGE_PATH}" %s').open(url)

        elif selected == "Chrome":
            CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.get(f'"{CHROME_PATH}" %s').open(url)

    def Clear_Searchbox_History(self):
        self.SearchBox.delete(0,END)
        self.SearchBox.focus()

    def Google_Button_Logic(self):
        User_Query = self.SearchBox.get()
        User_Query_Corrected = User_Query.replace(" ","+")
        Google_Base_URL = "https://www.google.com/search?q="
        User_answer_URL = F"{Google_Base_URL}{User_Query_Corrected}"
        self.open_browser(User_answer_URL)

    def Youtube_Button_Logic(self):
        User_Query = self.SearchBox.get()
        User_Query_Corrected = User_Query.replace(" ","+")
        YouTube_Base_URL = "https://www.youtube.com/results?search_query="
        User_answer_URL = F"{YouTube_Base_URL}{User_Query_Corrected}"
        self.open_browser(User_answer_URL)

    def Bing_Button_Logic(self):
        query = self.SearchBox.get()
        query = query.replace(" ", "+")
        base_url = "https://www.bing.com/search?q="
        final_url = base_url + query
        self.open_browser(final_url)

    def GitHub_Button_Logic(self):
        User_Query = self.SearchBox.get()
        User_Query_Corrected = User_Query.replace(" ","+")
        Base_URL = "https://github.com/search?q="
        User_answer_URL = F"{Base_URL}{User_Query_Corrected}"
        self.open_browser(User_answer_URL)

    def Instagram_Button_Logic(self):
        User_Query = self.SearchBox.get()
        User_Query_Corrected = User_Query.replace(" ","+")
        Base_URL = "https://www.instagram.com/"
        User_answer_URL = F"{Base_URL}{User_Query_Corrected}"
        self.open_browser(User_answer_URL)

    def Facebook_Button_Logic(self):
        query = self.SearchBox.get()
        query = query.replace(" ", "+")
        base_url = "https://www.facebook.com/search/top/?q="
        final_url = base_url + query
        self.open_browser(final_url)

    def Wikipedia_Button_Logic(self):
        query = self.SearchBox.get()
        query = query.replace(" ", "+")
        base_url = "https://en.wikipedia.org/w/index.php?search="
        final_url = base_url + query
        self.open_browser(final_url)

PersonalSearchEngine()