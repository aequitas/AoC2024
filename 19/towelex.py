import regex as re

IN = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

REGEX = re.compile = r"((r|wr|b|g|bwu|rb|gb|br)(?=\1))"
# REGEX = re.compile = r"(?=(r|b|g))"
# REGEX = re.compile = r"brwrr"

towels = IN.splitlines()[0].split(", ")

designs = [x for x in IN.splitlines()[2:] if x]

for design in designs:
    print(design)
    print(re.findall(REGEX, design, overlapped=True))
