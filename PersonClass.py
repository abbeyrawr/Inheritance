class Person:
    def __init__(self, nm, add, num):
        self.__name = nm
        self.__address = add
        self.__phone = num

    def print_person(self):
        print("Customer Name: ", self.__name)
        print("Address: ", self.__address)
        print("Phone Number", self.__phone)


class Customer(Person):
    def __init__(self, cust_num, mail):
        self.__customer_number = cust_num
        self.__mailing_list = mail

    def print_person(self):
        print("Customer Number: ", self.__customer_number)
        print("Mailing Preference: ", self.__mailing_list)


"""
     def get_nm(self):
        return self.__nm

     def get_add(self):
        return self.__add

     def get_num(self):
        return self.__num

"""
