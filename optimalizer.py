import sys

help : str = 'USAGE:\n \tpython optimalizer.py source_file excluded_modules_file'
modules_file_help: str = 'MODULE FILE USAGE:\n \t[moduleA]\n\t[moduleB]\n\t[moduleN]'

try:
    print(sys.argv[1])
    src_file = open(sys.argv[1], 'r')
    modules_file = open(sys.argv[2], 'r')
except:
  print(help)
  exit() 


modules : list[str] = modules_file.readlines()
for module in modules:
    if module[0] != '[' and (module[-2] != ']' or module[-1] != ']'):
        print(modules_file_help)
        exit() 
    

lines : list[str] = src_file.readlines()
out : list[str] = []

is_cleaning : int = 0
for line in lines:
    for c in line:
        if c == '{' : 
            is_cleaning += 1
        elif c == '}':
            is_cleaning -= 1
    is_matched : bool = False
    for module in modules:
        if module in line:
            is_matched = True
            if is_cleaning != 0:
                out.append(line)
    if is_matched == False:
        out.append(line)

out_file = open('optimalized.plantuml', 'w')
out_file.writelines(out)

print('File saved as: optimalized.plantuml')