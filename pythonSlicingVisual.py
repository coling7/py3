__author__ = "@coling7"
__version__ = "11/3/2016"

# v EDIT THESE VARIABLES
word = "Hello world!";
start = None; # Can be set to int or None
end = 5; # Can be set to int or None

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

print("\n\nword[" + (str(start) != "None" and str(start) or "") + ":" + (str(end) != "None" and str(end) or "") + "] is", word[start:end], end = "\n\n")
