#an example of quine in python: Mallika Prabhakar
quote=chr(34)
comma=chr(44)
tab='    '
lst=["#an example of quine in python: Mallika Prabhakar",
    "quote=chr(34)",
    "comma=chr(44)",
    "tab='    '",
    "lst=[",
    "]",
    "for index in range(0,4):",
    "    print(lst[index])",
    "print(lst[4]+quote+lst[0]+quote+comma)",
    "for index in range(1,len(lst)-1):",
    "    print(tab+quote+lst[index]+quote+comma)",
    "print(tab+quote+lst[-1]+quote)",
    "for index in range(5,len(lst)):",
    "    print(lst[index])"
]
for index in range(0,4):
    print(lst[index])
print(lst[4]+quote+lst[0]+quote+comma)
for index in range(1,len(lst)-1):
    print(tab+quote+lst[index]+quote+comma)
print(tab+quote+lst[-1]+quote)
for index in range(5,len(lst)):
    print(lst[index])