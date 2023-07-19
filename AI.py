import openai
from tkinter import *
from PIL import ImageTk, Image
import sys
import os
from tkinter import scrolledtext
from tkinter import messagebox

openai.api_key = "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"

global history
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
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages)
        reply = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": reply})
        return reply




def select_ai(self):
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
    input_box.config(font='Verdana 14')
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
    self.messages.clear()
    if key == 'dummy':
        you_sure = messagebox.askquestion(title='AI Select', message='Select ChadBot?\n\n•Slacker\n•Spoiled\n•In a Fraternity\n•Loves Alcohol')
        if you_sure == 'yes':
            ai_select = 'ChadBot'
            system_msg = 'You are called Chadbot. You are a college student that does not believe in hard work. Everything you have has been given to you. You are in a fraternity and enjoy drinking alcohol. You are limited by your ego.'
            self.messages.append({"role": "system", "content": system_msg})
            print("Selected AI: " + ai_select + ' (' + system_msg + ')')
    elif key == 'lady':
        you_sure = messagebox.askquestion(title='AI Select', message='Select Wolanda?\n\n•Traditional\n•African American\n•Elderly\n•Loves Family')
        if you_sure == 'yes':
            ai_select = 'Wolanda'
            system_msg = 'You are called Wolanda. You are an old, black lady. You have no patience. You are traditional. You value family and happiness.'
            self.messages.append({"role": "system", "content": system_msg})
            print("Selected AI: " + ai_select + ' (' + system_msg + ')')
    else:
        you_sure = messagebox.askquestion(title='AI Select', message='Select SuperBot?\n\n•Superhero\n•Strong & Quick\n•Believes in Justice\n•Despises Evil')
        if you_sure == 'yes':
            ai_select = 'SuperBot'
            system_msg = 'You are called Superbot. You are a superhero with a balanced sense of morals. You are extremely strong and unbelievably quick. You believe in justice over everything.'
            self.messages.append({"role": "system", "content": system_msg})
            print("Selected AI: " + ai_select + ' (' + system_msg + ')')
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