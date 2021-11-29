path_to_folder = 'code/pete/python/examples/file_io/'
with open(path_to_folder + 'fire-and-ice.txt', 'r') as f:
    print(f, type(f)) # f is a fileIO wrapper
    text = f.read()
    # lines = f.readlines()
    # lines = f.read().split('\n')

print(text)
# print(lines)