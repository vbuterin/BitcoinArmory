import sys
sys.path.append('..')
sys.path.append('.')

from armoryengine import *
import connector

import p2ptrade
import colortools

connector.init()

class EchoExchangeComm:
    def __init__(self):
        self.agents = []
    def addAgent(self, agent):
        self.agents.append(agent)
    def postMessage(self, content):
        print content
        for a in self.agents:
            a.dispatchMessage(content)

comm = EchoExchangeComm()

def mkagent(wfile):
    wlt = PyBtcWallet().readWalletFile(wfile)
    connector.register_wallet(wlt)
    a = p2ptrade.ExchangePeerAgent(wlt, comm)
    comm.addAgent(a)
    return a

ag1 = mkagent(CLI_ARGS[0])
ag2 = mkagent(CLI_ARGS[1])

testcolor = '8ec9668e393f2b7682daa2fd40eeee873c07c9ed'
uncolored = ''

o1 = p2ptrade.ExchangeOffer(None, {"value": 100, "colorid": testcolor}, {'value': 100, 'colorid': uncolored})
o2 = p2ptrade.ExchangeOffer(None, {"value": 100, "colorid": uncolored}, {"value": 100, 'colorid': testcolor})

ag1.registerMyOffer(o1)
print "o1 registered"
ag2.registerMyOffer(o2)
print "o2 registered"

ag1.postMessage(o1)
print "o1 posted"

