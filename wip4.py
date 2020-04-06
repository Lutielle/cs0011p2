ACCESSNUMBER = ["M55150_at", "U50136_rna1_at", "X95735_at", "U22376_cds2_s_at", "M16038_at", "M23197_at", "M84526_at", "U66497_at", "U82759_at", "D49950_at", "X59417_at", "M27891_at", "X17042_at", "U05259_rna1_at", "U12471_cds1_at", "U46751_at", "M92287_at", "Y00787_s_at", "L08246_at", "X74262_at"]

def read_data_tsv(filename):
    data_list = []
    with open(filename) as cur_file:
        for line in cur_file:
            split_data = line.split("\t")
            for i in range(2, len(split_data)):
                split_data[i] = int(split_data[i])
            data_list.append(split_data)

    return data_list

def read_label_tsv(filename):
    label_list = []
    with open(filename) as cur_file:
        header = True
        for line in cur_file:
            #here I'm making a toggle so that it'll skip the first (header) line
            if header:
                header = False
            else:
                split_labels = line.strip().split("\t")
                split_labels[0] = int(split_labels[0])
                label_list.append(split_labels)

    return label_list

def train(labels, data):
    #here i'm separating out the header line from the data list
    header = data[0]
    #and updating the data variable to exclude it so it's easier to work with
    data = data[1:]

    outerdict = {}

    for line in data:
        if line[1] not in ACCESSNUMBER:
            continue

        AML_sum = 0
        AML_div = 0
        ALL_sum = 0
        ALL_div = 0

        for i in range(2, len(line)):
            for label in labels:
                if label[0] == header[i]:
                    if label[1] == "AML":
                        AML_sum += line[i]
                        AML_div += 1
                    elif label[1] == "ALL":
                        ALL_sum += line[i]
                        ALL_div += 1

        AML_avg = AML_sum / AML_div
        ALL_avg = ALL_sum / ALL_div

        #print(line[1] + " AML mean: " + format(AML_avg,".3f"))
        #print(line[1] + " ALL mean: " + format(ALL_avg,".3f"), end = "\n\n")

        innerdict = {}
        innerdict["AML"] = AML_avg
        innerdict["ALL"] = ALL_avg
        #print(innerdict)

        outerdict[line[1]] = innerdict
    #prints used to check that train() was working as expected
    #print(outerdict)
    #print(len(outerdict))
    return outerdict

def classify(averages, data):
    sampleclass = {}

    for sample in range(2, len(data[0])):
        AML_total = 0
        ALL_total = 0

        for line in data[1:]:
            if line[1] not in ACCESSNUMBER:
                continue

            for i in line[2:]:
                AML_diff = abs(averages[line[1]]["AML"] - i)
                ALL_diff = abs(averages[line[1]]["ALL"] - i)

                if AML_diff > ALL_diff:
                    AML_total += 1
                else:
                    ALL_total += 1

        if AML_total > ALL_total:
            sampleclass[data[0][sample]] = "AML"
        elif ALL_total > AML_total:
            sampleclass[data[0][sample]] = "ALL"
        else:
            sampleclass[data[0][sample]] = "Undetermined"

    print(sampleclass)
    #return sampleclass


def main():
    testing_data = read_data_tsv("ALL_AML_testing.tsv")
    training_data = read_data_tsv("ALL_AML_training.tsv")
    labels = read_label_tsv("ALL_AML_labels.tsv")

    selected_gan = train(labels, training_data)

    classify(selected_gan, testing_data)

main()
