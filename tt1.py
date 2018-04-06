from PIL import Image#import biblijoteke
import os
import progressbar

datoteka=input("uneti mesto datoteke")#dobijam input od korisnika preko input() 
visina=input("visina")
duzina=input("duzina")
dimenzije=[int(visina),int(duzina)]# sacuvam dobijeni input u obliku liste i pretvaram ih u int 
fajl=True #dajem uslov za pravljenje fajla 

os.chdir(datoteka) #menjam radni folder 
print(os.getcwd())
for f in os.listdir():#pretrazujem folder za slike 
    if f.endswith(".jpg") or f.endswith(".png"): #akko se slike zavrsavaju sa jpg ili png
        for i in progressbar.progressbar(range(20)):
            if True == 0 :# pravim folder
                 os.mkdir("edited_images")
                 fajl =False    
            slika=Image.open(f)#ovde editujem slike
            fn,ftext=os.path.splitext(f)#uzimam ime slike 
            slika.thumbnail(dimenzije)#stavljam im dimenzije
            slika.save("edited_images/{}_rsz{}".format(fn, ftext))#cuvam ih u folder sa nastavkom _rsz
    
