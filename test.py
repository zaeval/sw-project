data = [raw_word.strip(".,\"\'*-?!").upper() for raw_word in f.read().split()]
Counter(data).most_common()