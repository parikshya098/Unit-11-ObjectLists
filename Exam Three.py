# class House:
#     def __init__(self, address, sqft, price):
#         self.address = address
#         self.sqft = Squarefeet
#         self.price = price

#     def costpersqft():
#         return self.price / self.sqft

#     ar = float(ar) / 100 / 12
#     ny = float(ny) * 12
#     def payment(ar, ny):
#         return 100

# #         # Formula for mortgage calculator
# # # M = L(I(1 + I)**N) / ((1 + I)**N - 1)
# # # M = Monthly Payment, L = Loan, I = Interest, N = Number of payments, ** = exponent

# # # Declares and asks for user to input loan amount. Then converts to float
# # loanAmount = input('Enter loan amount \n')
# # loanAmount = float(loanAmount)

# # # Declares and asks user to input number of payments in years. Then converts to float. Years * 12 to get
# # #  total number of months
# # years = input('How many years will you have the loan? \n')
# # years = float(years) * 12

# # # Declares and asks user to input interest rate. Then converts to float and input interest rate is /100/12
# # interestRate = input('Enter Interest Rate \n')
# # interestRate = float(interestRate) / 100 / 12

# # # Formula to calculate monthly payments
# # mortgagePayment = loanAmount * (interestRate * ((1 + interestRate)** years) / ((1 + interestRate) ** years - 1))

# # # Prints monthly payment on next line and reformat the string to a float using 2 decimal places
# # print("The monthly mortgage payment is\n (%.2f) " % mortgagePayment)

# examfile = open(' Exam Three Houses.txt', 'r')
# examfile.readline()
# examfile = examfile.strip('\n').split(',')


class House:

  # Initiazes the House object
  def __init__(self, address, sqft, price):
      self.address = address
      self.sqft = sqft
      self.price = price

  # method that finds the cost per square feet
  def costpersqft(self):
      return self.price / self.sqft

  # method that calculates the annual payment
  def payment(self, ar, ny):
      return 100

# list to store the Houses
HouseList = []
# Reading the file Houses.txt line by line and creating the House objects
n = open("Exam Three Houses.txt", "r")
for line in n:
  # split the line to different values
  data = line.split(', ')
  # extrats the values for the list
  address = data[0]
  sqft = int(data[1])
  price = int(data[2])
  # creating the House object using the
  house = House(address, sqft, price)
  # appending to the HouseList
  HouseList.append(house)

# prompt the user to enter the intrest rate
interest = int(input("Enter Interest Rate: "))
# divide by hudred to the get the percentage
interest = interest / 100
# prompt the user to enter number of years
years = int(input("Enter years for Mortage: "))
# prints data for all the houses
print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}\n".format("Address", "Sq Ft", "SqFt Cost", "Price", "Payment")) # using formatting
for house in HouseList:
    print("{0:<15}{1:<15}{2:<15.2f}{3:<15.2f}{4:<15.2f}".format(house.address, house.sqft, house.costpersqft(), house.price, house.payment(interest, years)))
