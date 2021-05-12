import re

emails = """

saminsakur@bangladesh.com
samin.sakur@myschool.edu
samin820@bangla.com.bd
samin-29-2016@my-work.net

"""

# pattern = re.compile(r"[a-zA-Z.0-9-]+@[a-zA-Z-]+\.[a-zA-Z0-9-.]+")  # this can also be used
pattern = re.compile(r"[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(com|net|edu)(\.bd)?")
matches = re.finditer(pattern, emails)
for i in matches:
    print(i)