def MaximumDiscount(quantityOfGoods, prices):
    if(quantityOfGoods < 3):
        return 0
    if(quantityOfGoods == 3):
        return min(prices)
        
    def minPrice(prices):
        return min(prices)
        
    if(quantityOfGoods > 3):
        sortedPrices = sorted(prices,reverse = True)
        baseDiscount = 0
        slicedPrices = []
        
        freeGoodsQuantity = len(prices)//3
        baseDiscount = sum(sortedPrices[-freeGoodsQuantity:])
        pointer = 0
        
        for x in range(len(sortedPrices)):
            p = sortedPrices[pointer:pointer+3]
            if(len(p) == 3):
                slicedPrices.append(p)
            pointer += 3
        
        discount = 0
        
        for x in range(len(slicedPrices)):
            discount += min(slicedPrices[x])
        
        if(discount >= baseDiscount):
            return discount
        else:
            return baseDiscount
