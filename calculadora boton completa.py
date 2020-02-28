from tkinter import *
global c
global num,ope
ope=0
num=0
global A,B
N1=""
N2=""
c=0
def suma ():
    global num
    num=1
    global ope
    ope=0
 

    
def resta ():
    global num
    num=1
    global ope
    ope=1
    
def division ():
    global num
    num=1
    global ope
    ope=2
    
def multiplicacion ():
    global num
    num=1
    global ope
    ope=3
    



def igual():
    global N1,N2,c,num
    
    
    if(ope==0):
        c=float(N1)+float(N2)
        l=Label(ventana,text=c).grid(column=7,row=0)
        N1=str(c)
        N2=""
        num=1
        l=Label(ventana,text=" \t\t\t\t ").grid(column=0,row=0)
    if(ope==1):
        c=float(N1)-float(N2)
        l=Label(ventana,text=c).grid(column=7,row=0)
        N1=str(c)
        N2=""
        num=1
        l=Label(ventana,text=" \t\t\t\t ").grid(column=0,row=0)
        
    if(ope==3):
        c=float(N1)*float(N2)
        l=Label(ventana,text=c).grid(column=7,row=0)
        N1=str(c)
        N2=""
        num=1
        l=Label(ventana,text=" \t\t\t\t ").grid(column=0,row=0)
        
    if(ope==2):
       
        if(float(N2)!=0):
            c=float(N1)/float(N2)
            l=Label(ventana,text=c).grid(column=7,row=0)
            N1=str(c)
            N2=""
            num=1
            l=Label(ventana,text=" \t\t\t\t ").grid(column=0,row=0)
            
        else:
            l=Label(ventana,text="operacion incorrecta").grid(column=7,row=0) 
            N1=""
            l=Label(ventana,text=" \t\t\t\t ").grid(column=0,row=0)
def Reinicio ():
    global N1,N2,num
    N1=""
    N2=""
    ope=0
    num=0
    l=Label(ventana,text=" \t\t\t\t ").grid(column=0,row=0)
    l=Label(ventana,text=" \t\t\t\t ").grid(column=7,row=0)

    
def A ():
    global N1,N2,c
    if (num==0):
        N1=N1+"1"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"1"
        l=Label(ventana,text=N2).grid(column=0,row=0)
    
def B ():
    global N1,N2
    if (num==0):
        N1=N1+"2"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"2"
        l=Label(ventana,text=N2).grid(column=0,row=0)
def C ():
    global N1,N2
    if (num==0):
        N1=N1+"3"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"3"
        l=Label(ventana,text=N2).grid(column=0,row=0)
        B=3
def D ():
    global N1,N2
    if (num==0):
        N1=N1+"4"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"4"
        l=Label(ventana,text=N2).grid(column=0,row=0)
def E ():
    global N1,N2
    if (num==0):
        N1=N1+"5"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"5"
        l=Label(ventana,text=N2).grid(column=0,row=0)
def F ():
    global N1,N2
    if (num==0):
        N1=N1+"6"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"6"
        l=Label(ventana,text=N2).grid(column=0,row=0)
def G ():
    global N1,N2
    if (num==0):
        N1=N1+"7"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"7"
        l=Label(ventana,text=N2).grid(column=0,row=0)
def H():
    global N1,N2
    if (num==0):
        N1=N1+"8"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"8"
        l=Label(ventana,text=N2).grid(column=0,row=0)
def I():
    global N1,N2
    if (num==0):
        N1=N1+"9"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"9"
        l=Label(ventana,text=N2).grid(column=0,row=0)
def J():
    global N1,N2
    if (num==0):
        N1=N1+"0"
        l=Label(ventana,text=N1).grid(column=0,row=0)
    if (num==1):
        l=Label(ventana,text=N2).grid(column=0,row=0)
        N2=N2+"0"
        l=Label(ventana,text=N2).grid(column=0,row=0)



ventana=Tk()
l=Label(ventana,text=" \t\t\t\t ").grid(column=0,row=0)
l=Label(ventana,text=" \t\t\t\t ").grid(column=7,row=0)
B16=Button(ventana,text=0,command=J).grid(column=6,row=2)
B1=Button(ventana,text=1,command=A).grid(column=1,row=0)
B2=Button(ventana,text=2,command=B).grid(column=1,row=1)
B3=Button(ventana,text=3,command=C).grid(column=1,row=2)
B4=Button(ventana,text=4,command=D).grid(column=2,row=0)
B5=Button(ventana,text=5,command=E).grid(column=2,row=1)
B6=Button(ventana,text=6,command=F).grid(column=2,row=2)
B7=Button(ventana,text=7,command=G).grid(column=3,row=0)
B8=Button(ventana,text=8,command=H).grid(column=3,row=1)
B9=Button(ventana,text=9,command=I).grid(column=3,row=2)
B10=Button(ventana,text="+",command=suma).grid(column=4,row=0)
B11=Button(ventana,text="-",command=resta).grid(column=4,row=1)
B12=Button(ventana,text="/",command=division).grid(column=4,row=2)
B13=Button(ventana,text="x",command=multiplicacion).grid(column=5,row=0)
B14=Button(ventana,text="=",command=igual).grid(column=5,row=1)
B15=Button(ventana,text="REINICIO",command=Reinicio).grid(column=5,row=2)
ventana.mainloop()









