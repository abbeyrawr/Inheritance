import PersonClass as p

name = "John"
address = "1234 Main St"
phone = 1234
cust_nm = 1234
on_list = True


person1 = p.Person(name, address, phone)

customer1 = p.Customer(name, address, phone, cust_nm, on_list)

person1.print_person()

print()
print()
print()

customer1.print_person()
