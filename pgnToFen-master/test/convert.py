import pgntofen

#filenames = ["pgndata/data00.pgn","pgndata/data01.pgn", "pgndata/data02.pgn", "pgndata/data03.pgn", "pgndata/data04.pgn", "pgndata/data05.pgn", "pgndata/data06.pgn","pgndata/data07.pgn", "pgndata/data08.pgn", "pgndata/data09.pgn"]
# for testdata
filenames = ["pgndata/data06.pgn"]#, "pgndata/data05.pgn"] #, "pgndata/data02.pgn", "pgndata/data03.pgn"]
#filenames = ["fischer_keres.pgn"]
pgnConverter = pgntofen.PgnToFen()
for filename in filenames:
    pgnConverter.resetBoard()
    stats = pgnConverter.pgnFile(filename)
    
    # Output file for FEN
    f = open("strides6_fen", "a")
    print("#### succeeded:", len(stats['succeeded']), "failed:", len(stats['failed']), "#####")
    for game in stats['succeeded']:
        try:
            fenlist = game[-1]
            # write in batches of 12 with a stride of 3
            stride = 9
            chunk_size = 12
            chunks = [fenlist[i:i+chunk_size] for i in range(0, len(fenlist)-chunk_size+1, stride)]
            for batch in chunks:
                f.write(';'.join(batch) + '\n')
        except IndexError:
            pass

    f.close()

