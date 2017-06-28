#!/usr/bin/env python
import sys

def replaceInLine(old, new_, l):
    if old in l:
        l = l.replace(old, new_)
    return l


name = sys.argv[1].split(".")[0]
ext = sys.argv[1].split(".")[1]
new_filename = name + "_new." + ext
with open(new_filename, "w+") as newf:
    with open(sys.argv[1]) as f:
        for line in f:


            # This cannot be done in a more inefficient way,
            # but it was easier to type!
            line = replaceInLine("212,a", "12#,b", line)
            line = replaceInLine("24,a", "212#,a", line)
            line = replaceInLine("30,a", "212#,b", line)
            line = replaceInLine("50,a",  "24#,a", line)
            line = replaceInLine("65,a",  "30#,a", line)
            line = replaceInLine("69,a",  "24#,b", line)
            line = replaceInLine("75,a",  "30#,b", line)
            line = replaceInLine("12,b",  "50#,a", line)
            line = replaceInLine("212,b", "50#,b", line)
            line = replaceInLine("24,b",  "65#,a", line)
            line = replaceInLine("30,b",  "65#,b", line)
            line = replaceInLine("50,b",  "69#,a", line)
            line = replaceInLine("65,b",  "75#,a", line)
            line = replaceInLine("224,a", "4#,b",  line)
            line = replaceInLine("38,a", "224#,a", line)
            line = replaceInLine("57,a", "224#,b", line)
            line = replaceInLine("4,b",   "38#,a", line)
            line = replaceInLine("224,b", "38#,b", line)
            line = replaceInLine("38,b",  "57#,a", line)
            line = replaceInLine("210,a", "10#,b", line)
            line = replaceInLine("22,a", "210#,a", line)
            line = replaceInLine("44,a", "210#,b", line)
            line = replaceInLine("63,a",  "22#,a", line)
            line = replaceInLine("10,b",  "22#,b", line)
            line = replaceInLine("210,b", "44#,a", line)
            line = replaceInLine("22,b",  "44#,b", line)
            line = replaceInLine("44,b",  "63#,a", line)
            line = replaceInLine("228,a",  "8#,b", line)
            line = replaceInLine("28,a", "228#,a", line)
            line = replaceInLine("34,a", "228#,b", line)
            line = replaceInLine("48,a",  "28#,a", line)
            line = replaceInLine("61,a",  "34#,a", line)
            line = replaceInLine("8,b",   "28#,b", line)
            line = replaceInLine("228,b", "34#,b", line)
            line = replaceInLine("28,b",  "48#,a", line)
            line = replaceInLine("34,b",  "48#,b", line)
            line = replaceInLine("48,b",  "61#,a", line)
            line = replaceInLine("67,a",  "52#,b", line)
            line = replaceInLine("52,b",  "67#,a", line)


            line = replaceInLine("#", "", line)
            newf.write(line)