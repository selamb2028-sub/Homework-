# Created on iPad.
def cal(tax):
    if tax > 0 and tax <= 2000:
        print(f"0%, Net income = {tax}")
    elif tax >= 2001 and tax <= 4000:
        print(f"15%,Net income = {tax/15 *100}" )
    elif tax >= 4001 and tax <= 7000:
        print(f"20%,Net income = {tax/20 *100}")
    elif tax >= 7001 and tax <= 10000:
        print(f"25%,Net income = {tax/25 *100}")
    elif tax >= 10001 and tax <= 14000:
        print(f"30%,Net income = {tax/30 *100}")
    else:
        print(f"35%,Net income = {tax/35 *100}")

tax = int(input("enter tax"))

cal(tax)
