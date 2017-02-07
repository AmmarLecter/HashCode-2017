#!/usr/bin/env python3

from collections import namedtuple

point = namedtuple('Point', ['x', 'y'])
rectangle = namedtuple('Rectangle', ['up_left', 'down_right'])

def parse():
    r, _, l, h = map(int, input().split())
    p = [list(map(lambda c: int(c=='M'), input())) for _ in range(r)]
    return p, l, h

def output(d):
    print(len(d))
    for (r1,c1),(r2,c2) in d: print(r1, c1, r2, c2)

def score(d):
    return sum(get_area(rect) for rect in d)

def psum(p):
    ps = [[0]*(len(p[0])+1) for _ in range(len(p)+1)]
    for r in range(len(p)):
        for c in range(len(p[0])):
            ps[r+1][c+1] = p[r][c] + ps[r][c+1] + ps[r+1][c] - ps[r][c]
    return ps

def get_area(rect):
    return (abs(rect.up_left.x - rect.down_right.x) + 1) * (abs(rect.up_left.y - rect.down_right.y) + 1)

def get_zeros_and_ones(rect, pizza):
    up_left, down_right = rect
    ones = pizza[down_right.x+1][down_right.y+1] - pizza[up_left.x][down_right.y+1] - pizza[down_right.x+1][up_left.y] + pizza[up_left.x][up_left.y]
    zeros = get_area(rect) - ones
    return zeros, ones

def valid(rect, pizza, l, h):
    if get_area(rect) > h:
        return False
    zeros, ones = get_zeros_and_ones(rect, pizza)
    if (zeros < l) or (ones < l):
        return False
    return True

def main():
    p, l, h = parse()
    ps = psum(p)
    for i in p:
        print(i)
    print()
    for i in ps:
        print(i)
    print()
    rect = rectangle(point(1, 2), point(2, 3))
    print(rect, get_area(rect), get_zeros_and_ones(rect, ps), valid(rect, ps, l, h))
    #output([((1,2),(3,4))])

if __name__ == '__main__': main()
