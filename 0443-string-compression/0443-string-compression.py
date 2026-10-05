class Solution(object):
    def compress(self, chars):
        read = 0
        write = 0

        while read < len(chars):
            start = read
            while read < len(chars) and chars[read] == chars[start]:
                read += 1
            count = read - start
            chars[write] = chars[start]
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write