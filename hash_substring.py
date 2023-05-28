#python3-2


    def read_input():
    input_type = input().rstrip()
    if input_type == "i": 
        #Ievades veids ir "i", nolasa rakstu un tekstu no lietotāja ievades
        p = input().rstrip()  #Nolasa rakstu
        t = input().rstrip()  #Nolasa tekstu
        return (p, t)
    elif input_type == "f":
       #Ievades veids ir "f", nolasa rakstu un tekstu no faila
        f = input()  #Nolasa faila nosaukumu
        tests = './tests/'
        fails = tests + f  #Izveido faila ceļu
        with open(fails, 'r') as f:
            #Nolasa faila pirmās divas rindas kā tekstu
            return (f.readline().rstrip(), f.readline().rstrip())

def print_occurrences(output):
    #Pārvērš sarakstu ar sastapšanās vietām par tekstu, kur atdalītājs ir simbols
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    q = 156  #skaitlis, ko izmanto hash" funkcijā
    w = 256  #Iespējamo simbolu skaits

    p_garums = len(pattern)  #pattern garums
    p_hash = 0  #hash vērtība
    t_garums = len(text)  #Teksta garums
    t_hash = 0  #Pašreizējā teksta loga hash" vērtība

    h = 1  #Vērtība kas izmantota hash aprēķinā
    rezultats = []  #Saraksts kurā saglabā sastapšanās vietas

    #Aprēķina vērtību h
  for i in range(p_len-1):
        h = (h * w) % q

    #Aprēķina sākotnējās hash" vērtības rakstam un pirmajam teksta logam
    for i in range(p_range):
        p_hash = (w * p_hash + ord(pattern[i])) % q
        t_hash = (w * t_hash + ord(text[i])) % q

    #Pārslīd rakstu pa tekstām un pārbauda sastapšanos
    for i in range(t_range - p_range + 1):
        if p_hash == t_hash:  #Ja hasha vērtības sakrīt, pārbauda faktisko raksta sakritību
            match = True
            for j in range(p_range):
                if text[i + j] != pattern[j]:  #Ja simboli nesakrīt, pārveido match uz false
                    match = False
                    break

            if match:  #Ja match joprojām ir True, raksts sākas indeksā i
               result.append(i)

        if i < t_range - p_range:  #Atjauno hash vērtību nākamajam teksta logam
            t_hash = (w * (t_hash - ord(text[i]) * h) + ord(text[i + p_range])) % q

            if t_hash < 0:  #Izlabot Hash vērtību ja tā kļūst negatīva
                t_hash += q

    return result

if __name__ == '__main__':
    #Nolasa ievadi, atrod sastapšanās vietas un tos izvada
    print_occurrences(get_occurrences(*read_input()))

