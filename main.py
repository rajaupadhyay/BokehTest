import pandas as pd
from bokeh.charts import Bar, output_file, show

# I could just use Counter from Collections but too bad
def collectUniqueWords(filename):
    file_to_check = open(filename, 'r')
    dict1 = {}
    lines = file_to_check.readlines()
    file_to_check.close()
    for line in lines:
        line = line.split()
        for word in line:
            if word.lower() in dict1:
                dict1[word.lower()] += 1
            else:
                dict1[word.lower()] = 1

    return dict1


dictVals = collectUniqueWords("example.txt")

frequencies = pd.DataFrame(list(dictVals.items()))

frequencies.columns = ["word", "frequency"]

print(frequencies)

p = Bar(frequencies[:30], 'word', values='frequency', title="Word Frequency")

output_file("bar.html")

show(p)