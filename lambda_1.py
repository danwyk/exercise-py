def name_and_alias(name,alias):
    return name.strip().title() + ': ' + alias.strip().title()

print(name_and_alias('     john ClEEse  ','HECKLER        '))


name_alias = lambda name, alias: name.strip().title() + ": " + alias.strip().title()
print(name_alias("     dAniEL WANg  ", "   tHe ChoSEN onE  "))