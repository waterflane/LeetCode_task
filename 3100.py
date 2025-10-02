def numWaterBottles(numBottles: int, numExchange: int) -> int:
    drinked = 0 
    numNullBottles = 0
    while True:
        drinked += numBottles 
        numNullBottles += numBottles
        numBottles = 0

        if numNullBottles >= numExchange:
            numBottles += 1
            numNullBottles = numNullBottles - numExchange
            numExchange += 1
        else: return drinked
            

print(numWaterBottles(13, 6))
