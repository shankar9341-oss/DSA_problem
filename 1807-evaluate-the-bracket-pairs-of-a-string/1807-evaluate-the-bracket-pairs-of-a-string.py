class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapp = {}
        for i,j in knowledge:
            mapp[i] = j
        result = []
        curr = []
        start = False
        for char in s:
            if char == "(":
                start = True
            elif char == ")":
                start = False
                join = "".join(curr)
                result.append(mapp[join] if join in mapp else "?")
                curr = []
            else:
                if start:
                    curr.append(char)
                else:
                    result.append(char)
                
        return "".join(result)