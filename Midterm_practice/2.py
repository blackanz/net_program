days = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
        'May': 31, 'June': 30, 'July': 31, 'August': 31,
        'September': 30, 'October': 31, 'November': 30,
        'December': 3}

print(sorted(days.keys()))  # A

print(sorted(days.items(), key=lambda x: x[1]))  # B

inp = input()
if len(inp) == 3:
  for k in days:
    if k.startswith(inp):
      print(days[k])
