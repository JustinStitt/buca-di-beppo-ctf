import sys

file_name = sys.argv[1]
ans_file = open(file_name)
assert(ans_file is not None)

raw_dat = ans_file.read()

out = ''
allowed = {'1', '2', '3', '4'}
for c in raw_dat:
    out += c if c in allowed else ''

print(out)
