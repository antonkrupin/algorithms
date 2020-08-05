def MaximumDiscount(quantityOfGoods, prices):
    sortedPrices = sorted(prices)
    baseDiscount = 0
    slicedPrices = []
    if(quantityOfGoods < 3):
        return 0
    if(quantityOfGoods == 3):
        return min(prices)
        
    def minPrice(prices):
        return min(prices)
        
    if(quantityOfGoods > 3):
        freeGoodsQuantity = len(prices)//3
        baseDiscount = sum(sortedPrices[:freeGoodsQuantity])
        pointer = 0
        
        for x in range(len(prices)):
            p = prices[pointer:pointer+3]
            if(len(p) == 3):
                slicedPrices.append(prices[pointer:pointer+3])
            pointer += 3
            
        discount = 0
        
        for x in range(len(slicedPrices)):
            discount += min(slicedPrices[x])
        
        if(discount >= baseDiscount):
            return discount
        else:
            return baseDiscount

print(MaximumDiscount(9,[250,400,50,100,25,175,15,85,500]))
