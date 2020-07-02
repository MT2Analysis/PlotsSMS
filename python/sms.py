from array import *

class sms():

    def __init__(self, modelname):
        self.mTopDiagOn = False
        self.t2ccDiagOn = False
        self.diagOn     = False
        self.extraText  = False
        if modelname.find("rpvMonoPhi") != -1: self.rpvMonoPhi()
        if modelname.find("T1tttt") != -1: self.T1tttt()
        if modelname.find("T1bbbb") != -1: self.T1bbbb()
        if modelname.find("T1qqqq") != -1: self.T1qqqq()
        if modelname.find("T2tt")   != -1: self.T2tt  ()
        if modelname.find("T2bb")   != -1: self.T2bb  ()
        if modelname.find("T2qq")   != -1: self.T2qq  ()
        if modelname.find("T2cc")   != -1: self.T2cc  ()
        if modelname.find("T2ttcc") != -1: self.T2ttcc()
        if modelname.find("T2bW")   != -1: self.T2bW  ()
        if modelname.find("T2bt")   != -1: self.T2bt  ()


    def rpvMonoPhi(self):
        # model name
        self.modelname = "rpvMonoPhi"
        # decay chain
        self.label= "pp #rightarrow #phi #rightarrow q #font[4]{#psi}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 800
        self.Xmax = 2000
        self.Ymin = 0
        self.Ymax = 2500
        #self.Zmin = 0.0005
        self.Zmin = 0.01
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#phi} [GeV]"
        # LSP
        self.LSP = "m_{#psi} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[0, 20000])
        # turn off diagonal lines
        self.diagOn = False
        self.mTopDiagOn = False 
        self.blanklep = False

    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 600
        self.Xmax = 2200
        self.Ymin = 0
        self.Ymax = 1900
        self.Zmin = 0.0001
#        self.Zmin = 0.001
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.2]{#tilde{g}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mT = 175
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mT, 20000-mT])        
        # turn off diagonal lines
        self.diagOn = False
        self.mTopDiagOn = False
        
    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} #tilde{#chi}^{0}_{1}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600
        self.Xmax = 2300
        self.Ymin = 0
        self.Ymax = 2000
        #self.Zmin = 0.0005
        self.Zmin = 0.0001
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.2]{#tilde{g}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[0, 20000])
        # turn off diagonal lines
        self.diagOn = False
        self.mTopDiagOn = False
 
    def T1qqqq(self):
        # model name
        self.modelname = "T1qqqq"
        # decay chain
#        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1}";
#        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1} or tilde{g} #rightarrow q q' #tilde{#chi}^{#pm}_{1} #rightarrow #pi^{#pm} #tilde{#chi}^{0}_{1}";
        self.label= "pp #rightarrow #tilde{g} #tilde{g}; c#tau_{0}(#tilde{#chi}^{#pm}_{1})=10 cm   Approx. NNLO+NNLL exclusion"
        # plot boundary. The top 1/4 of the y axis is taken by the legend
#        self.Xmin = 600
#        self.Xmax = 2200
#        self.Ymin = 0
#        self.Ymax = 1900
        self.Xmin = 1200
        self.Xmax = 2800
        self.Ymin = 0
        self.Ymax = 3000
        #self.Zmin = 0.001
        self.Zmin = 0.00001
        self.Zmax = 0.1
        # produce sparticle
        self.sParticle = "m_{#kern[0.2]{#tilde{g}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[0, 20000])
        # turn off diagonal lines
        self.diagOn = False
        self.mTopDiagOn = False
        self.blanklep = False
#        self.blanklep = True
        self.extraText = False
        self.extraText1=""
        self.extraText2=""
#        self.extraText = True
#        self.extraText1 = "#splitline{BR(#tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1}) = #frac{1}{3}}{#splitline{BR(#tilde{g} #rightarrow q_{d} #bar{q}_{u} #tilde{#chi}^{+}_{1}, #tilde{#chi}^{+}_{1} #rightarrow #pi^{+} #tilde{#chi}^{0}_{1}) = #frac{1}{3}}{BR(#tilde{g} #rightarrow q_{u} #bar{q}_{d} #tilde{#chi}^{-}_{1}, #tilde{#chi}^{-}_{1} #rightarrow #pi^{-} #tilde{#chi}^{0}_{1}) = #frac{1}{3}}}"
#        self.extraText2 = "Wino-like #tilde{#chi}^{#pm}_{1} - #tilde{#chi}^{0}_{1}"

    def T2tt(self):
        # model name
        self.modelname = "T2tt"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{_{_{ }}#tilde{t}_{_{ }}}, #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 150
        #self.Xmin = 350
        self.Xmax = 1500
        self.Ymin = 0
        self.Ymax = 1200
       # self.Zmin = 0.0
       # self.Zmax = 20

        #self.Zmin = 0.001
        self.Zmin = 0.0001
        self.Zmax = 10

        #self.Zmin = 0.1
        #self.Zmax = 10
        # produce sparticle
        self.sParticle = "m_{#kern[0.7]{#tilde{t}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = True
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = True
        self.blanklep = False
 
    def T2ttcc(self):
        # model name
        self.modelname = "T2ttcc"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow t(c) #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 100
        self.Xmax = 900
        self.Ymin = 0
        self.Ymax = 500
        self.Zmin = 0.001
        self.Zmax = 200
        #self.Zmin = 0.1
        #self.Zmax = 10
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        #self.diagOn = True
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = True
    

    # def T2cc(self):        
    #     # model name       
    #     self.modelname = "T2cc"       
    #     # decay chain      
    #     self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow c #tilde{#chi}^{0}_{1}";  
    #     # scan range to plot   
    #     self.Xmin = 100       
    #     self.Xmax = 600       
    #     self.Ymin = 0       
    #     self.Ymax = 800        
    #     self.Zmin = 1       
    #     self.Zmax = 100     
    #     # self.Zmin = 0.1     
    #     # self.Zmax = 10      
    #     # produce sparticle    
    #     self.sParticle = "m_{#tilde{t}} [GeV]"       
    #     # LSP       
    #     self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"       
    #     # diagonal position: mLSP = mgluino - 2mtop        
    #     mW = 0       
    #     self.diagX = array('d',[0,20000])  
    #     self.diagY = array('d',[-mW, 20000-mW])               
    #     # turn off diagonal lines       
    #     self.diagOn = False       
    #     #  self.mT, self.dM = 172.5, 6.25     
    #     self.mT, self.dM = 80, 0       
    #     self.mTopDiagOn = False       
    #     self.t2ccDiagOn = True


    def T2cc(self):
        # model name
        self.modelname = "T2cc"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow c #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 200
        self.Xmax = 800
        self.Ymin = 0
        self.Ymax = 950
        self.Zmin = 0.01
        self.Zmax = 5
        #self.Zmin = 0.1
        #self.Zmax = 10
        # produce sparticle
        self.sParticle = "m_{#kern[0.7]{#tilde{t}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 0
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 80, 0
        self.mTopDiagOn = False
        self.t2ccDiagOn = True
        self.blanklep = False

    def T2bb(self):
        # model name
        self.modelname = "T2bb"
        # decay chain
        self.label= "pp #rightarrow #tilde{b} #bar{#tilde{b}}, #tilde{b} #rightarrow b #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 300
        self.Xmax = 1500
        self.Ymin = 0
        self.Ymax = 1200
        #self.Zmin = 0.001
        self.Zmin = 0.0001
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.1]{#tilde{b}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = False
        self.blanklep = False
        
    def T2qq(self):
        # model name
        self.modelname = "T2qq"
        # decay chain
        self.label= "pp #rightarrow #tilde{q} #bar{#tilde{q}}, #tilde{q} #rightarrow q #tilde{#chi}^{0}_{1}";
#        self.label= "pp #rightarrow #tilde{q} #bar{#tilde{q}}; c#tau_{0}(#tilde{#chi}^{#pm}_{1})=10 cm   Approx. NNLO+NNLL exclusion"#, #tilde{q} #rightarrow q #tilde{#chi}^{0}_{1}";
        # scan range to plot
#        self.Xmin = 600
#        self.Xmax = 2000
#        self.Ymin = 0
#        self.Ymax = 2000
        self.Xmin = 525
        self.Xmax = 2000
        self.Ymin = 0
        self.Ymax = 1600
        #self.Zmin = 0.001
        self.Zmin = 0.0001
        self.Zmax = 4
#        self.Zmax = 1
        # produce sparticle
        self.sParticle = "m_{#kern[0.15]{#tilde{q}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = False
        self.blanklep = False
        self.extraText = False
        self.extraText1=""
        self.extraText2=""
#        self.blanklep = True
#        self.extraText = True
#        #self.extraText1 = "#splitline{BR(#tilde{q} #rightarrow q #tilde{#chi}^{0}_{1}) = #frac{1}{3}}{#splitline{BR(#tilde{q} #rightarrow q #tilde{#chi}^{+}_{1}, #tilde{#chi}^{+}_{1} #rightarrow #pi^{+} #tilde{#chi}^{0}_{1}) = #frac{1}{3}}{BR(#tilde{q} #rightarrow q #tilde{#chi}^{-}_{1}, #tilde{#chi}^{-}_{1} #rightarrow #pi^{-} #tilde{#chi}^{0}_{1}) = #frac{1}{3}}}"        
#        self.extraText1 = "#splitline{BR(#tilde{q} #rightarrow q #tilde{#chi}^{0}_{1}) = #frac{1}{2}}{#splitline{BR(#tilde{q}_{u} #rightarrow q_{d} #tilde{#chi}^{+}_{1}, #tilde{#chi}^{+}_{1} #rightarrow #pi^{+} #tilde{#chi}^{0}_{1}) = #frac{1}{4}}{BR(#tilde{q}_{d} #rightarrow q_{u} #tilde{#chi}^{-}_{1}, #tilde{#chi}^{-}_{1} #rightarrow #pi^{-} #tilde{#chi}^{0}_{1}) = #frac{1}{4}}}"
#        self.extraText2 = "Wino-like #tilde{#chi}^{#pm}_{1} - #tilde{#chi}^{0}_{1}"




    def T2bt(self):
        # model name
        self.modelname = "T2bt"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b #tilde{#chi}^{#pm}_{1} #rightarrow b W^{#pm} #tilde{#chi}^{0}_{1} or #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}"
#        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1} / b #tilde{#chi}^{#pm}_{1} ";
# scan range to plot
        self.Xmin = 300
        self.Xmax = 1500
        self.Ymin = 0
        self.Ymax = 870
        self.Zmin = 0.0005
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.7]{#tilde{t}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = False
        self.blanklep = False
        self.extraText = True
        self.extraText1 = "m_{#tilde{#chi}_{1}^{#pm}}-m_{#tilde{#chi}_{1}^{0}} = 5 GeV"
        self.extraText2 = "#bf{#it{#Beta}}(#tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}) = 50%"



    def T2bW(self):
        # model name
        self.modelname = "T2bW"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b #tilde{#chi}^{#pm}_{1}, #tilde{#chi}^{#pm}_{1} #rightarrow W^{#pm} #tilde{#chi}_{1}^{0}";
        # scan range to plot
        self.Xmin = 300
        self.Xmax = 1500
        self.Ymin = 0
        self.Ymax = 800
        self.Zmin = 0.001
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.7]{#tilde{t}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.blanklep = False
        self.extraText = True
        self.extraText1 = "m_{#tilde{#chi}_{1}^{#pm}} = (m_{#tilde{t}} + m_{#tilde{#chi}_{1}^{0}})/2"
        self.extraText2 = ""

#        # model name
#        self.modelname = "T2bW"
#        # decay chain
#        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow b #tilde{#chi}^{#pm}_{1} ";
#        # scan range to plot
#        self.Xmin = 300
#        self.Xmax = 1000
#        self.Ymin = 0
#        self.Ymax = 800
#        self.Zmin = 0.001
#        self.Zmax = 10
#        # produce sparticle
#        self.sParticle = "m_{#tilde{t}} [GeV]"
#        # LSP
#        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
#        # diagonal position: mLSP = mgluino - 2mtop 
#        mW = 75
#        self.diagX = array('d',[0,20000])
#        self.diagY = array('d',[-mW, 20000-mW])        
#        # turn off diagonal lines
#        self.diagOn = False
#        #self.mT, self.dM = 172.5, 6.25
#        self.mT, self.dM = 175, 25
#        self.mTopDiagOn = False
