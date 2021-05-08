#Prita Kapoor
#8010339

from FinalProjectItem import InventoryItem
from datetime import datetime
import locale


def main():
    # open the manufacturer list file
    manufacturingFile = open("ManufacturerList.csv")
    manufacturingData = manufacturingFile.readlines()

    count = 0
    for line in manufacturingData:
        manufacturingData[count] = line.split(",")
        manufacturingData[count] = InventoryItem(manufacturingData[count][0],
                                                 manufacturingData[count][1],
                                                 manufacturingData[count][2],
                                                 manufacturingData[count][3])
        count += 1

    manufacturingFile.close()

    # open the price list file and assign the price list data to the file
    priceListFile = open("PriceList.csv")
    priceListData = priceListFile.readlines()

    count = 0
    for line in priceListData:
        priceListData[count] = line.split(",")

        for item in manufacturingData:
            # print(item.getID() + ' ' + priceListData[count][0])
            if item.__getattribute__('itemID') == priceListData[count][0]:
                item.__setattr__('itemPrice', float(priceListData[count][1]))

        count += 1

    priceListFile.close()

    # open the service date file
    serviceDateFileName = open("ServiceDatesList.csv")
    serviceDateFile = serviceDateFileName.readlines()
    locale.setlocale(locale.LC_TIME, 'C')

    count = 0
    for line in serviceDateFile:
        serviceDateFile[count] = line.split(",")
        count += 1

    count = 0
    for line in serviceDateFile:

        for item in manufacturingData:
            # print(item.getID() + ' ' + priceListData[count][0])
            if item.__getattribute__('itemID') == serviceDateFile[count][0]:
                dateObj = datetime.strptime(serviceDateFile[count][1][:-1], '%m/%d/%Y')
                item.__setattr__('serviceDate', dateObj)

        count += 1

    serviceDateFileName.close()

    # open the full inventory output file
    fullInventoryOutFile = open("FullInventory.csv", "w")

    # sort the full inventory by the name of the item
    manufacturingData = sorted(manufacturingData, key=lambda InventoryItem: InventoryItem.itemName)

    # write the full inventory to file
    for lines in manufacturingData:
        fullInventoryOutFile.write(lines.__str__())
        fullInventoryOutFile.write('\n')

    fullInventoryOutFile.close()

    # create inventory file arrays
    inventoryFileArray = []
    for items in manufacturingData:
        fileName = items.__getattribute__('itemType').capitalize() + "Inventory.csv"
        tempFile = open(fileName, "w")

        found = False
        for files in inventoryFileArray:
            if files.name == fileName:
                found = True

        if found:
            tempFile.close()
        else:
            inventoryFileArray.append(tempFile)

    # sort the inventory by id
    manufacturingData = sorted(manufacturingData, key=lambda InventoryItem: InventoryItem.itemID)
    for item in manufacturingData:
        itemType = item.__getattribute__('itemType')
        for file in inventoryFileArray:
            if (file.name.__contains__(itemType.capitalize())):
                file.write(item.__getattribute__('itemID') + ", " + item.__getattribute__('itemName') + ", " + str(
                    item.__getattribute__('itemPrice')) + ", " + item.serviceDateToString())
                if item.__getattribute__('isDamaged') != '\n':
                    file.write(", " + item.__getattribute__('isDamaged'))
                file.write('\n')

    # close the inventory file array
    for files in inventoryFileArray:
        files.close()

    pastServiceFile = open("PastServiceDateInventory.csv", "w")

    # sort manufacturing data by date
    manufacturingData = sorted(manufacturingData, key=lambda InventoryItem: InventoryItem.serviceDate)

    count = 0
    for items in manufacturingData:
        if items.__getattribute__('serviceDate') < datetime.now():
            pastServiceFile.write(items.__str__())
            pastServiceFile.write('\n')
        count += 1

    pastServiceFile.close()

    damagedItemsFile = open("DamagedInventory.csv", "w")

    manufacturingData = sorted(manufacturingData, key=lambda InventoryItem: InventoryItem.itemPrice, reverse=True)

    for item in manufacturingData:
        if item.__getattribute__('isDamaged').__contains__("damaged"):
            damagedItemsFile.write(
                item.__getattribute__('itemID') + ", " + item.__getattribute__('itemName') + ", " + str(
                    item.__getattribute__('itemPrice')) + ", " + item.serviceDateToString())
            damagedItemsFile.write('\n')

    damagedItemsFile.close()

if __name__ == "__main__":
    main()
