#Disorganised page lists
def find_page_number(pages):
    i=1
    a=[]
    for j in pages:
        if i!=j:
            a.append(j)
            continue
        i+=1
    return a
