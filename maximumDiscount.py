def MaximumDiscount(quantityOfGoods, prices):
    sortedPrices = sorted(prices)
    baseDiscount = 0
    if(quantityOfGoods < 3):
        return 0
    if(quantityOfGoods == 3):
        return min(prices)
        
    def minPrice(prices):
        return min(prices)
        
    if(quantityOfGoods > 3):
        freeGoodsQuantity = len(prices)//3
        baseDiscount = sum(sortedPrices[0:freeGoodsQuantity])
