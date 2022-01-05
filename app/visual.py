from tkinter import *
from tkinter import ttk
import os
class login(Tk):
    def __init__(self):
        super().__init__()
        self.title("WebApp Maker")
        self.geometry("700x500+550+200")
        self.resizable(False,False)
    def label(self):
        self.bgImage=PhotoImage(file="/home/pi/WebAppMaker/app/image.png")
        self.Image=Label(self,image=self.bgImage)
        self.Image.place(x=0,y=0)
        #Title
        self.title=Label(self,text="WebApp Maker",font="Courier 35")
        self.title.place(x=183,y=88)
        self.title['bg']='#ffffff'
        #App Name
        self.appName=Label(self,text="App Name",font="Courier 10")
        self.appName.place(x=200,y=170)
        self.appName['bg']='#ffffff'
        #Domain
        self.webDomain=Label(self,text="Web Domain (https://example.com)",font="Courier 10")
        self.webDomain.place(x=200,y=225)
        self.webDomain['bg']='#ffffff'
        #Category
        self.category=Label(self,text="Category",font="Courier 10")
        self.category.place(x=200,y=286)
        self.category['bg']='#ffffff'
        #Icon Location
        self.iconLocation=Label(self,text="Icon Location (optional)",font="Courier 10")
        self.iconLocation.place(x=200,y=347)
        self.iconLocation['bg']='#ffffff'
               
    def Entry(self):
        self.appName=Text(self,borderwidth=0,highlightthickness=0,width=19,height=1)
        self.appName['bg']='#0469d5'
        self.appName.place(x=438,y=165)
        
        self.webDomain=Text(self,borderwidth=0,highlightthickness=0)
        self.webDomain['bg']='#0469d5'
        self.webDomain.place(x=438,y=220,width=156,height=20)
        
        style=ttk.Style()
        style.configure("TCombobox", fieldbackground= '#0469d5', background= '#0469d5',borderwidth=0,highlightthickness=0)
        self.category=ttk.Combobox(self,values=['Internet', 'Web', 'Accessories', 'Games', 'Graphics', 'Office', 'Sound&Video', 'Programming', 'Education'])
        self.category.place(x=440,y=283,width=156,height=20)
        
        self.iconLocation=Text(self,borderwidth=0,highlightthickness=0)
        self.iconLocation['bg']='#0469d5'
        self.iconLocation.place(x=444,y=342,width=150,height=20)
        
    def Button(self):
        self.buttonImage=PhotoImage(file='/home/pi/WebAppMaker/app/button.png')
        self.applyAndRun=Button(self,bg='#ffffff',fg='#ffffff', activebackground='#ffffff', activeforeground='#ffffff',command=self.Apply,image=self.buttonImage,borderwidth=0,highlightthickness=0)
        self.applyAndRun.place(x=277,y=370, width=150, height=60)
    
    def Apply(self):
            #made = open('apps-made.txt', 'w+')
            #apps_made = made.write(str(int(made.read()) + 1))
            app_name = self.appName.get('1.0', 'end')
            web_domain = self.webDomain.get('1.0', 'end')
            icon_location = self.iconLocation.get('1.0', 'end')
            sel = self.category.get()
            file = open(f'{app_name[:-1:]}', 'w+')
            file.write("[Desktop Entry]\nVersion=1.0\nName=" + app_name + "Comment=Web App Built With WebApp Maker\nExec=chromium-browser --app=https://" + web_domain + """Terminal=false\nX-MultipleArgs=false\nType=Application\nIcon=""" + icon_location +"""Categories=GTK;"""+ sel + """;\nMimeType=text/html;text/xml;application/xhtml_xml;\nStartupWMClass=""" + app_name +"""StartupNotify=true\nX-WebApp-URL=https://""" + web_domain +"""X-WebApp-Isolated=true""")
            os.system(f'mv /home/pi/WebAppMaker/{app_name[:-1:]} /home/pi/Desktop/')
            self.finish=Canvas(self, width=500, height=360,borderwidth=0,highlightthickness=0)
            self.finish['bg']='#ffffff'
            self.finish.place(x=103,y=65)
            self.finishText=Label(self,text=f"You can now find\n the app on your\n desktop.",font="Courier 20")
            self.finishText['bg']='#ffffff'
            self.finishText.place(x=230,y=215)
            self.ok=Button(self,text='ok',command=self.removeCanvas)
            self.ok.place(x=345,y=303)
        
        
    def removeCanvas(self):
        self.destroy()
        Login=login()
        Login.label()
        Login.Entry()
        Login.Button()
        Login.mainloop()
if __name__=="__main__":
    Login=login()
    Login.label()
    Login.Entry()
    Login.Button()
    Login.mainloop()