#write a program for a hotel where it takes a users input as the users choice of the food items available and prints out the price of the item.
#use the menu as Baja Taco:4.00,Burrito:7.50,Bowl:8.50,Nachos:11.00,Quesdilla:8.50,Super Burrito:8.50,Taco:3.00,Tortilla Salad:8.00.

def main():
    choice = get_choice()
    print(choice)

def get_choice():
    try:
        Total = 0
        ttotal = []
        while True:
            foods = {
                "Baja Taco" : 4.00,
                "Burrito" : 7.50,
                'Bowl' : 8.50,
                "Nachos" : 11.00,
                'Quesadilla' : 8.50,
                "Super Burrito" : 8.50,
                "Taco" : 3.00,
                "Tortilla Salad" : 8.00
                }

            users_ch = (input('Item:')).title()
            for k,v in foods.items():
                if users_ch == k:
                    Total = v
                    print(f'Total: ${Total}0')
                    ttotal.append(v)
                else:
                    return Total
                


    except EOFError:
        print()
        return (f"${sum(ttotal)}0")



main()