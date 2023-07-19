from typing import List

from test_framework import generic_test

def buy_and_sell_stock_once(prices: List[float]) -> float:
    # Saves the indexes of the best
    # buy day and the best sell day
    # and also the current possibly highest profit days
    possible_highest_profit = {"lowest": prices[0], "highest": None, "profit": 0, "indexes": [0, None]}
    highest_profit = {"lowest": None, "highest": None, "profit": 0, "indexes": [None, None]}

    
    for i in range(1, len(prices)):
        num = prices[i]
        # profit can be negative 
        # profit = num - lowest
        # selling_days.append(profit)


        if num < possible_highest_profit["lowest"]:
            # Change New highest profit if it is bigger then the highest
            if possible_highest_profit["profit"] > highest_profit["profit"]:
                highest_profit = dict(possible_highest_profit)

            # Start the next possible_highest_profit search from here 
            # because from this point forward the lowest day to buy is this one
            possible_highest_profit["lowest"] = num
            possible_highest_profit["highest"] = None
            possible_highest_profit["profit"] = 0
            possible_highest_profit["indexes"] = [i, None]

        
        else:
            # Check if new possible_highest_profit search was started
            if not possible_highest_profit["highest"]:
                possible_highest_profit["highest"] = num
                possible_highest_profit["indexes"][1] = i
                possible_highest_profit["profit"] = num - possible_highest_profit["lowest"]
            # Check if in this search the highest selling day was overcome
            # and if so calculate the new max profit and add this days index 
            else:
                if possible_highest_profit["highest"] < num:
                    possible_highest_profit["highest"] = num
                    possible_highest_profit["indexes"][1] = i
                    possible_highest_profit["profit"] = num - possible_highest_profit["lowest"]

        
    if possible_highest_profit["profit"] > highest_profit["profit"]:
        highest_profit = possible_highest_profit

    return highest_profit["profit"]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
