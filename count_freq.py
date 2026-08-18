def count_freq(s,target):
    count = 0
    for ch in s:
        if ch == target:
            count += 1
    return count
s = input("enter a string")
target = input("enter a target")
res = count_freq(s,target)
print(f"the frequency of {target} is {res}")