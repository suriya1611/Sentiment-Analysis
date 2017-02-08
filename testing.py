from replacers import SpellingReplacer
import enchant
input="i ahve nt done"
input_list=input.split(" ")
replacer=SpellingReplacer()
length=len(input_list)
print length
i=0
dGB=enchant.Dict('en_GB')
while i<length:
    if not dGB.check(input_list[i]):
        input_list[i]=replacer.replace(input_list[i])
    i=i+1
print str(input_list)