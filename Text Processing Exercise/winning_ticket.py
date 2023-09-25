tickets = [ticket.strip() for ticket in input().split(', ')]

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')

    else:
        left = ticket[:10]
        right = ticket[10:]
        for symbol in winning_symbols:
            if symbol in left and symbol in right:
                if symbol in left == symbol * 10 and symbol in right == symbol * 10:
                    print(f'ticket "{ticket}" - {left.count(symbol)}{symbol} Jackpot!')
                elif symbol * 6 in left:
                    print(f'ticket "{ticket}" - {left.count(symbol)}{symbol}')
                else:
                    print(f'ticket "{ticket}" - no match')




