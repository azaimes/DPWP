
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #sets up balances and functions
        joe = balance()
        joe.initial_balance = 42128.96
        joe.debit1 = 250.88
        joe.debit2 = 1545.23
        joe.debit3 = 120.00
        joe.debit4 = 980.00
        joe.credit1 = 995.00
        joe.calc_balance()

        colleen = ballance()
        colleen.initial_balance = 24128.96
        colleen.debit1 = 45.33
        colleen.debit2 = 1124.95
        colleen.debit3 = 450.44
        colleen.debit4 = 99.99
        colleen.credit1 = 1200.00
        colleen.calc_balance()

        



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
