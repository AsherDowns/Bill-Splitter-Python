initial_value = int(input())
number_list = [initial_value]
for i in number_list:
    next_input = input()
    if next_input == '.':
        break
    else:
        number_list.append(int(next_input))
print(sum(number_list) / len(number_list))