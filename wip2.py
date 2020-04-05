def read_data_tsv(filename):
    data_list = []
    with open(filename) as cur_file:
        for line in cur_file:
            split_data = line.split("\t")
            for i in range(2, len(split_data)):
                split_data[i] = int(split_data[i])
            data_list.append(split_data)
            
    cur_file.close()
    return data_list      
            
def read_label_tsv(filename):
    label_list = []
    with open(filename) as cur_file:
        for line in cur_file:
            split_labels = line.split("\t")
            split_labels[0] = int(split_labels[0])
            label_list.append(split_labels)

    cur_file.close()
    return label_list

def main():
    pass
