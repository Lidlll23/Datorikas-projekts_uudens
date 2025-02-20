udens=float(input("Ievadi savu ikdienas ūdens patēriņu (litros):"))

udensD=udens
udensM=udens*30
udensG=udens*365
#Šeit arī varētu ielikt datu krātuvi (prioritāte)

print(f"Tu vidēji iztērē {udensD}l ūdens dienā, {udensM}l mēnesī un {udensG}l gadā.")

skd=int(input("Ivadi skolēnu skaitu:"))
skvid=float(input("Ivadi 1 skolēna vidējo saldūdens patēriņu 1 dienā:"))
#Optimizēšu/mainīšu 9. un 10. rindiņu (prioritāte)
#Varbūt šeit ielikšu datu krātuvi (prioritāte)

skvidG=skd*skvid*365

visud=37017300000000000000
#11-Python nespēj veikt aprēķinus ar šitik lieliem skaitļiem

patud=skvidG/visud*100
#Neesmu pārliecināta par šo procentu rēķināšanas metodi
#Kaut kas aprēķinos ir nepareizs (skat. #11-), ievadot mazāku skd un skvid, procentu skaits patud palielinās. (prioritāte, viss lielākā)

print(f"Tava klase vidēji gadā iztērē {patud}% no visām pasaules saldūdens krātuvēm!")

if patud<10:
    #Precizēšu pieļaujamos procentus vēlāk, pašlaiku paliks 10% (šī būs prioritāte pēc aprēķinu salabošanas)
    print("Jūs esat eko draudzīgi!")
else:
    print("Jūs neesat eko draudzīgi!")
    
izvele=input("Vai gribi izmantot programmu atkal? (jā/nē):")

while True:
    if izvele=="jā":
        udens=float(input("Ievadi savu ikdienas ūdens patēriņu (litros):"))

        udensD=udens
        udensM=udens*30
        udensG=udens*365

        print(f"Tu vidēji iztērē {udensD}l ūdens dienā, {udensM}l mēnesī un {udensG}l gadā.")

        skd=int(input("Ivadi skolēnu skaitu:"))
        skvid=float(input("Ivadi 1 skolēna vidējo saldūdens patēriņu 1 dienā:"))

        skvidG=skd*skvid*365

        visud=37017300000000000000

        patud=skvidG/visud*100

        print(f"Tava klase vidēji gadā iztērē {patud}% no visām pasaules saldūdens krātuvēm!")

        if patud>10:
            print("Jūs esat eko draudzīgi!")
        else:
            print("Jūs neesat eko draudzīgi!")

        izvele=input("Vai gribi izmantot programmu atkal? (jā/nē):")
    else:
        print("Paldies par programmas izmantošanu!")
        break
    #Ja atradīšu kā, tad optimizēšu šo ciklu (šī nav prioritāte)
 
#Uzlabosim tekstu (kopumā) (šī nav prioritāte)
#Vajag izmantot datu krātuves(google tutorials) (veseli 2 punkti, prioritāte)
