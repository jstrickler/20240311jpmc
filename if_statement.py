value = -14

# Python IDES:  vscode intellij+ext pycharm spyder eclipse sagemaker
# Python notebook: Jupyter Lab (notebooks, +++) 
#   (2nd tier)  sublime atom etc 

# if elif else while for with def class  

if value > 75:
    print("kangaroo")
    print("koala")
elif value > 50:
    print("platypus")
    print("quokka")
    if value > 60:
        print("kookaburra")
elif value:   # is value T or T
    print("weird??")
else:
    print("wombat")
    print("wallaby")

print("ALL DONE")


#  False values:
#  None
#  False  (builtin number)
#  0 or 0.0  (numeric zero)
#  len(x) == 0  (len of container is zero)

# True False

#   if x == True:      # is x == 1  DON'T DO THIS
#   if x:              # is x true   YES YES YES

shout = True

text =  "HEY YOU!" if shout else "hey you!" 

if shout:
    text = "HEY YOU!"
else:
    text = "hey you!"



print(f"{text = }")

#   text = shout ? "HEY YOU!" : "hey you!"    ternary operator

#  == != > < >= <=




