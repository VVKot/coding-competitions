class Solution:

    def lemonadeChange(self, bills):
        fives, tens = 0, 0
        for bill in bills:
            if bill == 10:
                if not fives:
                    return False
                fives -= 1
                tens += 1
            elif bill == 20:
                if not fives:
                    return False
                if tens:
                    fives -= 1
                    tens -= 1
                else:
                    if fives < 3:
                        return False
                    fives -= 3
            else:
                fives += 1
        return True
