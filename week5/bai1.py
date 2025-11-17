def remove_punctuation(chuoi):
    chuoixoa = ''
    for i in chuoi :
        if i.isalnum() or i in " " :
            chuoixoa += i
        else :
            continue
    return chuoixoa
def to_lower(chuoi):
    return chuoi.lower()
def remove_stopwords(chuoi, stopwords):
    tu = chuoi.split()
    xoatu = ''
    for i in tu:
        if i not in stopwords:
            xoatu += i + ' '
        else :
            continue
    return xoatu
def pipeline(chuoi,stopwords):
    chuoi = remove_punctuation(chuoi)
    chuoi = to_lower(chuoi)
    chuoi = remove_stopwords(chuoi,stopwords)
    return chuoi
def count_words(chuoi):
    lit = chuoi.split()
    demso = {}
    for i in lit:
        demso[i] = lit.count(i)
    return demso
chuoi = input("nhap chuoi : ")
stopwords = input("nhap chuoi dung : ").split()
chuoisua = pipeline(chuoi,stopwords)
print(f"chuoi sau chinh sua : {chuoisua}")
print(f"{count_words(chuoisua)}")