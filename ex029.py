speed = int(input("What is the speed of the car? "))
fine = (speed - 80) * 7
if speed <= 80:
    print(f"HAVE A GOOD TRIP! Drive carefully.")
else:
    print(f"YOU HAVE BEEN FINED! You will pay US${fine}.")
