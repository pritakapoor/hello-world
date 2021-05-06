#Prita Kapoor
#8010339

from datetime import datetime


class InventoryItem:
    def __init__(self, id, name, itemType, isDamaged):
        self.itemID = id
        self.itemName = name
        self.itemType = itemType
        self.isDamaged = isDamaged
        self.itemPrice = 0.0
        self.serviceDate = datetime.now()

    def serviceDateToString(self):
        return str(self.serviceDate.month) + "/" + str(self.serviceDate.day) + "/" + str(self.serviceDate.year)

    def __str__(self):
        string = str(self.itemID + ", " + self.itemName + ", " + self.itemType + ", " +
                     str(self.itemPrice) + ", " + str(self.serviceDate.month) + "/" + str(
            self.serviceDate.day) + "/" + str(self.serviceDate.year))
        if self.isDamaged != '\n':
            string += ", " + self.isDamaged[:-1]
        return string

    def __eq__(self, other):
        return self.itemID == other.itemID and self.itemName == other.itemName and self.itemType == other.itemType and self.itemPrice == other.itemPrice and self.serviceDate == other.serviceDate and self.isDamaged == other.isDamaged
