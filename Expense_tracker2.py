#ExpenseTracker2.0
#greeting 
class Expense:
    #used for a single expense 
    def __init__(self,item,cost,categ,des):
      self.item = item 
      self.cost = cost 
      self.categ = categ 
      self.des = des 
      
    def __str__(self):
      return f"Item:{self.item}\nAmmount:{self.cost}\nCategory:{self.categ}\nDescription:{self.des}"

class ExpenseTracker:
   #this will help with the process
    def __init__(self):
        self.expenses = []
    def options(self):
        print("=========WELCOME TO EXPENSE TRACKER ========")
        print("1.add your expense ")
        print("2.view all expense")
        print("3.calculate total expense")
        print("4.Exit")

        print("=======================================")
        
    def add(self):
        
        item = input("Enter the item you want to add: ")
        while True:
            try:
                cost = int(input("Enter the cost :$"))
                if cost<0:
                    print("Cost cannot be negative.")
                    continue
                break
            
            except ValueError:
                print("Eror:integers only!!")
                
            
        categ = input("Explain the category:")
        des = input("Describe the product:")
        new_expense = Expense(item,cost,categ,des)
        self.expenses.append(new_expense)
        print("Your expense is added succesfully✨🤗")
        

    def view(self):
        if len(self.expenses)== 0:
            print("no expenses added")
        else:
            for new_expense in self.expenses:
                print(new_expense)

    def calculate(self):
        if len(self.expenses) == 0:
            print("No expenses to calculate!")
            return
        total = 0
        for new_expense in self.expenses:
            total =  new_expense.cost + total
            print("Total Expense:$",total)

#Actualprocess            
work = ExpenseTracker()
while True:
    work.options()
    try:
        choice= float(input("choose your option:")) 
        
        if choice == 1:
            work.add()
        elif choice ==2:
            work.view()
        elif choice == 3:
            work.calculate()
        elif choice == 4:
            print("Good bye ")
            break
        else:
            print("Invalid choice! Please choose from 1 to 4.")
    except ValueError:
       print("Please enter an whole number.")

    
     
       

        
            
        
