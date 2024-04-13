import numpy as np
import random as rand
from flask import jsonify
import constants
    
class Game:

    __piece_category_map = {}
    __board_map = {}
    __white_pieces = {}
    __black_pieces = {}
    __board_ranks = 8
    __board_files = 9
    __init_piece = "---"

    def __init__(self, is_demo) -> None:
        self.__piece_category_map = {'5SG': 1, '4SG': 1, '3SG': 1, '2SG': 1, '1SG' :1,
                            'COL': 1, 'LTC': 1, 'MAJ': 1,
                            'CPT': 1, '1LT': 1, '2LT': 1,
                            'SRG': 1, 'PVT': 6, 'SPY': 2,
                            'FLG': 1}
                
        self.__board_map = np.full((self.__board_ranks, self.__board_files), self.__init_piece, dtype=object)

        self.start()

    def start(self) -> None:
        self.draft_pieces()

    def draft_pieces(self) -> None:
        self.draft_white()
        self.draft_black()
    
    def draft_white(self):
        self.put_pieces_random(0, 3, 0, self.__board_files) # can be replaced

    def draft_black(self):
        self.put_pieces_random(5, self.__board_ranks, 0, self.__board_files) # can be replaced

    '''
    Putting pieces randomly
    '''
    def put_pieces_random(self, start_rank, stop_rank, start_file, stop_file):
        piece_denomination_map = self.__piece_category_map
        for key, value in piece_denomination_map.items():
            for c in range(0,value):
                while True:
                    (rank, file) = self.get_random_position(start_rank, stop_rank, start_file, stop_file)
                    if self.__board_map[rank][file] == self.__init_piece:
                        self.__board_map[rank][file] = key
                        break
                    else:
                        continue

    def get_random_position(self, start_rank, stop_rank, start_file, stop_file):
        random_rank = rand.randrange(start_rank,stop_rank)
        random_file = rand.randrange(start_file,stop_file)
        return (random_rank, random_file)

    '''display board in console'''
    def display_board(self):
        for x in self.__board_map:
            print("{0}\n".format(x))

    '''return board to frontend as json'''
    def board_to_json(self) -> str:
        lists = self.__board_map.tolist()
        #json_str = json.dumps(lists)
        return jsonify(lists)
    

    '''
    Piece movement
    '''
    def move(self):
        constants.arbitration_map
        pass

    
    