names = {
    'Jason': {
      'first_name' : 'Jason', 
      'last_name' : 'Chun', 
      'age' : '13', 
      'city' : 'Ova ther'
      },

    'Philip' : {
      'first_name' : 'Philip', 
      'last_name' : 'Philp?', 
      'age' : '13-14', 
      'city' : 'On the corner of the asteriod5 and past the dust pellet next to the sauser'
      },

    'Jaden' : {
      'first_name' : 'Jaden', 
      'last_name' : 'Jaden?', 
      'age' : '13-14', 
      'city' : 'Milkyway on the right next to the asteriod on the left of the black part'
      }
    }

for name, info in names.items():
  print()
  full_name = f"{info['first_name']} {info['last_name']}"
  print(f"\nName: {full_name.title()}")
  print(f"Age: {info['age']}")
  print(f"Location: {info['city']}")