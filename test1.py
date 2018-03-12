def get_issuer(number):
    a = {'AMEX':[[34, 37], [15]],'Discover': [[6011], [16]],'Mastercard': [[51, 52, 53, 54, 55], [16]],'VISA': [[4], [13, 16]]}
    number=str(number)
    j=1
    while j<5:
        for keys, values in a.items():
            if len(number) in values[1] and int(number[0:j]) in values[0] :
                return keys
        j+=1
    return 'Unknown'

print(get_issuer(4111111111111111))