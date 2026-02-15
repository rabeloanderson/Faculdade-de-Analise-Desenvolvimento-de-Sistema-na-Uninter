# Strings base
ant = 'ant'
bat = 'bat'
cod = 'cod'

# a) 'ant bat cod'
print(ant + ' ' + bat + ' ' + cod)

# b) 'ant ant ant ant ant ant ant ant ant '
print((ant + ' ') * 9)

# c) 'ant bat bat cod cod cod'
print(ant + ' ' + (bat + ' ') * 2 + (cod + ' ') * 2 + cod)

# d) 'ant bat ant bat ant bat ant bat ant bat ant bat '
print((ant + ' ' + bat + ' ') * 6)

# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
print((bat + bat + cod + ' ') * 5)
