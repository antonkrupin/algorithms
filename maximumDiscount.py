def MaximumDiscount(quantityOfGoods, prices):
    #sortedPrices = sorted(prices)
    baseDiscount = 0
    if(quantityOfGoods < 3):
        return 0
    if(quantityOfGoods == 3):
        return min(prices)
        
    def minPrice(prices):
        return min(prices)
        
    if(quantityOfGoods > 3):
        freeGoodsQuantity = len(prices)//3
        baseDiscount = sum(prices[-freeGoodsQuantity:])
        print(baseDiscount)
        print(prices)
        

print(MaximumDiscount(7,[250,400,100,50,25,15,175]))
