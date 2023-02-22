class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone

    def print_person(self):
        print("Customer Name: ", self.__name)
        print("Address: ", self.__address)
        print("Phone Number", self.__phone)


class Customer(Person):
    def __init__(self, name, address, phone, cust_num, on_list):
        Person.__init__(self, name, address, phone)

        self.__customer_number = cust_num
        self.__on_list = list

    def print_person(self):
        """
        print("Customer Name: ", self.__name)
        print("Address: ", self.__address)
        print("Phone Number", self.__phone)
        """
        Person.rint_person(self)
        print("Customer Number: ", self.__customer_number)
        if self.__on_list:
            print("On Mailing List: YES")
        else:
            print("On Mailing List: NO")

        print("Method 2")
        print(f"Name:  {Person.get_name(self)}")
        print(f"Address:  {Person.get_address(self)}")
        print(f"Phone:  {Person.get_phone_number(self)}")
        print(f"Customer Number:", self.__cust_num)
        if self.__on_list:
            print("On Mailing List: YES")
        else:
            print("On Mailing List: NO")
