
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

        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
