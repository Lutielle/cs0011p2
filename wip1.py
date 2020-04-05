def read_lines(filename):
    with open(filename) as cur_file:
        for line in cur_file:
            for ch in line:
                print(ch, "!", sep = "", end = "")
            #print(line)

def main():
    #hi i'm currently using manually truncated versions of these text files
    #because i was getting really sick of how much scrolling i had to do
    #and also my computer is Old and Slow sometimes and it was just Not Happy with what was going on
    #i'll fix this with the correct files later
    read_lines("data_set_ALL_AML_train1.txt")
    read_lines("table_ALL_AML_samples1.txt")

main()
