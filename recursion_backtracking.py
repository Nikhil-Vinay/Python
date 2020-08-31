# Print all valid parenthesis combination of a given length n

print("Provide the length of parenthesis")
n = int(input())

def print_parenthesis(open_bracket, closed_bracket, n, s, pos):
    if(closed_bracket == n):
    	#print(s) // it will print list
        print("".join(s))
        return
    else:
    	if(open_bracket > closed_bracket):
            s[pos] = ")"
            print_parenthesis(open_bracket, closed_bracket+1, n, s, pos+1)
        if(open_bracket < n):
            s[pos] = "("
            print_parenthesis(open_bracket+1, closed_bracket, n, s, pos+1)
            
            
#s = list();  # equivalent to s = [] # empty list
open_bracket = 0
closed_bracket = 0
pos = 0
# initialize a list of 2*n empty string
s = [""] * 2 * n
print_parenthesis(open_bracket, closed_bracket, n, s, pos) 
