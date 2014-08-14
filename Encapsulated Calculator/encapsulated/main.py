
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #sets up balances and functions
        joe = Balance()
        joe.initial_balance = 42128.96
        joe.debit1 = 250.88
        joe.debit2 = 1545.23
        joe.debit3 = 120.00
        joe.debit4 = 980.00
        joe.credit1 = 995.00
        joe.calc_balance()

        colleen = Balance()
        colleen.initial_balance = 24128.96
        colleen.debit1 = 45.33
        colleen.debit2 = 1124.95
        colleen.debit3 = 450.44
        colleen.debit4 = 99.99
        colleen.credit1 = 1200.00
        colleen.calc_balance()

        bubba = Balance()
        bubba.initial_balance = 180454.55
        bubba.debit1 = 8983.43
        bubba.debit2 = 125.65
        bubba.debit3 = 774.90
        bubba.debit4 = 12.99
        bubba.credit1 = 4533.00
        bubba.calc_balance()

        dawn = Balance()
        dawn.initial_balance = 50345.44
        dawn.debit1 = 883.22
        dawn.debit2 = 99.99
        dawn.debit3 = 88.42
        dawn.debit4 = 19.99
        dawn.credit1 = 999.00
        dawn.calc_balance()

        stanley = Balance()
        stanley.initial_balance = 24845.21
        stanley.debit1 = 603.22
        stanley.debit2 = 18.89
        stanley.debit3 = 358.34
        stanley.debit4 = 88.99
        stanley.credit1 = 2477.00
        stanley.calc_balance()

        #start webpage
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Account Balance Calculator</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div class="wrapper">
    '''

        page_body = '''

        <div class="customers">
            <h1>Frederica National Bank</h1>
            <a href="?name=Joe Bazooka&balance={joe.initial_balance}&debit1=
            {joe.debit1}&debit2={joe.debit2}&debit3={joe.debit3}&debit4={joe.debit4}&credit={joe.credit1}
            &end_balance={joe.end_balance}">Joe</a><br/>

            <a href="?name=Colleen Smith&balance={colleen.initial_balance}&debit1=
            {colleen.debit1}&debit2={colleen.debit2}&debit3={colleen.debit3}&debit4={colleen.debit4}&credit=
            {colleen.credit1}&end_balance={colleen.end_balance}">Colleen</a><br/>

             <a href="?name=Bubba Jones&balance={bubba.initial_balance}&debit1=
            {bubba.debit1}&debit2={bubba.debit2}&debit3={bubba.debit3}&debit4={bubba.debit4}&credit={bubba.credit1}
            &end_balance={bubba.end_balance}">Bubba</a><br/>

            <a href="?name=Dawn Rocker&balance={dawn.initial_balance}&debit1=
            {dawn.debit1}&debit2={dawn.debit2}&debit3={dawn.debit3}&debit4={dawn.debit4}&credit={dawn.credit1}
            &end_balance={dawn.end_balance}">Dawn</a><br/>

            <a href="?name=Stanley Johnson&balance={stanley.initial_balance}&debit1=
            {stanley.debit1}&debit2={stanley.debit2}&debit3={stanley.debit3}&debit4={stanley.debit4}&credit=
            {stanley.credit1}&end_balance={stanley.end_balance}">Stanley</a><br/>
        </div>'''

        page_info = '''<div class="customers">
        <div class="cus_wrap"
        <p>Name: {name}</p>
        <p>Initial balance: {balance}</p>
        <p>Debit #1: {debit1}</p>
        <p>Debit #2: {debit2}</p>
        <p>Debit #3: {debit3}</p>
        <p>Debit #4: {debit4}</p>
        <p>Credit: {credit}</p>
        <p>Ending Balance: {end_balance}</p>
        </div>
        <a href="?">Return</a></div>
        '''

        page_close = '''
        </div>
    </body>
</html>'''

        page_body = page_body.format(**locals())

        if self.request.GET:
            name = self.request.GET['name']
            balance = self.request.GET['balance']
            debit1 = self.request.GET['debit1']
            debit2 = self.request.GET['debit2']
            debit3 = self.request.GET['debit3']
            debit4 = self.request.GET['debit4']
            credit = self.request.GET['credit']
            end_balance = self.request.GET['end_balance']

            page_info = page_info.format(**locals())
            self.response.write(page_head + page_info + page_close)
        else:
            self.response.write(page_head + page_body + page_close)


class Balance(object):
    def __init__(self):
        self.initial_balance = 0
        self.debit1 = 0
        self.debit2 = 0
        self.debit3  = 0
        self.debit4 = 0
        self.credit1 = 0
        self.__end_balance = 0

  

#never touch this!!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
