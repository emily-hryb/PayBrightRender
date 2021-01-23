import urllib.parse
from urllib.parse import urlencode
       
#Here is where the values will be authenticated 
class AuthAPI():
    x_account_id = ''
    x_amount = ''
    x_currency = ''
    x_customer_billing_address1 = ''
    x_customer_billing_city = ''
    x_customer_billing_country = ''
    x_customer_billing_phone = ''
    x_customer_billing_state = ''
    x_customer_billing_zip = ''
    x_customer_billing_email = ''
    x_customer_first_name = ''
    x_customer_last_name = ''
    x_customer_phone = ''
    x_customer_shipping_address1 = ''
    x_customer_shipping_city = ''
    x_customer_shipping_country = ''
    x_customer_shipping_first_name = ''
    x_customer_shipping_last_name = ''
    x_customer_shipping_phone = ''
    x_customer_shipping_state = ''
    x_customer_shipping_zip = ''
    x_reference = ''
    x_shop_country = ''
    x_shop_name = ''
    x_test = ''
    x_url_callback = ''
    x_url_cancel = ''
    x_url_complete = ''
    def createBodyString(self):
        body = {'x_account_id' : self.x_account_id,
                     'x_amount' : self.x_amount, 
                     'x_currency' : self.x_currency,
                     'x_customer_billing_address1' : self.x_customer_billing_address1,
                     'x_customer_billing_city' : self.x_customer_billing_city,
                     'x_customer_billing_country' : self.x_customer_billing_country,
                     'x_customer_billing_phone' : self.x_customer_billing_phone,
                     'x_customer_billing_state' : self.x_customer_billing_state,
                     'x_customer_billing_zip' : self.x_customer_billing_zip,
                     'x_customer_billing_email' : self.x_customer_billing_email,
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
                     'x_reference' : self.x_reference,
                     'x_shop_country' : self.x_shop_country,
                     'x_shop_name' : self.x_shop_name,
                     'x_test' : self.x_test,
                     'x_url_callback' : self.x_url_callback,
                     'x_url_cancel' : self.x_url_cancel,
                     'x_url_complete' : self.x_url_complete
                     }

        bodyString = urllib.parse.urlencode(body)        
        signatureString = ""

        for chunk in (bodyString.split('&')):
            param = chunk.split('=')
            if (param and param[1] != ''): 
                signatureString = signatureString + urldecode(param[0]) + urldecode(param[1]);
    

        pb_sig = hash_hmac('sha256', signatureString, 'N88G3X1zPKkSEG1xdQGV7Bfy4OmJ1IMteX9CtmnwSU7VWgBzJR')
        bodyString = bodyString + "&x_signature=" + pb_sig
        return bodyString
    
    def render(self, bodyString):
        url = 'https://sandbox.paybright.com/CheckOut/ApplicationForm.aspx'
        req = urllib2.Request(url, bodyString) 
        response = urllib2.urlopen(req) 
        page = response.read()
        print (page + '\n\n')
        
        