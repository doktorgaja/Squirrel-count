# # csv fajlovi su fajlovi koji sluze da budu informacije
# # u nekim excel projektima primer na weather_data
#
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
# # vadimo samo temperaturu iz weather_data
#
# # prvi primer je primer iscitavanja sadrzaja weather_data
# # u listi a donji primer je koriscenje csv biblioteke
# # pomocu metode reader koja nam dozvoljava da prodjemo
# # kroz sadrzaj fajla a pomocu for petlje smo iscitali svaki
# # objekat u tabelu u konzoli
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
# # pretvaranje u dictionary
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
#
# # ovako na primer ispisujemo samo temperaturu, samo
# # u zagradu stavimo ime kolone iz csv fajla koju zelimo da
# # ispisemo, pandas koristi prvi red kao ime reda ili kolone
# # pandas je biblioteka koja sluzi za citanje podataka poput txt, csv
# # takodje bolja je od klasicnih po izgledu koda i plus
# # po jednostavnosti i u konzoli izbacuje lepse poredjane podatke
# # ako sa type metodom iscitamo podatke zavisi kako ih citamo
# # ako ih sve iscitamo odjednom kao na liniji 29 to znaci da tretira celu tabelu kao podatak
# # ako iscitamo samo deo dakle ako navedemo kao na liniji 30 sa temp on tretira samo tu kolonu kao podatak
#
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# # average = sum(temp_list) / len(temp_list)
# # print(average) PRVI NACIN
#
# print(data["temp"].mean())
# # mean je ugradjena pandas metoda koja sluzi za racunanje prosecne vrednosti
# # DRUGI NACIN
#
# print(data["temp"].max())
# # dobijanje maksimalne vrednosti
#
# print(data["condition"])
# print(data.condition)
# # dva nacina pisanja
#
# # PISANJE REDOVA
#
# print(data[data.day == "Monday"])
# # ispisan je prvi red koji smo i trazili, preko provere
# # da u tom redu u koloni day ima Monday
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 9/5 + 32)
#
# # NAPRAVITI DATAFRAME
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# squirrel_count = {
#     "Fur color": ["Red", "Grey", "Black"],
#     "Count":
# }

import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

