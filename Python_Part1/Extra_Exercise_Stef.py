#%% EXERCISE1 RETHINK ABOUT A SHORTER SOLUTION
time_first = int(input('Enter time one: '))
time_second = int(input('Enter time two: '))
time_third = int(input('Enter time three: '))
def myfunction(a,b,c):
    total = a + b + c
    minutes = total / 60
    seconds = total % 60
    x = print('The time taken in format MINUTE:SECOND is',round(minutes),'minute(s)',':',seconds,'seconds')   
    return x
myfunction(time_first,time_second,time_third)




#%% EXERCISE2 RETHINK ABOUT A SHORTER SOLUTION ---------------I HAVE TO COME BACK TO THIS
a = int(input('Enter the number x: '))
#bonus1 = 0
#bonus2 = 0
def myfunction(x):
    if x % 2 ==0:
        bonus1 = 1
        if x <= 100:
            bonus2 = 5
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
        elif (x > 100) and (x <= 1000):
            bonus2 = x*0.2
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
        elif x > 1000:
            bonus2 = x*0.1
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
    elif x % 5 == 0:
        bonus1 = 2
        if x <= 100:
            bonus2 = 5
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
        elif (x > 100) and (x <= 1000):
            bonus2 = x*0.2
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
        elif x > 1000:
            bonus2 = x*0.1
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
    else:
        bonus1 = 0
        if x <= 100:
            bonus2 = 5
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
        elif (x > 100) and (x <= 1000):
            bonus2 = x*0.2
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
        elif x > 1000:
            bonus2 = x*0.1
            total_bonus = bonus1 + bonus2
            total_point = x+bonus1+bonus2
    return print('the total bonus is: ',total_bonus,'and the total points are: ',total_point)
myfunction(a)

#%% EXERCISE3 LONG VERSION WORKIN WELL TOO
a = str(input('Enter the season: ').lower())
b = int(input('Tnter the number of people: '))

#discount = 0
def seasons(season,people):
    if season == 'spring':
        price1 = 3000
        if people % 2 == 0:
            discount2 = 0.05
            if people <= 6:
                discount = 0.1
                final_price = price1 - (price1 * discount) - (price1 * discount2)
            elif people in range(7,12):
                discount = 0.15
                final_price = price1 - (price1 * discount) - (price1 * discount2)
            elif people > 11:
                discount = 0.25
                final_price = price1 - (price1 * discount) - (price1 * discount2)
        else:
            if people <= 6:
                discount = 0.1
                final_price = price1 - (price1 * discount)
            elif people in range(7,12):
                discount = 0.15
                final_price = price1 - (price1 * discount)
            elif people > 11:
                discount = 0.25
                final_price = price1 - (price1 * discount)
            
    elif season == 'autumn':
        price1 = 4200
        if people <= 6:
            discount = 0.1
            final_price = price1 - (price1 * discount)
        elif people in range(7,12):
            discount = 0.15
            final_price = price1 - (price1 * discount)
        elif people > 11:
            discount = 0.25
            final_price = price1 - (price1 * discount)
            
    elif season == 'winter':
        price1 = 2600
        if people % 2 == 0:
            discount2 = 0.05
            if people <= 6:
                discount = 0.1
                final_price = price1 - (price1 * discount) - (price1 * discount2)
            elif people in range(7,12):
                discount = 0.15
                final_price = price1 - (price1 * discount) - (price1 * discount2)
            elif people > 11:
                discount = 0.25
                final_price = price1 - (price1 * discount) - (price1 * discount2)
        else:
            if people <= 6:
                discount = 0.1
                final_price = price1 - (price1 * discount)
            elif people in range(7,12):
                discount = 0.15
                final_price = price1 - (price1 * discount)
            elif people > 11:
                discount = 0.25
                final_price = price1 - (price1 * discount)
                
    elif season == 'summer':
        price1 = 4200
        if people % 2 == 0:
            discount2 = 0.05
            if people <= 6:
                discount = 0.1
                final_price = price1 - (price1 * discount) - (price1 * discount2)
            elif people in range(7,12):
                discount = 0.15
                final_price = price1 - (price1 * discount) - (price1 * discount2)
            elif people > 11:
                discount = 0.25
                final_price = price1 - (price1 * discount) - (price1 * discount2)
        else:
            if people <= 6:
                discount = 0.1
                final_price = price1 - (price1 * discount)
            elif people in range(7,12):
                discount = 0.15
                final_price = price1 - (price1 * discount)
            elif people > 11:
                discount = 0.25
                final_price = price1 - (price1 * discount)
    
    else:
        print('enter the correct season')
        
    return print('The final price is: ',final_price,'$')
seasons(a,b)    
#%% EXERCISE3 SHORT VERSION WORKIN WELL
a = str(input('Enter the season: ').lower())
b = int(input('Tnter the number of people: '))
dict1 = {'spring' : 3000,'summer': 4200,'autumn': 4200 ,'winter': 2600}
#list2 = [3000,4200,4200,2600]
def seasons(season,people):
    for x in dict1.keys():
        if season == x and season != 'autumn':
            price1 = dict1[x]
            if people % 2 == 0:
                discount2 = 0.05
                if people <= 6:
                    discount = 0.1
                    final_price = price1 - (price1 * discount) - (price1 * discount2)
                elif people in range(7,12):
                    discount = 0.15
                    final_price = price1 - (price1 * discount) - (price1 * discount2)
                elif people > 11:
                    discount = 0.25
                    final_price = price1 - (price1 * discount) - (price1 * discount2)
            else:
                if people <= 6:
                    discount = 0.1
                    final_price = price1 - (price1 * discount)
                elif people in range(7,12):
                    discount = 0.15
                    final_price = price1 - (price1 * discount)
                elif people > 11:
                    discount = 0.25
                    final_price = price1 - (price1 * discount)
                    
        elif season == 'autumn':
            price1 = 4200
            if people <= 6:
                discount = 0.1
                final_price = price1 - (price1 * discount)
            elif people in range(7,12):
                discount = 0.15
                final_price = price1 - (price1 * discount)
            elif people > 11:
                discount = 0.25
                final_price = price1 - (price1 * discount)
            
          #else:
           # print('enter the correct season')
 

    return print('The final price is: ',final_price,'$')
seasons(a,b)          

#%% EXERCISE4 
#b = 0
list1 = []
while True:
    c = 0
    x = int(input('enter the number: '))
    list1.append(x)
    print(list1)
    for a in range(len(list1)):
        b = list1[a]
        c += b
    print(c)
    if c == 10000:
        print('Good job Ana you reached 10 000steps')
        break
    if str(x) == 'Going home':
        print('Today you did not reach your goal')
        break