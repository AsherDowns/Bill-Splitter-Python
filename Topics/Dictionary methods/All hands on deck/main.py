card_values = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
hand_values = []
i = 1
while i <= 6:
    card = input()
    if card not in card_values:
        card = int(card)
        hand_values.append(card)
    else:
        hand_values.append(card_values[card])
    i += 1

print(sum(hand_values) / len(hand_values))