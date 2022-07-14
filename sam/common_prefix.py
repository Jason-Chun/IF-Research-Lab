words = ['prelude', 'previous', 'preprocess', 'prejudge', 'predict', 'prefix', 'prefer' ]

def common_prefix(words):
  record = 0
  for i in range(len(words)):
    for j in range(len(words)):
      borb = min(len(words[i]), len(words[j]))
      for k in range(borb):
        if words[i][k] == words[j][k]:
          continue
        else:
          record = k
          break      
  return words[0][:record]

print(common_prefix(words))