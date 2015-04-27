'''Pyg latin is an assignment on codeacademy where we take a word, put the first letter at the end and add ay at the end.
Fun way to start with the basics of python'''

pyg = 'ay'  //the ay to be added to the end!

original = raw_input('Enter a word:') //take a word input from the user

if len(original) > 0 and original.isalpha()://check whether entered word is legit!
    print original
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print "The new word:" + new_word
else:
    print 'empty'
