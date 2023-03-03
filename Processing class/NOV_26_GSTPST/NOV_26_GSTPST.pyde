import Ask

def setup():
    totalAmount = getTotal()
    totalGST = calculateGST(totalAmount)
    totalPST = calculatePST(totalAmount)
    displayFinalSummary(totalAmount, totalGST,totalPST)
    
def getTotal():
    firstValue = Ask.forFloat("How much is the first item?")
    secondValue = Ask.forFloat("How much is the second item?")
    total = firstValue + secondValue
    return total

#calculate GST function receives an amount and returens gst payable
def calculateGST(amount):
    gstTax = amount * 0.05
    return gstTax

def calculatePST(amount):
    pstTax = amount * 0.08
    return pstTax

def displayFinalSummary(total,gst,pst):
    """
    final = float(total) + float(gst) + float(pst)
    return final
    """
    print "The total is : " + str(total)
    print "The GST is: " + str(gst)
    print "The PST is : " + str(pst)
