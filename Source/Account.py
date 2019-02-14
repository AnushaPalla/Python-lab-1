import sys
total = 0
for line in sys.stdin:
    parts = line.split(' ')
    if parts[0] == 'Deposit':
        total += int(parts[1])
    elif parts[0] == 'Withdraw':
        total -= int(parts[1])
    else:
        continue
print('Total = ' + str(total))
