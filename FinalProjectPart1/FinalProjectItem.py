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

    # def __gt__(self, otherItem):
    #     return self.itemName > otherItem.itemName
    #
    # def __lt__(self, otherItem):
    #     return self.itemName < otherItem.itemName
    #
    #
    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value

    def serviceDateToString(self):
        return str(self.serviceDate.month) + "/" + str(self.serviceDate.day) + "/" + str(self.serviceDate.year)

    def __str__(self):
        string = str(self.itemID + ", " + self.itemName + ", " + self.itemType + ", " +
                     str(self.itemPrice) + ", " + str(self.serviceDate.month) + "/" + str(
            self.serviceDate.day) + "/" + str(self.serviceDate.year))
        if self.isDamaged != '\n':
            string += ", " + self.isDamaged[:-1]
        return string
