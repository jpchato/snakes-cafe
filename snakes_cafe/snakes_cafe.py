from textwrap import dedent
print("*"*38)
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type 'quit' **")
print("*"*38)
print("")
print("")
print("Appetizers")
print("-"*10)
print("Wings")
print("Cookies")
print("Spring Rolls")
print("")
print("Entrees")
print("")
print("Salmon")
print("Steak")
print("Meat Tornado")
print("A Literal Garden")
print("")
print("Desserts")
print("-"*8)
print("Ice Cream")
print("Cake")
print("Pie")
print("")
print("Drinks")
print("-"*6)
print("Coffee")
print("Tea")
print("Unicorn Tears")
print("")
print("*"*35)
print("** What would you like to order? **")
print("*"*35)

Food_menu = {
  "wings" : 0,
  "cookies" : 0,
  "spring rolls" : 0,
  "salmon" : 0,
  "steak" : 0,
  "meat tornado" : 0,
  "a literal garden" : 0,
  "ice cream" : 0,
  "cake" : 0,
  "pie" : 0,
  "coffee" : 0,
  "tea" : 0,
  "unicorn tears" : 0
}

while True:
  order = input("")
  if order == 'quit':
    break
  # if order.lower() in Food_menu:
  #   print("nice")
  # if order.lower in Food_menu:
  #   Food_menu[order.lower()] += 1
  #   if Food_menu[order.lower()] == 1:
  #     print("**", f'1 order of {order} have been added to your meal', "**")
  #   else:
  #     print("**", f'{Food_menu[order.lower()]} order of {order} have been added to your meal', "**")




