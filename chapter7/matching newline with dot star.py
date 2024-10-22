
import re
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())



noNewlineRegex = re.compile('.*',re.DOTALL)
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
