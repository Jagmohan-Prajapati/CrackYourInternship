def find_dup(string):
    x=[]
    for i in string:
        if i not in x and string.count(i)>1:
            x.append(i)
    print(" ".join(x))