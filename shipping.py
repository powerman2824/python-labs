print("--Hello and Welcome to Joe's Freight Depot\n--Where we take care of all your Freight Needs")
print("--Please choose from the following\n--Help us deliver your Freight on Time")
cust_input_ship_method = input("--Please select a shippment method\n--Ground = 1\n--Ground Premium = 2\n--Drone = 3\n-->")
cust_input_pack_weight = input("--Please enter the weight of your package\n-->")
global cust_ship_cost

if int(cust_input_ship_method) == 1:
    Ground_Shipping_Weight_of_Package = int(cust_input_pack_weight)
    Ground_Shipping_Price_per_Pound = ""
    if Ground_Shipping_Weight_of_Package <= 2:
        Ground_Shipping_Price_per_Pound = 1.50
        Ground_Shipping_Flat_Charge = 20
        cust_ship_cost = Ground_Shipping_Weight_of_Package * Ground_Shipping_Price_per_Pound + Ground_Shipping_Flat_Charge
        print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
    elif Ground_Shipping_Weight_of_Package > 2 or Ground_Shipping_Weight_of_Package <= 6:
        Ground_Shipping_Price_per_Pound = 3
        Ground_Shipping_Flat_Charge = 20
        cust_ship_cost = Ground_Shipping_Weight_of_Package * Ground_Shipping_Price_per_Pound + Ground_Shipping_Flat_Charge
        print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
    elif Ground_Shipping_Weight_of_Package > 6 or Ground_Shipping_Weight_of_Package <= 10:
        Ground_Shipping_Price_per_Pound = 4
        Ground_Shipping_Flat_Charge = 20
        cust_ship_cost = Ground_Shipping_Weight_of_Package * Ground_Shipping_Price_per_Pound + Ground_Shipping_Flat_Charge
        print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
    elif Ground_Shipping_Weight_of_Package > 10:
        Ground_Shipping_Price_per_Pound = 4.75
        Ground_Shipping_Flat_Charge = 20
        cust_ship_cost = Ground_Shipping_Weight_of_Package * Ground_Shipping_Price_per_Pound + Ground_Shipping_Flat_Charge
        print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
elif int(cust_input_ship_method) == 2:
    Ground_Shipping_Premium_Flat_Charge = 125
    cust_ship_cost = Ground_Shipping_Premium_Flat_Charge
    print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
elif int(cust_input_ship_method) == 3:
    Drone_Shipping_Weight_of_Package = int(cust_input_pack_weight)
    Drone_Shipping__Price_per_Pound = ""
    if Drone_Shipping_Weight_of_Package <= 2:
        Drone_Shipping__Price_per_Pound = 4.50
        Drone_Shipping__Flat_Charge = 0
        cust_ship_cost = Drone_Shipping_Weight_of_Package * Drone_Shipping__Price_per_Pound + Drone_Shipping__Flat_Charge
        print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
    elif Drone_Shipping_Weight_of_Package > 2 or Drone_Shipping_Weight_of_Package <= 6:
        Drone_Shipping__Price_per_Pound = 9
        Drone_Shipping__Flat_Charge = 0
        cust_ship_cost = Drone_Shipping_Weight_of_Package * Drone_Shipping__Price_per_Pound + Drone_Shipping__Flat_Charge
        print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
    elif Drone_Shipping_Weight_of_Package > 6 or Drone_Shipping_Weight_of_Package <= 10:
        Drone_Shipping__Price_per_Pound = 12
        Drone_Shipping__Flat_Charge = 0
        cust_ship_cost = Drone_Shipping_Weight_of_Package * Drone_Shipping__Price_per_Pound + Drone_Shipping__Flat_Charge
        print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
    elif Drone_Shipping_Weight_of_Package > 10:
        Drone_Shipping__Price_per_Pound = 14.25
        Drone_Shipping__Flat_Charge = 0
        cust_ship_cost = Drone_Shipping_Weight_of_Package * Drone_Shipping__Price_per_Pound + Drone_Shipping__Flat_Charge
        print("--Your estimated shipping cost is:\n--$", cust_ship_cost)
else:
    print("Please enter a correct selction")
