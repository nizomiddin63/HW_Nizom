class plastic_card:
    def __init__(self, card_holder, card_number, card_term, card_balance):
        self.card_holder = card_holder
        self.__card_number = card_number
        self._card_term = card_term
        self.__password = "123456"
        self.card_balance = card_balance

    def __change_password(self):
        default_password = input("Enter default password: ")
        if default_password == self.__password:
            new_password = input("Enter new password: ")
            self.__password = new_password
            print("Password changed successfully!")
        else:
            print("Incorrect default password!")

    def change_password(self):
        self.__change_password()

    def sort_by_card_balance(self, cards):
        cards.sort(key=lambda card: card.card_balance, reverse=True)
        return cards

card = plastic_card("Nizom", "1234567890123456", "2023-09-26", 100)

card.change_password()

cards = [
    plastic_card("Nizom", "1234567890123456", "2023-09-26", 100),
    plastic_card("Alish", "9876543210987654", "2023-09-26", 50),
    plastic_card("Umid", "5432109876543210", "2023-09-26", 25),
]

sorted_cards = card.sort_by_card_balance(cards)

for card in sorted_cards:
    print(card.card_holder, card.card_balance)
