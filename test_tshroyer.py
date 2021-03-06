from shipping import Address
from shipping import Package
from ups import PACKAGES
import logging
logging.basicConfig(level=logging.DEBUG, filename='test.log')
from shipping import setLoggingLevel
setLoggingLevel(logging.DEBUG)
#logging.getLogger('%s.ups' % __name__).setLevel(logging.DEBUG)
#logging.getLogger('%s.fedex' % __name__).setLevel(logging.DEBUG)


white_house = Address('Mr. President', '1600 Pennsylvania Avenue NW', 'Washington', 'DC', '20500', 'US', company_name='White House')
powells = Address('Manager', '1005 W Burnside', 'Portland', 'OR', '97209', 'US', is_residence = False, company_name='Powell\'s City of Books')
our_place = Address('Wholesale Imports Guy', '4957 Summer Ave', 'Memphis', 'TN', '38122', 'US', is_residence = False, company_name='WholesaleImport.com')

import config
ups_config = config.getConfig('ups')
fedex_prod = config.getConfig('fedex')
fedex_test = config.getConfig('fedex_test')

from ups import UPS
ups = UPS(ups_config, debug=False)
#print(white_house)
#print(ups.validate(white_house))

#print(powells)
#r = ups.validate(powells)
#print r

ten_pound_box = Package(10.0 * 16, 12, 12, 12, value=100, require_signature=3, reference='a12302b')
our_packaging =  PACKAGES[0][0]

# Send some books to powells because they need some more
#print(ups.rate([ten_pound_box], our_packaging, our_place, powells))

import fedex
prod = fedex.Fedex(fedex_prod, debug=False)
test = fedex.Fedex(fedex_test, debug=True)
our_packaging = fedex.PACKAGES[4]
# Powells really likes books
#r = test.rate([ten_pound_box], our_packaging, our_place, powells)
#print r
try:
   r = prod.rate([ten_pound_box], our_packaging, our_place, powells)
   print r
except Exception as e:
   r = e
   print r