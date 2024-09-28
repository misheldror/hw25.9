
temperatures: list[float] = []
SENTINAL: int = -999
max_t = None
min_t = None

while True:
    t: float = int(input("Enter temperature: "))
    if -50 <= t <= 50:
        temperatures.append(t)
    temperatures.extend(-20.0, 39.1, 18.5)
    if min_t is None or max_t > t :
        print(f"highest temperature is {max_t}")
    if max_t is None or min_t < t:
        print(f"lowest temperature is {min_t}")
    if t == SENTINAL:
        break

#ההבדל הוא שבextend משנים את הרשימה שאותה הרחבנו בלבד לעומת + שזה חיבור של הרשימות יחד לרשימה חדשה אחרת

print(18.5 in temperatures)

print(f" 20 is {temperatures.count(20.0)} times on the list")

print(f" av temperature: {sum(temperatures) / len(temperatures)}")

for t in temperatures:
    print(t)

print(f" the index of 39.1: {temperatures.index(39.1)}")

del temperatures[0]

print(temperatures[0::2])

18.5 in temperatures
temperatures.remove(18.5)

temp_last: float = temperatures.pop(len(temperatures))
print(f"last temperature: {temp_last}")

temperatures2 = temperatures.copy()
print(temperatures2.sort())

temperatures3n = temperatures2.copy()
print(temperatures3n[-1::-1])

