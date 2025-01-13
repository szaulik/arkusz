def is_keith_number(n):
    digits = [int(d) for d in str(n)]
    seq = digits[:]
    
    while seq[-1] < n:
        seq.append(sum(seq[-len(digits):]))
    
    return seq[-1] == n

def find_keith_numbers(in_file, out_file):
    with open(in_file) as f1, open(out_file, 'w') as f2:
        keith_nums = [num for num in f1.read().splitlines() 
                     if is_keith_number(int(num))]
        f2.write('\n'.join(keith_nums))

# Uruchomienie
find_keith_numbers('liczby.txt', 'liczby_keitha.txt')