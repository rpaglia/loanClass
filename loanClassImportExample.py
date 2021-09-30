# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:52:02 2021
@author: Richard Paglia

example use of loanClass
"""

import loanClass

richie = loanClass.loan('Richie')
richie.who()

richie.setRate(4.4)
richie.setMonths(48)
richie.setPmt(399)

richie.computePV()