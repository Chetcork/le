age = 24
print("my age is {0} years".format(age))

print("there are {0} days in {1}, {2}, {3}, {4},{5},{6} and {7}"
      .format(31,"jan", "mar","may","jul","aug","oct","dec"))
print("there are {0} days in jan, mar, may, jul, aug, oct and dec".format(31))

print("jan: {2}, feb: {0}, mar: {2}, apr: {1}, may: {2}, jun: {1}, jul: {2}, sep: {1}, oct: {2}, nov: {1}, dec: {2}"
      .format(28, 30, 31))

print()

print("""jan: {2}
feb: {0}
mar: {2}
apr: {1}
may: {2}
jun: {1}
jul: {2}
sep: {1}
oct: {2}
nov: {1}
dec: {2}""".format(28,30,31))