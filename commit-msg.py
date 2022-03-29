#!/usr/bin/python
import sys
import re

import submodules.rules as rules


def main():
    with open(sys.argv[1], 'r') as fp:
        lines = fp.readlines()

        for idx, line in enumerate(lines):

            if line.strip() == "# ------------------------ >8 ------------------------":
                break

            if line[0] == "#":
                continue
                    
            line_valid(idx, line)
            
    
    sys.exit(0)

# return re.match("^[A-Z].{,48}[0-9A-z \t]$", line)





def line_valid(idx, line):
    if idx == 0:
        if not re.match("^[A-Z]", line):
            print(rules.rule_intro)
            print(rules.rule_cap)
            sys.exit(1)
        if line.strip().endswith('.'):
            print(rules.rule_intro)
            print(rules.rule_period)
            sys.exit(1)
        
        if line.strip() > 50:
            print(rules.rule_intro)
            print(rules.rule_50)
        
    if idx == 1:
        return len(line.strip()) == 0
    else:
        return len(line.strip()) >= 72


def show_rules():
    print(rules)

if __name__ == '__main__':
    main()
