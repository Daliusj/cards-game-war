from utils import CardsDeck, Player, Game, get_players_names, print_table


def main():
    name_1, name_2 = get_players_names()
    cards = CardsDeck()
    cards.shuffled()
    stack_1, stack_2 = cards.split_deck()
    player_1 = Player(name=name_1)
    player_2 = Player(name=name_2)
    player_1.stack = stack_1
    player_2.stack = stack_2
    while True:
        game = Game()
        cards_1 = []
        cards_2 = []
        cards_1 = player_1.get_card(1)
        cards_2 = player_2.get_card(1)
        print_table()
        input()
        if game.is_war(cards_1, cards_2):
            cards_1 = player_1.get_card(4)
            cards_2 = player_2.get_card(4)
            print_table()
            input()
        if game.check_winner(player1_cards=cards_1, player1_cards=cards_2) == "player1":
            player_1.add_cards(cards_1, cards_2)
        if game.check_winner(player1_cards=cards_1, player1_cards=cards_2) == "player2":
            player_2.add_cards(cards_1, cards_2)
        if player_1.is_winner() or player_2.is_winner():
            break
    if player_1.is_winner():
        print(f"{player_1.name} is winner!")
    if player_2.is_winner():
        print(f"{player_2.name} is winner!")


main()
