# DS: String
# ALGO: String Slicing, String Pattern Search
# Time: O(n). Space: O(1)

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        str_list = []
        for s in strs:
            length = str(len(s))
            str_list.append(f"{length}#{s}")
        return "".join(str_list)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        str_list = []
        i = 0
        total_length = len(s)
        while i < total_length:
            # find delimiter
            j = s.find("#", i)
            if j == -1:
                break  # Shouldn't happen if string encoded correctly
            length = int(s[i:j])

            # read actual string
            j += 1
            str_list.append(s[j:j+length])
            i = j+length

        return str_list


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
