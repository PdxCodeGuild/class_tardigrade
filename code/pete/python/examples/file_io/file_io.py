path_to_folder = 'code/pete/python/examples/file_io/'
with open(path_to_folder + 'fire-and-ice.txt', 'r', encoding='utf-8') as f:
    print(f, type(f)) # f is a fileIO wrapper
    text = f.read()
    # lines = f.readlines()
    # lines = f.read().split('\n')

    print(text)
    # print(lines)
    text = text.upper()

    print(text)

with open(path_to_folder + 'FIRE-AND-ICE-IMPROVED.txt', 'w', encoding='utf-8') as f:
    f.write(text)