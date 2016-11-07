__author__ = "@coling7"
__version__ = "11/3/2016"

# v EDIT THESE VARIABLES
word = "Hello world!";
start = None; # Can be set to int or None
end = 5; # Can be set to int or None
step = 1; # >0 is forwards, <0 is backwards

print("\n ", end = '')
for i in range(len(word) + 1):
	print(i, " " * (3 - len(str(i))), end = '')
print("\n ", end = '')
for i in word:
	print("+---", end = '')
print("+\n ", end = '')
for i in word:
	print("|", i + " ", end = '')
print("|\n ", end = '')
for i in word:
	print("+---", end = '')
print("+")
for i in range(-len(word), 0):
	print(i, " " * (3 - len(str(i))), end = '')

print("\n\nword[" + (str(start) != "None" and str(start) or "") + ":" + (str(end) != "None" and str(end) or "") + (step != 1 and (":" + str(step)) or "") + "] is", word[start:end:step], end = "\n\n")
