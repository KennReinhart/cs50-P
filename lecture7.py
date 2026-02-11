email = input("Enter your email: ")

# Validation without regular expressions
if "@" in email and "." in email:
    print("Your email is valid\n")
else:
    print("Your email is invalid\n")

username, domain = email.split("@")
print("Your username is " + username)
print("Your domain is " + domain)

if username and domain.endswith(".edu"):
    print("Email Valid\n")
else:
    print("Email Invalid\n")

# Using re library, regular expression library
'''
. any char except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
"\\" special sequence
r raw input
^ matches the start of the string
$ matches the end of the string or just before the newline in str
[] set of characters
[^] complementing the set, example:
    [^@], every char except @ is allowed
\\ d decimal digit
\\ D not a decimal digit
\\ s whitespace char
\\ S not a whitespace char
\\ w word char
\\ W not a word char
'''
import re

# email = input("Enter your email: ")
while True:
    try:
        email = input("Enter your email: ").strip()
        # any char except @ then @ sign + one or more things to the left then any char except @ then .edu end
        #^[^@]]+@[^@].+\\.edu$
        #[] set of char.
        #[a-zA-Z0-9_] + @ [a-zA-Z0-9_] + \\.edu$
        # re.IGNORECASE and .lower(), one ignores the case and lower the input so its all lowercase first.
        # or just use libraries
        if re.search("^(\\w|\\.)+@\\w+\\.edu$", email):
            print("Your email is valid\n")
        else:
            print("Your email is invalid\n")
        break
    except ValueError:
        print("Your email is invalid\n")




