udens=float(input("Ievadi savu ikdienas ūdens patēriņu (litros):"))

udensD=udens
udensM=udens*30
udensG=udens*365

print(f"Tu vidēji iztērē {udensD}l ūdens dienā, {udensM}l mēnesī un {udensG}l gadā.")

skd=int(input("Ivadi skolēnu skaitu:"))
skvid=float(input("Ivadi 1 skolēna vidējo saldūdens patēriņu 1 dienā:"))
#Optimizēšu/mainīšu 9. un 10. rindiņu 

skvidG=skd*skvid*365

visud=37017300000000000000

patud=skvidG/visud*100
#Neesmu pārliecināta par šo procentu rēķināšanas metodi

print(f"Tava klase vidēji gadā iztērē {patud}% no visām pasaules saldūdens krātuvēm!")

if patud<10:
    #Precizēšu pieļaujamos procentus vēlāk. (pašlaiku paliks 10%)
    print("Jūs esat eko draudzīgi!")
else:
    print("Jūs neesat eko draudzīgi!")

#Uzlabosim tekstu (kopumā)