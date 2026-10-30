#String methods
text = "hello python"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

text2 = " Hello World "
print(text2.strip())

text = "I like Java, Java is my life"
print(text.replace("Java", "Python"))
print(text.split())
text = "apple,banana,orange"
print(text.split(","))
text = "I like Java, Java is my life"
temp = text.split()
print(" ".join(temp))
print(text.find("Java"))
print(text.count("a"))



