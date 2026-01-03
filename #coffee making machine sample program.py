#coffee making machine 
#Initial ingredients 
'''
water : 300ml
milk : 200ml
coffee : 100g

'''
#3 type of coffee
'''
espresso : water = 50ml , coffee = 18g , cost = 15
latte : water= 100ml , coffee = 24g , milk = 150ml , cost = 25
cappachino : water = 250ml , coffee = 24g , milk = 100ml , cost = 35
'''
#user input 
#are the ingredients present 
#make payment 
#confirm payment is successfull or not 
#issue the coffee 
#reduce the quantity of the ingredients according to the costumer choice 

menu = {
     'espresso': { 'ingredients':{'water':50, 'coffee':18 },'cost':15 },
     'latte': { 'ingredients':{'water':200, 'coffee':24, 'milk':150},'cost':25 },
     'cappacchino': {'ingredients':{'water':250, 'coffee':24, 'milk':100},'cost':35 }
}
resouces = {
     'water' : 300,
     'milk' : 200,
     'coffee' : 100
}
profit = 0
def isingredentspresent(userchoiceingredients):
     for item in userchoiceingredients :
          if userchoiceingredients [item]> resouces[item]:
               print(f"sorry we dont have enough item:{item} ")
               return False
          return True
def processpayment():
     totalamount=int(input("how many one rs coins "))
     totalamount+=int(input("how many tow rs coins "))*2
     totalamount+=int(input("how many five rs coins "))*5
     totalamount+=int(input("how many ten rs coins "))*10
     return totalamount
def istransactionsuccessfull(userpayment,actualcost):
     global profit
     print(actualcost)
     if userpayment<actualcost:
          print("sorry amount is insufficient")
          print(f"please collect the {userpayment} back")
          return False
     else:
          profit+=actualcost
          print(f"please collect  the remaining change: {userpayment-actualcost}")
          return True
def issuedrink(useringredients):
     for item in useringredients:
          resouces[item]-=useringredients[item]
isonn=True
while isonn:
     choice=input("what would you like to order?(espresso:15rs,latte:25rs,cappacchino:35rs,off,report)")
     if choice=='off':
          isonn=False
     elif choice=='report':
          print(f"the water left:{resouces['water']}")
          print(f"the milk left:{resouces['milk']}")     
          print(f"the coffee left:{resouces['coffee']}")
          print(f"the profit generated is: {profit}")
     else:
          drink=menu[choice]
          if isingredentspresent(drink['ingredients']):
           payment=processpayment()
           if istransactionsuccessfull(payment,drink['cost']):
             issuedrink(drink['ingredients'])
             print(f"please collect {choice} from the dispenser")
 

            
              