sõne="Programmerimine"
print(sõne)
list_sõne=list(sõne)
print(list_sõne)
print(f"Viies täht: {list_sõne[4]}")
print(f"Sõnes on {len(sõne)} t")
elemendid=[]
for i in range(5):
    elemendid.append(input(f"{i+1}. elememt: "))
print(elemendid)
for e in elemendid:
    print(e)



#extend
list_sõne.extend(elemendid)
print(list_sõne)
print(elemendid)

#insert
elemendid.insert(0,"A")
print(elemendid)

#remove
elemendid.remove("A")
print(elemendid)

#pop
elemendid.pop(0)
elemendid.pop()
print(elemendid)

#index
ind=list_sõne.index("r")
print(f"Täht r on {ind}-indeksiga")

#count
k=list_sõne.count("r")
print(f"Täht r kohtume {k} korde sõnes {sõne}")

#sort
list_sõne.sort(reverse=True)
print(list_sõne)

#reverse
list_sõne.reverse()
print(list_sõne)

#copy
list_sõne2=list_sõne.copy()

#clear
list_sõne2.clear()
print(list_sõne2)

#Töö 4.4

#Ül 1
from operator import index
from string import *
vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
konsonanti=["z","x","c","v","b","n","m","l","k","h","g","f","d","s","w","r","t","p"]
numbrid=digits
märkid=punctuation
v=k=n=m=t=0
tekst=input("Sisend (sõna või lause): ").lower()
tekst_list=list(tekst)
if tekst_list.index(" ")>0:
    print("See on lause")
    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1
        elif s in numbrid:
            n+=1
        elif s in märkid:
            t+=1
    print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")
else:
    print(f"Kokku on {len(tekst_list)}")

#Ül 2
#2.1
nimed=[]
for i in range(5):
    nimi=input(f"Sisesta {i+1}. nimi: ")
    nimed.append(nimi)
nimed.sort()
print("Nimed tähestikulises järjekorras:", nimed)
print("Viimati lisatud nimi:", nimed[-1])
index=int(input("Sisesta muudetava nime järjekorranumber (1-5): ")) - 1
if 0<=index<5:
    uus_nimi=input("Sisesta uus nimi: ")
    nimed.index=uus_nimi
    print("Uuendatud nimed:",sorted(nimed))
else:
    print("Vale indeks!")

#2.2
opilased=["Milana","Denis","Katya","Katya","Mark","Mark"]
unikaalsed_opilased=list(set(opilased))
print("Nimed ilma kordusteta: ",unikaalsed_opilased)

#2.3
vanused=[23,12,40,5,67,52]
min_vanus=min(vanused)
max_vanus=max(vanused)
summa=sum(vanused)
keskmine=summa/len(vanused)
print(f"Väikseim vanus: {min_vanus}")
print(f"Suurim vanus: {max_vanus}")
print(f"Vanuste kogusumma: {summa}")
print(f"Keskmine vanus: {round(keskmine,2)}")


#Ül 3
arvud=[18,19,32,37,48,12]
for arv in arvud:
    print('*'*arv)

#Ül 6
#список
list=[10,5,3,7,2]

if len(list)>0:
    max_num=max(list)
    max_index=list.index(max_num)
    resultaat=max_num/len(list)
    list[max_index]=resultaat

print("Tulemus:", list)

#Ül 7
n=int(input("Sisestage numbrite arv: "))
numbers=[]
for i in range(n):
    num=int(input(f"Sisestage {i+1}. number: "))
    numbers.append(num)
tellimus=input("Kas soovite sorteerida kasvavas (k) või kahanevas (d) järjekorras? ").lower()
if tellimus=="k":
    numbers.sort(key=abs)
elif tellimus=="d":
    numbers.sort(key=abs, reverse=True)
else:
    print("Vigane sisend!")
    numbers=[]
print("Sorteeritud nimekiri:", numbers)


#ül 8
#списки
lists=[
    ["крот","белка","выхухоль"],
    ["а","aa","aaa","aaaa","aaaaa"],
    ["qweasdqweas","q","rteww","ewqqqqq"]
]
for list in lists:
    max_pikkus=max(len(item) for item in list)
    resultaat=[item.ljust(max_pikkus, "_") for item in list]
    print(resultaat)

