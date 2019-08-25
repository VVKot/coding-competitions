from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:

    CLOSE_TIME = 60

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        transactions_by_name = defaultdict(lambda: defaultdict(list)) \
            # type: Dict[str, Dict[str, List[int]]]
        for transaction in transactions:
            name, timestamp, _, city = self._get_transaction_parts(transaction)
            transactions_by_name[name][city].append(timestamp)

        for transaction in transactions:
            name, timestamp, amount, city = \
                self._get_transaction_parts(transaction)
            if amount > 1000:
                result.append(transaction)
            else:
                should_add = False
                for other_city, times in transactions_by_name[name].items():
                    if other_city == city:
                        continue
                    for other_city_time in times:
                        if abs(other_city_time-timestamp) <= self.CLOSE_TIME:
                            should_add = True
                            break
                if should_add:
                    result.append(transaction)
        return result

    def _get_transaction_parts(self, transaction) -> Tuple[str, int, int, str]:
        name, time_str, amount_str, city = transaction.split(',')
        timestamp = int(time_str)
        amount = int(amount_str)
        return name, timestamp, amount, city
