
import md5

@profile
def slow():
    s = ""
    with open('/usr/share/dict/words') as f:
        for l in f:
            s += l
    return s
    
@profile
def fast():
    with open('/usr/share/dict/words') as f:
        s = "".join(f)
        return s

if __name__ == "__main__":
    s1 = slow()
    s2 = fast()
    assert(s1 == s2)
