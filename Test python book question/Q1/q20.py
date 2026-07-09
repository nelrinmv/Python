# Q1.20
count = {
    'Unit':1,
    'Tenth':10,
    'Hundedth':100
}
for key, value in count.items():
    print('{0:10} ==> {1:10d}'.format(key,value)) #Output: Unit       ==>          1<newline>Tenth      ==>         10<newline>Hundedth   ==>        100
