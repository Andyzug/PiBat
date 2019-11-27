# pibat.py

import smbus
import time

full=4.05
empty=3.26
class MCP3021:
    VINmax = 5.1
    bus = smbus.SMBus(1)
    
    def __init__(self, address = 0x4D):
        self.address = address
    
    def setVINmax(self, v):
        self.VINmax = v
    
    def readRaw(self):
        # Reads word (16 bits) as int
        rd = self.bus.read_word_data(self.address, 0)
        # Exchanges high and low bytes
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        # Ignores two least significiant bits
        return data >> 2
    
    def getValue(self):
        return float(self.VINmax) * self.readRaw() / 1023.0

adc = MCP3021()
def draw():
    print """
         \033[1;32;40m ,,ww,,     ,,,ww,,
        @]mM**MNg"w#"gNM*MMmC@
        @]b *Ng, $' [ ,gP" $\P
         N"N,  ]P`  '%   ,@)F
          ]N;2@,,m*Mw,;][/@
            \033[1;31;40m gP]g    ]"%, 
        ,K%*,r"''m-]P"`"N[NK$
       @V"$]-     P$     ]gP*pw
      ]UL [],   ,@ 'N    /"W $$
       %AmL, ""]P" `"%""`wm@myC
        $]- '*,$      @@`  ]yC
     \033[1;30;40m ,g@@K   '@@,  g@@    @@Ng
     g@" "@g   @PPPP"$K  ,@@  *@.
    j@^    "MNNPJ@ J@"NNMP"    ]@
    "RPMBN                 g@NP*R
         ]@Nw,          ,g@@`
         ,  `%N,,    ,,@P-,,
         @P   '""Bb@P"`'  ]@
         M`  @P   @[  ]@  *P
             @P   ,   ]@
                  @[
                  %F
           \033[1;37;40m PiBat Status"""
def ReadVoltage(num): #num- number of samples

    i=0
    tmp=0
    voltage = 0
    for x in range(num):
        tmp = adc.getValue()
        voltage =voltage + tmp
       
    return voltage/num;

def pibatlvl(v): # returns battery %, 'v' is voltage
    lvl= ((v - empty) * 100) / (full - empty)
    if lvl>100: # when charging this value can be more than 100% that's why we use this 'if'
        return 100
    else:
        return lvl

draw()
print "Voltage=%4.1f"%ReadVoltage(50),"v", "    Level=%4.1f"%pibatlvl(ReadVoltage(50)),"%" 

