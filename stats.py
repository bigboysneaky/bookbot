def number_of_words(file_contents):
    split_contents = file_contents.split()
    count = 0
    for word in split_contents:
        count += 1
    return count

def number_of_strings(file_contents):
    lowered_contents = file_contents.lower()
    count_of_strings = {}
    for string in lowered_contents:
        if string in count_of_strings:
            count_of_strings[string] += 1
        else:
            count_of_strings[string] = 1
    return count_of_strings

def sort_on(element):
    return element["num"]

def sort_a_dictionary(count_of_strings):
    sorted_list = []
    for key in count_of_strings:
        this_dict = {"char": key, "num": count_of_strings[key]}
        sorted_list.append(this_dict)
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list

