people = []

def data():
    number = int(input("Enter number of people: "))
    for i in range(number):
        name = input("Enter name of person: ")
        amount = float(input(f"How much did {name} pay ?"))
        people.append([name, amount])

cal_share = lambda total, count: total/count

def split():
    total_amount = 0
    for p in people:
        total_amount = total_amount + p[1]

    number_of_people = len(people)
    share = cal_share(total_amount, number_of_people)

    print("\nTotal amount: ",total_amount)
    print("Each should pay: ",share)
    print("\n Final Contribution")

    for p in people:
        name = p[0]
        paid = p[1]
        diff = paid - share

        if diff > 0:
            print(f"{name} should receive, {diff}")
        elif diff < 0:
            print(f"{name}, should pay, {diff}")
        else:
            print(f"{name}, is settled ")

print("Let's split the bill")
data()
split()        