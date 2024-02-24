def solve():
    s = "rat"
    t = "car"
    for i in s:
        if i in t:
            t = t.replace(i,'',1)
        else:
            return False
    if len(t) > 0:
        return False
    return True
# print(solve())
def sol():
    s = "anagram"
    t = "anargam"
    if len( s ) != len( t ) :
        return False
    d = {}
    for i in s :
        if d.get( i ) :
            d[ i ] += 1
        else :
            d[ i ] = 1
    for i in t :
        if d.get( i ) :
            d[ i ] -= 1
        else :
            return False
    return sum( d.values() ) == 0
print(sol())

