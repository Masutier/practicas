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
    milking = []
    for x in vacasColl.find():
        milking.append(x)

    day1 = int(milking[0]["0"][0]) + int(milking[0]["0"][1])
    day2 = int(milking[0]["1"][0]) + int(milking[0]["1"][1])
    tot1 = day1 + day2

    print("week 1:", milking[0])
    print("week 1 day 1:", milking[0]["0"])
    print("week 1 day 2:", milking[0]["1"])
    print("Total production week 1 day 1:", day1, " Liters")
    print("Total production week 1 day 2:", day2, " Liters")
    print("*" * 40)
    print("Total production week 1:", tot1, " Liters")


def updateReg(docId, dayUp, cow1Up, cow2Up):
    from bson.objectid import ObjectId
    _id = ObjectId(docId)

    updates = {
        "$set": {dayUp: [cow1Up, cow2Up]}
    }

    vacasColl.update_one({"_id": _id}, updates)


def deleteReg(docId):
    from bson.objectid import ObjectId
    _id = ObjectId(docId)

    vacasColl.delete_one({"_id": _id})



#("******************************************")

for x in vacasColl.find():
    print(x)

# CREATE DOCUMENT
#milkingCows()

# LIST ALL
listAll()

# UPDATE
#docId = input("Id of Week to Update: ")
#dayUp = input("Day to Update (0 ~ n): ")
#cow1Up = input("Cow 1 Production: ")
#cow2Up = input("Cow 2 Production: ")
#updateReg(docId, dayUp, cow1Up, cow2Up)

# DELETE
#docId = input("Delete week: ")
#deleteReg(docId)

for x in vacasColl.find():
    print(x)
