import os
clear = lambda:os.system('clear')
clear()

def myFun(score, lang):
    print("I score %d in %s"%(score, lang))

# myFun("CPP", 100) this will throw an error becuase argument is not in order
myFun(lang = "Python", score = 90) # this will work because we use keyword argument
