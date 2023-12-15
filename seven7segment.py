input_number = input("Masukkan angka (antara 0 sampai 9)=> ")
def display_seven_segment(number):
    segments = {
        0: [' _ ', '| |', '|_|'],
        1: ['   ', '  |', '  |', '   '],
        2: [' _ ', ' _|', '|_  '],
        3: [' _ ', ' _|', ' _|'],
        4: ['   ', '|_|', '  |', '   '],
        5: [' _ ', '|_  ', ' _|'],
        6: ['  _ ', ' |_ ', ' |_| '],
        7: [' _ ', '  |', '  |', '   '],
        8: [' _ ', '|_|', '|_|'],
        9: [' _ ', '|_|', ' _|'],
        ' ': ['  ', '  ', '  ', '  ', '  ']
    }
    binary_truth = {
        0: '00001111110', 1: '00010110000', 2: '00101101101', 3: '00111111001', 4: '01000110011', 5: '01011011011', 
        6: '01101011111', 7: '01111110000', 8: '10001111111', 9: '10011111011'
    }

    digit = str(number)
    lines = ['' for _ in range(5)]

    for d in digit:
        segments_of_d = segments.get(int(d), segments[' '])
        for i, line in enumerate(segments_of_d):
            lines[i] += line + ' ' # Mengambil bagian yang merepresentasikan garis

    for line in lines:
        print(line)

    print("\nTruth Table Binary :")
    print("------------------------------------------------------")
    print("|       input            |           output          |")
    print("|------------------------|---------------------------|")
    print("| Number | w | x | y | z | a | b | c | d | e | f | g |")
    print("|------------------------|---------------------------|")
    for d in digit:
        binary = binary_truth.get(int(d),'    ')
        print(f"|   {d}    | {binary[0]} | {binary[1]} | {binary[2]} | {binary[3]} | {binary[4]} | {binary[5]} | {binary[6]} | {binary[7]} | {binary[8]} | {binary[9]} | {binary[10]} |")
        print("------------------------------------------------------")

display_seven_segment(input_number)
