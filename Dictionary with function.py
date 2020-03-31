def returnSum(dict):
    sum=0
    for i in dict:
        sum=sum+dict[i]
    return sum
dict={'Rick':85,'Amit':42,'George':53,'Tanya':60,'Linda':35}
print 'sum:', returnSum(dict)
