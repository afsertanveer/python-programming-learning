customer = {
    "name": "Go",
    "age": 20,
    "is_verified": True
}
print(customer["age"])
print(customer.get("is_verified"))
print(customer.get("birthdate","Jan 1 1980"))
customer["name"] ="hello"
print(customer["name"])
print(customer)