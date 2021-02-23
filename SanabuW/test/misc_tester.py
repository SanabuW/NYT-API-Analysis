
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

if list1 != []:
    print("OK!")
else:
    print("NG!")



for i, j in zip(list1, list2):
    print(f'{i} and {j}!')



engine = create_engine('postgresql://[username]:[password]@[host]/[databaseName]')
connection = engine.connect()


