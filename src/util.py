import random, string

def random_string(len):
   chars = [random.choice(string.ascii_lowercase) for i in range(len)]
   return ''.join(chars)
