def get_transactions(t):
    global transactions
    if t == 'print_it':
        for trans_type, info in transactions.items():
            print(f"{info['count']} {trans_type} {info['total']}")
    else:
        phone, trans = t.split('-')
        trans_type, amount = trans.split(':')
        amount = int(amount)

        if trans_type not in transactions:
            transactions[trans_type] = {'count': 1, 'total': amount}
        else:
            transactions[trans_type]['count'] += 1
            transactions[trans_type]['total'] += amount

transactions = {}

get_transactions('880005553535-перевод:100')
get_transactions('111111111-перевод:1000')
get_transactions('880005553535-оплата_жкх:10000')
get_transactions('89065664312-перевод:50000000')
get_transactions('print_it')
