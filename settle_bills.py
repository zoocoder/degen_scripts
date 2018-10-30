from collections import defaultdict


def remove_zero_bills(bills):
    names = []
    for name in bills:
        if bills[name] == 0:
            names.append(name)

    for name in names:
        bills.pop(name)


def verify_bills(bills):
    balance = 0
    for name in bills:
        balance += bills[name]
    if balance == 0:
        print "Great, the net balance checks out to be 0."
    else:
        print "Something is wrong, the net balance of the bills is off by: ", balance
        exit()


def settle_bills(bills):
    while len(bills) > 0:
        # Sort the bills by values
        bill_list = sorted(bills.items(), key=lambda(k, v): v, reverse=True)
        # print bill_list

        if len(bill_list) < 2:
            print "We have a problem, the remaining bills cannot settle: ", bill_list
            return

        # Get two biggest bills to settle.
        positive_name,  positive_balance = bill_list[0]
        negative_name, negative_balance = bill_list[-1]

        # Print out the transaction
        settled_balance = min(abs(positive_balance), abs(negative_balance))
        print negative_name, " --> ", positive_name, " : ", settled_balance

        # Settle the transaction
        bills[positive_name] = positive_balance - settled_balance
        bills[negative_name] = negative_balance + settled_balance

        # Remove all people that are already settled
        remove_zero_bills(bills)
    return


def main():
    bills = defaultdict(int)

    ################
    bills["Adam"] = 0
    bills["Alex"] = 0
    bills["Andrei"] = 0

    bills["Ben"] = 0
    bills["Bernie"] = 0
    bills["Boram"] = 0
    bills["Brian"] = 0

    bills["Dan"] = 0
    bills["Daniel"] = 2071
    bills["Dannis"] = 0
    bills["David"] = 0
    bills["Frank"] = 0

    bills["Heming"] = 0
    bills["Ian"] = 0
    bills["Jeff"] = -2000
    bills["Ji"] = 164
    bills["Jiggity"] = 0
    bills["Jimmy"] = 0
    bills["Jesper"] = 0
    bills["Joanne"] = 0
    bills["Julian"] = 0
    bills["Justin"] = 0

    bills["Kevin"] = 0
    bills["Lemur"] = 0

    bills["Matt"] = 0
    bills["Michael_L"] = 1335
    bills["Michael_S"] = 0

    bills["Peter"] = 0
    bills["Robin"] = 0
    bills["Roland"] = -800
    bills["Ryan"] = 0

    bills["Sameh"] = 0
    bills["Shariq"] = 0
    bills["Simeon"] = 0
    bills["Stanley"] = 0

    bills["VDong"] = 0
    bills["VZhu"] = 72

    bills["Wonjun"] = 0
    bills["Yuan"] = -842
    bills["Zi"] = 0


    remove_zero_bills(bills)

    print "----- All bills: -----"

    for name in bills:
        print name, bills[name]

    print "----- Verifying bills:"
    verify_bills(bills)

    print "----- Transactions to settle bills:"
    settle_bills(bills)

if __name__ == '__main__':
    main()
