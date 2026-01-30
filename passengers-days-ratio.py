passengers = input("Number of Passengers: ").strip()
days = input("Number of Days: ").strip()
average = int(passengers)/int(days)
print(f"Average Number of Passengers: {average}")
while True:
    rate = input("How many days until you reach ___ Passengers?")
    real_rate = int(rate)/int(average)
    print(f"It will take {real_rate} days to reach {rate} passengers.")