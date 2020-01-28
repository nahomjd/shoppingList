menuOption = None

mylist = []
mylistTest = ['corn','banana','flour','apple','vitimans','gaterade']
menuText = '''
1.) Add item 
2.) Print list
3.) Remove item by number
4.) Save list to file
5.) Load list from file
6.) Exit
'''

while menuOption != '6':
    print(menuText)
    menuOption = input("Enter selection: ")
    #print(menuOption)
    if menuOption == '1':
        print("Add item")
        item = input("What item would you like to add:  ")
        mylist.append(item)
    
    elif menuOption == '2':
        print('Print list')
        mylist.sort(key=str.lower)
        i = 1
        for item in mylist:
            print(str(i) + '.) ' + item)
            i += 1
            
    elif menuOption == '3':
        print('Remove item by number')
        print('What item would you like to remove: ')
        number = input()
        try:
            number = int(number)
            myListTemp = []
            removedItem = mylistmylist[number-1]
            for item in mylist:
                if item != removedItem:
                    myListTemp.append(item)
            mylist = myListTemp
        except Exception as e:
            print('Not a valid input' + str(e))
    
    elif menuOption == '4':
        print('Saved list to file')
        file = open('shoppingList.txt', 'w')
        i = 1
        for item in mylist:
            file.write(str(i) + '). ' + item + '\n')
            i += 1
        file.close()
    
    #needs to be the same format as saved to file        
    elif menuOption == '5':
        print('Load list from file')
        file = open('shoppingList.txt', 'r')
        mylist = []
        for line in file:
            mylist.append(line[4:-1])
        
    elif menuOption == '6':
        print('Exit')
    else:
        print('Your Selection was not recongnized!')
        
    