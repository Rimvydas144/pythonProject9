import datetime

# print("---1.2---")

# filmas = {
#     "Pavadinimas": "Rojaus kampelis",
#     "Režisierius": "Arnold Dudo",
#     "Biudžetas": 200000,
#     "Uždirbo": 5000000,
#     "Žanras": "Komedija",
#     "Trukmė": 155,
#     "Išleidimo_metai": 2020,
#     "Aktoriai":{
#         "Aktorius1": "Zosė Zebrienė",
#         "Aktorius2": "Tomas Ruika",
#         "Aktorius3": "Adolfas Zuika",
#         "Aktorius4": "Simona Simonaitytė"
#     }
# }
# print(filmas)
# pelnas = filmas ["Uždirbo"] - filmas ["Biudžetas"]
# print(f' Filmo pelnas:', {pelnas})
# aktorių_kiekis = len(filmas["Aktoriai"])
# print(f" Filme dalyvavo {aktorių_kiekis} aktorių")
# dabartinė_data = datetime.date.today().year
# filmui_metų = dabartinė_data - filmas["Išleidimo_metai"]
# print(f"Filmui yra {filmui_metų} metų.")

# print("---1.8---")

# studentas1 = {
#     "Vardas": "Tomas",
#     "Pavardė": "Gudauskas",
#     "Studijų_programa": "Matematika",
#     "Pažymiai": [5,4,9,6,6]
# }
# studentas2 = {
#     "Vardas": "Romas",
#     "Pavardė": "Adomauskas",
#     "Studijų_programa": "Matematika",
#     "Pažymiai": [7,4,8,8,6]
# }
# print(studentas1)
# print(studentas2)
# Vidurkis1 = sum(studentas1 ["Pažymiai"]) / len(studentas1 ["Pažymiai"])
# print(Vidurkis1)
# Vidurkis2 = sum(studentas2 ["Pažymiai"]) / len(studentas2 ["Pažymiai"])
# print(Vidurkis2)
# if Vidurkis1 > Vidurkis2:
#     print(f' Studento {studentas1["Vardas"]} {studentas1["Pavardė"]} vidurkis didesnis')
# elif Vidurkis2 > Vidurkis1:
#     print(f' Studento {studentas2["Vardas"]} {studentas2["Pavardė"]} vidurkis didesnis')
# else:
#     print("Abiejų studentų vidurkiai vienodi")

# print("---1.14---")
# automobiliai = [
#     {
#         "Markė": "Audi",
#         "Modelis": "A4",
#         "Degalai": "Elektra",
#         "Pagaminimo_data":2023
#     },
#     {
#         "Markė": "Audi",
#         "Modelis": "A3",
#         "Degalai": "Dujos",
#         "Pagaminimo_data":2010
#     },
#     {
#         "Markė": "Audi",
#         "Modelis": "A6",
#         "Degalai": "Dyzelinas",
#         "Pagaminimo_data":2001
#     }
# ]
# dabartinė_data = datetime.date.today().year
# for automobilis in automobiliai:
#     automobiliui_metų = dabartinė_data - automobilis["Pagaminimo_data"]
#     print(f"Automobiliui {automobilis["Markė"]} {automobilis["Modelis"]} yra {automobiliui_metų} metų.")

# print("---1.18---")
# parduotuve = {
#     "Pavadinimas": "Kregždutė",
#     "Adresas": "Savanorių pr. 100, Klaipėda",
#     "Darbuotojų_kiekis": 11,
#     "Prekės":[
#         {
#         "Pavadinimas": "Pienas",
#         "Kodas": 20368,
#         "Kaina": 1.25,
#         "Savikaina": 0.50,
#         "Kiekis": 25
#         },
#         {
#         "Pavadinimas": "Duona",
#         "Kodas": 26668,
#         "Kaina": 1.05,
#         "Savikaina": 0.35,
#         "Kiekis": 41
#         },
#         {
#         "Pavadinimas": "Sviestas",
#         "Kodas": 32168,
#         "Kaina": 1.75,
#         "Savikaina": 0.99,
#         "Kiekis": 12
#         },
#         {
#         "Pavadinimas": "Grietinė",
#         "Kodas": 26118,
#         "Kaina": 1.45,
#         "Savikaina": 0.85,
#         "Kiekis": 22
#         },
#         {
#         "Pavadinimas": "Majonezas",
#         "Kodas": 26634,
#         "Kaina": 1.99,
#         "Savikaina": 1.35,
#         "Kiekis": 5
#         }
#     ]
# }
# Viso_prekių = sum(prekė["Kiekis"] for prekė in parduotuve["Prekės"])
# mažiausiai = parduotuve["Prekės"][0]
# daugiausiai = parduotuve["Prekės"][0]
# for preke in parduotuve ["Prekės"]:
#     if preke["Kiekis"] < mažiausiai["Kiekis"]:
#         mažiausiai = preke
#     if preke["Kiekis"] > daugiausiai["Kiekis"]:
#         daugiausiai = preke
# print("***PARDUOTUVĖ***\n", f' PAVADINIMAS: {parduotuve["Pavadinimas"]}, ADRESAS: {parduotuve["Adresas"]}, DARBUOTOJŲ SKAIČIUS: {parduotuve["Darbuotojų_kiekis"]}')
# print("Pirma prekė:\n", parduotuve["Prekės"][0]["Pavadinimas"], ",Kaina:", parduotuve["Prekės"][0]["Kaina"], ",Kiekis:", parduotuve["Prekės"][0]["Kiekis"])
# print("Antra prekė:\n", parduotuve["Prekės"][1]["Pavadinimas"], ",Kaina:", parduotuve["Prekės"][1]["Kaina"], ",Kiekis:", parduotuve["Prekės"][1]["Kiekis"])
# print("Trečia prekė:\n", parduotuve["Prekės"][2]["Pavadinimas"], ",Kaina:", parduotuve["Prekės"][2]["Kaina"], ",Kiekis:", parduotuve["Prekės"][2]["Kiekis"])
# print("Ketvirta prekė:\n", parduotuve["Prekės"][3]["Pavadinimas"], ",Kaina:", parduotuve["Prekės"][3]["Kaina"], ",Kiekis:", parduotuve["Prekės"][3]["Kiekis"])
# print("Penkta prekė:\n", parduotuve["Prekės"][4]["Pavadinimas"], ",Kaina:", parduotuve["Prekės"][4]["Kaina"], ",Kiekis:", parduotuve["Prekės"][4]["Kiekis"])
# print("Parduotuvėje prekių kiekis yra:", Viso_prekių)
# print(f'Mažiausiai prekių: {mažiausiai}')
# print(f'Daugiausia prekių: {daugiausiai}')

# print("---1.18---")
