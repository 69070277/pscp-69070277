"""lab"""
def main():
    """lab"""
    dic = []
    for _ in range(5):
        text = input()
        dic.append(text)
    for i in range(5):
        while True:
            if not dic[i]:
                break
            if (dic[i])[0]!= " " and (dic[i])[-1]!= " ":
                break
            if (dic[i])[0]== " ":
                dic[i] = (dic[i])[1:]
            if (dic[i])[-1]== " ":
                dic[i] = (dic[i])[:-1]
    most = max(len(dic[0]),len(dic[1]),len(dic[2]),len(dic[3]),len(dic[4]))
    print("*"*(most+4))
    for i in range(5):
        print("* "+dic[i]+" "*(most-len(dic[i])+1)+"*")
    print("*"*(most+4))
main()
