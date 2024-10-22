import re
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))



agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that AgentEve knew Agent Bob was a double agent.'))
