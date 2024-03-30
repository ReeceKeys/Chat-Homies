import openai
from tkinter import *
from PIL import ImageTk, Image
import sys
import os
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from pathlib import Path
from PyPDF2 import PdfReader
import json
from pathlib import Path
from base64 import b64decode



openai.api_key = "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" #Change, must generate a key from OpenAI website 


global history
global ai_select
global wolanda
global superbot
global chadbot
history = ''

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Client:
    def __init__(self, messages): 
        messages = []
        self.messages = messages


def chat(self, message):
        try:
            self.messages.append({"role": "user", "content": message})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages
            )
            reply = response.choices[0].message["content"]
            self.messages.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred. Please check your API setup."

def img(self):
    ask_prompt = simpledialog.askstring(title='IMG Prompt', prompt='\t\t\t\t\t\t\tEnter image prompt. Try to be as descriptive as possible:\t\t\t\t\t\t\t')
    if ask_prompt != '':
        response = openai.images.generate(
            model="dall-e-3",
            prompt = ask_prompt,
            n=1,
            quality="hd",
            size = "1024x1024",
        )
        
        

        print(ask_prompt)
        win = Tk()
        canvas = Canvas(win, width=300, height=300, bg='#333333')
        canvas.pack()
        box = scrolledtext.ScrolledText(win, bg='black', wrap=WORD, fg='white')
        canvas.create_window(150, 50, height=300, width=300, anchor = 'n', window = box) 
        retry_btn = Button
        box.insert('end', response.data[0].url, 'white')
        win.protocol("WM_DELETE_WINDOW", lambda:[win.destroy(), select_ai(self)])
        win.mainloop()
    else:
        win = Tk()
        win.config(height="100px", width="400px")
        
        copy_me = Text(win, bg="black", fg="white")
        copy_me.insert("end", "Invalid", "white")
        win.protocol("WM_DELETE_WINDOW", lambda:[win.destroy(), select_ai(self)])
        win.mainloop()
        

def teddy(self):
    global ai_select
    global system_msg
    you_sure = messagebox.askquestion(title='AI Select', message='Select Teddy?\n\n•Reads [text]books \n•Retains and uses their knowledge! \n•Accepts [.txt, .pdf]')
    if you_sure == 'yes':
        ai_select = 'Teddy'
        system_msg = 'You are called Teddy. Everything after this message are the contents of a book. You are to use this reading to answer further questions. '
    
        break_flag = False
        while break_flag == False:
            file_path = filedialog.askopenfilename()
            full_file_name = Path(file_path).name
            file_name = Path(file_path).stem
            stem = Path(file_path).suffix
            if not file_path:
                break_flag = True
                pass
            elif stem == '.txt':
                textbook = Path(file_path).read_text()
                break_flag = True
                print("File name: " + str(full_file_name))
                system_msg += 'The reading is as follows: (' + str(textbook) + ').'
                system_msg += 'Cite to the reading as ' + str([file_name]) + '. Use this reading to answer any questions asked that relate to the context of this reading.'  
            elif stem == '.pdf':
                textbook = ''
                text = ''
                ask_pages = [0,0]
                ask_pages_flag = [False, False]
                pdf = PdfReader(file_path)
                while ask_pages_flag[0] == False:
                    ask_pages[0] = simpledialog.askinteger('Page select', 'Select the range of pages: [empty, empty]')
                    if not ask_pages[0]:
                        break
                    elif ask_pages[0] < 0 or ask_pages[0] > len(pdf.pages):
                        messagebox.showerror('Invalid Input', 'Please select a valid page number.')
                    else:
                        ask_pages_flag[0] = True
                        while (ask_pages_flag[1] == False):
                            ask_pages[1] = simpledialog.askinteger('Page select', 'Select the range of pages: [' + str(ask_pages[0]) + ' : empty]')
                            if not ask_pages[1]:
                                break
                            elif ask_pages[1] < 0 or ask_pages[0] > len(pdf.pages) or ask_pages[1] < ask_pages[0]:
                                messagebox.showerror('Invalid Input', 'Please select a valid page number.')
                            else:
                                ask_pages_flag[1] = True
                if ask_pages_flag == [True,True]:
                    if ask_pages[1] - ask_pages[0] > 3:
                        messagebox.showerror('Index Error', 'This application only allows up to 3 pages of reading.')
                        ask_pages_flag = [False,False]
                    else:
                        for i in range(ask_pages[0], ask_pages[1]):  #60 - 62
                            pages = pdf.pages[i] # pages = 62
                            text += pages.extract_text() # text = page 62 extracted text 
                        textbook = text
                        break_flag = True  
                print("File name: " + str(full_file_name))
                system_msg += 'The reading is as follows: (' + str(textbook) + ').'
                system_msg += 'Cite to the reading as ' + str([file_name]) + '. Use this reading to answer any questions asked that relate to the context of this reading.'  
            else:
                messagebox.showerror("File unsupported", 'Supported file types: [txt, pdf]')
                system_msg = ''
                break_flag = True
                
            print("Stem: " + str(stem))
    else:
        system_msg = ''
        pass

    
    
    
global super_img
global chadbot_img
global wolanda_img
def select_ai(self):
    global super_img
    global chadbot_img
    global wolanda_img
    win = Tk()
    win.title('Chat Homies')
    win.geometry('600x600')
    canvas = Canvas(win, width=600, height=600, bg='#333333')
    canvas.pack()
    select_page = Label(win, text='Choose An AI', fg='white',bg='#333333')
    select_page.config(font='Cascadia 30')
    canvas.create_window(300, 40, anchor='n', window=select_page)
    

    selected = Label(win, text='Selected AI: ' + ai_select, fg='white',bg='#333333')
    selected.config(font='Verdana 12')
    canvas.create_window(300, 100, anchor='n', window=selected)

    super_img = ImageTk.PhotoImage(superbot)
    superhero_btn = Button(win, text='SuperBot', image= super_img, fg='dark green', bg='#CBF2B8', command=lambda:[win.destroy(), set_ai(self, 'superhero')])
    superhero_btn.config(font='Verdana 12') 
    canvas.create_window(200, 280, anchor='e', window=superhero_btn)

    wolanda_img = ImageTk.PhotoImage(wolanda)
    lady_btn = Button(win, text='Wolanda', image= wolanda_img, fg='dark green', bg='#FAF4B7', command=lambda:[win.destroy(), set_ai(self, 'lady')])
    lady_btn.config(font='Verdana 12')
    canvas.create_window(300, 280, anchor='center', window=lady_btn)

    chadbot_img = ImageTk.PhotoImage(chadbot)
    dummy_btn = Button(win, text='ChadBot', image= chadbot_img, fg='dark green', bg='#FFC4C4', command=lambda:[win.destroy(), set_ai(self, 'dummy')])
    dummy_btn.config(font='Verdana 12')
    canvas.create_window(400, 280, anchor='w', window=dummy_btn)

    guru_btn = Button(win, text='Guru', fg='white', bg='light blue', command=lambda:[win.destroy(), set_ai(self, 'guru')])
    guru_btn.config(font='Verdana 12')
    canvas.create_window(260, 360, anchor='ne', window=guru_btn)


    edgy_btn = Button(win, text='Teddy', fg='white', bg='purple', command=lambda:[win.destroy(), set_ai(self, 'teddy')])
    edgy_btn.config(font='Verdana 12')
    canvas.create_window(340, 360, anchor='nw', window=edgy_btn)

    edgy_btn = Button(win, text='IMG', fg='white', bg='orange', command=lambda:[win.destroy(), set_ai(self, 'img')])
    edgy_btn.config(font='Verdana 12')
    canvas.create_window(300, 360, anchor='n', window=edgy_btn)

    info = Label(win, text='Welcome to Chat Homies!', fg='light green', bg='#333333')
    info.config(font='Verdana 12 italic')
    canvas.create_window(300, 400, anchor = 'n', window=info)

    info2 = Label(win, text='Select an AI from above\nand chat with an AI that truly has a personality.\nMore personalities coming soon!', fg='white', bg='#333333')
    info2.config(font='Verdana 10')
    canvas.create_window(300, 440, anchor = 'n', window=info2)

    info3 = Label(win, text='Made by Reece Harris utilizing OpenAI.\nVersion 1.0', fg='white', bg='#333333')
    info3.config(font='Verdana 8 italic')
    canvas.create_window(300, 500, anchor = 'n', window=info3)

    chat_btn = Button(win, text='Chat', fg='light green', bg='black', command=lambda:[win.destroy(), chat_box(self)])
    chat_btn.config(font='Verdana 12')
    canvas.create_window(310, 580, anchor='sw', window=chat_btn)

    close = Button(win, text='Close', fg='light blue', bg='black', command=lambda:win.destroy())
    close.config(font='Verdana 12')
    canvas.create_window(290, 580, anchor='se', window=close)



    win.mainloop()


def chat_box(self):
    win = Tk()
    win.title('Chat Homies')
    win.geometry('600x600')
    canvas = Canvas(win, width=600, height=600, bg='#333333')
    canvas.pack()

    selected = Label(win, text='Selected AI: ' + ai_select, fg='white',bg='#333333')
    selected.config(font='Cascadia 20')
    canvas.create_window(300, 40, anchor='n', window=selected)

    chat_label = Label(win, text='Chat Log', fg='white', bg='#333333')
    chat_label.config(font='Verdana 12 italic')
    canvas.create_window(300, 90, anchor='n', window=chat_label)

    box = scrolledtext.ScrolledText(win, bg='black', wrap=WORD)
    box.config(state='disabled')
    canvas.create_window(300, 120, height=300, width=450, anchor = 'n', window = box) 

    input_label = Label(win, text='Ask Away!', fg='white', bg='#333333')
    input_label.config(font='Verdana 12 italic')
    canvas.create_window(300, 430, anchor='n', window=input_label)

    input_box = Text(win, bg='white', fg='black')

    box.tag_config('light_green', foreground='light green', background='black')
    box.tag_config('light_blue', foreground='light blue', background='black')
    box.tag_config('white', foreground='white',background='black')
        

    def send(self, message):
        global history 
        if message != '':
            input_box.delete('1.0', 'end')
            response = chat(self, message)
            history += '[User]\n'
            history += message + '\n'
            history += '[AI]' 
            history += response + '\n' 

            print("[History]\n" + str(history))

            box.config(state='normal')
            box.insert('end', 'User: ', 'light_green')
            box.insert('end', (': ' + message), 'white')
            box.insert('end', ai_select, 'light_blue')
            box.insert('end', (': ' + response + '\n'), 'white')
            box.config(state='disabled')
    input_box.config(font='Verdana 14',wrap=WORD)
    canvas.create_window(300, 460, height=60, width=450, anchor = 'n', window = input_box) 

        
        

    send_btn = Button(win, text='Chat', fg='light green', bg='black', command=lambda:  send(self, input_box.get('1.0', 'end')))
    send_btn.config(font='Verdana 12')
    canvas.create_window(340, 580, anchor = 'sw', window = send_btn) 
    
    clear_btn = Button(win, text='Clear', fg='white', bg='black', command=lambda: [win.destroy(), chat_box(self)])
    clear_btn.config(font='Verdana 12')
    canvas.create_window(300, 580, anchor = 's', window = clear_btn) 

    close = Button(win, text='Go Back', fg='light blue', bg='black', command=lambda:[win.destroy(), select_ai(self)])
    close.config(font='Verdana 12')
    canvas.create_window(260, 580, anchor = 'se', window = close) 
    


    win.mainloop()


def set_ai(self, key):
    global ai_select
    global system_msg
    self.messages.clear()
    system_msg = ''
    if key == 'dummy':
        you_sure = messagebox.askquestion(title='AI Select', message='Select ChadBot?\n\n•Slacker\n•Spoiled\n•In a Fraternity\n•Loves Alcohol')
        if you_sure == 'yes':
            ai_select = 'ChadBot'
            system_msg = 'You are called Chadbot. You are a college student that does not believe in hard work. Everything you have has been given to you. You are in a fraternity and enjoy drinking alcohol. You are limited by your ego.'
    elif key == 'lady':
        you_sure = messagebox.askquestion(title='AI Select', message='Select Wolanda?\n\n•Traditional\n•African American\n•Elderly\n•Loves Family')
        if you_sure == 'yes':
            ai_select = 'Wolanda'
            system_msg = 'You are called Wolanda. You are an old, black lady. You have no patience. You are traditional. You value family and happiness.'
    elif key == 'superhero':
        you_sure = messagebox.askquestion(title='AI Select', message='Select SuperBot?\n\n•Superhero\n•Strong & Quick\n•Believes in Justice\n•Despises Evil')
        if you_sure == 'yes':
            ai_select = 'SuperBot'
            system_msg = 'You are called Superbot. You are a superhero with a balanced sense of morals. You are extremely strong and unbelievably quick. You believe in justice over everything.'
    elif key == 'guru':
        you_sure = messagebox.askquestion(title='AI Select', message='Select Guru?\n\n•Knows Stocks\n•Arrogant\n•Loves Money\n•Has Not Met His Kid Yet')
        if you_sure == 'yes':
            ai_select = 'Guru'
            system_msg = 'You are called Guru. You are very smart with stocks. You know which current stocks are going to make the most money. You are good at investments. You do not know your kids and do not care about family. You are arrogant.'
    elif key == 'teddy':
        teddy(self)
    elif key == 'img':
        img(self)
    if (system_msg != ''):
        self.messages.append({"role": "system", "content": system_msg})
        print("Selected AI: " + ai_select)
    select_ai(self)

def run():
    global ai_select
    global wolanda
    global superbot
    global chadbot

    wol = Image.open(resource_path('Wol.png'), 'r')
    hero = Image.open(resource_path('Super.png'), 'r')
    chad = Image.open(resource_path('Chad.png'), 'r')

    wolanda = wol.resize((120, 120))
    superbot = hero.resize((120, 120))
    chadbot = chad.resize((120, 120))

    ai_select = 'none'
    self = Client('')
    print('Created client.')
    select_ai(self)

run()

