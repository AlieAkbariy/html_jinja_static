# Author : Ali Akbari

def find_index(temp_1, key):
    for i in range(0, len(temp_1)):
        if key in temp_1[i]:
            return i


def change_line_form(line, key):
    editted_line = key + '= "{% static '
    temp = line.split(key)
    temp_1 = line.strip().split(" ")
    temp_2 = temp[1].split('"')  # get url of static file form file
    editted_line = temp[0] + editted_line + "'" + temp_2[1] + "' %}" + '"'
    index = find_index(temp_1, key)

    if index + 1 == len(temp_1):
        editted_line += ">"

    for i in range(index + 1, len(temp_1)):
        editted_line += temp_1[i]

    return editted_line


def django_prepare(input_path , output_path):
    html_file = open(input_path, 'r')
    edited_html_file = open(output_path, 'a')

    lines = html_file.readlines()

    for line in lines:
        if "<link" in line:

            line = change_line_form(line, "href")

        elif "<img" in line:

            line = change_line_form(line, "src")

        edited_html_file.write(line + '\n')

    edited_html_file.close()

    return


if __name__ == '__main__':
    input_path = input("Enter the input file path :")
    output_file = input("Enter the output file path (where you want to save edited file) :")
    output_file += "/edited.html"
    django_prepare(input_path , output_file)
    print("we saved your edited code in output path that you enter with name 'edited.html' ")
