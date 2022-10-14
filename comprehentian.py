# # Set Comprehension
# x = set(i*2 for i in range(4) if i%2==0)
# print(x)
#
# x = set(i for i in [1,2,3,4] if i %2==0)
# print(x)
#
# x = set((a,b) for b in range(3) for a in range(4))
# print(x)
#
# #Dict Comprehension
# dict = {'a':1, 'b':2, 'c':3, 'd':4}
#
# new_dict_values = {k:v*2 for (k,v) in dict.items()}
# print(new_dict_values)
#
# new_dict_kyes = {k*2:v for (k,v) in dict.items()}
# print(new_dict_kyes)
#
# dict = {}
#
# for i in range(10):
#     if i%2==0:
#         dict[i]= i**2
#
# print(dict)
#
# dict = {i:i**2 for i in range(10) if i%2==0}
#print(dict)

# LAMBDA FUNCTION

# feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}
# cel = list(map(lambda x:(float(5)/9)*(x-32), feh.values()))
#
# cel_dict = dict(zip(feh.keys(), cel))
# print(cel_dict)
#
# feh1 = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}
#
# cel_dict = {k:(float(5)/9)*(v-32) for (k,v) in feh1.items()}
# print(cel_dict)


# dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
# new_dict1 = {k:v for (k,v) in dict1.items() if v>3}
# print(new_dict1)
# new_dict2 = {k:('even No' if v%2==0 else 'odd No') for (k,v) in dict1.items()}
# print(new_dict2)

# NESTED DICTIONARY COMPREHENSION

dict3 = {'one':{'a':10},'two':{'b':20}}

for (external_key, external_value) in dict3.items():
    for (internal_key, internal_value) in external_value.items():
        external_value.update({internal_key:float(internal_value)})
dict3.update({external_key:external_value})
print(dict3)
