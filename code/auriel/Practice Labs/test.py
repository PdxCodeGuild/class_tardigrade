sorted_socks = {'ankle' : 23, 'crew' : 21, 'calf' : 28, 'thigh' : 28}

if 'ankle' in sorted_socks:
        num = sorted_socks.get('ankle')
        if num % 2 == 0:
            sorted_socks['ankle'] = num / 2
        else:
            div = (num - 1) / 2
            sorted_socks['ankle'] = div
            sorted_socks['ankle loners'] = num - (num - 1)



for key in sorted(sorted_socks.keys()):
    print('%s: %s' % (key, sorted_socks[key]))