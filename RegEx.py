import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
