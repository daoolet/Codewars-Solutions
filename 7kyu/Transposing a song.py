sharp = 'A,A#,B,C,C#,D,D#,E,F,F#,G,G#'.split(',')
flat  = 'A,Bb,B,C,Db,D,Eb,E,F,Gb,G,Ab'.split(',')

def transpose(song, interval):
    return [sharp[(sharp.index(i)+interval)%12] if i in sharp else sharp[(flat.index(i)+interval)%12] for i in song]

