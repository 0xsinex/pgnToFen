import pgntofen

filenames = ["path/to/file1", "path/to/file2"]

pgnConverter = pgntofen.PgnToFen()
for filename in filenames:
    pgnConverter.resetBoard()
    stats = pgnConverter.pgnFile(filename)
    
    # Output file for FEN
    f = open("path/to/output/file", "a")
    print("#### succeeded:", len(stats['succeeded']), "failed:", len(stats['failed']), "#####")
    for game in stats['succeeded']:
        try:
            fenlist = game[-1]
            # writes in batches of 12 with a stride of 3, replace with regular writing if needed
            stride = 9
            chunk_size = 12
            chunks = [fenlist[i:i+chunk_size] for i in range(0, len(fenlist)-chunk_size+1, stride)]
            for batch in chunks:
                f.write(';'.join(batch) + '\n')
        except IndexError:
            pass

    f.close()

