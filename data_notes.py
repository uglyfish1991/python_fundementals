CamelCaseAnswer = ''
for w in str.split ('the cow jumps over the moon'):
  CamelCaseAnswer += w.capitalize() + ' '
CamelCaseAnswer = CamelCaseAnswer.strip()
print(CamelCaseAnswer)