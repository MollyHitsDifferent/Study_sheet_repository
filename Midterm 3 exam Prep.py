"""Midterm Exam study sheet 3"""
import random
# Exercise 1

def make_array(prototype,length):
    return [prototype] * length

#Exer 2
def string_to_array(a_string):
    return [a_string[i] for i in range(0,len(a_string))]
  

#Exer 3 
def threes_and_fives(an_array):
    arr = []
    for i in range(len(an_array)):
        if an_array[i] % 3 == 0 or an_array[i] % 5 == 0:
            arr.append(an_array[i])
        else:
            continue

    return arr

"exercise 4"

def alegebraic(number):
        if number == 1:
            return 1    
        elif number < 1:
            return 
        elif number % 2 != 0:
            return number + alegebraic(number+1)
        elif number % 2 == 0:
            return number + alegebraic(number/2)

def linear_search(an_arr, target):
    for i in range(0,len(an_arr)):
        if target == an_arr[i]:
            return i
        else:
            continue        
""" exer 6 """
def shuffle(an_array):
    shuffled = []
    array_len = len(an_array)     
    for i in range(0,len(an_array)):
            if len(an_array) > 1:
                roll = random.randint(0,len(an_array)-1)
                shuffled.append(an_array[roll])
                an_array.pop(roll)
            else:
                shuffled.append(an_array[0])
                return shuffled
                
            
""" exer 7"""
def random_search(an_array,target):
    tick_down = shuffle([q for q in range(0,len(an_array)-1)])
    for i in tick_down:  
        if target == an_array[tick_down[i]]:
            return tick_down[i]
        if target != an_array[tick_down[i]]:
            continue  
  
""" Exer 8"""
def swapper(an_array,target1,target2):
    holder = an_array[target2]
    an_array[target2] = an_array[target1]
    an_array[target1] = holder

def swap_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(1,i+1):
            if arr[j] < arr[j-1]:
                swapper(arr,j,j-1)
    return arr
"""exer 9"""

def make_tuple(a,b,c):
    return  (a,b,c)



"""Exer 10"""
def reverse_tuple(sequence):
    tuple = ()
    for i in range(len(sequence)-1,-1,-1):
        tuple += (sequence[i],)
    return tuple

"""exer 11"""
def make_trading_card(name,mana_value,power,toughness):
    return (name,mana_value,power,toughness)

"""exer 12 """
def mana_key(trading_card):
    manakey = trading_card[1]
    # manakey = list(manakey)
    # print(manakey)
    mana_brut = 0
    for i in range(0,len(manakey)):
        if i == 0:
            mana_brut += int(manakey[i])
        else:
            mana_brut +=1
    return mana_brut
"""exer 13"""

def power_key(trading_card):
    return trading_card[2]

def toughness_key(trading_card):
    return trading_card[3]

def name_key(trading_card):
    return trading_card[0]

"""exer 14"""
def make_list(a,b,c):
    return [a,b,c]

"""exer 15"""
def nth_list(sequence, n):
    for i in range(0)

def main():
    #exercise 1

    # print(make_array(3,7))


    #exeercise 2
    # print(string_to_array("LOLOLOL POWNED 6969"))

    #exercise 3
    # an_array = [1701 , 1703, 69, 420, 9999999, 100000000, 17, 11, 427]
    # print(threes_and_fives(an_array))

#Exercise 4
    # print(alegebraic(10))
    # print(alegebraic(1))
    # print(alegebraic(15))
    # print(alegebraic(0))
    # print(alegebraic(101))

# exer 5
    # random.seed(1)
    # arr = [random.randint(0,20) for i in range(0,20)]
    # print(arr)
#     print(linear_search(arr,13))

# #exer 6
#     # arr = [1,2,3,4,5,6,7,8,9,10]
#     # random.seed(1)
#     # print(shuffle(arr))

# #exer 7 
#     print(random_search(arr,13))

#exer 8
    # print(swap_sort(arr))

#exer 9
    # a = 1
    # b = 2
    # c = 3
    # print(make_tuple(a,b,c))
    # print(make_tuple(4,5,6))

#exer 10 
    # sequence = "Dancing"
    # print(reverse_tuple(sequence))

# """Exer 11"""

    # print(make_trading_card("borborygmos","3rrgg",6,7))
    # print(make_trading_card("Shivan Dragon", "4RR",5,5))

# #exer 12 & 13
    # sd = make_trading_card("Shivan Dragon", "4RRGGGB",5,5)
    # print(sd)
    # print(name_key(sd))
    # print(mana_key(sd))
    # print(power_key(sd))
    # print(toughness_key(sd))

#exer 14
    # print(make_list(1,("420","69"), 1337))
    # print(make_list(7,"rebecca",4.25))

#exer 15



if __name__ == "__main__":
    main()