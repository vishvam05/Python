cars=[
    {'year':2000,'car':'bmw'},
    {'year':2015,'car':'audi'},
    {'year':2012,'car':'mercedez'},
    {'year':1968,'car':'volvo'}
]
def myfunc(x):
   return x['year']
cars.sort(key=myfunc)
print(cars)