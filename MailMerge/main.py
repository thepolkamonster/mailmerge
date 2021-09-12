with open("names.txt") as names:
    all_names = names.readlines()

with open("Letter.txt" ) as lfile:
    letter=lfile.read()

for x in all_names:
    fname=x.strip()
    new = letter.replace("[name]", fname)
    with open(f"{fname}.txt","w+") as fout:
        fout.write(new)





