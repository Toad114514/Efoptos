#!/usr/bin/env python
# encoding: utf-8
import npyscreen
class hcmc(npyscreen.Form):
    def create(self):
        self.myName        = self.add(npyscreen.TitleText, name='EfoptOS帮助中心(TUI)')
        self.realylabel       = self.add(npyscreen.TitleText, name='选择帮助指引')

def myFunction(*args):
    F = hcmc(name = "EfoptOS 帮助中心")
    F.edit()
    return "Created record for " + F.myName.value

if __name__ == '__main__':
    print( npyscreen.wrapper_basic(myFunction))