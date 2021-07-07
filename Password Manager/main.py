import string
import tkinter as tk
import tkinter.ttk as ttk
from random import uniform, random, choice, sample, randint
import cryptography
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

f = open("key", 'rb')
key = f.readline()
f.close()

logged = False

class TestApp:
    def __init__(self, master=None):
        # build ui
        self.frame4 = ttk.Frame(master)
        self.frame1 = tk.Frame(self.frame4)
        self.button5 = tk.Button(self.frame1)
        self.button5.configure(background='#27333f', compound='top', cursor='hand2', font='TkTextFont')
        self.button5.configure(foreground='white', justify='center', overrelief='ridge', relief='flat')
        self.button5.configure(text='GENERATE PASSWORD')
        self.button5.place(anchor='center', height='35', relx='0.5', rely='0.5', width='200', x='0', y='0')
        self.button5.bind('<1>', self.generatePassword, add='')
        self.button3 = tk.Button(self.frame1)
        self.button3.configure(background='#27333f', compound='top', cursor='hand2', font='TkTextFont')
        self.button3.configure(foreground='white', justify='center', overrelief='ridge', relief='flat')
        self.button3.configure(text='SAVE PASSWORD')
        self.button3.place(anchor='center', height='35', relx='0.5', rely='0.6', width='200', x='0', y='0')
        self.button3.bind('<1>', self.openSave, add='')
        self.button1 = tk.Button(self.frame1)
        self.button1.configure(background='#27333f', compound='top', cursor='hand2', font='TkTextFont')
        self.button1.configure(foreground='white', justify='center', overrelief='ridge', relief='flat')
        self.button1.configure(text='LOAD PASSWORD')
        self.button1.place(anchor='center', height='35', relx='0.5', rely='0.4', width='200', x='0', y='0')
        self.button1.bind('<1>', self.openLoad, add='')
        self.button8 = tk.Button(self.frame1)
        self.user_png = tk.PhotoImage(file='img/user.png')
        self.button8.configure(activebackground='#27333f', background='#27333f', image=self.user_png, justify='center')
        self.button8.configure(relief='flat', text='button8')
        self.button8.place(anchor='center', relx='0.5', rely='0.15', x='0')
        self.button2 = tk.Button(self.frame1)
        self.button2.configure(background='#27333f', compound='top', cursor='hand2', font='TkTextFont')
        self.button2.configure(foreground='white', justify='center', overrelief='ridge', relief='flat')
        self.button2.configure(text='SAVED PASSWORDS')
        self.button2.place(anchor='center', height='35', relx='0.5', rely='0.69', width='200', x='0', y='0')
        self.button2.bind('<1>', self.openSavedPasswords, add='')
        self.frame1.configure(background='#27333f', height='200', width='200')
        self.frame1.grid(column='0', ipady='200', row='0')
        self.frame3 = tk.Frame(self.frame4)
        self.savePasswordPage = tk.Frame(self.frame3)
        self.frame7 = tk.Frame(self.savePasswordPage)
        self.descriptionEntry = tk.Entry(self.frame7)
        self.descriptionEntry.configure(justify='center')
        self.descriptionEntry.place(anchor='center', height='25', relx='0.5', rely='0.3', width='170', x='0', y='0')
        self.label2 = tk.Label(self.frame7)
        self.label2.configure(background='#27333f', font='{Arial} 14 {}', foreground='white', text='DESCRIPTION')
        self.label2.place(anchor='center', relx='0.5', rely='0.15', x='0', y='0')
        self.label3 = tk.Label(self.frame7)
        self.label3.configure(background='#27333f', font='{Arial} 14 {}', foreground='white', justify='left')
        self.label3.configure(text='PASSWORD')
        self.label3.place(anchor='center', relx='0.5', rely='0.5', x='0', y='0')
        self.passwordEntry = tk.Entry(self.frame7)
        self.passwordEntry.configure(justify='center')
        self.passwordEntry.place(anchor='center', height='25', relx='0.5', rely='0.65', width='170', x='0', y='0')
        self.submitSaveBtn = tk.Button(self.frame7)
        self.submitSaveBtn.configure(background='#3d4955', cursor='hand2', font='{Arial} 12 {}', foreground='white')
        self.submitSaveBtn.configure(relief='flat', takefocus=False, text='SAVE')
        self.submitSaveBtn.place(anchor='center', relx='0.5', rely='0.85', x='0', y='0')
        self.submitSaveBtn.bind('<1>', self.savePassword, add='')
        self.frame7.configure(background='#27333f', height='200', width='200')
        self.frame7.pack(ipadx='30', ipady='40', side='top')
        self.savePasswordPage.configure(background='#3d4955', height='600', width='600')
        self.savePasswordPage.place(anchor='center', relx='0.5', rely='0.5', x='0', y='1000')
        self.savePasswordPage.bind('<1>', self.callback, add='')
        self.savePasswordPage.bind('<1>', self.callback, add='')
        self.frameLogin = tk.Frame(self.frame3)
        self.label1 = tk.Label(self.frameLogin)
        self.label1.configure(background='#27333f', font='{Arial} 24 {}', foreground='white', text='LOGIN')
        self.label1.place(anchor='center', relx='0.5', rely='0.25', x='0', y='0')
        self.entryLogin = tk.Entry(self.frameLogin)
        self.entryLogin.configure(font='{Arial} 12 {}', foreground='white', justify='center')
        self.entryLogin.place(anchor='center', height='30', relx='0.5', rely='0.5', width='300', x='0', y='0')
        self.logBtn = tk.Button(self.frameLogin)
        self.logBtn.configure(background='#3d4955', cursor='hand2', font='{Arial CE} 16 {}', foreground='white')
        self.logBtn.configure(relief='flat', text='SUBMIT')
        self.logBtn.place(anchor='center', relx='0.5', rely='0.8', x='0', y='0')
        self.logBtn.configure(command=self.logIn)
        self.frameLogin.configure(background='#27333f', height='200', width='200')
        self.frameLogin.place(anchor='center', height='400', relx='0.5', rely='0.5', width='400', x='0', y='0')
        self.frameLoad = tk.Frame(self.frame3)
        self.label4 = tk.Label(self.frameLoad)
        self.label4.configure(background='#27333f', font='{arial} 16 {}', foreground='white', text='PASSWORD LOADER')
        self.label4.place(anchor='center', relx='0.5', rely='0.15', x='0', y='0')
        self.label5 = tk.Label(self.frameLoad)
        self.label5.configure(background='#27333f', font='{arial} 9 {}', foreground='white', text='Please refer the password description')
        self.label5.place(anchor='center', relx='0.5', rely='0.3', x='0', y='0')
        self.entryPassName = tk.Entry(self.frameLoad)
        self.entryPassName.configure(font='{arial} 14 {}', justify='center')
        self.entryPassName.place(anchor='center', relx='0.5', rely='0.4', x='0', y='0')
        self.loadBtn = tk.Button(self.frameLoad)
        self.loadBtn.configure(background='#3d4955', cursor='hand2', font='{arial} 12 {}', foreground='white')
        self.loadBtn.configure(relief='flat', text='LOAD')
        self.loadBtn.place(anchor='center', relx='0.5', rely='0.55', x='0', y='0')
        self.loadBtn.bind('<1>', self.loadPassword, add='')
        self.loadLabel = tk.Label(self.frameLoad)
        self.loadLabel.configure(background='#27333f', foreground='#27333f', relief='flat', text='Password')
        self.loadLabel.place(anchor='center', relx='0.5', rely='0.7', x='0', y='0')
        self.textPass = tk.Text(self.frameLoad)
        self.textPass.configure(background='#27333f', font='{arial} 10 {}', foreground='white', height='10')
        self.textPass.configure(relief='flat', width='50')
        self.textPass.place(anchor='center', height='35', relx='0.5', rely='0.85', width='180', x='0', y='0')
        self.frameLoad.configure(background='#27333f', height='200', width='200')
        self.frameLoad.place(anchor='center', height='300', relx='0.5', rely='0.5', width='280', y='1000')
        self.frameGenerator = tk.Frame(self.frame3)
        self.label8 = tk.Label(self.frameGenerator)
        self.label8.configure(background='#27333f', font='{arial} 15 {}', foreground='white', text='GENERATED PASSWORD')
        self.label8.place(anchor='center', relx='0.5', rely='0.3', x='0', y='0')
        self.generatedPassword = tk.Entry(self.frameGenerator)
        self.generatedPassword.configure(background='#27333f', foreground='white', justify='center', relief='flat')
        self.generatedPassword.place(anchor='center', relx='0.5', rely='0.65', width='200', x='0', y='0')
        self.frameGenerator.configure(background='#27333f', height='200', width='200')
        self.frameGenerator.place(anchor='center', height='150', relx='0.5', rely='0.5', width='280', x='0', y='1000')
        self.savedPasswords = tk.Frame(self.frame3)
        self.passwordList = tk.Listbox(self.savedPasswords)
        self.passwordList.place(anchor='center', height='500', relx='0.5', rely='0.5', width='450', x='0', y='0')
        self.savedPasswords.configure(height='200', width='200')
        self.savedPasswords.place(anchor='center', height='500', relx='0.5', rely='0.5', width='450', y='1000')
        self.frame3.configure(background='#3d4955', height='200', width='200')
        self.frame3.grid(column='1', ipadx='200', ipady='200', row='0')
        self.frame4.configure(height='200', width='200')
        self.frame4.grid(column='0', row='0')

        # Main widget
        self.mainwindow = self.frame4

    def openSavedPasswords(self, event=None):
        if logged == False:
            return
        self.savePasswordPage.place(y='1000')
        self.frameLoad.place(y='1000')
        self.frameGenerator.place(y='1000')
        self.savedPasswords.place(y='0')
        fernet = Fernet(key)
        f = open("save.txt", 'rb')
        cpt = 1
        self.passwordList.delete(0, 99999999)
        for x in f:
            if cpt%2!=0:
                self.passwordList.insert(0, fernet.decrypt(x).decode())
            cpt +=1
        f.close()
        pass

    def openLoad(self, event=None):
        if logged == False:
            return
        self.savePasswordPage.place(y='1000')
        self.frameLoad.place(y='0')
        self.frameGenerator.place(y='1000')
        self.savedPasswords.place(y='1000')
        pass

    def loadPassword(self, event=None):
        fernet = Fernet(key)
        f = open("save.txt", 'rb')
        i = 0
        next = False
        found = False
        for x in f:
            i += 1
            if next == True:
                self.loadLabel.configure(text=f'Password {self.entryPassName.get()}', fg="white")
                self.textPass.delete('1.0', tk.END)
                self.textPass.insert(tk.END, fernet.decrypt(x).decode())
                found = True
                break
            if i%2!=0 and fernet.decrypt(x).decode() == self.entryPassName.get():
                next = True
        if not found:
            self.loadLabel.configure(text='', fg="#27333f")
            self.textPass.delete('1.0', tk.END)
            self.entryPassName.delete(0, 9999)
        f.close()
        pass

    def callback(self):
        pass



    def logIn(self):
        if self.entryLogin.get()=="root":
            self.frameLogin.place(y='5000')
            global logged
            logged = True
        pass

    def savePassword(self, event=None):
        if not self.passwordEntry.get().strip():
            return
        elif not self.descriptionEntry.get().strip():
            return
        else:
            fernet = Fernet(key)

            f = open("save.txt", "ab")
            description = self.descriptionEntry.get()
            encodedDesc = description.encode()
            encryptedDesc = fernet.encrypt(encodedDesc)
            f.write(encryptedDesc)
            f.close()

            fsaut = open("save.txt", 'a')
            fsaut.write('\n')
            fsaut.close()

            f = open("save.txt", "ab")
            password = self.passwordEntry.get()
            encodedPass = password.encode()
            encryptedPass = fernet.encrypt(encodedPass)
            f.write(encryptedPass)
            f.close()

            fsaut = open("save.txt", 'a')
            fsaut.write('\n')
            fsaut.close()

            self.descriptionEntry.delete(0, 10000)
            self.passwordEntry.delete(0, 10000)
        pass

    def openSave(self, event=None):
        if logged == False:
            return
        self.savePasswordPage.place(y='0')
        self.frameGenerator.place(y='1000')
        self.frameLoad.place(y='1000')
        self.savedPasswords.place(y='1000')
        pass

    def generatePassword(self, event=None):
        if logged == False:
            return
        self.frameGenerator.place(y='0')
        self.savePasswordPage.place(y='1000')
        self.frameLoad.place(y='1000')
        self.savedPasswords.place(y='1000')
        ps = ""
        for x in range(20):
            r = randint(1, 3)
            if r == 1:
                ps = ps+choice(string.ascii_letters)
            elif r == 2:
                ps = ps+choice(string.digits)
            else:
                ps = ps+choice(string.punctuation)
        self.generatedPassword.delete('0', '99999')
        self.generatedPassword.insert('0', ps)

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.resizable(False, False)
    app = TestApp(root)
    app.run()

