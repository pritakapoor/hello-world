#Prita Kapoor
#8010339

import locale
from FinalProjectInput2 import InventoryItem
from datetime import datetime
import math


def readIn():
    manufacturerFile = open("ManufacturerList.csv")
    manufacturerFileData = manufacturerFile.readlines()

    count = 0
    for items in manufacturerFileData:
        lineParsed = items.split(",")
        manufacturerFileData[count] = InventoryItem(lineParsed[0].replace(" ", ""), lineParsed[1].replace(" ", ""),
                                                    lineParsed[2].replace(" ", ""), lineParsed[3].replace(" ", ""))
        count += 1

    # open the price list file and assign the price list data to the file
    priceListFile = open("PriceList.csv")
    priceListData = priceListFile.readlines()

    count = 0
    for line in priceListData:
        priceListData[count] = line.split(",")

        for item in manufacturerFileData:
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

        for item in manufacturerFileData:
            # print(item.getID() + ' ' + priceListData[count][0])
            if item.__getattribute__('itemID') == serviceDateFile[count][0]:
                dateObj = datetime.strptime(serviceDateFile[count][1][:-1], '%m/%d/%Y')
                item.__setattr__('serviceDate', dateObj)

        count += 1

    serviceDateFileName.close()

    return manufacturerFileData


def binSearchByItemName(manData, key):
    mid = math.floor(len(manData) / 2)
    hi = len(manData) - 1
    lo = 0
    locIndex = -1
    found = False

    while lo <= hi and not found:
        if manData[mid].itemName < key:
            lo = mid + 1
            mid = math.floor((hi + lo) / 2)
        elif manData[mid].itemName > key:
            hi = mid - 1
            mid = math.floor((hi + lo) / 2)
        else:
            found = True
            locIndex = mid

    return locIndex


def binSearchByItemCategory(manData, key):
    mid = math.floor(len(manData) / 2)
    hi = len(manData) - 1
    lo = 0
    locIndex = -1
    found = False

    while lo <= hi and not found:
        if manData[mid].itemType < key:
            lo = mid + 1
            mid = math.floor((hi + lo) / 2)
        elif manData[mid].itemType > key:
            hi = mid - 1
            mid = math.floor((hi + lo) / 2)
        else:
            found = True
            locIndex = mid

    return locIndex


def main():
    manufacturerData = readIn()
    promptManufacturer = " "

    while promptManufacturer.capitalize() != 'Q':
        promptManufacturer = input("Enter the manufacturer and itemType (press 'q' to quit): ")
        promptManufacturerInput = promptManufacturer.split(' ')

        if promptManufacturer.capitalize() == 'Q':
            break

        manufacturerData.sort(key=lambda InventoryItem: InventoryItem.itemName)

        count = 0
        manufactNameNdx = -1
        manufactNameNdxInput = 0
        while manufactNameNdx == -1 and count < len(promptManufacturerInput):
            manufactNameNdx = binSearchByItemName(manufacturerData, promptManufacturerInput[count])
            manufactNameNdxInput = count
            count += 1

        foundFirst = False
        foundSearchItem = manufacturerData[count]
        if manufactNameNdx != -1 and manufactNameNdxInput < len(promptManufacturerInput) - 1:
            promptManufacturerInput[manufactNameNdxInput + 1] = promptManufacturerInput[manufactNameNdxInput + 1][
                                                                :1].lower() + promptManufacturerInput[
                                                                                  manufactNameNdxInput + 1][1:]
            for i in range(0, 2):
                count = manufactNameNdx
                while 0 <= count < len(manufacturerData) and manufacturerData[count].__getattribute__(
                        'itemName') == promptManufacturerInput[manufactNameNdxInput] and not foundFirst:
                    if manufacturerData[count].__getattribute__('itemType') == promptManufacturerInput[
                        manufactNameNdxInput + 1] and not manufacturerData[count].__getattribute__(
                        'isDamaged').__contains__("damaged") and manufacturerData[count].__getattribute__(
                        'serviceDate') > datetime.now():
                        if not foundFirst:
                            foundSearchItem = manufacturerData[count]
                            print("Your item is: ID: " + foundSearchItem.__getattribute__('itemID') +
                                  ', Manufacturer: ' + foundSearchItem.__getattribute__('itemName') +
                                  ', ItemType: ' + foundSearchItem.__getattribute__('itemType') +
                                  ', ItemPrice: ' + str(foundSearchItem.__getattribute__('itemPrice')))
                            foundFirst = True

                    if i == 0:
                        count += 1
                    else:
                        count -= 1

            if not foundFirst:
                print("No such item in Inventory")
        else:
            print("No such item in Inventory")

        if foundFirst:
            manufacturerData.sort(key=lambda InventoryItem: InventoryItem.itemType)
            itemTypeNdx = binSearchByItemCategory(manufacturerData, foundSearchItem.__getattribute__('itemType'))

            if itemTypeNdx != -1 and manufactNameNdxInput < len(promptManufacturerInput) - 1:
                print("\nYou may, also, consider:")
                for i in range(0, 2):
                    count = itemTypeNdx

                    if i != 0:
                        count -= 1

                    while count >= 0 and count < len(manufacturerData) and manufacturerData[count].__getattribute__(
                            'itemType') == promptManufacturerInput[manufactNameNdxInput + 1]:
                        if not manufacturerData[count].__getattribute__('isDamaged').__contains__("damaged") and \
                                manufacturerData[count].__getattribute__('serviceDate') > datetime.now():
                            foundItem = manufacturerData[count]

                            if not foundItem == foundSearchItem:
                                print("ID: " + foundItem.__getattribute__('itemID') +
                                      ', Manufacturer: ' + foundItem.__getattribute__('itemName') +
                                      ', ItemType: ' + foundItem.__getattribute__('itemType') +
                                      ', ItemPrice: ' + str(foundItem.__getattribute__('itemPrice')))

                        if i == 0:
                            count += 1
                        else:
                            count -= 1


if __name__ == '__main__':
    main()
