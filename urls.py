import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r"https?://(www\.)?([A-Za-z]+)(\.\w+)")

matches = re.finditer(pattern, urls)

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)
# for match in matches:
#     print(match.group(1))