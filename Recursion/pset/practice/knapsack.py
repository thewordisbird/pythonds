# Given a list of items with values and weights, as well as a max weight, 
# find the maximum value you can generate from items where the sum of the weights is less than the max.

def knapsack_r(items, maxWeight, i=0):
    print(maxWeight) 
    if i == len(items):
        return 0
    if maxWeight - items[i]['w'] < 0:
        return knapsack_r(items[0:i] + items[i+1:], maxWeight, i)
    else:
        return  max(knapsack_r(items, maxWeight - items[i]['w'], i+1) + items[i]['v'], \
            knapsack_r(items[0:i] + items[i+1:], maxWeight, i))            

def knapsack_r_cache(items, maxWeight, i=0, cache={}):
    if maxWeight not in cache.keys():
        print(maxWeight) 
        if i == len(items):
            result = 0
        if maxWeight - items[i]['w'] < 0:
            result = knapsack_r(items[0:i] + items[i+1:], maxWeight, i)
        else:
            result =  max(knapsack_r(items, maxWeight - items[i]['w'], i+1) + items[i]['v'], \
                knapsack_r(items[0:i] + items[i+1:], maxWeight, i))   
        cache[maxWeight] = result
    else:
        result = cache[maxWeight]
    return result

if __name__ == '__main__':
    items =[{'w':1, 'v':6}, {'w':2, 'v':10}, {'w':3, 'v':12}, {'w':4, 'v':14}, {'w':1, 'v':122}]
    maxWeight = 5
    print(knapsack_r(items, maxWeight))
    print(knapsack_r_cache(items, maxWeight))