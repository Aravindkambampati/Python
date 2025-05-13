"""
1. Write the data into the text file (word_data.txt)
   and read the same file and write the count of words into another file.

"""
def write_file(input_string):
    file1 = open('word.txt','w')
    file1.write(input_string)
    file1.close()
    return file1
input_string = 'we are learning python programming.\nwe are currently learning file handling topic of python'
print(write_file(input_string))
def read_file(file_name):
    file2 = open(file_name,'r')
    read_lines = file2.readlines()
    file2.close()
    return read_lines
file_name = 'word.txt'
obj = read_file(file_name)
print(obj)

def counting_words(obj):
    string_list = []
    for result in obj:
        string_list.extend(result.split())
    f = open('words_count.txt', 'w')
    count_list = []
    for word1 in string_list:
        word_count = 0
        for word2 in string_list:
            if word1 == word2:
                word_count += 1
        count_list.append((word1,word_count))
    count_list = list(set(count_list))
    f.write(str(count_list))
    return f
print(counting_words(obj))
