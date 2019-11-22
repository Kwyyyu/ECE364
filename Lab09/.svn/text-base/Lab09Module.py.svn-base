#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/29/2019>
#######################################################

import re

def getNumberPattern():
    pattern=r"[+-]*[0-9Ee+-]+[0-9.]*"
    return pattern

def getLinkPattern():
    pattern = r'<a[ ]*href="(?P<url>.+)">(?P<text>.+)</a>'
    return pattern

def getDataPattern():
    pattern = r'"(?P<key>[\w]+)?"[ ]*:[ ]*"(?P<value>.+)?"'
    return pattern


class Action:
    def __init__(self, actionType: str, amount: float):
        if actionType == 'W' or actionType == 'D':
            self.actionType = actionType
        else:
            raise ValueError("Wrong actionType input!")
        if amount < 0:
            raise ValueError("Amount should be positive!")
        else:
            self.amount = round(amount, 2)

    def __str__(self):
        return self.actionType+" "+str(self.amount)


class Client:
    def __init__(self, fn: str, ln: str):
        self.firstName = fn
        self.lastName = ln

    def __str__(self):
        return self.firstName + " " + self.lastName


class Account:
    def __init__(self, number: str, client: Client, amount: float, min: float):
        self.accountNumber = number
        self.client = client
        self.amount = round(amount, 2)
        self.minThreshold = min

    def __str__(self):
        name = self.client.firstName + " " + self.client.lastName
        if self.amount >= 0:
            return f"{self.accountNumber}, {name}, Balance = ${'%.2f' % self.amount}"
        else:
            amount = '%.2f' % self.amount
            return f"{self.accountNumber}, {name}, Balance = (${amount[1:]})"

    def performAction(self, act: Action):
        if act.actionType == 'D':
            self.amount += act.amount
            self.amount = round(self.amount, 2)
        else:
            if self.amount - act.amount >= 0:
                self.amount -= act.amount
                self.amount = round(self.amount, 2)
                if self.amount < self.minThreshold:
                    self.amount -= 10.00
                    self.amount = round(self.amount, 2)
            else:
                raise ValueError("Not enough amount to be withdraw in the account!")

class Institute:
    def __init__(self):
        self.account = {}

    def createNew(self, fn: str, ln: str, num: str):
        if num not in self.account:
            client = Client(fn, ln)
            new_account = Account(num, client, 500.00, 1000.00)
            self.account[new_account] = new_account.accountNumber

    def performAction(self, num: str, act: Action):
        accounts = self.account.keys()
        index = 0
        for a in accounts:
            if num == a.accountNumber:
                print(a.amount)
                a.performAction(act)
                print(a.amount)
                break


def loadHistory(filename: str):
    inst = Institute()
    account = set()
    with open(filename, "r") as nFile:
        contents = nFile.readlines()
    for content in contents[3:]:
        _, name, _, num, _, trans, _ = content.split('"')
        if num not in account:
            fn, ln = name.split(" ")
            account.add(num)
            inst.createNew(fn,ln,num)
            if "(" in trans:
                num = float(trans[2:len(trans)-1])
            else:
                num = float(trans[1:len(trans)])


    for a in inst.account:
        print(a.accountNumber, a.amount)






if __name__ == "__main__":
    # pattern = getNumberPattern()
    # s = "With the electron -1.67e-19"
    # print(re.findall(pattern,s))
    # pattern = getLinkPattern()
    # s = 'acvd sertser <a href="http://abc.com">website A</a> end adfae.'
    # m=re.search(pattern, s)
    # print(m['url'])
    # print(m['text'])
    # pattern = getDataPattern()
    # s = '{"NAme" : "Kai Yu", "test" : "abcd"}'
    # m = re.findall(pattern,s)
    # print(m)
    act1 = Action('W', 27.3175)
    # act2 = Action('W', 1100.564)
    # print(act1)
    # client1 = Client("John", "Smith")
    # print(client1)
    # account1 = Account("15234-56844", client1, 1123, 100)
    # print(account1)
    # account1.performAction(act2)
    # print(account1)
    inst1 = Institute()
    inst1.createNew("John", "Dow", "12345-56789")
    inst1.createNew("John", "Smith", "15234-56844")
    inst1.performAction("15234-56874", act1)
    print()
    loadHistory("history.txt")
