import os


def main():
    chunk = []
    all_text = []
    my_file = os.path.join('.', 'SbSCookbook.txt')

    with open(my_file, encoding='utf8') as in_file:
        read_file = in_file.readlines()

        for line in read_file:
            if line.strip():
                chunk.append(line)
            if 'people)' in line:
                all_text = wrap_name(chunk, all_text)
                chunk = []
                if line.strip():
                    chunk.append(line)
            if line.strip() == 'Method:':
                all_text = wrap_ingredients(chunk, all_text)
                chunk = []
                if line.strip():
                    chunk.append(line)
            if line.strip() == '(End)':
                all_text = wrap_method(chunk, all_text)
                chunk = []
                if line.strip():
                    chunk.append(line)

    with open("output_file.html", "a", encoding='utf8') as out_file:
        for line in all_text:
            out_file.writelines(line)

    print("Over and out")


def wrap_name(chunk, all_text):
    all_text.append('<button class="recipe">\n')
    all_text.append('\t<h3>' + chunk[0].strip() + '</h3>\n')
    all_text.append('</button>\n\n')

    return all_text


def wrap_ingredients(chunk, all_text):
    all_text.append('<div class="ingredienser">\n')
    all_text.append('\t<p class="antal">' + chunk[0].strip() + '</p>\n')
    all_text.append('\t<b>Ingredienser:</b>\n')

    for ingredient_line in chunk:
        if 'people' in ingredient_line or 'Method:' in ingredient_line:
            pass
        else:
            all_text.append('\t<p><label><input type="checkbox">' + ingredient_line.strip() + '</label></p>\n')

    all_text.append('</div>\n\n')

    return all_text


def wrap_method(chunk, all_text):
    all_text.append('<div class="howto"> <b> Method: </b>\n')

    for method_line in chunk:
        if 'Method:' in method_line or '(End)' in method_line:
            pass
        else:
            all_text.append('\t<p><label><input type="checkbox">' + method_line.strip() + '</label></p>\n')

    all_text.append('\n')
    all_text.append('\t<button class="slut">(End)</button>\n')
    all_text.append('</div>\n\n')

    return all_text


if __name__ == '__main__':
    main()
