import operator
def word_count(str):
    count=dict()
    w=str.split()
   # d=sorted(w)
    for a in w:
        if a in count:
            count[a] += 1
        else:
            count[a] =1
    return count

string=input("Enter the string: ")
c=word_count(string)
sorted_x=sorted(c.items(),key=operator.itemgetter(0))
print(sorted_x)
