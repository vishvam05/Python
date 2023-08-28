cities=['meerut','dehli','ghaziabad','mumbai']
cities.sort(key=len)
print('cities after sorting by length',cities)
cities.sort(key=len,reverse=True)
print('cities after sorting by length but in descending order',cities)