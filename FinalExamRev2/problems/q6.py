# return the sqrt with the amount of digits to the right of the dot
# limited to precision given
# You cannot use the sqrt function in the maths module 
def getSqrt(n, precision):
#---------------------
# Your JOB HERE 
#---------------------


# ---------------------
# Main Program
# ---------------------
arr = [10, 100, 3030];
for x in arr:
    val = getSqrt(x, 5);
    print("Sqrt of " + str(x) + ": " + str(val));
