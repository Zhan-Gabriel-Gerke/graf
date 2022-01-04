from tkinter import *
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
    text=txt.get()#From Entry to text
    lbl.configure(text=text_to_lbl)
    txt.delete(0,END)
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("400x300")
nupp=Button(aken,text="Mina olen nupp\nValjutama mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_minus)
lbl=Label(aken,text="...",font="Arial 20",fg="green",bg="lightblue",height=4,width=20,relief=GROOVE)
txt=Entry(aken,text="...",font="Arial 20",fg="blue",bg="lightblue",width=20,relief=GROOVE, justify=CENTER)
txt

lbl.pack()
nupp.pack(side=LEFT)#side=LEFT,TOP,RIGHT
txt.pack()
aken.mainloop()
