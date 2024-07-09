from string import ascii_uppercase as alp


def get_best_word(points, words):
    zipped_dict = {letter: point for point, letter in zip(points, alp)}
    answer = []
    max_sum = 0

    for idx, word in enumerate(words):

        current_sum = sum(list(map(lambda x: zipped_dict.get(x), word)))
        if current_sum >= max_sum:
            max_sum = current_sum
            answer.append([idx, word, max_sum])

    answer.sort(key=lambda x: x[2], reverse=True)
    return answer
    
points = (1,3,3,2,1,4,2,4,1,8,10,1,2,1,1,3,8,1,1,1,1,4,10,10,10,10)

print(get_best_word(points, ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG']))

print(get_best_word(points, ["NOQ","TXAY","S","OM","ESFT","CJUKQ","QL","QO","ASTK","Y"]))