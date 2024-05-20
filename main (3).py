name = input()

if " " in name:
  first, second = name.split(" ")
  caps1 = first[0].upper() + first[1:]
  caps2 = second[0].upper() + second[1:]
  print(caps1, caps2)
elif " " not in name:
  caps3 = name[0].upper() + name[1:]
  print(caps3)

