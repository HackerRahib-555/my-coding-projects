files = ["Button_Save.txt", "Light_record.txt", "Temprature_record.txt", "Humidity_record.txt", "Distance_record.txt"]
for f in files:
    open(f, "w").close()  
print("Clearing successful.")