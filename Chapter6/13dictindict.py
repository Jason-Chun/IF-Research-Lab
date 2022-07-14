user = {
    'babyyoda' : {
        'First' : 'Jason',
        'Last' : 'Chun',
        'Location' : 'milkyway'
    },

    'Phil' : {
        'First' : 'Philip',
        'Last' : 'Philip',
        'Location' : 'Irvine somewhere'
    },
    'Jad' : {
        'First' : 'Jaden',
        'Last' : 'Jaden',
        'Location' : 'house'
    }
}

for username, user_info in user.items():
  print(f"Username: {username}")
  full_name = f"{user_info['First']} {user_info['Last']}"
  location = user_info['Location']
  print(f"\tFull name: {full_name.title()}")
  print(f"\tLocation: {location.title()}")