import re, collections

def get_stats(dictionary):
    #유니그램의 pair들의 빈도수를 카운트
    pairs = collections.defaultdict(int)

    for word, freq in dictionary.items():
        symbols = word.split()

        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i + 1]] += freq

    print('현재 pair들의 빈도수: ', dict(pairs))
    return pairs

def merge_dictionary(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')

    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]

    return v_out

# OOV
def get_pairs(word):
    ''' Return set of symbol pairs in a word.
    Word is represented as a tuple of symbols (symbols being variable-length strings).
    '''

    pairs = set()
    prev_char = word[0]

    for char in word[1:]:
        pairs.add((prev_char, char))
        prev_char = char

    return pairs

def encode(orig):
    ''' Encode word based on list of BPE merge operations, which are applied consecutively'''

    word = tuple(orig) + ('</w>',)
    print('word split into character: {}'.format(word))

    pairs = get_pairs(word)

    if not pairs:
        return orig

    iteration = 0
    while True:
        iteration += 1
        print('Iteration {}:'.format(iteration))
        print('bigrams in the word: {}'.format(pairs))

        bigram = min(pairs, key = lambda pair: bpe_codes.get(pair, float('inf')))
        print('candidate for merging: {}'.format(bigram))

        if bigram not in bpe_codes:
            print('Candidate not in BPE merges, algorithm stops.')
            break

        first, second = bigram
        new_word = []
        i = 0
        while i < len(word):
            try:
                j = word.index(first, i)
                new_word.extend(word[i:j])
                i = j
            except:
                new_word.extend(word[i:])
                break

            if word[i] == first and i < len(word) - 1 and word[i + 1] == second:
                new_word.append(first + second)
                i += 2
            else:
                new_word.append(word[i])
                i += 1

        new_word = tuple(new_word)
        word = new_word
        print('word after merging: {}'.format(word))

        if len(word) == 1:
            break
        else:
            pairs = get_pairs(word)

    # </w>는 출력하지 X
    if word[-1] == '</w>':
        word = word[:-1]
    elif word[-1].endswith('</w>'):     # 지정된 접미사로 끝나면 True, 그렇지 않으면 False 반환
        word = word[:-1] + (word[-1].replace('</w>', ''),)

    return word

if __name__ == '__main__':
    num_merges = 10
    dictionary = {'l o w </w>': 5,
                  'l o w e r </w>': 2,
                  'n e w e s t </w>': 6,
                  'w i d e s t </w>': 3}

    bpe_codes = {}
    bpe_codes_reverse = {}

    for i in range(num_merges):
        print("Iteration {}".format(i + 1))
        pairs = get_stats(dictionary)
        best = max(pairs, key=pairs.get)
        dictionary = merge_dictionary(best, dictionary)

        bpe_codes[best] = i
        bpe_codes_reverse[best[0] + best[1]] = best

        print("new merge: {}".format(best))
        print("dictionary: {}".format(dictionary))
        print()

    print()
    print('bpe_codes: ', bpe_codes)
    print('bpe_codes_reverse: ', bpe_codes_reverse)
    print()

    # OOV
    print(encode('loki'))
    print('-------------------------------------------')
    print(encode('lowest'))
    print('-------------------------------------------')
    print(encode('lowing'))
    print('-------------------------------------------')
    print(encode('highing'))