from datetime import datetime


name = input("Enter Your Name : ")
#LISTS Of Items
lists = """
Rice    Rs  20/kg
Sugar   Rs  30/kg
salt    Rs  20/kg
oil     Rs  80/liter
paneer  Rs  110/kg
maggi   Rs  50/kg
boost   Rs  90/each
colgate Rs  85/each
"""
#print(lists)

#declaration
Price = 0
Price_List = []
Total_Price = 0
Final_Price = 0
I_List = []
Q_List = []
P_List = []

#rates for items(decionery formate)

items = {"rice": 20, 
         "sugar": 30,
         "salt": 20,
         "oil": 80,
         "paneer": 110, 
         "maggi": 50, 
         "boost": 90, 
         "colgate": 85}

option = int(input("for list of iteams press 1"))

if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("if you want to buy press 1 or 2 for exit: "))
    if inp1 == 2:
        break
    if inp1==1:
        item =input("Enter your items :")
        quantity = int(input("Enter quantity: "))
        if item in items.keys():
            price= quantity*(items[item])
            Price_List.append((item,quantity,items,price))
            Total_Price+=price
            I_List.append(item)
            Q_List.append(quantity)
            P_List.append(price)
            gst = (Total_Price*5)/100
            Final_Price =gst+Total_Price
        else:
            print("sorry you entered item is not availabe")
    else:
        print("You entered Wrong number")
    inp = input("can i bill the items yes or no: ")
    if inp=="yes":
        pass
        if Final_Price!=0:
            print(25* "=","super market",25*"=")
            print(28* "=","wanaparthy")
            print("Name:",name, 30*" ", "Date:", datetime.now())
            print(75*"-")
            print("sno", 8*" ", "items", 8* " ", "Quantity", 3*" ", "price" ) 
            for i in range(len(Price_List)):
                print(i, 4* " ",5* ' ', I_List[i],  10* " ", Q_List[i],  8* " ",  P_List[i] )
            print(75* "-")
            print(50* " ", "TotalAmount:", "Rs", Total_Price)
            print("gst amount", 50* " ", "Rs", gst)
            print(75*"-")
            print(50* " ", "FinalAmount:", "Rs", Final_Price)
            print(75*"-")
            print(25* " ", "Thanks For Visting")
            print(75*"-")


