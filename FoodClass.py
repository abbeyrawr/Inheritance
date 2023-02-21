class Customer:
    def __init__(self, cust_id, nm, add, email, phone, mem_stat):
        self.__name = nm
        self.__customerid = cust_id
        self.__address = add
        self.__email = email
        self.__phone = phone
        self.__member_status = mem_stat

    def get_name(self):
        return self.__name

    def get_cust_id(self):
        return self.__customerid

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_status(self):
        return self.__member_status


class Transaction:
    def __init__(self, date, item_nm, cost, cust_id):
        self.__date = date
        self.__item_number = item_nm
        self.__item_cost = cost
        self.__customer_id = cust_id

    def getdate(self):
        return self.__date

    def get_item_nm(self):
        return self.__item_number

    def get_cost(self):
        return self.__item_cost

    def get_cust_id(self):
        return self.__customer_id
