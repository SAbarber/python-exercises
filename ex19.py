## Create a mapping of state to abbreviation
# Add Oklahoma and Texas to the end of the list of States.

states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI',
          'Oklahoma': "OK",
          'Texas': 'TX'}
          
cities = {'CA': 'San Francisco',
          'MI': 'Detroit', 
          'FL': 'Jacksonville'}  
          
#add the rest of the cities here including Oklahoma and Texas

cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'
cities ['OK'] = 'Oklahoma City'
cities ['TX'] = 'Austin'

# Print out all the cities
print ('-' * 20)
print ("NY State has: ", cities['NY'])
print ("CA State has: ", cities['CA'])
print ("MI State has: ", cities['MI'])
print ("FL State has: ", cities['FL'])
print ("OR State has: ", cities['OR'])
print ("OK State has: ", cities['OK'])
print ("TX State has: ", cities['TX'])


# Print out all the states
print ('-' * 20)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("New York's abbreviation is: ", states['New York'])
print ("California's abbreviation is: ", states['California'])
print ("Florida's abbreviation is: ", states['Florida'])
print ("Oregon's abbreviation is: ", states['Oregon'])
print ("Oklahoma's abbreviation is: ", states['Oklahoma'])
print ("Texas' abbreviation is: ", states['Texas'])

