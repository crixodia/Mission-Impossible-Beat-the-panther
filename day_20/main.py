enteros = [1, 2, 3, 4, 5, 6, 7, 9, 10, 12]


def find_missing(nums: list) -> int:
    last = nums[0]
    missing = []
    for i in range(1, len(nums)):
        if last + 1 != nums[i]:
            missing.append(last + 1)
        last = nums[i]
    
    return missing

print(enteros)
print(find_missing(enteros))