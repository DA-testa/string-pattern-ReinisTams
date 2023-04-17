#python3-2

    def read_input():
    input_type = input().rstrip()
    if input_type == "i":

        p = input().rstrip()
        t = input().rstrip()
        return (p, t)

    elif input_type == "f":
        f = input()
        test ='./tests/'
        file = test+f
        with open(file, 'r') as f:
        return (f.readline().rstrip(),f.readline().rstrip())

    def print_occurrences(output):
    print(' '.join(map(str, output)))

    def get_occurrences(pattern, text):
 
    q = 156
    w = 256

    p_len = len(pattern)
    p_hash = 0
    t_len = len(text)
    t_hash = 0

    h = 1
    result = []
    for i in range(p_len-1):
            h = (h * w) % q

    for i in range(p_len):
          p_hash = (w * p_hash + ord(pattern[i])) % q
          t_hash = (w * t_hash + ord(text[i])) % q
          
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            match = True
            for j in range(p_len):
                if text[i + j] != pattern[j]:
                    match = False
                    break

        if match:
            result.append(i)

        if i < t_len - p_len:
            t_hash = (w * (t_hash - ord(text[i]) * h) + ord(text[i + p_len])) % q

            if t_hash < 0:
                t_hash += q

    return result
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
