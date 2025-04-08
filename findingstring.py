word = 'NMREC'

# returns first occurrence of Substring
result = word.find('EC')
print("Substring 'EC' found at index:", result)

# How to use find()
if word.find('EC') != -1:
	print("Contains given substring ")
else:
	print("Doesn't contains given substring")
