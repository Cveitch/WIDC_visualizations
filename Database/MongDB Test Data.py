# Author: Daniel O'Reilly

from Database.MongoDB import sensorData

# Can take any amount of data without having to add 999 or an arbitrary value to the database
# this allows for easier querying and overall ease of use

data = [1, 2, 3]

user = sensorData()
try:

    user.temperature1 = data[0]
    user.save()
except IndexError:

    user.temperature1 = 'null'

try:

    user.temperature2 = data[1]
    user.save()

except IndexError:

    user.temperature2 = 'null'

try:
    user.temperature3 = data[2]
    user.save()

except IndexError:

    user.tempreature3 = 'nulll'

try:
    user.temperature4 = data[3]
    user.save()

except IndexError:

    user.temperature4 = 'null'

try:

    user.temperature5 = data[4]
    user.save()

except IndexError:

    user.temperature5 = 'null'

try:
    user.temperature6 = data[5]
    user.save()

except IndexError:

    user.temperature6 = 'null'

try:
    user.temperature7 = data[6]
    user.save()

except IndexError:

    user.temperature7 = 'null'

try:
    user.temperature8 = data[7]
    user.save()

except IndexError:

    user.temperature8 = 'null'
