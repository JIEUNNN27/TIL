#기타 자료형 - 자가진단6
# dcity = {
#     "Korea":"Seoul",
#     "Russia":"Moscow",
#     "USA":"Washington_D.C",
#     "Britain":"London",
#     "Germany":"Berlin"
# }

dcountry_city = {}


for i in range(int(input())):
    country, city = input().split()
    dcountry_city[country] = city

print(dcountry_city.get(input(),"Unknown Country"))