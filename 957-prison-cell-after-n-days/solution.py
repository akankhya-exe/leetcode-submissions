class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}

        while n > 0:
            state = tuple(cells) # python doesn't let lists be dictionary keys cuz mutable

            if state in seen:
                cycle = seen[state] - n
                n %= cycle
            
            seen[state] = n

            if n > 0:
                n -= 1
            
                nxt = [0] * 8

                for i in range(1, 7): # 0 and 8 will be zero always
                    if cells[i-1] == cells[i+1]:
                        nxt[i] = 1
                cells = nxt
        return cells        
