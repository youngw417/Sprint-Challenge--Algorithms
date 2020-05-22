'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
       #stoppage case
    if len(word) == 0:
        return 0
    if word[0:2] == 'th':
        sliced = word[2:]
        # when matches, move by 2
        return count_th(sliced) + 1
    else:
        sliced = word[1:]
        # when did not match, move by 1
        return count_th(sliced)

print(count_th('thisistheisthe'))