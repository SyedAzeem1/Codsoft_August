#Task 3: To create a password generator allpication using python
import  string
import random
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.punctuation
s4 = string.digits
passlen = int(input("Enter length of password:\n"))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("".join(random.sample(s,passlen)))