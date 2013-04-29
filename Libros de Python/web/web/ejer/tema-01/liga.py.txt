
from operator import itemgetter

def result (fin, fout):
    fin  = open (fin) 
    data = [filter (bool, s.split (' ')) for s in fin]
    fin.close ()
    
    data = [(l[0], sum (map (int, l[1:]))) for l in data]
    data = sorted (data, reverse=True, key=itemgetter (1))
    data = [' '.join (map (str, l)) + '\n' for l in data]

    fout = open (fout, 'w')
    fout.writelines (data)
    fout.close ()
