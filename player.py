#!/usr/bin/python

import copy
from logging.config import valid_ident
import sys
import json
import socket
import numpy as np

postion_delta = [[-1, -1], [-1, 0], [-1,1], [0,-1], [0, 1], [1,-1], [1, 0], [1, 1]]

#params: piece ([row, col]), our_pieces [], enemy_pieces [], board (game board)
#returns an array of possible moves
# check all around one player piece
def check_adjacent_pieces(piece, board, player, enemy):
  valid_moves = []
  for thing in postion_delta:
    location_to_check = [piece[0] + thing[0], piece[1] + thing[1]]
    pos = helper(location_to_check, board, player, enemy, thing)
    #iff helper returned an array, store it in valid_moves
    if pos:
      valid_moves.append(pos)
  return valid_moves

def helper(location_to_check,board,player, enemy, delta):
    #out of bounds check
    if location_to_check[0] < 0 or location_to_check[0] >= 8 or location_to_check[1] < 0 or location_to_check[1] >= 8:
      return False
    #empty space
    elif board[location_to_check[0]][location_to_check[1]] == 0:
      return False
    #player piece
    elif board[location_to_check[0]][location_to_check[1]] == player:
      return False
    #enemy piece
    elif board[location_to_check[0]][location_to_check[1]] == enemy:
      # end_not_found = False
      while location_to_check[0]+delta[0]>=0 and location_to_check[0]+delta[0]<=7 and location_to_check[1]+delta[1]>=0 and location_to_check[1]+delta[1]<=7:
            location_to_check[0] = location_to_check[0] + delta[0]
            location_to_check[1] = location_to_check[1] + delta[1]
            if board[location_to_check[0]][location_to_check[1]] == player:
              return False
            elif board[location_to_check[0]][location_to_check[1]] == 0:
              return location_to_check
      return False


def get_valid_moves(player, board):
  valid_moves = []
  if player == 1:
    enemy = 2
  else:
    enemy = 1
  our_pieces = []
  enemy_pieces = []
# 1. make array of enemy pieces and our piece
  row_counter = 0
  for row in board:
    col_counter = 0
    for col in row:
      # if piece is black, add to th e correct array
      piece = board[row_counter][col_counter]
      if piece == 1:
        if player == 1:
          our_pieces.append([row_counter, col_counter])
        elif player == 2:
          enemy_pieces.append([row_counter, col_counter])
      # if piece is black, add to the correct array
      if piece == 2:
        if player == 1:
          enemy_pieces.append([row_counter, col_counter])
        elif player == 2:
          our_pieces.append([row_counter, col_counter])

      # keeps track of row index
      col_counter += 1
      # print(row_counter, col_counter, piece)  # tester?
    row_counter += 1

  #make valid move list
  for piece in our_pieces:
    move_list = check_adjacent_pieces(piece,board, player, enemy)
    for move in move_list:
      valid_moves.append(move)

    #tests
    # check_adjacent_pieces(piece, our_pieces, enemy_pieces, board, player, enemy)
    # print("testing check_adjacent_pieces ", check_adjacent_pieces([4,4], board, player, enemy))

  return valid_moves

def get_move(player, board):
  # TODO determine valid moves
  valid_moves = get_valid_moves(player, board)
  print(evalBoard(board))
  evaluated_moves = []
  bestMove = -500
  bestMoveIdx = valid_moves[0]
  for i in valid_moves:
    a = evalBoard(makeMove(board,i,player))
    evaluated_moves.append(a)
    if a>bestMove:
      bestMove = a
      bestMoveIdx = i
  return bestMoveIdx


def evalBoard(board):
    count = 0
    for i in board:
      for j in i:
          if j == 1:
            count+=1
          if j == 2:
            count-=1
    return count

def bestMove(board,search_depth):
  if search_depth ==0:
    return evalBoard(board)

def makeMove(board,move,player):
    new_board = copy.deepcopy(board)
    new_board[move[0]][move[1]] = player
    if player == 1:
      enemy = 2
    else:
      enemy = 1
    for i in postion_delta:
      location = [move[0]+i[0],move[1]+i[1]]
      if wrappDir(new_board,player,location,enemy,i):
        while new_board[location[0]][location[1]] != player:
            new_board[location[0]][location[1]] = player
            location[0]+=i[0]
            location[1]+=i[1]
    return new_board

def wrappDir(board,player,location_to_check,enemy,delta):
     #out of bounds check
    if location_to_check[0] < 0 or location_to_check[0] >= 8 or location_to_check[1] < 0 or location_to_check[1] >= 8:
      return False
    #empty space
    elif board[location_to_check[0]][location_to_check[1]] == 0:
      return False
    #player piece
    elif board[location_to_check[0]][location_to_check[1]] == player:
      return False
    #enemy piece
    elif board[location_to_check[0]][location_to_check[1]] == enemy:
      # end_not_found = False
      while location_to_check[0]+delta[0]>=0 and location_to_check[0]+delta[0]<=7 and location_to_check[1]+delta[1]>=0 and location_to_check[1]+delta[1]<=7:
            location_to_check[0] = location_to_check[0] + delta[0]
            location_to_check[1] = location_to_check[1] + delta[1]
            if board[location_to_check[0]][location_to_check[1]] == player:
              return True
            elif board[location_to_check[0]][location_to_check[1]] == 0:
              return False
      return False


def prepare_response(move):
  response = '{}\n'.format(move).encode()
  # response = '{}'.format(move).encode()
  print('sending {!r}'.format(response))
  return response

if __name__ == "__main__":
  port = int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]) else 1337
  host = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2]) else socket.gethostname()

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect((host, port))
    while True:
      data = sock.recv(1024)
      if not data:
        print('connection to server closed')
        break
      json_data = json.loads(str(data.decode('UTF-8')))
      board = json_data['board']
      maxTurnTime = json_data['maxTurnTime']
      player = json_data['player']
      print(player, maxTurnTime, board)

      move = get_move(player, board)
      print("valid move list: ", move)

      response = prepare_response(move)
      sock.sendall(response)
  finally:
    sock.close()
