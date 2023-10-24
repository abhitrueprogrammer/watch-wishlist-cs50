from collections import OrderedDict
dictionary = {}
dictionary[5] = "Abhinav"
dictionary[15] = "Sumita"
dictionary2 = {}
OD = OrderedDict()
OD[5] = "Abhinav"
OD[15] = "Sumita"
OD2 = OrderedDict()
OD2[15] = "Sumita"
OD2[5] = "Abhinav"

dictionary2[15] = "Sumita"
dictionary2[5] = "Abhinav"
print(OD == OD2)
print(dictionary == dictionary2)