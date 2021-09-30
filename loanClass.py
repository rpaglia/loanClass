# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:42:53 2021
@author: Richard Paglia

Modify class loan to include a computation: 
    add two functions setPmt to specify how much you can
    affort, and computePV to compute how much $$
    you can borrow at that payment

formula: pmt = PV*(r*(1+r)**n)/((1+r)**months -1)

Suppose you budget $399/mo for the purchase;
    how much would you have to put down to get
    you payment to be $399 or less. 
"""

class loan(object):
    def __init__(self, name):
        self._name = name

    def who(self):
        print(self._name)

    def setPV(self, PV):
        self._PV = PV
        print('present value = ', self._PV)

    def setRate(self, ratePct):
        #set interest, apr
        self._ratePct = ratePct
        print('APR = ', self._ratePct,'%')

    def setMonths(self, months):
        self._months = months
        print(self._months, 'months')

    def computePmt(self):
        r = self._ratePct/100/12
        self._Pmt = self._PV*(r*(1+r)**self._months)/((1+r)**self._months-1)
        print('payment = $', round(self._Pmt,2))
        return self._Pmt
    
    def setPmt(self, Pmt):
        self._Pmt = Pmt
        print('set the payment to {}'.format(round(self._Pmt,2)))
              
    def computePV(self):
        r = self._ratePct/100/12
        self.PV = self._Pmt/r*(1-(1-r)**self._months)
        print('max loan = ${}'.format(round(self.PV,2)))

if __name__ == "__main__":
    loan1 = loan('Richie')
    loan1.who()

    loan1.setPV(27150)  #mini cooper
    loan1.setRate(1.9)
    loan1.setMonths(42)
    payment = loan1.computePmt()