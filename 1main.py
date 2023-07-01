customers = []
address = []

def register():

    while True:
        print("Provide user information")

        infoData = {}
        infoData['name'] = input("Name: ")
        infoData['password'] = input("Password: ")

        infoData['email'] = input("Email: ")
        list = {i['email']: i for i in customers}
        while infoData['email'] in list:
            infoData['email'] = input("[Email in use, Try again.] Email: ")
        
        infoData['login'] = input("Login: ")
        list = {i['login']: i for i in customers}
        while infoData['login'] in list:
            infoData['login'] = input("[Login in use, Try again.] Login: ")
        
        infoData['Cell-Phone'] = input("Phone number: ")
        list = {i['Cell-Phone']: i for i in customers}
        while infoData['Cell-Phone'] in list:
            infoData['Cell-Phone'] = input("[Phone in use, Try again.] Phone number: ")
        
        customers.append(infoData)

        print("Completed registration.")
        option = input("Would you like to add someone else? (Y/N): ").strip().lower()
        if (option == 'n'):
            menu()
            break

def Address():
    
    while True:

        print("Provide a login of a user")
        list_dict = {i['login']: i for i in customers}
        search = input("Login: ")

        #Only to a valid user

        if search in list_dict:
            print("[Provide customer addres]: ")
        
            infoLocal = {}
            infoLocal['id'] = search
            infoLocal['state'] = input("State: ")
            infoLocal['city'] = input("City: ")
            infoLocal['street'] = input("Street and Number: ")
            infoLocal['cep'] = input("CEP: ")

            address.append(infoLocal)

        else:
            print('')
            print("Couldn't find user!")
            print('')
        
        option = input("Would you like to add another address? (Y/N): ").strip().lower()
        if(option == 'n'):
            menu()
            break

def showData():
    
    while True:
        print("Provide a Login of a user to view informations from the user!")

        list_dict = {i['login']: i for i in customers}
        list2 = {i['id']: i for i in address}

        search = input("Login: ")

        if search in list_dict and search not in list2:
            print(f"Customer data: [{search.upper()}]: {list[search]}")

            print('')
            print("Address not registered")
            print('')

        elif search in list_dict and search in list2:
            print('')
            print(f"Customer data: [{search.upper()}]: {list[search]}")
            print('')
            print(f"Customer address: [{search.upper()}]: ")
            print('')
            result = list(filter(lambda item: item['id'] == search, address))
            for i in result:
                print(i)
            print('')
        
        else:
            print('')
            print("Couldn't find user!")
            print('')
        
        option = input("Would you like to view anoter customer? (Y/N): ").strip().lower()
        if(option == 'n'):
            menu()
            break

def showCustomers():
    
    while True:
        print('')
        print("Registered users: ")
        print('')

        for i in customers:
            print("Name:", i['name'], "Login:", i['login'])
        print('')

        option = input("Do you want to check again? (Y/N): ").strip().lower()
        if(option == 'n'):
            menu()
            break

def menu():

    print('')
    print('[1] Register customer')
    print('[2] Register address to customer')
    print('[3] View customer data')
    print('[4] View customers')
    print('[0] Leave')
    print('')

menu()

while True:

    x = int(input("Choose > [1] [2] [3] [4] [0]: "))

    while x > 4 or x < 0:
        x = int(input("[Error, Try again] Choose a option: "))
    
    if x == 1:
        register()
    elif x == 2:
        Address()
    elif x == 3:
        showData()
    elif x == 4:
        showCustomers()
    else:
        print('')
        print('[Program has terminated.]')
        print('')
        break
