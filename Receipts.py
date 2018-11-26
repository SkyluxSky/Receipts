#Furniture Description and Prices
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#Sales Tax 8.8%
sales_tax = .088

#Customers who haven't purchased anything yet
customer_one_total = 0
#We should also keep a list of the descriptions of things they're purchasing.
customer_one_itemization = ""
#Our customer has decided they are going to purchase our Lovely Loveseat! 
customer_one_total += lovely_loveseat_price
#Let's start keeping track of the items our customer purchased.
customer_one_itemization += lovely_loveseat_description
#Our customer has decided they are going to purchase our Luxurious Lamp
customer_one_total += luxurious_lamp_price
#Let's keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.
customer_one_itemization += luxurious_lamp_description

#They're ready to check out! Let's begin by calculating sales tax.
customer_one_tax = customer_one_total * sales_tax

customer_one_total + customer_one_tax
#Let's start printing up their receipt! Begin by printing out the heading for their itemization.
print("Customer One Items:")
print(customer_one_itemization)
#Now print out their total! Our first customer now has a receipt for the things they purchased.
print("Customer One Total:")
print(customer_one_total + customer_one_tax)

#Customer Two
customer_two_total = 0
#Begin their itemization with a new variable
customer_two_itemization = ""

#Customer two purchases
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description
#Purchase and checkout
customer_two_tax = customer_two_total * sales_tax
customer_two_total + customer_two_tax
print("Customer Two Items:")
print(customer_two_itemization)
print("Customer Two Total:")
print(customer_two_total + customer_two_tax)




