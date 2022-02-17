#!/usr/bin/env python3
import timeit
# get b, z, n from user
# b^x = z (mod n)

print("This will solve the following equation for x")
print("b^x = z (mod n)")

b = int(input("Please enter the b term: "))
z = int(input("Please enter the z term: "))
n = int(input("Please enter the n term: "))

print("Solving ...")
start = timeit.default_timer()
x = 1
while pow(b, x, n) != (z % n):
    print(f"{b}^{x} = {z} (mod {n}) => {pow(b, x, n)} = {z} (mod {n}) => {pow(b, x, n)} = {z % n}")
    x += 1
end = timeit.default_timer()
print("Found x = %d, took %.4f seconds" % (x,(end - start)))
print(f"b^x = z (mod n) => {b}^{x} = {z} (mod {n}) => {pow(b, x, n)} = {z} (mod {n}) => {pow(b, x, n)} = {z % n}")
