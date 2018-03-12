#Credit card issuer checking
def get_issuer(number):
    a = {'AMEX':[[34, 37], [15]],'Discover': [[6011], [16]],'Mastercard': [[51, 52, 53, 54, 55], [16]],'VISA': [[4], [13, 16]]}
    b=str(number)
    j=1
    res='Unknown'
    while j<5:
        for keys, values in a.items():
            if len(b) in values[1] and int(b[0:j]) in values[0] :
                return keys
        j+=1
    return res