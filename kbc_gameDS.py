#KBC Game Made by DISHANK SOLANKI
print("Welcome in KBC made by DISHANK SOLANKI")
Price = 0
print("Question 1 : What is the capital of India")
print("A) Mumbai\nB) New Delhi \nC) Kolkata \nD) Chennai")
option=input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Right Answer")
        Price+=1000
        print(Price)
    case "C":
        print("Wrong Answer")
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

        #QUESTION 2
print("Question 2 : How many days are there in a week?")
print("A) 5\nB) 6 \nC) 7 \nD) 8")
option=input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Wrong Answer")

    case "C":
        print("Right Answer")
        Price+=1000
        print(Price)
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

#QUESTION 3
print("Question 3 :  Which planet is known as the Red Planet?")
print("A) Venus\nB) Mars \nC) Jupiter \nD) Saturn")
option=input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Right Answer")
        Price += 1000
        print(Price)
    case "C":
        print("Wrong Answer")
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

# QUESTION 4
print("Question 4 :   Who is known as the Father of the Nation in India?")
print("A) Jawaharlal Nehru\nB) Bhagat Singh \nC) Mahatma Gandhi  \nD) Sardar Patel")
option = input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Wrong Answer")

    case "C":
        print("Right Answer")
        Price += 1000
        print(Price)
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

#QUESTION 5
print("Question 5 :   Which animal is called the King of the Jungle?")
print("A) Tiger\nB) Elephant\nC) Lion \nD) Leopard")
option = input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Wrong Answer")

    case "C":
        print("Right Answer")
        Price += 1000
        print(Price)
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

#QUESTION 6
print("Question 6 :   Which is the largest ocean on Earth?")
print("A) Atlantic Ocean\nB) Indian Ocean\nC) Pacific Ocean \nD) Arctic Ocean")
option = input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Wrong Answer")

    case "C":
        print("Right Answer")
        Price += 3000
        print(Price)
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

        # QUESTION 7
print("Question 7 :  What is the chemical symbol for Gold?")
print("A)  Ag\nB) Au \nC) Gd\nD) Go")
option = input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Right Answer")
        Price += 3000
        print(Price)
    case "C":
        print("Wrong Answer")
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

 # QUESTION 8
print("Question 8 : Who wrote the Indian National Anthem?")
print("A) Bankim Chandra Chattopadhyay\nB) Rabindranath Tagore \nC) Premchand\nD) Sarojini Naidu")
option = input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Right Answer")
        Price += 3000
        print(Price)
    case "C":
        print("Wrong Answer")
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

# QUESTION 9
print("Question 9 :  Which is the largest desert in the world?")
print("A) Sahara\nB) Arabian\nC) Antarctic Desert \nD) Gobi")
option = input("Enter your choice: ").upper()
match option:
    case "A":
        print("Wrong Answer")
    case "B":
        print("Wrong Answer")

    case "C":
        print("Right Answer")
        Price += 5000
        print(Price)
    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

# QUESTION 10
print("Question 10 :  Who was the first President of India?")
print("A) Rajendra Prasad \nB) Jawaharlal Nehru\nC) S. Radhakrishnan\nD) Zakir Hussain")
option = input("Enter your choice: ").upper()
match option:
    case "A":
        print("Right Answer")
        Price += 5000
        print(Price)
    case "B":
        print("Wrong Answer")

    case "C":
        print("Wrong Answer")

    case "D":
        print("Wrong Answer")
    case _:
        print("Option not available")

print("You Won ",Price)