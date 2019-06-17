import re
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Check to see if there are invlaid chars before we execute
    if charRange(skus) and whiteSpace(skus):
        value = basket(skus)
    else:
        value = -1

    return value


# Regex check
def charRange(strg, search=re.compile(r'[^A-D.]').search):
    return not bool(search(strg))


# Regex check
def whiteSpace(strg, search=re.compile(r'[^\S\n\t]').search):
    return not bool(search(strg))


# Basket of items
def basket(skus):

    # Convert string into list
    cart = sort(list(skus))
    nested_list_A = []
    nested_list_B = []
    nested_list_C = []
    nested_list_D = []
    itemAPrice = 50
    itemBPrice = 30
    itemCPrice = 20
    itemDPrice = 15
    itemA = 'A'
    itemB = 'B'
    itemC = 'C'
    itemD = 'D'
    valueA = 0
    valueB = 0
    valueC = 0
    valueD = 0

    # Sort the list into separate lists
    for i in range(len(cart)):
        if cart[i] == itemA:
            nested_list_A.append(cart[i])
        elif cart[i] == itemB:
            nested_list_B.append(cart[i])
        elif cart[i] == itemC:
            nested_list_C.append(cart[i])
        elif cart[i] == itemD:
            nested_list_D.append(cart[i])

    # With the sorted lists get their values
    if itemA in skus:
        valueA = getTotal(nested_list_A, itemA, itemAPrice)
    if itemB in skus:
        valueB = getTotal(nested_list_B, itemB, itemBPrice)
    if itemC in skus:
        valueC = getTotal(nested_list_C, itemC, itemCPrice)
    if itemD in skus:
        valueD = getTotal(nested_list_D, itemD, itemDPrice)

    # Add all the values and return the total
    cartTotal = valueA + valueB + valueC + valueD
    return cartTotal


#  Calculate totals and offers if they apply
def getTotal(list, item, price):
    offerPrice = 1
    itemTotal = 0
    # Apply and calculate totals for each item
    if item == 'A':
        offerPrice = 130
        itemTotal = addOffer(list, item, 3, price, offerPrice)
    elif item == 'B':
        offerPrice = 45
        itemTotal = addOffer(list, item, 2, price, offerPrice)
    elif item == 'C':
        itemTotal = addOffer(list, item, 1, price, offerPrice)
    elif item == 'D':
        itemTotal = addOffer(list, item, 1, price, offerPrice)
    else:
        itemTotal = addOffer(list, item, 1, price, offerPrice)

    return itemTotal


# Applying offers
def addOffer(list, item, offer, price, offerPrice):
    total = 0
    # Count the size of each sublist - create sublists of offers
    list = [list[i:i + offer] for i in range(0, len(list), offer)]
    # Count how manu items there are in all lists
    totalSum = sum(x.count(item) for x in list)
    # Count how many deals there are for this item in the list
    counter = [len(x) for x in list if x != ""]
    if offer == 3:
        deal = counter.count(3)
        newOffer = deal * offerPrice
        nodeal = (totalSum - (deal * 3)) * price
        total = newOffer + nodeal
    elif offer == 2:
        deal = counter.count(2)
        newOffer = deal * offerPrice
        nodeal = (totalSum - (deal * 2)) * price
        total = newOffer + nodeal
    else:
        nodeal1 = counter.count(1)
        total = (nodeal1 * price)

    return total


# Sort list
def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst]
    return lst
