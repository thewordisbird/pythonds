# Find all substrings of a given string. 
# For example:
# Given 'abc' return 'a', 'b', 'c', 'ab', 'bc', 'ac', 'abc'

# For problems where all end nodes need to be returned or stored, The action must happen in the base case
# otherwise recurse to the next level with and without the added item

#   0       1       2       3       4       5       6       7
#               start string ='abc'                 
#               /                \              Keep or remove 'a'
#           'abc'                 'bc'
#         /     \                /    \         Keep or remove 'b'
#    'abc'       'ac'        'bc'      'c' 
#   /     \     /    \     /     \    /   \     Keep or remove 'c'
# 'abc'  'ab'  'ac'  'a'  'bc'  'b'  'c'  ''                      
# 
# When the bottome of the tree is reached that is the base case. 
# At this point perform action. In this case add to the sub array
     
def substrings(s, subs=set(), i=0):
    '''Recursive function to find all substrings in a string'''
    if i == len(s):
        subs.add(s)
    else:
        # recurse down including s[i]
        substrings(s, subs, i+1)
        # recurse down not including s[i]
        substrings(s[0:i] + s[i+1::], subs, i)
    return subs
    

if __name__ =='__main__':
    s = 'aaa'
    print(substrings(s), len(substrings(s)))