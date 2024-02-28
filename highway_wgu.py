highway_number = int(input())



if highway_number % 2 == 0:

  direction = 'going east/west.'

else:

  direction = 'going north/south.'

  

if highway_number < 100:

    road = 'primary,'

    serving = '' 

else:

    road = 'auxiliary,'

    serving_number = str(highway_number % 100)

    serving = 'serving I-' +  serving_number + ','

    

  

if highway_number < 1 or highway_number > 999 or highway_number == 200:

    print(highway_number,'is not a valid interstate highway number.')

else:

    print(f'I-{highway_number} is {road} {serving} {direction}')