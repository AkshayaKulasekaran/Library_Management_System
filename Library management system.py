## NOTES FOR PORGATE PYTHON WORKSHOP

#Organizer: Ankita Mishra from Progate
#Speaker: Disha Pongati from Delloite

#Olden day library -> Card catalogue
#Now, we have library management systems
#Today, we'll be thinking about the library management systems!
#repl.it python -> online python environment

#Note: list()->[], tuple()->(), dict()->{}
#Librarian: calling function, LMS: called functions

library={'Networking 101' : 10, 'Harry Potter' : 20, 'Cyber Security' : 5} # 'book_title' : number_of_copies
def printlib():
    print(library)

#Think about what you want to do and add functions accordingly

#function to add x number of books
def add_book(book_name, num_copies):
    library[book_name] = num_copies #new key-value pair


#if __name__ == __main__:
#    add_book('DBMS',3)

#to return a book
def return_book(book_name):
    library[book_name] = library[book_name] + 1


#to update the number of copies
def update_cop(book_name, extra_cop):
    library[book_name] = library[book_name] + extra_cop #old+new

#To issue a book
def issue_book(book_name):
    if book_name in library.keys() and library[book_name]>0:
        library[book_name] = library[book_name] - 1
        print("Here's your book!")
    else:
        print("Not availible")

# To search for a book
def search_book(book_name):
    if book_name in library:
        print("Availible")
    else:
        print("Not Availible")





# Let's try something along the lines of MVC
print("Hello and welcome to the library management system!")
print("What do you want to do now?")
ch=1
while ch==1:
    print("Hi!")
    ch=int(input("Do you want to continue? "))
    #ch=ch.upper()
    print("You have chosen "+ch)
    #if ch=="YES" or ch=="Y" or ch=="YUP":
     #   ch==1
    
