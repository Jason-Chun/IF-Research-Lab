def build(first, last, **info):
  info['first name'] = first
  info['last name'] = last
  return info

profile = build('jason', 'chun', location = 'room', field = 'gaming', age = 14)

print(profile)