import re
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Check to see if there are invlaid chars before we execute
    if charRange(skus) and whiteSpace(skus):
        # Sort the array of items and add offers
        value = addOffer(sort(list(skus)))
        print(value)
    else:
        value = -1
        print(value)
    return value


# Applying offers
def addOffer(list):

    itemA = 'A'
    itemB = 'B'
    itemC = 'C'
    itemD = 'D'
    itemE = 'E'
    # Convert string into list
    listA = createLists(list, itemA)
    listB = createLists(list, itemB)
    listC = createLists(list, itemC)
    listD = createLists(list, itemD)
    listE = createLists(list, itemE)

    # Sort out the deals here
    totalA = sum(x.count(itemA) for x in listA)
    totalB = sum(x.count(itemB) for x in listB)
    totalC = sum(x.count(itemC) for x in listC)
    totalD = sum(x.count(itemD) for x in listD)
    totalE = sum(x.count(itemE) for x in listE)

    costA = 0
    costB = 0
    costC = 0
    costD = 0
    costE = 0

    nodealA = 0
    nodealB = 0

    if itemA in list:
        # You have a problem when applying the offers here
        # Check if the 5 deal applies first
        if len(listA) >= 5:
            offer = 5
            countListA = [listA[i:i + offer] for i in range(0, len(listA), offer)]
            # Count how many deals there are for this item in the list
            counterA = [len(x) for x in countListA if x != ""]
            # How man 5 deals
            deal5 = counterA.count(5)
            # How many 3 deals
            deal3 = counterA.count(3)
            # Number of no deals
            nodealA = totalA - (deal5*5) - (deal3*3)
            # Calculate Total
            costA = (deal5*200) + (deal3*130) + (nodealA*50)
        # If nto apply just the three deal
        else:
            offer = 3
            countListA = [listA[i:i + offer] for i in range(0, len(listA), offer)]
            # Count how many deals there are for this item in the list
            counterA = [len(x) for x in countListA if x != ""]
            # How many 3 deals
            deal3 = counterA.count(3)
            # Number of no deals
            nodealA = totalA - (deal3*3)
            # Calculate Total
            costA = (deal3*130) + (nodealA*50)
    if itemB in list:
        offer = 2
        countListB = [listB[i:i + offer] for i in range(0, len(listB), offer)]
        counterB = [len(x) for x in countListB if x != ""]
        deal2 = counterB.count(2)
        nodealB = totalB - deal2*2
        costB = (deal2*45) + (nodealB*30)
    if itemC in list:
        costC = totalC*20
    if itemD in list:
        costD = totalD*15
    if itemE in list:
        offer = 2
        countListE = [listE[i:i + offer] for i in range(0, len(listE), offer)]
        counterE = [len(x) for x in countListE if x != ""]
        deal2 = counterE.count(2)
        costE = totalE * 40
        if deal2 != 0 and nodealB != 0:
            offerB = nodealB*30
            costB = costB - offerB

    total = costA + costB + costC + costD + costE
    return total


def createLists(cart, item):
    list = []
    for i in range(len(cart)):
        if cart[i] == item:
            list.append(cart[i])
    return list


# Sort list
def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst]
    return lst


# Regex check
def charRange(strg, search=re.compile(r'[^A-E.]').search):
    return not bool(search(strg))


# Regex check
def whiteSpace(strg, search=re.compile(r'[^\S\n\t]').search):
    return not bool(search(strg))
