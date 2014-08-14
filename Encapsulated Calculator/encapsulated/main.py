
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

        bubba = balance()
        bubba.initial_balance = 180454.55
        bubba.debit1 = 8983.43
        bubba.debit2 = 125.65
        bubba.debit3 = 774.90
        bubba.debit4 = 12.99
        bubba.credit1 = 4533.00
        bubba.calc_balance()

        dawn = balance()
        dawn.initial_balance = 50345.44
        dawn.debit1 = 883.22
        dawn.debit2 = 99.99
        dawn.debit3 = 88.42
        dawn.debit4 = 19.99
        dawn.credit1 = 999.00
        dawn.calc_balance()








app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
