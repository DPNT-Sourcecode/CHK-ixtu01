import re
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Check toA see if there are invlaid chars before we execute
    if charRange(skus) and whiteSpace(skus):
        # Sort the array of items and add offers
        value = addOffer(sort(list(skus)))
        print(value)
    else:
        value = -1
    return value


# Applying offers
def addOffer(list):

    itemA = 'A'
    itemB = 'B'
    itemC = 'C'
    itemD = 'D'
    itemE = 'E'
    itemF = 'F'

    # Convert string into list
    listA = createLists(list, itemA)
    listB = createLists(list, itemB)
    listC = createLists(list, itemC)
    listD = createLists(list, itemD)
    listE = createLists(list, itemE)
    listF = createLists(list, itemF)

    # Sort out the deals here
    totalA = sum(x.count(itemA) for x in listA)
    totalB = sum(x.count(itemB) for x in listB)
    totalC = sum(x.count(itemC) for x in listC)
    totalD = sum(x.count(itemD) for x in listD)
    totalE = sum(x.count(itemE) for x in listE)
    totalF = sum(x.count(itemF) for x in listF)

    costA = 0
    costB = 0
    costC = 0
    costD = 0
    costE = 0
    costF = 0
    nodealB = 0

    if itemA in list:
        normal = 0
        nodeal = 0
        nodealA = 0
        four = 0
        three = 0
        five = 5
        countListA = [listA[i:i + five] for i in range(0, len(listA), five)]
        # print(listA)
        # print(countListA)
        counterA = [len(x) for x in countListA if x != ""]
        # How man 5 deals
        deal5 = counterA.count(5)
        # How many 3 deals
        nodealA = totalA - (deal5 * 5)

        if nodealA == 4:
            nodealA = (nodealA - 3)
            four = nodealA
            normal = 1
        elif nodealA == 3:
            three = 1
        elif nodealA == 2:
            normal = 2
        elif nodealA == 1:
            normal = 1

        # Calculate Total
        costA = (deal5 * 200) + (four * 130) + (three * 130) + (normal * 50)
    if itemB in list:
        offer = 2
        countListB = [listB[i:i + offer] for i in range(0, len(listB), offer)]
        counterB = [len(x) for x in countListB if x != ""]
        dealB = counterB.count(2)
        nodealB = totalB - dealB * 2
        costB = (dealB * 45) + (nodealB * 30)
    if itemC in list:
        costC = totalC * 20
    if itemD in list:
        costD = totalD * 15
    if itemE in list:
        offer = 2
        countListE = [listE[i:i + offer] for i in range(0, len(listE), offer)]
        counterE = [len(x) for x in countListE if x != ""]
        deal2 = counterE.count(2)
        costE = totalE * 40
        if deal2 != 0 and nodealB != 0:
            offerB = nodealB * 30
            costB = costB - offerB
        elif deal2 != 0 and totalB != 0:
            ans = (totalB - deal2)
            costB = (ans * 30)
    if itemF in list:
        offer = 2
        nodeal = 0
        countListF = [listF[i:i + offer] for i in range(0, len(listF), offer)]
        counterF = [len(x) for x in countListF if x != ""]
        deal = counterF.count(2)
        nodeal = counterF.count(1)
        costF = totalF * 10
        if(deal >= 1 and totalF > 3 and nodeal > 1):
            reduce = (totalF/deal) * 10
            costF = costF - reduce
        elif(nodeal > 0 and totalF > 1):
            costF = costF - nodeal*10
        elif(nodeal == 0 and ((totalF/deal) * 10)/costF == 0):
            deal = deal - 1
            costF = costF - deal*10

    total = costA + costB + costC + costD + costE + costF
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
def charRange(strg, search=re.compile(r'[^A-F.]').search):
    return not bool(search(strg))


# Regex check
def whiteSpace(strg, search=re.compile(r'[^\S\n\t]').search):
    return not bool(search(strg))


checkout("FFFF")
