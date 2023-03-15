# 230315

# 크로아티아 알파벳


counting = 0
strings = input()
counting += strings.count('c=')
counting += strings.count('c-')
counting += strings.count('dz=')
counting += strings.count('d-')
counting += strings.count('lj')
counting += strings.count('nj')
counting += strings.count('s=')
counting += strings.count('z=')

print(len(strings)-counting)
