from textwrap import dedent

def message():
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
message()

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
  order = input("").lower()
  if order == 'quit':
    break
  if order in Food_menu:
    Food_menu[order] += 1
    print(f'{Food_menu[order]} {order} has been added to your meal')
  if order not in Food_menu:
    print('invalid input')
 


