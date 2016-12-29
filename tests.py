from golombo_codding import encode, decode
import random

# m = 2
# print(m)
# array = [5, 3, 7, 1, 10]
# print(array)
# encoded = encode(array, m)
# print(encoded)
# decoded = decode(encoded, m)
# print(decoded)


for i in range(100):
    print(i, 'is started')
    m = random.choice([1, 2, 4, 8, 7, 3, 6])
    print('m:', m)
    array = [random.randint(1, 10) for _ in range(5)]
    print(array)
    encoded = encode(array, m)
    print(encoded)
    decoded = decode(encoded, m)
    print(decoded)
    assert array == decoded
    print(i, 'is completed')
