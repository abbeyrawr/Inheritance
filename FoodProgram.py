import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0

cust_id = 570
nm = "Danni Sellyar"
add = "97 Mitchell Way Hewitt Texas 76712"
email = "dsellyarft@gmpg.org"
phone = "254-555-9362"
mem_stat = False

"""
cust_id = 569
nm = "Aubree Himsworth"
add = "1172 Moulton Hill Waco Texas 76710"
email = "ahimsworthfs@list-manage.com"
phone = "254-555-2273"
mem_stat = True

"""
info = fc.Customer(cust_id, nm, add, email, phone, mem_stat)

if cust_id == 569:
    print("Customer Name: ", info.get_name())
    print("Phone: ", info.get_phone())
    cust_id = 570

else:
    print("Customer Name: ", info.get_name())
    print("Phone: ", info.get_phone())
    cust_id = 569

for x in dict:
    date = dict[x][0]
    item_nm = dict[x][1]
    cost = dict[x][2]
    cust_id = dict[x][3]
    tran = fc.Transaction(date, item_nm, cost, cust_id)
    if tran.get_cust_id() == info.get_cust_id():
        order_total += tran.get_cost()
        print(
            "Order Item: ",
            tran.get_item_nm(),
            "  ",
            "Price: $",
            format(tran.get_cost(), ".2f"),
            sep="",
        )

print("Total Cost: $", format(order_total, ".2f"), sep="")

if info.get_status() == True:
    dis = 0.2 * order_total
    grand_total = order_total - dis
    print("Membern Discount: $", format(dis, ".2f"), sep="")
    print("Total Cost after discount: $", format(grand_total, ".2f"), sep="")
