#!/usr/bin/python3

from draughts import Board

moves = ["33-28", "17-21", "34-30", "18-22", "28x26", "11-17", "30-25", "13-18", "39-34", "6-11", "35-30"]

board = Board(variant="standard", fen="startpos")

# Each choice is a tuple (move_index, number of legal moves)
choices = []

for move in moves:
    legal_moves = board.legal_moves()

    ordered_moves = [(move_obj.pdn_move, move_obj) for move_obj in legal_moves]
    ordered_moves.sort()

    move_index = [move_tuple[0] for move_tuple in ordered_moves].index(move)
    
    choices.append((move_index, len(legal_moves)))


    board.push(ordered_moves[move_index][1])

decimal_number = 0
for move_index, legal_move_count in reversed(choices):
    decimal_number *= legal_move_count
    decimal_number += move_index

plaintext = ""
while decimal_number != 0:
    plaintext += chr(ord('a') + decimal_number % 26)

    decimal_number //= 26

print(plaintext)
