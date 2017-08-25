motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(0k)
print(motorcycles)
print(popped_motorcycle)
