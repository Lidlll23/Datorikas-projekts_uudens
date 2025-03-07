print("Esi sveicināts! Šī programma aprēķina tavu un 9. klašu vidējo saldūdens patēriņu.")
print("Jūsu zināšanai, Latvijā viens cilvēks vidēji dienā patērē 100l saldūdens!")

udens=float(input("Ievadi savu vidējo saldūdens patēriņu 1 dienā(litros):"))

udensD=udens
udensM=udens*30
udensG=udens*365

print(f"Tu vidēji iztērē {udensD}l saldūdens dienā, {udensM}l mēnesī un {udensG}l gadā.")

skd=int(input("Ivadi 9. klašu skolēnu skaitu:"))
skvid=float(input("Ivadi 1 skolēna vidējo saldūdens patēriņu 1 dienā:"))

skvidG=skd*skvid*365

visud=3701730000
#Pilnais skaits ir 37017300000000000000m^3, bet, pēc testēšanas secināju, ka python programma sāk rādīt kļūdas, ja skaitlī ir vairāk par 10 cipariem.

patud=(skvidG/visud)*100
patud_r=round(patud,4)

#Neesmu pārliecināta par šo procentu rēķināšanas metodi.
#Kaut kas aprēķinos ir nepareizs, ievadot mazāku skd un skvid, procentu skaits patud palielinās.
#Aprēķinu problēma ir mainīgais visud (skaitlis ir pārāk liels).

print(f"Tava klase vidēji gadā iztērē {skvidG}l saldūdens, kas ir {patud_r}*10^-9% no visām pasaules saldūdens krātuvēm!")

if patud<0.048:
    print("Jūs esat eko draudzīgi!")
else:
    print("Jūs neesat eko draudzīgi!")
    
izvele=input("Vai gribi izmantot programmu atkal? (jā/nē):")

while True:
    if izvele=="jā":
        udens=float(input("Ievadi savu vidējo saldūdens patēriņu 1 dienā(litros):"))

        udensD=udens
        udensM=udens*30
        udensG=udens*365

        print(f"Tu vidēji iztērē {udensD}l saldūdens dienā, {udensM}l mēnesī un {udensG}l gadā.")

        skd=int(input("Ivadi 9. klašu skolēnu skaitu:"))
        skvid=float(input("Ivadi 1 skolēna vidējo saldūdens patēriņu 1 dienā:"))

        skvidG=skd*skvid*365
        visud=3701730000
        patud=(skvidG/visud)*100
        patud_r=round(patud,4)

        print(f"Tava klase vidēji gadā iztērē {skvidG}l saldūdens, kas ir {patud_r}*10^-9% no visām pasaules saldūdens krātuvēm!")

        if patud<0.048:
            print("Jūs esat eko draudzīgi!")
        else:
            print("Jūs neesat eko draudzīgi!")

        izvele=input("Vai gribi izmantot programmu atkal? (jā/nē):")
    else:
        print("Paldies par programmas izmantošanu!")
        break
