import re

#print(r'\tTab')

text_to_search = """
myText
myAnotherText
myThirdText
Hello
abc
cdef
def
"""

# See the difference between this 2.
# \t Gives us a tab.
# However, the r tells Python to not treat the backslash with
# any kind of special way.

print("\tTab")
print(r"\tTab")

# Hence, we can apply remove the backslash effects with the r here
pattern = re.compile(r"abc")

# finditer returns an iterator.
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)



# What is the backslash character for in Python? \
# \t is tab, \n is newline, \r is carriage return
# Furthermore, pre-fixing a special character will turn it ordinary
# myString = "It\'s raining", will be correct. 

pattern = re.compile(r'.')
# The period here is actually a special character to find ALL characters
# If we want a match that has a literal period, we will need
pattern = re.compile(r'\.')

# List of simple regex commands
# . - Any character except new Line
# \d - any digit 0-9
# \D - Not a Digit 0-9
# \w - Word Character(a-z, A-Z, 0-9, _ )
# \s - whitespace (space,tab,newline)
# \S - Not whitespace (space,tab, newline)

# \b - Word boundary ( The beginning or end of a word. This means a whiteSpace or start of a line )
# \B - Not a word boundary
# ^ - Beginning of a String
# $ - End of a string 

## Practice 1, we need to match : XXX-XXX-XXXX, where the X's are numbers
practice1Input = """
555-333-2222
4444-444-3333
444-4444-33333
222-2222-2222222
Hello
"""
patternPractice1 = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
matches = patternPractice1.finditer(practice1Input)
for match in matches: print(match)

# Learning Point 1 
# Note that iterating through an iterator will exhaust it. It will not work for the below
# function. 
for match in matches: print(match)

# Learning Point 2
# You can always do this : .\d\d\d\d-\d\d\d-\d\d\d\d.
# The periods will allow you to grab the whole string.

# Learning Point 3
# [-.] - dash or a dot.
# [98] - Single 9 or 8.
# The bracket [] will OR the characters inside the bracket
# for a SINGLE character 
# \d\d\d[-.]\d\d\d\d[-.]\d\d\d

# Learning Point 4
# a-z
# 1-5 / 1-9 / 1-2, can also specify ranges.
# [a-zA-Z1-9]
# However, when you have the caret ^, [^a-ZA-Z] inside the bracket
# it will match everything NOT INSIDE the brackets!


# Quantifiers. Matches the expression to the left.
##  * - 0 or more
##  + - 1 or more
##  ? - 0 or One
##  {3} - Exact Number
##  {3,4} - Range of Numbers ( Minimum, Maximum )

# Numbers
pattern = re.compile(r'\d{3}.\d{4}.\d{4}')
# is equivalent to
pattern = re.compile(r'\d\d\d.\d\d\d\d.\d\d\d\d')

# Practice 2 with quantifiers
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
myInput = """
Mr. Schafer
Mr Smith
Mr. T
"""
# Problem 1 :
# We need deal with the optional period .
# Hence, r'Mr\.?' will make sure its optional

# Problem 2 :
# The person's first name must start with a letter, from A-Z
# capitalized.
# Furthermore, the name can either be a single letter, or a word.
# Hence, \s[A-Z], followed by \w*, which means word 0 or more times.
# Genius solution

# Groups
# https://docs.python.org/3/library/re.html#regular-expression-syntax
# ( abc | def )
# This is just the [], but with the whole word.
# so this is either 'abc' OR 'def'.

# Furthermore, having grouped things, we can now reference the groups

# Practice 3 :
urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r'https?://(www\.)?\w+\.(com|gov)')
# Hence, the first group handles whether www exists or not
# However, we now want the domain name to be in a group.
pattern = re.compile(r'https?://(www\.)?(\w)+\.(com|gov)')
# Like this, we can reference the domain groups.

newUrls = pattern.sub(r'\2\3',urls) # Reference group 2 and group 3
# Group 0 is the entire match!!!
print(newUrls)

# You can do this for the iteration also
matches = pattern.finditer(urls)
for match in matches:
    print(matches.group(0))
    print(matches.group(1))
# If the group does not exist, then it'll just exist there.

# google.com
# coreyms.com   
# youtube.com
# nasa.gov

# useful functions
# findAll
# match - Find from the start
# search - Find anywhere
# ignore casing

# FLAGS
# re.I or re.IGNORECASE
pattern = re.compile(r'https?://(www\.)?\w+\.(com|gov)', re.I)






















