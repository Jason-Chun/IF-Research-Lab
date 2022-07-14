def album(artist, title):
  alb = {artist : title}
  val = alb[artist]
  return val

hi = album('me', 'you')
print(hi)