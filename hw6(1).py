target = input()
sentences = []

while True:
    _input = input()
    if _input == "INPUT_END":
        break
    sentences.append(_input.strip())

combined_sentence = ""
for i in range(len(sentences)):
    combined_sentence += sentences[i]
    if i != len(sentences) - 1:
        combined_sentence += " "
    print(combined_sentence)

if target in combined_sentence:
    index_list = []
    start_index = 0
    while target in combined_sentence[start_index:]:
        start, end = start_index, len(combined_sentence)
        _index = combined_sentence.index(target, start, end)
        index_list.append(_index)
        start_index = _index + 1
    for j in range(len(index_list)):
        output = ""
        if index_list[j] < 7:
            output += combined_sentence[:index_list[j]]
        else:
            output += combined_sentence[index_list[j]-7:index_list[j]]

        output += "**" + target + "**"

        after_target_index = index_list[j]+len(target)
        output += combined_sentence[after_target_index:after_target_index+7]
        print(output)
else:
    print("NO_MATCH")