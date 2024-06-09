questions=[["Who developed Python Programming language?",
            "a.Wick van Rossum b.Rasmus Lerdorf c.Guido van Rossum d.Niene"],
           ["Which keyword is used for function in Python language",
            "a.Function,b.def,c.Fun,d.Define"],
           ["Which of the following character is used to give single-line comment",
            "a.// b.# c.! d./*"],
           ["Which of the following statement is used to create an empty set in Python",
            "a.() b.[] c.{} d.set()"],
           ["To add a new element to a list we use which Python command?",
            "a.list1.addEnd(5) b.list1.addLst(5) c.list1.append(5) d.list1.add(5)"]
           ]

print("Python quiz")
print("Choose the correct Answer",end="\n\n")

l=[]
for que in questions:
    cnt=0
    for i in range(len(que)):
        print(que[i])
    l.append(input())
    cnt=cnt+1
    print()
answers=['c','b','b','d','c']

counter=0

for ans in range(5):
    if answers[ans]==l[ans]:
        counter=counter+1
   
print("Your Total score is:",counter,"/5")

match counter:
    case 5:
        print("Fantastic, Keep it up")
    case _ if 2<counter<5:
        print("Very Nice")
    case _ if 0<=counter<=2:
        print("Betten Luck Next Time")

