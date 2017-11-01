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
            line = replaceInLine("V212,a", "V12#,b", line)
            line = replaceInLine("V212,b", "V50#,b", line)
            line = replaceInLine("V224,a", "V4#,b",  line)
            line = replaceInLine("V224,b", "V38#,b", line)
            line = replaceInLine("V210,a", "V10#,b", line)
            line = replaceInLine("V210,b", "V44#,a", line)
            line = replaceInLine("V228,a",  "V8#,b", line)
            line = replaceInLine("V228,b", "V34#,b", line)
            line = replaceInLine("V28,a", "V228#,a", line)
            line = replaceInLine("V28,b",  "V48#,a", line)
            line = replaceInLine("V24,a", "V212#,a", line)
            line = replaceInLine("V24,b",  "V65#,a", line)
            line = replaceInLine("V30,a", "V212#,b", line)
            line = replaceInLine("V30,b",  "V65#,b", line)
            line = replaceInLine("V50,a",  "V24#,a", line)
            line = replaceInLine("V50,b",  "V69#,a", line)
            line = replaceInLine("V65,a",  "V30#,a", line)
            line = replaceInLine("V65,b",  "V75#,a", line)
            line = replaceInLine("V38,a", "V224#,a", line)
            line = replaceInLine("V38,b",  "V57#,a", line)
            line = replaceInLine("V22,a", "V210#,a", line)
            line = replaceInLine("V22,b",  "V44#,b", line)
            line = replaceInLine("V44,a", "V210#,b", line)
            line = replaceInLine("V44,b",  "V63#,a", line)
            line = replaceInLine("V34,a", "V228#,b", line)
            line = replaceInLine("V34,b",  "V48#,b", line)
            line = replaceInLine("V48,a",  "V28#,a", line)
            line = replaceInLine("V48,b",  "V61#,a", line)
            line = replaceInLine("V69,a",  "V24#,b", line)
            line = replaceInLine("V75,a",  "V30#,b", line)
            line = replaceInLine("V12,b",  "V50#,a", line)
            line = replaceInLine("V57,a", "V224#,b", line)
            line = replaceInLine("V63,a",  "V22#,a", line)
            line = replaceInLine("V10,b",  "V22#,b", line)
            line = replaceInLine("V61,a",  "V34#,a", line)
            line = replaceInLine("V67,a",  "V52#,b", line)
            line = replaceInLine("V52,b",  "V67#,a", line)
            line = replaceInLine("V4,b",   "V38#,a", line)
            line = replaceInLine("V8,b",   "V28#,b", line)


            line = replaceInLine("#", "", line)
            newf.write(line)