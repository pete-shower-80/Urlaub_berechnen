## First Baby Steps in Python :-)
## Tool to calculate the vacation-days for an worker

def vacation_days():
    basic_vacation = 26
    under18_vacation = 30
    vacation = 0    
    
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("The age can`t be negative.")
            break
        except ValueError:
            print("Please Enter a valid number.")

    while True:
        gdb50_input = input("Do you have a disability grade 50% or higher? (yes/no): ").lower()
        if gdb50_input in ['no', 'yes']:
            gdb50 = gdb50_input == 'yes'
            break
        else:
            print("Please enter 'yes' or 'no'.")

    while True:
        over10_input = input("Are you employed 10 years or more? (yes/no): ").lower()
        if over10_input in ['yes', 'no']:
            over10 = over10_input == 'yes'
            break
        else:
            print("Please enter 'yes' or 'no'.")

    if age < 18:
        vacation = under18_vacation
        if gdb50:
            vacation += 5
        if over10:
            vacation += 2
    else:
        vacation = basic_vacation
        if gdb50:
            vacation += 5
        if over10:
            vacation += 2

    print(f"Your vacation time: {urlaub} days.")    

vacation_days()
