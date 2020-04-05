myInventary = {'rope': 1,
               'torch': 6,
               'gold coin': 42,
               'dagger': 1,
               'arrow': 12}

def displayInventary(base):
    print('Inventary:')
    itemTotal = 0
    for k, v in base.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print('Total number of items: ' + str(itemTotal))

displayInventary(myInventary)
    
    
