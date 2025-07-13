#What will be the output of the following Python code?

def test_output():
    result = []
    for i in range(3):
        result.append(lambda i : i*2)
    return [f() for f in result]

print(test_output())

#Predict the output of code below

#def build_functions():
#    funcs = []
##    for i in range(4):
 #       funcs.append(lambda i = i : i)
 #   return funcs

#f_list = build_functions()
#output = [f() for f in f_list]
#print(output)

#fix the bug

#def create_multipliers():
 #   return [lambda x, i=i: i*x for i in range(3)]

#multipliers = create_multipliers()
#print([f(2) for f in multipliers])