class Solution:
    def collapseAsteroids(self, asts, new_):
        while True:
            if not asts or asts[-1] < 0:
                asts.append(new_)
                break
            last = asts[-1] 
            if last == -new_:
                asts.pop()
                break
            elif last > -new_:
                break
            else:
                asts.pop()	
        return asts 

    def asteroidCollision(self, ast):
        result = []
        for a in ast:
            if result and result[-1] > 0 and a < 0:
                result = self.collapseAsteroids(result, a)
            else:
                result.append(a)
        return result
