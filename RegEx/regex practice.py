import re
from string import punctuation

def text_match(text):
        patterns = r"\s?[a-zA-Z0-9]+\s?"
        if re.search(patterns,  text):
                print(re.findall(patterns, text))
                return 'Found a match!'
        else:
                return 'Not matched!'


print(text_match('fds faAb, '))
print(text_match('sfd ggfdsfdasdfafdfdb'))
print(text_match('fsd sdfgdsf'))
print(text_match('fsfFFDffdFgfdf'))