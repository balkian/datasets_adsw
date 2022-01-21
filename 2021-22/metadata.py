import ast
import csv

def clean_field(fname, value):
    if fname == 'spoken_languages':
        try:
            value = ast.literal_eval(value)
            return ','.join(l['iso_639_1'] for l in value)
        except Exception:
            print("Could not evaluate AST: ", value)
            return ''
    
    if fname == 'genres':
        value = ast.literal_eval(value)
        return ','.join(v['name'] for v in value)
    return value

keep_fields = [
    'popularity',
    'vote_average',
    'vote_count'
    'id',
    'imdb_id',
    'original_title',
    'budget',
    'genres',
    'homepage',
    'original_language',
    'overview',
    'release_date',
    'revenue',
    'runtime',
    'spoken_languages',
    'tagline',
    'title',
    'adult',]


with open('metadata.tsv', 'w') as fmeta:
    writer = csv.DictWriter(fmeta, delimiter='\t', fieldnames=keep_fields)
    writer.writeheader()
    with open('../movies/kaggle/movies_metadata.csv') as forig:
        corig = csv.DictReader(forig)
        for row in corig:
            writer.writerow({k:clean_field(k, v) for (k,v) in row.items() if k in keep_fields})
