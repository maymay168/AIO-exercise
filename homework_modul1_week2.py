# -*- coding: utf-8 -*-
"""homework-modul1-week2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lciW8LiWaJr2bFaGmIRBOo-XvvJFRJ48
"""

#Exercise 1
nnum_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
start_indexs = list(range(0, len(num_list)-k+1))
end_indexs = list(range(k, len(num_list)+1))

result = []
for start_indexs, end_indexs in zip(start_indexs, end_indexs):
    sub_list = num_list[start_indexs:end_indexs]
    result.append(max(sub_list))

print(result)

#Exercise 2
def character_count(word):
    character_statistic = {}

    for character in word:
        if character in character_statistic:
            character_statistic[character] += 1
        else:
            character_statistic[character] = 1
    return character_statistic

print(character_count('Happiness'))

#Exercise 3
#!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = '/content/P1_data.txt'
with open (file_path, 'r') as f:
  documents = f.readlines()
def word_count(sentences):
  for sentence in sentences:
    sentence = sentence.lower().strip()
    words = sentence.split(' ')
    set_words = set(words)
    wcount = {}
    for word in set_words:
      if word in wcount:
        wcount[word] += 1
      else:
        wcount[word] = 1
    print(wcount)

#Exercise 4
def levenshtein_calc(source, target):
  distances = [[0] * (len(target) + 1) for _ in range(len(source) + 1)]

  for i in range(len(target) + 1):
    distances[0][i] = i

  for j in range(len(source) + 1):
    distances[j][0] = j

  del_cost = 1
  ins_cost = 1
  for r in range(1, len(source) + 1):
    for c in range (1, len(target) + 1):
      if source[r - 1] == target[c - 1]:
        sub_cost = 0
      else:
        sub_cost = 1
      distances[r][c] = min(distances[r-1][c] + del_cost
                           , distances[r][c-1] + ins_cost
                           , distances[r-1][c-1] + sub_cost)
  return distances[len(source)][len(target)]