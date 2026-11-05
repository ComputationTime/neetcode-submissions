class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for e in strs:
            e.replace("/", "/s")
            encoded += "//" + e
        return encoded
    def decode(self, s: str) -> List[str]:
        strs = []

        curr = ""
        i = 2
        while i < len(s):
            if s[i] == "/":
                if s[i + 1] == "s":
                    curr += "/"
                    i += 1
                elif s[i + 1] == "/":
                    strs.append(curr)
                    curr = ""
                    i += 1
                else:
                    curr += s[i]
            else:
                curr += s[i]
            i += 1
        
        if len(s) > 0:
            strs.append(curr)
        
        return strs