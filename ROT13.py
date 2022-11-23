import codecs

def rot13(message):
    return codecs.decode(message,'rot-13')
