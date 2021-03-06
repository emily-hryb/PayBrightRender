import binascii
import urllib.parse
from urllib.parse import urlencode
from urllib import request
import hmac
import hashlib 
import base64
import requests
from . import views
import logging
       
#Here is where the values will be authenticated 
class AuthAPI():
    x_account_id = ''
    x_amount = '800.00'
    x_currency = 'CAD'
    x_customer_billing_address1 = '9 Pali Drive'
    x_customer_billing_city = 'Brampton'
    x_customer_billing_country = 'CA'
    x_customer_billing_phone = '4168290145'
    x_customer_billing_state = 'ON'
    x_customer_billing_zip = 'L6P1G3'
    x_customer_email = 'ehryb@paybright.com'
    x_customer_first_name = 'Emily'
    x_customer_last_name = 'Hryb'
    x_customer_phone = '4168290145'
    x_customer_shipping_address1 = '9 Pali Drive'
    x_customer_shipping_city = 'Brampton'
    x_customer_shipping_country = 'CA'
    x_customer_shipping_first_name = 'Emily'
    x_customer_shipping_last_name = 'Hryb'
    x_customer_shipping_phone = '4168290145'
    x_customer_shipping_state = 'ON'
    x_customer_shipping_zip = 'L6P1G3'
    x_locale = 'en'
    x_reference = '680013618833'
    x_shop_country = 'CA'
    x_shop_name = 'Carlton'
    x_test = 'true'
    x_url_callback = 'https://google.com'
    x_url_cancel = 'https://google.com'
    x_url_complete = 'https://google.com'
    def createBodyString(self, key, token):
        body = {'x_account_id' : key,
                     'x_amount' : self.x_amount, 
                     'x_currency' : self.x_currency,
                     'x_customer_billing_address1' : self.x_customer_billing_address1,
                     'x_customer_billing_city' : self.x_customer_billing_city,
                     'x_customer_billing_country' : self.x_customer_billing_country,
                     'x_customer_billing_phone' : self.x_customer_billing_phone,
                     'x_customer_billing_state' : self.x_customer_billing_state,
                     'x_customer_billing_zip' : self.x_customer_billing_zip,
                     'x_customer_email' : self.x_customer_email,
                     'x_customer_first_name' : self.x_customer_first_name,
                     'x_customer_last_name' : self.x_customer_last_name,
                     'x_customer_phone' : self.x_customer_phone,
                     'x_customer_shipping_address1' : self.x_customer_shipping_address1,
                     'x_customer_shipping_city' : self.x_customer_shipping_city,
                     'x_customer_shipping_country' : self.x_customer_shipping_country,
                     'x_customer_shipping_first_name' : self.x_customer_shipping_first_name,
                     'x_customer_shipping_last_name' : self.x_customer_shipping_last_name,                     
                     'x_customer_shipping_phone' : self.x_customer_shipping_phone,
                     'x_customer_shipping_state' : self.x_customer_shipping_state,
                     'x_customer_shipping_zip' : self.x_customer_shipping_zip,
                     'x_locale' : self.x_locale,
                     'x_reference' : self.x_reference,
                     'x_shop_country' : self.x_shop_country,
                     'x_shop_name' : self.x_shop_name,
                     'x_test' : self.x_test,
                     'x_url_callback' : self.x_url_callback,
                     'x_url_cancel' : self.x_url_cancel,
                     'x_url_complete' : self.x_url_complete
                     }
        bodyAsString = ""
        for element in body:
            bodyAsString = bodyAsString + element + body[element]
       
        bodyEncoded = urllib.parse.urlencode(body)         
        signatureString = ""
        signatureStringDecoded = ""

        for chunk in (bodyEncoded.split('&')):
            param = chunk.split('=')
            if (param and param[1] != ''): 
                parm1 = urllib.parse.quote_plus(param[0])
                parm2 = urllib.parse.quote_plus(param[1])
                signatureString = signatureString + parm1 + parm2                 
        
        secretKey = token       
        
        pb_sig = hmac.new(bytes(secretKey, 'utf-8'), bodyAsString.encode('utf-8'), hashlib.sha256).hexdigest()        
        bodyEncoded = bodyEncoded + "&x_signature=" + pb_sig
        
        return bodyEncoded
    
    def render(self, bodyString):
        logging.basicConfig(level=logging.DEBUG, filename='myapp.log', format='%(asctime)s %(levelname)s:%(message)s')
        url = 'https://sandbox.paybright.com/CheckOut/ApplicationForm.aspx'    
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        r = requests.post(url, data=bodyString, headers=headers)
        logging.debug(r)
        return r
        