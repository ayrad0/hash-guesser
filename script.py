import hashlib
import itertools
import re

# Original input strings
input1 = "4812824d-1543-4218-9f6b-aae0b2f164d7@email.webhook.site"
input2 = "17735234"

# Simple concatenation of the original inputs, hashed 10 times
simple_concat = input1 + input2
hashed_concat = simple_concat
for i in range(10):
    hashed_concat = hashlib.md5(hashed_concat.encode()).hexdigest()

# Generate all possible complex concatenations using the original inputs
concatenations = []
for p in itertools.product(input1, input2, repeat=2):
    concat = ''.join(p)
    for i in range(1, len(concat)):
        for c in itertools.combinations(concat, i):
            c1 = ''.join(c)
            c2 = ''.join(list(reversed(c)))
            concatenations.extend([concat, c1, c2])
            pattern = re.compile(f"{re.escape(input1)}.*{re.escape(c1)}.*{re.escape(input2)}")
            rconcat = pattern.findall(concat)
            if rconcat:
                concatenations.extend(rconcat)
            rconcat = pattern.findall(c1)
            if rconcat:
                concatenations.extend(rconcat)
            rconcat = pattern.findall(c2)
            if rconcat:
                concatenations.extend(rconcat)

# Add the hashed simple concatenation to the concatenations list
concatenations.append(hashed_concat)

# Hash all the concatenations in the list
hash_values = [hashlib.md5(concat.encode()).hexdigest() for concat in concatenations]

# Match the hashed concatenations with a given input
given_input = "6b177620afc94df990c0c2c94a96243f"
if given_input in hash_values:
    print("The given input matches a hashed concatenation.")
else:
    print("The given input does not match any hashed concatenation.")

