from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import asksaveasfilename
from threading import Thread

def managerere():
    root.update()
    if val.get()==1:
        val2.set(0)
        val3.set(0)

    elif val2.get()==1:
        val.set(0)
        val3.set(0)
    elif val3.get()==1:
        val.set(0)
        val2.set(0)
    else:
        pass
    if val4.get()==1:
        val5.set(0)
    elif val5==1:
        val4.set(0)
def func():
    root.update()
    randomemail()
    if val.get()==1:
        val2.set(0)
        val3.set(0)

    elif val2.get()==1:
        val.set(0)
        val3.set(0)
    elif val3.get()==1:
        val.set(0)
        val2.set(0)
    else:
        pass
    if val4.get()==1:
        val5.set(0)
    elif val5==1:
        val4.set(0)



def manager():

    keywordsec()

    if val.get()==1:
        val2.set(0)
        val3.set(0)

    elif val2.get()==1:
        val.set(0)
        val3.set(0)
    elif val3.get()==1:
        val.set(0)
        val2.set(0)
    else:
        pass


def managerer():
    root.update()
    numbers()
    if val.get()==1:
        val2.set(0)
        val3.set(0)

    elif val2.get()==1:
        val.set(0)
        val3.set(0)
    elif val3.get()==1:
        val.set(0)
        val2.set(0)
    else:
        pass
    if val4.get()==1:
        val5.set(0)
    elif val5==1:
        val4.set(0)
    para=True

para=True
list=[]

def numbers():
    global list
    list=[]
    from random import randint
    for io in range(10000):
        a=randint(7,9)
        b=randint(6,9)
        c=randint(1,9)
        d=randint(1,9)
        e=randint(1,9)
        f=randint(1,9)
        g=randint(1,9)
        h=randint(1,9)
        ij=randint(1,9)
        k=randint(1,9)
        pr=f"+91{a}{b}{c}{d}{e}{f}{g}{h}{ij}{k}\n"
        list.append(pr)
    global para
    para=False

key=Thread()
def keyword():
    list=[]
    import re
    import requests
    value=0
    stop=0
    key=val7.get()
    while True:
        stop=stop+1
        value=value+10
        qc=requests.get(f"https://www.google.com/search?q=site:+%22facebook.com%22+%22{key}%22+%22%40gmail.com%22&ei=IKmGX5uoMvmc4-EP_o6mgA8&start={value}&sa=N&ved=2ahUKEwibuMSRyLPsAhV5zjgGHX6HCfAQ8tMDegQIBBAv&biw=1360&bih=654")
        qc2=requests.get(f"https://www.google.com/search?q=site:+%22google%22+%22{key}%22+%22%40gmail.com%22+%22%40yaaho.com%22&ei=mPyLX-y9CYzt9QOqwqewDA&start={value}&sa=N&ved=2ahUKEwjs6aK43L3sAhWMdn0KHSrhCcYQ8tMDegQIBRAv&biw=1360&bih=654")
        qc3=requests.get(f"https://www.google.com/search?q=site:+%22in.linkedin.com%22+%22{key}%22+%22%40gmail.com%22&ei=Uf6LX6SYNNOZmgfFmIm4CQ&start={value}&sa=N&ved=2ahUKEwjkhPKK3r3sAhXTjOYKHUVMApcQ8tMDegQIBBAv&biw=1360&bih=654")
        my_str=qc.text
        my_str2=qc2.text
        my_str3=qc3.text
        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)
        emails2 = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str2)
        emails3 = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str3)
        for mail in emails:
            list.append(f"{mail}\n")
        for mail2 in emails2:
            list.append(f"{mail2}\n")

        for mail3 in emails3:
            list.append(f"{mail3}\n")

        if stop==10:
            msg._show("Completed", "Done!")
            break
key.start()

#this code is writeen by tanay mishra instagram : tanay_mishra

def randomemail():
    global para
    global list
    list=[]
    import random
    # import string
    import names
    a=["male","female"]
    b=["gmail.com","yahho.com","outlook.com"]
    op=0
    while True:
        op=op+1
        numc=f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
        cbs=names.get_full_name(gender=random.choice(a))
        mcq=random.choice(b)
        cb=cbs.split(" ")
        fname=cb[0]
        lname=cb[1]
        vsc=f"{fname}{lname}"
        if mcq=="yahho.com":
            list.append(f"{vsc}{random.randint(1,9)}@{mcq}\n")
        elif mcq=="gmail.com":
            list.append(f"{vsc}{numc}@{mcq}\n")
        else:
            list.append(f"{vsc}{random.randint(1, 9)}@{mcq}\n")
        if op == 500:
            break
    para=False

# randomemail()
def keywordsec():
    msg._show("Enter Keywords","Please enter Keyword like a doctor,Electricians etc.")



#this code is writeen by tanay mishra instagram : tanay_mishra

def saveFile():
    global para
    global list
    global file
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[
                                       ("Text Documents", "*.txt")])
    if para==False:
        f = open(file, "w")
        for writer in list:
            #Save as a new file
            print(writer)
            f.write(writer)
        f.close()
        msg._show("Completed.", 'Completed!')
    else:
        keyword()
        f = open(file, "w")
        for writer in list:
            # Save as a new file
            print(writer)
            f.write(writer)
        f.close()


# file=None


#This code is writteen by tanay mishra
root=Tk()
root.configure(bg="RoyalBlue",borderwidth=10,relief=SUNKEN)
root.geometry("340x280")
root.title("Scarper")
root.minsize(340,280)
root.maxsize(340,280)
Label(text = "BulkZ Tools",bg="sky blue",fg="blue",padx=800,font="lucida 15 bold",borderwidth=3,relief=SOLID).pack(padx=5,pady=5)
fr=Frame(root,bg="royalblue")
fr.pack(anchor="w",padx=9,pady=5)
val=IntVar()
val2=IntVar()
val3=IntVar()
val4=IntVar()
val5=IntVar()
val6=StringVar()
val7=StringVar()
gt=StringVar()
val6.set("Not Started")
val7.set("doctors")
#this code is writeen by tanay mishra instagram : tanay_mishra

Checkbutton(fr,text="Phone numbers",variable=val,bg="skyblue",padx=4,pady=4,relief=RIDGE,command=managerer).pack(side="left",padx=0)
Checkbutton(fr,text="Keyword E-mail scarp",variable=val2,bg="skyblue",padx=4,pady=4,relief=RIDGE,command=manager).pack(side="right",padx=20)
f2=Frame(root,bg="royalblue")
Checkbutton(f2,text="Public E-mails",variable=val3,bg="skyblue",padx=4,pady=4,relief=RIDGE,command=func).pack(side="left",padx=0)
Entry(f2,textvariable=val7,bg="skyblue",relief=RIDGE,font="luida 12 bold ").pack(side="right",padx=20)
f2.pack(anchor="w",padx=9,pady=5)

Label(root,text="Save file",bg="skyblue3",fg="blue",padx=900,font="lucida 15 bold",borderwidth=3,relief=SOLID).pack(padx=5,pady=5)
f3=Frame(root,bg="royalblue")
# Checkbutton(f3,text="CSV",variable=val4,bg="skyblue",padx=4,pady=4,relief=RIDGE,command=managerere).pack(side="left",padx=50)
Button(text="Genrate",bg="skyblue",relief=SUNKEN,font="Helvetica 10 bold",command=saveFile).pack()
# Checkbutton(f3,text="TXT",variable=val5,bg="skyblue",padx=4,pady=4,relief=RIDGE,command=managerere).pack(side="left",padx=50)
f3.pack()
f4=Frame(root,bg="royalblue4").pack()
# Label(f4,bg="skyblue",relief=RIDGE,text=f"Scarped items :{val6.get()} ").pack(anchor="w",padx=20,pady=5)
# root.wm_iconbitmap('mylogo.ico')
root.title("BulkZ Tools - Developer : Tanay mishra")
root.mainloop()