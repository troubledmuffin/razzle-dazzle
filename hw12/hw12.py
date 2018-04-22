import os
def file_list():
    path = '.'
    files = os.listdir(path)
    i = 0
    a = []
    symbols="""(-),.:;"'—»«!?"""
    for f in files:
        base, ext = os.path.splitext(f)
        for b in base:
            for s in symbols:
                if s in b:
                    i+=1
                    a.append(base)
              
    print(i)
    print(a)

print(file_list())
