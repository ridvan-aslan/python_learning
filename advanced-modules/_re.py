import re

# result = dir(re)

# re module

my_string = "My Python Course (40 Hours)"

# re.findall()

# result = re.findall("Python", my_string)
# result = len(result)

# re.split()

# result = re.split(" ", my_string)
# result = re.split("P", my_string)

# re.sub()

# result = re.sub(" ", "-", my_string)
# result = re.sub(r"\s", "-", my_string)

# re.search()

# result = re.search("Python", my_string)

# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string

# regular expression

result = re.findall("[a-e]", my_string)
result = re.findall("[PMy]", my_string)
result = re.findall("[A-Z]", my_string)
result = re.findall("[a-z]", my_string)
result = re.findall("[0-5]", my_string)
result = re.findall("[^My ]", my_string)
result = re.findall("[^0-5 ()]", my_string)

result = re.findall("...", my_string)
result = re.findall("Co..se", my_string)

result = re.findall("^My", my_string)
result = re.findall(r"\)$", my_string)
result = re.findall(r"Hours\)$", my_string)

result = re.findall("Pytho*n", my_string)
result = re.findall("Pytho*n", my_string)
result = re.findall("Pyt+hon", my_string)
result = re.findall("Pyt?hon", my_string)

result = re.findall("e{2}", my_string)
result = re.findall("[0-9]{2}", my_string)

result = re.findall("\AMy", my_string)
result = re.findall(r"Hours\Z", my_string)

print(result)