def search(list,n):
    i=0
    while i< len(list):
        if list[i]==n:
            return True
        i= i+1
    return False

list = [5,8,6,9]
n=int(input('enter the nuber for search\n'))
if search(list, n):
    print("element found")
else:
    print('element not found')

pos = 1


def search(list, n):
    i = 0
    for i in range(0, n):
        if list[i] == n:
            globals()['pos'] = i
            return i

        return 0
