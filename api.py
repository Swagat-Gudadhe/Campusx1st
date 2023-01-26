import paralleldots

paralleldots.set_api_key('ZZb9jnRY6lYTP2BEA2JaHAXmdn7jmh2H9wYc5GrBwH0')

def ner(text):
    ner =paralleldots.ner(text)
    return ner
