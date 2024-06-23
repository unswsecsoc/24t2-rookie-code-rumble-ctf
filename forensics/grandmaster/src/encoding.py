from draughts import Board
from draughts.PDN import PDNWriter

board = Board(variant="standard", fen="startpos")

# secret_text = "jazz"
secret_text = "blunder"

letter_indexes = [ord(char) - ord('a') for char in secret_text]
print(letter_indexes)

decimal_number = 0
for i, letter_index in enumerate(letter_indexes):
    decimal_number += letter_index * 26**i

print(decimal_number)

while decimal_number != 0 and not board.is_over():
    moves = board.legal_moves()
    
    # Decide which move index
    move_index = decimal_number % len(moves)
    decimal_number //= len(moves)

    print(move_index)
    print(len(moves))
    print(decimal_number)

    # Make move
    moves_with_order = [(move.pdn_move, move) for move in moves]
    moves_with_order.sort()

    print([move_tuple[0] for move_tuple in moves_with_order])

    print(moves_with_order[move_index][0])

    print(board)

    board.push(moves_with_order[move_index][1])

print("FINAL BOARD")

print(board)
games = PDNWriter(filename="jazz_encoded.txt", board=board)