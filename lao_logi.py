from tkinter import *
import datetime
import os



#Loome akna ja selle seaded
aken = Tk()
aken.title("Lao Logi")
aken.geometry("600x230")
aken.resizable(0,0)

ripp = 0

x = datetime.datetime.now()
kuu = (x.strftime("%Y")+"."+ x.strftime("%m"))
kuupäev = (x.strftime("%Y")+"."+ x.strftime("%m")+"."+ x.strftime("%d"))
kell = (x.strftime("%H")+':'+x.strftime("%M"))


#saame kausta asukoha
dir = os.path.dirname(os.path.realpath(__file__))
 

#mis juhtub kui toimub kasutaja salvestamine
def Salvesta():
    Kasutaja = sisestus.get()
    with open('kasutajad.txt', 'a') as fail:
        fail.write(str(Kasutaja)+'\n')
# #värskendab nimekirja
# #bug olemasolevate kasutajate kontroll puudub
    with open('kasutajad.txt', 'r') as fail:
        kasutajad = []
        for rida in fail:
            rida = rida.strip()
            kasutajad.append(rida)
    
    ripp_väärtus = StringVar(aken)
    ripp_väärtus.set("Valik") # default value

    w = OptionMenu(aken, ripp_väärtus, *kasutajad, command=ripp_muutus)
    w.grid(row=1, column=1)
    
# Varaga seotud tegevuse salvestamine Sotud kasutajaga +kausta ja faili loomine
def V_salvesta():
       
    if not os.path.exists(kuu):
        os.mkdir(kuu)
        print("Directory " , kuu ,  " Created ")
    else:    
        print("Directory " , kuu ,  " already exists")
    
    filename = os.path.join(dir, kuu, kuupäev+'.txt')
    
    #logi kirje sisestamine
    with open(filename, 'a') as fail:
        inv_nr = sisestus2.get() #võtab inventari väljalt sisestatud väärtuse
        Suund = rbValue.get() #varaga seotud tegevuse suund

        fail.write(str(kuupäev)+','+str(kell)+','+str(ripp)+','+str(inv_nr)+','+str(Suund)+'\n')

        #Kuvan viimase sisestuse
        #tulevikus mõistlik muuta selliselt et loeks failist.
        viimane_kirje = Label(aken, text="Viimane sisestus", width=20, font="Tahoma 12")
        viimane_kirje.grid(row=4, columnspan=4)
        #        viimane_kirje_sisu1 = Label(aken, "Kuupäev    Kell  Kasutaja   Inv_nr.   Suund", width=70, font="Tahoma 12")
        #        viimane_kirje_sisu1.grid(row=5, column=1)
        if Suund == 0:
            suund2 = str('sisse')
        else:
            suund2= str('välja')
        viimane_kirje_sisu = Label(aken, text=str(kuupäev)+','+str(kell)+','+str(ripp)+','+str(inv_nr)+','+suund2, font="Tahoma 12")
        viimane_kirje_sisu.grid(row=6, columnspan=4)
        
        #logi asukoht
        logifail = Label(aken,text=str(filename), font="Tahoma 12")
        logifail.grid(row=7, columnspan=4)
      
        
    
    
    #kasutaja nime valiku kajastamine globaalses muutujas
def ripp_muutus(selection):
    global ripp
    ripp = str(selection)
    Button(aken, text="Salvesta", width=10, font="Tahoma 12", command=V_salvesta).grid(row=3, column=2, padx=2, pady=2)
    
    

  #Olemas olevate kasutajate valimise list
tekstikast = Label(aken, text="Valitud Kasutaja:", width=20, font="Tahoma 12")
tekstikast.grid(row=1, column=0)
# 
filepath = os.path.join(dir,'kasutajad.txt')
if not os.path.isfile(filepath):
    with open('kasutajad.txt', 'w') as fail:
        fail.write("tühi"+'\n')
with open('kasutajad.txt', 'r') as fail:
    kasutajad = []
    for rida in fail:
        rida = rida.strip()
        kasutajad.append(rida)

ripp_väärtus = StringVar(aken)
ripp_väärtus.set("Valik") # default value
w = OptionMenu(aken, ripp_väärtus, *kasutajad, command=ripp_muutus)
w.grid(row=1, column=1)

invNR = Entry(aken, width=20, font="Tahoma 12")
invNR.grid(row=0, column=1)

#radio button - vara sisse või välja
tekstikast = Label(aken, text="Vara suund:", width=20, font="Tahoma 12")
tekstikast.grid(row=2, column=0)
rbValue=IntVar()
vk1 = Radiobutton(aken, text="Sisse",variable=rbValue, value=0)
vk1.grid(row=2, column=1)
vk2 = Radiobutton(aken, text="Välja", variable=rbValue, value=1)
vk2.grid(row=2, column=2)

#inventari nr + sisestusvorm
tekstikast2 = Label(aken, text="Inventari nr:", width=20, font="Tahoma 12")
tekstikast2.grid(row=3, column=0)

sisestus2 = Entry(aken, width=20, font="Tahoma 12")
sisestus2.grid(row=3, column=1)

tekstikast = Label(aken, text="Kasutaja?", width=20, font="Tahoma 12")
tekstikast.grid(row=3, column=2)

#Kasutaja nime sisestusväli koos salvestus nupuga
tekstikast = Label(aken, text="Kasutaja sisestus:", width=20, font="Tahoma 12")
tekstikast.grid(row=0, column=0)

sisestus = Entry(aken, width=20, font="Tahoma 12")
sisestus.grid(row=0, column=1)
   
Button(aken, text="Salvesta", width=10, font="Tahoma 12", command=Salvesta).grid(row=0, column=2, padx=2, pady=2)


aken.mainloop()