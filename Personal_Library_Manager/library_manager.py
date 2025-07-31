import json
import os 

data_file = 'Library.txt'
def load_lib():
    if os.path.exists(data_file):
        with open(data_file ,'r') as file:
            return json.load(file) #File and not data_file due to using it as a obj and not a str
        
    return []

def save_lib(library):
    with open(data_file ,"w") as file:
        json.dump(library,file)


#Library is a list of dicts and not a dict itself

def add_book(library):
    Name = input("Enter the name of the book : ").strip().capitalize()
    Author = input("Enter the " \
    "author of the book : ").strip()
    Genre = input("What is its genre? : ").strip()
    
    # upcast only doing for max / min functions or else best is always string

    # while True: **** Not valid conversion of str and int
    #     if Year > 0 and type(Year)==int:
    #         Year = int(Year)
    #         break
    #     else:
    #         print("Wrong Input ")
    #         Year = input("Enter when the book was released : ")
    while True:
        Year_input = input("Enter when the book was released : ").strip()
        if Year_input.isdigit():
            Year=int(Year_input)
            break
        else:
            print("Invalid text please input val like (ex 2015) ")

    # Price =float(input("Whats its best price? $ : "))
    while True:
        Price_Val =input("Whats its best price? $: ").strip()
        try:
            Price = float(Price_Val)
            if Price>0:
                break
            else:
                print("The value must be Greater than 0")

        except ValueError:
            print("Put the Value price of book like (199.99)")



    Read = input("Have you read the book? (yes/no) ").strip().lower() =='yes'

    new_book ={
        "Name" :Name,
        "Author" :Author,
        "Genre":Genre,
        "Year": Year,
        "Price":Price,
        "Read" :Read

    }

    library.append(new_book)
    save_lib(library)
    print(f'Book {Name} Added Succesfully !')


def remove_books(library):

    if len(library)>0:
        Name = input("Give the name of Book you want to remove : ").strip().capitalize()
        Initial_len = len(library)
        updated_library = [book for book in library if book['Name'] !=Name]
        if len(updated_library) < Initial_len:
            save_lib(updated_library)
            print(f"{Name} Successfully removed !!")

        else:
            print(f"Cant find {Name} in the Library")

        return updated_library
    else:
        print("Library is Empty.")

def search_lib(library):
    if len(library) > 0:
        search_by = input("Search book by Author or Book name (Default=Name)").lower()


    # if search_by not in ["author","name"]: false
        if search_by!="author" or search_by!="book":
         search_by="name"
    


        search_val = input(f"Search the Library by {search_by}").capitalize()

        result = [ book for book in library if search_val in book[search_by]]

        if result:
            for book in result:
             status ="Read" if book['Read'] else "Unread"
            print(f"{book['Name']} by {book['Author']} _ {book['Genre']} {book['Year']} _ {book['Price']} _ {status}")

        else:
            print(f"No books found matching {search_val} searched by {search_by}")
    else:
        print("Library is Empty.")

def print_all(library):
    if library:
        for book in library:
            status = "Read" if book['Read'] else 'Not_Read'
            print(f"Book : {book['Name']} written by {book['Author']} is a {book['Genre']} book of the year {book['Year']} with a good price tag of {book['Price']}")
            print(f"You have {status} this masterpiece")

    else:
        print("The library is empty ")


def Characterstics(library):
    Total_Books = len(library)
    # Read_Books = len([book for book in library if book['Read']] )

    Read_Books = sum(1 for book in library if book['Read'] )
    Percentage_Read = (Read_Books / Total_Books) * 100 if Total_Books > 0 else 0

    print(f"Total Books in the Library are : {Total_Books}")
    print(f"Percentage of Already read books are : {Percentage_Read}")
    
    filters = input("Do you want to filter out more data ? (1/2) (1 == Yes _ 2 == No) ").strip()
    condition = True
    while condition:
        if filters == '1' and len(library)>0:
         best_price(library)
         condition = False
    
        elif filters == '2':
            break

        else:
            print("Invalid input or Library is empty")
            condition =False #break
        


def best_price(library):
    counter = 0
    for book in library:
        if book['Price'] < 200:
            counter+=1
   
   # price = [book for book in libary if book['Price'] < 200 ]
   # print(f"lower price {len(price)}")

    print(f"There are {counter} books lower than avg price of 200$ ")


    min_price = min(library,key=lambda book:book['Price'])
    #min_price_book = library[min_price] incorrect dicts

    # print(f"The minimum price book is {min_price_book} which is of amount {min_price}")
    
    print(f"The minimum price book is {min_price['Name']} which is costing ${min_price['Price']}.")
    
    max_price=max(library,key=lambda book:book['Price'])
    # max_price_book = library[max_price]

    print(f"The maximum price book is {max_price['Name']} which is costing ${max_price['Price']}.")

    counter1 = 0
    for book in library:
        if book['Year'] < 2010 :
            counter1 += 1

            # Either comprehesion or sum method

    print(f"Old Generational books (older then 2010) in Library = {counter1}")





def main():

    library = load_lib()
    print("__ Welcome to Personal Library manager __")
    while True :
            print("Menu")
            print("1. Add book to Library")
            print("2. Remove book from Library")
            print("3. Search for a Book")
            print("4. Display All existing books")
            print("5. Find characterstics and info")
            print("6. Exit")

            choice = input("Enter Your Prefered Choice : ")

            if(choice == '1'):
                add_book(library)

            elif(choice == '2'):
                library=remove_books(library)
                #Lib must be saved ,  the new variable should be upadted

            elif(choice == '3'):
                search_lib(library)

            elif(choice == '4'):
                print_all(library)

            elif(choice == '5'):
                Characterstics(library)

            elif(choice == '6'):
                print("-"* 36)
                print("Thanks for using our Wonderfull App ")
                break

            else:
                print("Invalid Input !")
                
if __name__ == '__main__':
    main()
