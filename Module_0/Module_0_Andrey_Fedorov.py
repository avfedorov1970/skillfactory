#!/usr/bin/env python
# coding: utf-8

# In[494]:


# The Game: Find the number with minimum iteration

# Setting the borders for search range
range_start = 1
range_end = 100


# Setting the target number by random function
import numpy as np
target_number = np.random.randint(range_start,range_end + 1) 
print (f"Загадано число от {range_start} до {range_end}")

# The variable to save the number of iterations
iteration_count=int()


def find_function(target_number):
    """ function to find the target number """   

    iteration_count = 0
    left = range_start 
    right = range_end  
    predict = 0
    
    while predict != target_number:    
        
        iteration_count += 1       
       
        predict = (left+right) // 2       

        if target_number == predict: break  
        
        elif target_number > predict: 
            left = predict +1

        elif target_number < predict: 
            right = predict -1

    return(iteration_count)    


print (f"Вы угадали число {target_number} за {find_function(target_number)} попыток")  


def mean_count(find_function):
    '''Calcualating mean count of iterations through testing "find_function" by 1000 times'''

    iteration_count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(range_start,range_end + 1, size=(1000))
    
    for number in random_array:
        iteration_count_ls.append(find_function(number))
    score = int(np.mean(iteration_count_ls))
    
    return(score)


print(f"Ваш алгоритм угадывает число в среднем за {mean_count(find_function)} попыток")

