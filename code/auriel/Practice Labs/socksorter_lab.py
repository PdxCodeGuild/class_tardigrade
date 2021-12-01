import random 

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_collection = []
socks = 100

def sock_chooser():
    for i in range(socks):
        sock_collection.append(random.choice(sock_types))
    return sock_collection

def sock_sorter():
    collection = sock_chooser() 
    count = {}
    for i in collection:
        if not i in count:
            count[i] = 1
        else:
            count[i] += 1
    print(count)
    return count

def sock_pairs():
    sorted_socks = sock_sorter()
    
    if 'ankle' in sorted_socks:
        num = sorted_socks.get('ankle')
        if num % 2 == 0:
            sorted_socks['ankle'] = num / 2
        else:
            sorted_socks['ankle'] = (num - 1) / 2
            sorted_socks['ankle loners'] = num - (num - 1)
    
    if 'crew' in sorted_socks:
        num = sorted_socks.get('crew')
        if num % 2 == 0:
            sorted_socks['crew'] = num / 2
        else:
            sorted_socks['crew'] = (num - 1) / 2
            sorted_socks['crew loners'] = num - (num - 1)

    if 'calf' in sorted_socks:
        num = sorted_socks.get('calf')
        if num % 2 == 0:
            sorted_socks['calf'] = num / 2
        else:
            sorted_socks['calf'] = (num - 1) / 2
            sorted_socks['calf loners'] = num - (num - 1)

    if 'thigh' in sorted_socks:
        num = sorted_socks.get('thigh')
        if num % 2 == 0:
            sorted_socks['thigh'] = num / 2
        else:
            sorted_socks['thigh'] = (num - 1) / 2
            sorted_socks['thigh loners'] = num - (num - 1)

    for key in sorted(sorted_socks.keys()):
        print('%s: %s' % (key, sorted_socks[key]))

sock_pairs()