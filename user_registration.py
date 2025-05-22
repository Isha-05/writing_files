#create a class 
class User:
    #create a constructor
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    #Implement a method
    def display(self):
        print("Name of the user: ", self.name)
        print("Email of the user: ", self.email)

details =[]   

#implement a method that takes input from the user
def user_registration():
    #take input from 2 users
    for i in range(2):
        name = str(input("Enter your name: "))
        email = str(input("Enter you valid email address: "))
        password = str(input("Enter your password: "))

        #check if email is already present in list or not    
        if email not in details:
            print("Account is created successfully.")
        else:
            print("Email address already present.") 
        
        #append user details in list one by one
        details.append(name)
        details.append(email)
        details.append(password)
        
        #Access the list
        name = details[0]
        email = details[1]
        password = details[2]
        
        #object of class User
        new_user = User(name, email, password) 

        new_user.display()

    # open file
    with open('user_information.txt', 'w+') as f:
        
        # write elements of list
        for items in details:
            f.write('%s\t' %items)
        
        print("File written successfully")   


        # close the file
        f.close()   
        
    return new_user   

#function call  
user_registration()
