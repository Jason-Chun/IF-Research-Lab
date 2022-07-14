def album(artist, title):
  alb = {artist : title}
  return alb

rorb = True

while rorb:
  artist = input("Tell me a music artist: ")
  if artist == 'quit':
     break

  title = input("Tell the title of a music album by the previous artist: ")
 
  hi = album(artist, title)
  print(hi)


