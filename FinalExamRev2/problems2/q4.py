# Tell if the array is in ascending order
# You should modify BLANK LINES ONLY!
def isAscending(arr):
    if len(arr)<=1:
        return True;
    else:
        partialArr = arr[1: len(arr)];
        if arr[0]>arr[1]:
            return False;
        return isAscending(partialArr);

# ----------------------------
# Main Program. Do NOT touch!!!
# ----------------------------
arr2d = [
    [1, 2, 3, 4, 5],
    [2, 3, 5, 4, 1],
    [3, 4, 5, 6, 100],
    [200, 100, 3, 5, 7],
    [1, 2, 3, 5, 4],
    [5, 4, 6, 7, 8]
];
for id in range(len(arr2d)):
    arr = arr2d[id];
    val = isAscending(arr);
    print("Arr"+str(id) + ": " + str(val));
