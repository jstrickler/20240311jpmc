s1 = "spam\n"   # all 4 are the same
s2 = 'spam\n'
s3 = """spam\n"""  # triple quotes
s4 = '''spam\n'''

print("Guido's the ex-BDFL of Python")
print()
print('Guido is the ex-"BDFL" of Python')
print()
print("""Guido's the ex-"BDFL" of Python""")

sql_statement = """
select *
from customers
where balance > 10500
order by zip_code
"""

# raw string
s3 = r"spam\n"
print(s3)




