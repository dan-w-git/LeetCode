# DS: String
# ALGO: Pointer Manipulation
# Time: O(n). Space: O(1)

class Codec:
    delimiter = ":"

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            str_len = len(s)
            result = result + str(str_len) + self.delimiter + s
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        str_list = []
        i = 0
        total_length = len(s)
        while i < total_length:
            # read string length
            length_str = ""
            while s[i] != self.delimiter and i < total_length:
                length_str += s[i]
                i += 1
            length_int = int(length_str)

            # read actual string
            i += 1
            str_read = ""
            while length_int > 0:
                str_read += s[i]
                length_int -= 1
                i += 1

            # append string to list
            str_list.append(str_read)
        return str_list


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
