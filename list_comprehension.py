# List Comprehension
[n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
## [2, 6, 10, 14, 18]

# if not,
a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)
## [2, 6, 10, 14, 18]

# else, Dictionary Comprehension
a = {}
for key, value in original.items():
    a[key] = value

# same as
a = {key: value for key, value in original.items()}
