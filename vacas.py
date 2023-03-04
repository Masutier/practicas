import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
vacasdb = client["vacasdb"]
vacasColl = vacasdb["milking"]


def milkingCows():
    days = int(input("Milking Days: "))
    cows = int(input("Number of cows: "))
    milkingTot = {}

    for day in range(days):
        print("Day ", day + 1)
        milkingDay = []

        for cow in range(cows):
            milking = input("Liters of milk produced by cow #" + str(cow + 1) + " on day " + str(day + 1) + ": ")
            milkingDay.append(milking)
        
        milkingTot[str(day)] = milkingDay
    
    todb = vacasColl.insert_one(milkingTot)
    print("Save to mongodb ", milkingTot)


def listAll():

    for x in vacasColl.find():
        print(x)



listAll()
