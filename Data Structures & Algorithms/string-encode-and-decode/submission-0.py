class Solution:

    def encode(self, strs: List[str]) -> str:
        string_ring = ""
        for x in strs:
            string_ring = string_ring + str(len(x)) + "#" + x

        return string_ring

    def decode(self, s: str) -> List[str]:

        result = []
        j = 0

        while j < len(s):
            i = j

            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            word = s[i+1 : i+1+length]
            result.append(word)
            j = i + 1 + length 

        return result 
