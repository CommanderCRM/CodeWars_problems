import string

def pig_it(text):
    splitted = text.split()
    pigged = [word[1:] + word[0] + 'ay'
              if word not in string.punctuation
              else word for word in splitted]
    return ' '.join(pigged)
