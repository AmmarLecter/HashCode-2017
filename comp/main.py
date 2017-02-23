#!/usr/bin/env python

def parse():
    pass

def out(cached):
    for idx, server in enumerate(cached):
        print idx
        print ' '.join(map(str, server))

def greedy():
    pass

def main():
    parse()
    out()

if __name__ == "__main__": main()
