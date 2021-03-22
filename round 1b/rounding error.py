# your code goes here
import sys

name = "input1"
path = ""

sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

import math
def get_ints():
    ret = tuple(map(int, input().strip().split()))
    # print(ret)
    return ret
def app(n):
    if n - int(n) >= 0.5:
        return math.ceil(n)
    else: return math.floor(n)

def solve_case(t):
    total_people, total_lang = get_ints()
    people = list()
    people = list(get_ints())
    total_people_in_list = sum(people)
    percent = list()
    for i in range(total_lang):
        percent.append(app(people[i]*100/total_people))
    rem = total_people - total_people_in_list
    final1 = sum(percent) + rem * app(100/total_people)
    final2 = 0
    for pos in range(total_lang):
        people[pos] = people[pos] + rem
        temp = percent[pos]
        percent[pos] = app(people[pos]*100/total_people)
        ans = sum(percent)
        if ans > final2:
            final2 = ans
        percent[pos] = temp

    if final1 > final2:
        print("Case #%d: %d" % (t, final1))
    else:
        print("Case #%d: %d" % (t, final2))


def main():
    t = get_ints()[ 0 ]
    for i in range(1, t + 1):
        solve_case(i)


try:
    main()
except Exception as e:
    print(e)