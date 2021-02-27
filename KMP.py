class KMP:

    def build_nxt(self, p):
        x = 1
        now = 0
        nxt = [0]
        while x < len(p):
            if p[now] == p[x]:
                now += 1
                x += 1
                nxt.append(now)
            elif now:
                now = nxt[now - 1]
            else:
                nxt.append(0)
                x += 1
        return nxt

    def match(self, s, p):
        res = []
        nxt = self.build_nxt(p)
        tar = 0
        pos = 0
        while tar < len(s):
            if s[tar] == p[pos]:
                tar += 1
                pos += 1
            elif pos:
                pos = nxt[pos - 1]
            else:
                tar += 1
            if pos == len(p):
                res.append(tar - pos + 1)
                pos = nxt[pos - 1]
        return res


if __name__ == '__main__':
    kmp = KMP()
    print(kmp.match('asdewghrasgfreasgjoiurnbvecnia', 'asg'))
