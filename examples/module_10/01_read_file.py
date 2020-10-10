import os
import matplotlib.pyplot as plt


script_dir = os.path.dirname(__file__)
script_dir = os.path.abspath(script_dir)
abs_file_path = os.path.join(script_dir, 'example.txt')


histogram = {}
with open(abs_file_path, 'r') as reader:
    for line in reader.readlines():
        for word in line.split(' '):
            word = word.strip()
            if word and word != '':
                if word in histogram:
                    histogram[word] += 1
                else:
                    histogram[word] = 1
print(histogram)


# Histogram graph
histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
labels = [item[0] for item in histogram]
values = [item[1] for item in histogram]
plt.bar(labels, values)
plt.show()
