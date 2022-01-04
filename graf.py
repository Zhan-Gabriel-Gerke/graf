from tkinter import*
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
def txt_to_lbl(event):
    #pass
    text_to_lbl=txt.get()#From Entry to text
    lbl.configure(text=text_to_lbl)
    txt.delete(0,END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_)
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("400x600")
nupp=Button(aken,text="Mina olen nupp\nValjutada mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)
#RAISED,SUNKEN,
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_minus)
bupp=Button(aken,text="Я кнопка",font="Arial 20",fg="green",bg="lightblue",height=4,width=20,relief=GROOVE)
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="lightblue",relief=GROOVE)
txt=Entry(aken,width=20,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)#Enter
i1=PhotoImage(file="gif.gif")
i2=PhotoImage(file="gif2.gif")
i3=PhotoImage(file="papii4.gif")
i4=PhotoImage(file="tomas.gif")
var=StringVar()
var.set(1)
r1=Radiobutton(aken,image=i1,variable=var,value="Üks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm",command=valik)
r4=Radiobutton(aken,image=i4,variable=var,value="Neli",command=valik)
bupp.pack()
lbl.pack()
nupp.pack()#side=LEFT,TOP,RIGHT
txt.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
r4.pack(side=TOP)
aken.mainloop()