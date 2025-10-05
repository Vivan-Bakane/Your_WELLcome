# © 2025 Vivan Bakane. All rights reserved.
# Unauthorized use or distribution of this file is prohibited.


import customtkinter as tk
import tkinter as t
from PIL import Image
import time
import requests
import matplotlib.pyplot as plt

u = ""
p = ""
PROMPT = ""
AGE = ""
GENDER = ""
PROBLEMS = ""
PAST_PROBLEMS = ""
YEARS = ""
MONTHS = ""
DAYS = ""
ANSWER = ""

AGER = ""
GENDERR = ""
PROBLEMSR = ""
PAST_PROBLEMSR = ""
YEARSR = ""
MONTHSR = ""
DAYSR = ""

S = ""
S2 = ""
SF = ""
Y = ""
M = ""
D = ""

LSO = ""
LST = ""
RLSO = ""
RLST = ""
TIME_LIST = []
P_LIST = []

root = tk.CTk()
root.title("Your WELLcome")

img = tk.CTkImage(light_image=Image.open("C:/Users/super/Downloads/fil.png"), size=(100, 100))


tk.set_appearance_mode("dark")

#LOGIN

frame2 = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame2.configure(height=900, width=900)
frame2.pack(padx=10, pady=50)

t1 = tk.CTkLabel(master=frame2, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
t1.pack(padx=10, pady=10)

h1 = tk.CTkLabel(master=frame2, text="Login Page", fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center")
h1.pack()

imagell = tk.CTkLabel(master=frame2, image=img, text="")
imagell.pack(pady=20)

username = tk.CTkEntry(master=frame2, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=30, placeholder_text="Username", placeholder_text_color="Black")
username.pack(padx=100, pady=70)

password = tk.CTkEntry(master=frame2, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=30, placeholder_text="Password", placeholder_text_color="Black")
password.pack()

frame = tk.CTkFrame(master=frame2, width=200, height=200, fg_color="#ffffff")
frame.pack(pady=60, padx=10)

def SUP():
    frame2.pack_forget()
    frame2S.pack(padx=10, pady=50)
    usernameS.delete(0, 'end')
    passwordS.delete(0, 'end')
    username.delete(0, 'end')
    password.delete(0, 'end')

    usernameS.configure(placeholder_text="Username")
    passwordS.configure(placeholder_text="Password")
    username.configure(placeholder_text="Username")
    password.configure(placeholder_text="Password") 


#NOT WORKING -- REWORK  --- NVM LOGIN

def LI():
        global u
        global p
        u = username.get()
        p = password.get()
        ugd = open("usernam.txt", "r")
        pgd = open("passwor.txt", "r")
        uc = str(ugd.read())
        pc = str(pgd.read())
        print(uc)
        print(pc)
        if u == uc and p == pc:
            print("YES")
            t.messagebox.showinfo("", "Success")
            frame3.pack(padx=10, pady=50)
            frame2.pack_forget()
            username.delete(0, 'end')
            usernameS.delete(0, 'end')
            password.delete(0, 'end')
            passwordS.delete(0, 'end')     
        elif u == "" or p == "":
            t.messagebox.showerror("Error", "No Username or Password Detected")
        else: 
            t.messagebox.showerror("Error", "Username or Password Incorrect")
             

login = tk.CTkButton(master=frame, text="Go to Sign Up", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=SUP)
login.pack(side="left", padx=20)

sign = tk.CTkButton(master=frame, text="Login", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=LI)
sign.pack(side="right", padx=20)

#SIGN UP

frame2S = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame2S.configure(height=900, width=900)
frame2S.pack_forget()

t1S = tk.CTkLabel(master=frame2S, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
t1S.pack(padx=10, pady=10)

h1S = tk.CTkLabel(master=frame2S, text="Sign Up Page", fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center")
h1S.pack(padx=10, pady=10)

imagell = tk.CTkLabel(master=frame2S, image=img, text="")
imagell.pack(pady=20)

usernameS = tk.CTkEntry(master=frame2S, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=30, placeholder_text="Username", placeholder_text_color="Black")
usernameS.pack(padx=100, pady=60)

passwordS = tk.CTkEntry(master=frame2S, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=30, placeholder_text="Password", placeholder_text_color="Black")
passwordS.pack()

frameS = tk.CTkFrame(master=frame2S, width=200, height=200, fg_color="#ffffff")
frameS.pack(pady=75, padx=10)



#Sign Up Logic

def LP():
    #t.messagebox.showinfo("", "Changed Page")  
    frame2S.pack_forget()
    frame2.pack(padx=10, pady=50)
    usernameS.delete(0, 'end')
    passwordS.delete(0, 'end')
    username.delete(0, 'end')
    password.delete(0, 'end')

    usernameS.configure(placeholder_text="Username")
    passwordS.configure(placeholder_text="Password")
    username.configure(placeholder_text="Username")
    password.configure(placeholder_text="Password") 


def SU(): 
    global u
    global p
    u = usernameS.get()
    p = passwordS.get()
    if u and p != "":
        t.messagebox.showinfo("", "Login Created!")      
        un = open("usernam.txt", "w")
        pw = open("passwor.txt", "w")
        un.write(u)
        pw.write(p)
        print(u)
        print(p)
    else:  
        t.messagebox.showerror("Error", "No Username or Password Detected")
         
loginS = tk.CTkButton(master=frameS, text="Go to Login", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=LP)
loginS.pack(side="left", padx=20)

signS = tk.CTkButton(master=frameS, text="Sign Up", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=SU)
signS.pack(side="right", padx=20)

#Main

frame3 = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame3.configure(height=900, width=900)
frame3.pack_forget()



title_main = tk.CTkLabel(master=frame3, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
title_main.pack(padx=10, pady=10)

imagel = tk.CTkLabel(master=frame3, image=img, text="")
imagel.pack()

#header_main = tk.CTkLabel(master=frame3, text="#", fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center")
#header_main.pack(padx=10, pady=10)

spas = tk.CTkLabel(master=frame3, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="")
spas.pack(padx=10, pady=20)

def f():
    frame3.pack_forget()
    #frame2.pack_forget()
    frame5.pack(pady=20)

Find = tk.CTkButton(master=frame3, text="Identify Issues", font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, height=60, width=700, command=f)
Find.pack(padx=25, pady=20)


def List():
    global LSO
    global LST
    global RLSO
    global RLST
    global TIME_LIST
    global P_LIST
    LSO = open("dd.txt", "r")
    LST = open("dd2.txt", "r")
    RLSO = LSO.read()
    RLST = LST.read()
    RLSO = RLSO.splitlines()
    RLST = RLST.splitlines()
    TIME_LIST = RLST
    TIME_LIST = list(map(int, RLST))
    P_LIST = RLSO
    print(TIME_LIST)
    print(P_LIST)
    plt.xlabel("Problems")
    plt.ylabel("Time (Days)")

    plt.bar(P_LIST, TIME_LIST)
    plt.show()
    


Past = tk.CTkButton(master=frame3, text="Past Issues", font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, height=60, width=700, command=List)
Past.pack(padx=25, pady=20)

#Chat = tk.CTkButton(master=frame3, text="Chat", font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, height=60, width=700)
#Chat.pack(padx=25, pady=20)

#Sett = tk.CTkButton(master=frame3, text="Settings", font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, height=60, width=700)
#Sett.pack(padx=25, pady=20)

#Find - AGE AND GENDER

frame5 = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame5.pack_forget()

title_main = tk.CTkLabel(master=frame5, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
title_main.pack(pady=10)

imagell = tk.CTkLabel(master=frame5, image=img, text="")
imagell.pack(pady=20)

spas2 = tk.CTkLabel(master=frame5, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="", width=650, height=50)
spas2.pack(padx=10, pady=20)

al = tk.CTkLabel(master=frame5, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Age")
al.pack(pady=9)

age = tk.CTkEntry(master=frame5, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=30, placeholder_text="Age", placeholder_text_color="Black")
age.pack()

spas3 = tk.CTkLabel(master=frame5, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="")
spas3.pack(padx=10, pady=10)

gl = tk.CTkLabel(master=frame5, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Gender")
gl.pack(pady=9)

gender = tk.CTkComboBox(master=frame5, state="readonly", values=["Male", "Female", "Other"], fg_color="#008080", font=("Comic Sans MS", 20), corner_radius=10, width=500, height=30)
gender.pack()

#spas3 = tk.CTkLabel(master=frame5, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="")
#spas3.pack(padx=10, pady=20)

def next():
    global PROMPT
    global GENDER
    global AGE
    global AGER
    global GENDERR
    AGE = str(age.get())
    GENDER = str(gender.get())
    if AGE == "" or GENDER == "":
        print("Hi")
        AGE = ""
        GENDER = ""
        t.messagebox.showerror("Error", "Age or Gender values not present")       
    elif AGE.isdigit() == False:
        print("wrong")
        AGE = ""
        t.messagebox.showerror("Error", "Age value not correct (Use numbers only)")
    else:
        t.messagebox.showinfo("", "Success")
        GENDERR = ", Gender: " + GENDER
        AGER = "Age: " + AGE
        PROMPT = AGER + GENDERR
        print(PROMPT)
        frame5.pack_forget()
        frame7.pack(pady=20)
        

F1 = tk.CTkFrame(master=frame5, fg_color="#ffffff", height=900, width=900)
F1.pack(pady=25)

n1 = tk.CTkButton(master=F1, text="Next", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=next)
n1.pack(padx=10, side="right")

def B():
    frame5.pack_forget()
    frame3.pack(pady=20)
    age.delete(0, 'end')
    gender.set("")
    problems.delete("0.0", "end")
    pastproblems.delete("0.0", "end")
    years.delete(0, 'end')
    months.delete(0, 'end')
    days.delete(0, 'end')
    s.configure(text="")


b1 = tk.CTkButton(master=F1, text="Back", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=B)
b1.pack(padx=10, side="left")

#Find 2 - Problems

frame7 = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame7.pack_forget()

title_main2 = tk.CTkLabel(master=frame7, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
title_main2.pack(padx=10, pady=10)

imagell = tk.CTkLabel(master=frame7, image=img, text="")
imagell.pack(pady=20)

spas2 = tk.CTkLabel(master=frame7, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="", width=650, height=50)
spas2.pack(padx=10, pady=20)

pl = tk.CTkLabel(master=frame7, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Problems")
pl.pack(pady=10)

problems = tk.CTkTextbox(master=frame7, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=300)#, placeholder_text="Problems", placeholder_text_color="Black"
problems.pack()

def next2():
    global PROMPT
    global PROBLEMS
    global S
    PROBLEMS = problems.get("1.0", "end-1c")
    if PROBLEMS == "":
        PROBLEMS = ""
        t.messagebox.showerror("Error", "Problem(s) not present")
    else:
        PROBLEMS = problems.get("1.0", "end-1c")
        t.messagebox.showwarning("Warning", "Make sure to include a detailed explaination of what is wrong")
        t.messagebox.showinfo("Success", "Success")
        #PROBLEMS = problems.get("1.0", "end-1c")

        S = open("D.txt", "a")
        S.write(PROBLEMS + "\n")

        PROMPT = PROMPT + ", Problems: " + PROBLEMS
        print(PROMPT)
        frame7.pack_forget()
        frame8.pack(pady=30)


F2 = tk.CTkFrame(master=frame7, fg_color="#ffffff", height=900, width=900)
F2.pack(pady=10)

def B2():
    global PROMPT
    global GENDERR
    global AGER
    frame7.pack_forget()
    frame5.pack(pady=20)
    e = str(AGER) + str(GENDERR)
    PROMPT = PROMPT.replace(e, "")
    print(PROMPT)

b6 = tk.CTkButton(master=F2, text="Back", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=B2)
b6.pack(padx=10, side="left")

n4 = tk.CTkButton(master=F2, text="Next", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=next2)
n4.pack(padx=10)

#Find 3 - Past Problems

frame8 = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame8.pack_forget()

title_main = tk.CTkLabel(master=frame8, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
title_main.pack(padx=10, pady=10)

imagell = tk.CTkLabel(master=frame8, image=img, text="")
imagell.pack(pady=10)

spas2 = tk.CTkLabel(master=frame8, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="", width=650, height=50)
spas2.pack(padx=10)

ppl = tk.CTkLabel(master=frame8, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Past Problems")
ppl.pack(pady=10)

pastproblems = tk.CTkTextbox(master=frame8, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=300)#, placeholder_text="Problems", placeholder_text_color="Black"
pastproblems.pack()

def next3():
    global PROMPT
    global PAST_PROBLEMS
    PAST_PROBLEMS = pastproblems.get("1.0", "end-1c")
    if PAST_PROBLEMS == "":
        PAST_PROBLEMS = ""
        t.messagebox.showerror("Error", "No Past Problem(s) present")
    else:
        t.messagebox.showwarning("Warning", "Make sure to include a detailed explaination of what is wrong")
        t.messagebox.showinfo("Success", "Success")
        PAST_PROBLEMS = pastproblems.get("1.0", "end-1c")
        PROMPT = PROMPT + ", Past Problems: " + PAST_PROBLEMS
        print(PROMPT)
        frame8.pack_forget()
        frame9.pack(pady=30)


F3 = tk.CTkFrame(master=frame8, fg_color="#ffffff", height=900, width=900)
F3.pack(pady=20)

def B3():
    frame8.pack_forget()
    frame7.pack(pady=10)
    global PROBLEMS
    global PROMPT
    global PROBLEMSR
    PROBLEMSR = ", Problems: " + PROBLEMS
    PROMPT = PROMPT.replace(PROBLEMSR, "")
    print(PROMPT)

b3 = tk.CTkButton(master=F3, text="Back", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=B3)
b3.pack(padx=10, side="left")

n8 = tk.CTkButton(master=F3, text="Next", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=next3)
n8.pack(padx=10, side="right")

#Next 3 - Time

frame9 = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame9.pack_forget()

title_main = tk.CTkLabel(master=frame9, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
title_main.pack(padx=10, pady=10)

imagell = tk.CTkLabel(master=frame9, image=img, text="")
imagell.pack(pady=10)

spas2 = tk.CTkLabel(master=frame9, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Be patient when clicking next, it may take 2-3 minutes to load information.", width=650, height=50)
spas2.pack(padx=10, pady=20)

yl = tk.CTkLabel(master=frame9, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Years")
yl.pack(pady=10)

years = tk.CTkEntry(master=frame9, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=30, placeholder_text="Years", placeholder_text_color="Black")#, placeholder_text="Problems", placeholder_text_color="Black"
years.pack(pady=10)

ml = tk.CTkLabel(master=frame9, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Months")
ml.pack(pady=10)

months = tk.CTkEntry(master=frame9, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=30, placeholder_text="Months", placeholder_text_color="Black")#, placeholder_text="Problems", placeholder_text_color="Black"
months.pack(pady=10)

dl = tk.CTkLabel(master=frame9, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Days")
dl.pack(pady=10)

days = tk.CTkEntry(master=frame9, fg_color="#008080", font=("Comic Sans MS", 20), text_color="Black", corner_radius=10, width=500, height=30, placeholder_text="Days", placeholder_text_color="Black")#, placeholder_text="Problems", placeholder_text_color="Black"
days.pack(pady=10)

def next4():
    global YEARS
    global MONTHS
    global DAYS
    global Y
    global D
    global M
    global PROMPT
    global S2
    global SF
    YEARS = years.get()
    MONTHS = months.get()
    DAYS = days.get()
    if YEARS == "" or MONTHS == "" or DAYS == "":
        YEARS = ""
        MONTHS = ""
        DAYS = ""
        t.messagebox.showwarning("Error", "Years, Months, or Days not detected")
    elif YEARS.isdigit() == False or MONTHS.isdigit() == False or MONTHS.isdigit() == False:
        YEARS = ""
        MONTHS = ""
        DAYS = ""
        t.messagebox.showwarning("Error", "Years, Months, or Days needs to be in correct format(numbers only)")
    else:
        PROMPT = PROMPT + ", Years: " + YEARS + ", Months: " + MONTHS + ", Days: " + DAYS + ", Possible problems and treatment"
        print(PROMPT)
        Y = int(YEARS) * 365
        M = int(MONTHS) * 30
        D = int(DAYS)
        S2 = Y + M + D
        print(S2)
        
        SF = open("dd2.txt", "a")
        SF.write(str(S2) + "\n")

        #s.after(100, api)
        api()


F4 = tk.CTkFrame(master=frame9, fg_color="#ffffff", height=900, width=900)
F4.pack(pady=10)

def B4():
    frame9.pack_forget()
    frame8.pack(pady=10)
    global PAST_PROBLEMS
    global PROMPT
    global PAST_PROBLEMSR
    PAST_PROBLEMSR = ", Past Problems: " + PAST_PROBLEMS
    PROMPT = PROMPT.replace(PAST_PROBLEMSR, "")
    print(PROMPT)


    
b4 = tk.CTkButton(master=F4, text="Back", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=B4)
b4.pack(padx=10, side="left")


n9 = tk.CTkButton(master=F4, text="Next", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=next4)
n9.pack(padx=10, side="right")


#LOAD/ DOES NOT MATTER



frame92 = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame92.pack_forget()

title_main = tk.CTkLabel(master=frame92, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
title_main.pack(padx=10, pady=10)

imagell = tk.CTkLabel(master=frame92, image=img, text="")
imagell.pack(pady=10)

spas22 = tk.CTkLabel(master=frame92, fg_color="#ffffff", font=("Trebuchet MS", 20), text_color="Black", corner_radius=10, anchor="center", text="Be patient when clicking next, it may take 2-3 minutes to load information.", width=650, height=50)
spas22.pack(padx=10, pady=40)

l = tk.CTkLabel(master=frame92, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Loading")
l.pack(pady=10)

l2 = tk.CTkLabel(master=frame92, fg_color="#008080", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="Be Patient as we are looking at the information you have given us.")
l2.pack(pady=10)

spas2 = tk.CTkLabel(master=frame92, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="", width=650, height=50)
spas2.pack(padx=10, pady=40)

spas2 = tk.CTkLabel(master=frame92, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="", width=650, height=50)
spas2.pack(padx=10, pady=40)

spas2 = tk.CTkLabel(master=frame92, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="", width=650, height=50)
spas2.pack(padx=10, pady=40)

#ANSWER

frame10 = tk.CTkFrame(master=root, fg_color="#ffffff", height=900, width=900)
frame10.pack_forget()

title_main = tk.CTkLabel(master=frame10, text="Your WELLcome", fg_color="#008080", font=("Trebuchet MS", 60), text_color="Black", corner_radius=10, anchor="center")
title_main.pack(padx=10, pady=10)

imagell = tk.CTkLabel(master=frame10, image=img, text="")
imagell.pack(pady=10)

spas22 = tk.CTkLabel(master=frame10, fg_color="#ffffff", font=("Trebuchet MS", 30), text_color="Black", corner_radius=10, anchor="center", text="", width=650, height=50)
spas22.pack(padx=10)

def api():
        
        global YEARS
        global MONTHS
        global DAYS
        global PROMPT
        YEARS = years.get()
        MONTHS = months.get()
        DAYS = days.get()
        global ANSWER
        #t.messagebox.showinfo("Success", "Success")
        #frame9.pack_forget()
        #frame92.pack(pady=20)

        response = requests.post(
            "http://localhost:11434/api/generate",#
            json={
                "model": "llama2",
                "prompt": PROMPT,
                "max_tokens": 120,
                "stream": False
            }, timeout=1000
        )
        data = response.json()
        ANSWER = data.get("response", "No response")#


        print("", data.get("response", "No response"))

        ANSWER = ANSWER.replace("{", "").replace("}", "")

        #for i in ANSWER:
        #    if "{" or "}" in ANSWER:
        #        ANSWER[i]
        s.configure(text=ANSWER)
        #time.sleep(110)
        frame9.pack_forget()
        frame10.pack(pady=10)


def nextfinal():
    frame10.pack_forget()
    frame3.pack(pady=10)
    age.delete(0, 'end')
    gender.set("")
    problems.delete("0.0", "end")
    pastproblems.delete("0.0", "end")
    years.delete(0, 'end')
    months.delete(0, 'end')
    days.delete(0, 'end')
    s.configure(text="")

    #DS = open("D.txt", "w")
    #DS.write(PROBLEMS)
    #print(PROBLEMS)

s = tk.CTkLabel(master=frame10, fg_color="#008080", font=("Trebuchet MS", 10), text_color="Black", corner_radius=10, text="Answer", width=650, height=400)
s.pack(pady=10)

n10 = tk.CTkButton(master=frame10, text="Back To Home", width=100, height=50, corner_radius=10, font=("Lucida Console", 20), fg_color="#008090", hover=True, border_color="Blue", border_width=5, command=nextfinal)
n10.pack(pady=10)

root.mainloop()