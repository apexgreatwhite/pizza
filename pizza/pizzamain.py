# Creating the dictionary 

av_size = ['small', 'medium', 'large', 'extra', 'extralarge']
prc_size = {'small': 5, 'medium': 6, 'large': 7, 'extra': 8, 'extralarge': 9}
av_topings = ['mushroom', 'onions', 'green pepper', 'extra cheese']
prc_topings = {'mushroom': 1, 'onions': 2, 'green pepper': 3, 'extra cheese': 4}
av_cheese = ['Mozzarella', 'Cheddar', 'Parmesan', 'Provolone', 'Ricotta']
prc_cheese = {'Mozzarella': 5, 'Cheddar': 7, 'Parmesan': 6, 'Provolone': 8, 'Ricotta ': 6.5}
sub_tot = []# I make saprate librarys to store one item price only because each time loop run one librery store and represent three functions value to gether so i seprate it make one time on key value
sub_top = []
sub_che = []
final_od = {}

# crearting multipale fuctions if we not have specific item in manu we can changes here and also comment out it...

def av_sizee():
    print("__Avalable size is__\n")
    print(">>>-----", *av_size, "-----<<<", sep='---')
    print("\n")
    while True:
        pizza = input("Which Size would you like to order?")
        if pizza in av_size:
            print(f">>>>>>>you have order a {pizza}---pizza.<<<<<<<\n")
            sub_tot.append(prc_size[pizza])
            final_od.setdefault(pizza,sub_tot)
            break
        if pizza not in av_size:
            print(f">>>>>>> i am sorry, currently do not have {pizza}.<<<<<<<")
            break


def av_topingss():
    print("__Avalable Topings is__\n")
    print(">>>>>-------", *av_topings, "-------<<<<<", sep="---")
    print("\n")
    while True:
        topings = input("Which Topings you whant to add in you pizza:")
        if topings in av_topings:
            print(f">>>>>>> you add a {topings}--pizaa.<<<<<<<\n")
            sub_top.append(prc_topings[topings])
            final_od.setdefault(topings,sub_top)
            break
        if topings not in av_topings:
            print(f">>>>>>> i am sorry, currently do not have {topings}.<<<<<<<")
            break


def av_cheesee():
    print("__Avalable cheese is__\n")
    print(">>>>>-------", *av_cheese, "-------<<<<<", sep=",")
    print("\n")
    while True:
        cheese = input("Which Cheesee you whant to add in you pizza:")
        if cheese in av_cheese:
            print(f">>>>>>> you add a {cheese}--pizaa.<<<<<<<\n")
            sub_che.append(prc_cheese[cheese])
            final_od.setdefault(cheese,sub_che)
            break
        if cheese not in av_cheese:
            print(f">>>>>>> i am sorry, currently do not have {cheese}.<<<<<<<")
            break
def shoe():
    print(">>>>>>your order is<<<<<<\n")
    print("Your pizza size,Toping and cheese with price here")
    print(final_od)
    print("youre order is >>>>>>>>>> ",*final_od.keys(),"<<<<<<<<<<\n")
##################################################################################
# The sum of librarys 
def addition():
    global sum
    sub = sub_che + sub_top + sub_tot
    sum = sum(sub)
    print("your bill is $",sum)
    print("Enjoy have a nice day !")

#####################################################################