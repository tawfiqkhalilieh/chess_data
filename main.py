from render_board import render_board
import chess.engine
import chess.pgn
import chess.polyglot

thinking_time = 0.1

stockfish = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
# komodo = chess.engine.SimpleEngine.popen_uci("komodo.exe")
batata = chess.engine.SimpleEngine.popen_uci("batata_engine/lc0.exe")


def data_writer(board, game_number):
    long_string = " ".join([str(move) for move in board.move_stack])
    print(long_string)
    with open(f"data/{thinking_time}/game{game_number}.txt", "w") as f:
        f.write(long_string)


count = 1 # for now you should update this manually

while True:
    board = chess.Board()
    try:
        while not board.is_game_over():
            board.push(stockfish.play(board, chess.engine.Limit(time=thinking_time )).move)
            render_board(board, thinking_time )
            if not board.is_game_over():
                board.push(batata.play(board, chess.engine.Limit(time=thinking_time )).move)
                render_board(board, thinking_time )
    except:
        stockfish = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
        batata = chess.engine.SimpleEngine.popen_uci("batata_engine/lc0.exe")

    data_writer(board=board, game_number=count)
    count += 1

    board = chess.Board()
    try:
        while not board.is_game_over():
            board.push(batata.play(board, chess.engine.Limit(time=thinking_time )).move)
            render_board(board, thinking_time )
            if not board.is_game_over():
                board.push(stockfish.play(board, chess.engine.Limit(time=thinking_time )).move)
                render_board(board, thinking_time )
    except:
        stockfish = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
        batata = chess.engine.SimpleEngine.popen_uci("batata_engine/lc0.exe")

    data_writer(board=board, game_number=count)
    count += 1

batata.quit()
stockfish.quit()
