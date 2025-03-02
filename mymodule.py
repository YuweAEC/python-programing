# import mymodule 
import mymodule as mx
import platform
# from mymodule import person1

def greeting(name):
    print("Hello, " + name)

mx.greeting("Yuvraj Singh")

person1 = {
    "name": "Yuvi",
    "age": 21,
    "country": "India"
}

a = mx.person1["country"]
print(a)

x = platform.system()
# x = dir(platform)

print(x)
