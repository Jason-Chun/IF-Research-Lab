def city_country(city, country):
  form = f"{city.title()}, {country.title()}"
  return form

done = city_country('Seoul', 'Korea')
print(done)

done2 = city_country('LA', 'US')
print(done2)

done3 = city_country('Vaughan', 'Canada')
print(done3)