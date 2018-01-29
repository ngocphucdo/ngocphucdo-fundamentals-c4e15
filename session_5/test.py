#person = ["Tuan Anh", 22, 2, "Ha Noi", "Moc Chau", 5, 4, "Maria", "ping pong"]

# person = {}
# print(person)
#
# person = {
#     #key : value
#     "name": "Tuan Anh"
# }
# print(person)

person = {
    "name": "Tuan Anh",
    "age" : 22,
    "sex": "male"
}
#duyet bang key
for key in person:
    print(key)
#Duyet bang value
for value in person.values():
    print(value)
#Duyet ca 2 cung 1 luc
for key, value in person.items():
    print(key, value)
