print("------------------- BATTERY LEVEL ------------------\n")
chargelevel = 10
for i in range(10, 101, 10):  
    print( "--------------- BATTERY LEVEL : ",chargelevel, "% ---------------")
    chargelevel = chargelevel + 10
print("\n--------------- BATTERY FULLY CHARGED ---------------")

## python -u "CLASSWORK_PYTHON/BATTERY CHARGING.py"
