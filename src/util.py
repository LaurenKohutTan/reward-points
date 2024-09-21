import random, string

# Generate a random string of length len using lowercase ASCII letters
def random_string(len):
   chars = [random.choice(string.ascii_lowercase) for i in range(len)]
   return ''.join(chars)
