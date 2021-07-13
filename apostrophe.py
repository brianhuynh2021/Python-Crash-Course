# Avoiding Syntax Errors with Strings
# One kind of error that you might see with some regularity is a syntax error.
# A syntax error occurs when Python doesn’t recognize a section of your pro-
# gram as valid Python code. For example, if you use an apostrophe within
# single quotes, you’ll produce an error. This happens because Python inter-
# prets everything between the first single quote and the apostrophe as a
# string. It then tries to interpret the rest of the text as Python code, which
# causes errors.

msg = "One of Python's strengths is its diverse community."
print(msg)
msg = 'One of Python's strengths is its diverse community.'