import re

text = "My numbers are 10, 20, 30 and 40"

result = re.findall(r"\d+", text)

print(result)
