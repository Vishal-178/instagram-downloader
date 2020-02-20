import tkinter as t
import requests
import bs4
import os 
root=t.Tk()
root.configure(background='light blue')
root.title('Registration_page')  
root.geometry('500x500') 
root.resizable(width=True, height=True)

root.title('InstaSave')


t1=t.Label(root,text="Download Link:",font=(10),bg='light blue')
t1.place(x=40,y=100)

global ue1
ue1=t.Entry(root,width=40)
ue1.place(x=200,y=105)



def boo():
    uname=str(ue1.get())
    play22 = requests.get(f'{uname}')
    plo = play22.text
    meta = bs4.BeautifulSoup(plo)
    meta1 = meta.select('head')
    j = meta1[0].findChildren('meta')
    v = len(j)
    for me in range(v):
        ram = j[me].get('property')
        if ram == 'og:image':
            YouAreHero = j[me].get('content')
    play = requests.get(YouAreHero)
    play.raise_for_status()
    jh = next(os.walk("C:\\Users\\vishal\\vishal\\book\\instagram image saver\\insta image"))[2]
    l = len(jh)
    print(l)
    count = 0
    for bob in range(l):
        kko = f'nm{bob}.jpeg'
        kko1= jh[bob]
        if kko == kko1:
            count +=1
        else:
            print('bob2')
    plimg = open(f'C:\\Users\\vishal\\vishal\\book\\instagram image saver\\insta image\\nm{count}.jpeg','wb')
    for chun in play.iter_content(1000):
    #------------.iter_content(10000)-------------
        plimg.write(chun)
    plimg.close()

sb1=t.Button(root,text="DOWNLOAD",font=("bold",10),width=(15),bg="light blue",command=boo)
sb1.place(x=200,y=200)
             
root.mainloop() 