# http://mathworld.wolfram.com/Machin-LikeFormulas.html

from math import atan, pi, fabs
if __name__=="__main__":
    n = min(int(raw_input("Enter number of digits of pi: ")), 51)
    ans = ("{0:.%df}"%n).format(4 * (4 * atan(1.0/5.0) - atan(1.0/239.0)))
    print ans
    print "Abs difference:",fabs(float(ans) - pi)
