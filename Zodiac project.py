print("If you don't know your signs yet, please click the link below and find out!")
print("https://askastrology.com/astrology/birth-natal-chart-calculator/")
print("Note: the other name for 'rising' is 'ascendant'.")

elements = {'cancer':'water',
            'pisces':'water',
            'scorpio':'water',
            'sagittarius':'fire',
            'leo':'fire',
            'aries':'fire',
            'libra':'air',
            'gemini':'air',
            'aquarius':'air',
            'taurus':'earth',
            'capricorn':'earth',
            'virgo':'earth'}

sun = input("What is your sun sign?").lower()
rising = input("What is your rising sign?").lower()
moon = input("What is your moon sign?").lower()

while sun not in elements:
  print("Please enter the correct sun.")
  sun = input("What is your sun sign?").lower()
  if sun in elements:
   break

while rising not in elements:
  print("Please enter the correct rising.")
  rising = input("What is your rising sign?").lower()
  if rising in elements:
    break

while moon not in elements:
  print("Please enter the correct moon.")
  moon = input("What is your moon sign?").lower()
  if moon in elements:
    break
    
#all three are the same
if sun == moon and moon == rising:
  print('Your sign probability is equal to 0,69%.')

#two are the same and the third one is in the same element
elif sun == moon and elements[sun] == elements[rising] and sun != rising or moon == rising and elements[rising] == elements[sun] and moon != sun or sun == rising and elements[rising] == elements[moon] and moon != sun:
  print('Your sign probability is equal to 2%.')

#two are the same, but the third one is in a different element
elif sun == moon and moon != rising and elements[sun] != elements[rising] or moon == rising and moon != sun and elements[moon] != elements[sun] or rising == sun and rising != moon and elements[rising] != elements[moon]:
  print('Your sign probability is equal to 6%.')

#all are in different elements (and different ofc)
elif elements[sun] != elements[moon] and elements[moon] != elements[rising]:
  print('Your sign probability is equal to 37,5%.')

#all are different, but are in the same element
elif sun != moon and moon != rising and elements[sun] == elements[moon] and elements[moon] == elements[rising]:
  print('Your sign probability is equal to 1,38%.')

#all are different, but two are in the same element and the third one is in a different one
elif sun != moon and moon != rising and elements[sun] == elements[moon] and elements[moon] != elements[rising] or sun != moon and moon != rising and elements[sun] != elements[moon] and elements[moon] == elements[rising] or sun != moon and moon != rising and elements[sun] != elements[moon] and elements[sun] == elements[rising]:
  print('Your sign probability is equal to 12,5%.')

else:
  print("Sorry, I'm not this good at math.")
