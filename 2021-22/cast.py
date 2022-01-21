import csv
import ast

delim = '\t'

with open("cast.tsv", "w") as cfile:
    with open('../movies/kaggle/credits.csv') as f:
        reader = csv.reader(f)
        next(reader, None)
        for (ix, row) in enumerate(reader):
            print(ix, '#'*10)
            txt = row[0][1:-1]
            try:
                cast = ast.literal_eval(txt) 
            except Exception:
                print("FAILED TO PARSE", row)
                cast = []
            if isinstance(cast, list) or isinstance(cast, tuple):
                actors = [c['name'] for c in cast]
            elif isinstance(cast, dict):
                actors = [cast['name']]
            elif isinstance(cast, str):
                actors = cast.split(',')
            else:
                print(cast, type(cast))
                raise Exception("UNKNOWN TYPE")
            print(row[2] + delim + delim.join(actors), file=cfile)
