def transfer(degit):
    words=["zero","one","two","three","four","five"]
    if 0<=degit<=5:
        return words[degit]
    else:
        return "invalid"
degit=int (input("enter degit "))
w=transfer(degit)
print("the word of degit",degit,"is",w)
