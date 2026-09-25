class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def brace(s):
            sett = set()
            curr = {""}
            i = 0
            while i < len(s):
                if s[i] == "{":
                    j = i
                    depth = 0

                    while True:
                        if s[j] == "{": depth -= 1
                        elif s[j] == "}": depth += 1
                        if depth == 0: break
                        j += 1
                
                    opt = brace(s[i+1: j])
                    curr = {a + b for a in curr for b in opt}
                    i = j + 1
            
                elif s[i] == ",":
                    sett |= curr
                    curr = {""}
                    i += 1
                else:
                    curr = {x + s[i] for x in curr}
                    i += 1

            sett |= curr
            return sett

        return sorted(brace(expression ))


