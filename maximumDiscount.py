def MaximumDiscount(quantityOfGoods, prices):
    b = sorted(prices,reverse = True)
    if(quantityOfGoods < 3):
        return 0
    if(quantityOfGoods == 3):
        return min(prices)
