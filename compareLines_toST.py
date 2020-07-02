import ROOT
import os, sys
import math

model = sys.argv[1]

if model == "T1tttt":
    f0 = ROOT.TFile("config/limits_2017_Mar07/limits_T1tttt_full_Mar07_V2.root")
elif model == "T1bbbb":
    f0 = ROOT.TFile("config/limits_2017_Mar07/limits_T1bbbb_Mar07_V2.root")
elif model == "T1qqqq":
    f0 = ROOT.TFile("config/fullrun2limits/T1qqqq_results.root")
elif model == "T2tt":
    f0 = ROOT.TFile("config/limits_2017_Mar07/limits_T2tt_full_Mar07_V2.root")
elif model == "T2bb":
    f0 = ROOT.TFile("config/limits_2017_Mar07/limits_T2bb_full_Mar07_V2.root")
elif model == "T2qq":
    f0 = ROOT.TFile("config/fullrun2limits/T2qq_results.root")
    f0b = ROOT.TFile("config/fullrun2limits/T2qq_results_OneFold.root")

#if model == "T1tttt":
#    f1 = ROOT.TFile("limits_T1tttt_FullRunII_17MCfor18_ttbbWeights_v2.root")
#else:
f1 = ROOT.TFile("config/limits_stscan/limits_"+model+"_50.root")
if model == "T2qq":
    f1b = ROOT.TFile("config/limits_stscan/limits_"+model+"_50-OneFold.root")

gbase = []
gbase1f = []
gcomp = []
gcomp1f = []

gbase.append(f0.Get("gr_exp_smoothed"))
gbase[0].SetLineColor(2)
gcomp.append(f1.Get("gr_exp_smoothed"))
gcomp[0].SetLineColor(2)
gbase[0].SetLineStyle(2)
gbase[0].SetLineWidth(2)
gcomp[0].SetLineWidth(2)

if model == "T2qq":
    gbase1f.append(f0b.Get("gr_exp_smoothed"))
    gbase1f[0].SetLineColor(2)
    gcomp1f.append(f1b.Get("gr_exp_smoothed"))
    gcomp1f[0].SetLineColor(2)
    gbase1f[0].SetLineStyle(2)
    gbase1f[0].SetLineWidth(2)
    gcomp1f[0].SetLineWidth(2)

gbase.append(f0.Get("gr_obs_smoothed"))
gbase[1].SetLineColor(1)
gcomp.append(f1.Get("gr_obs_smoothed"))
gcomp[1].SetLineColor(1)
gbase[1].SetLineStyle(2)
gbase[1].SetLineWidth(2)
gcomp[1].SetLineWidth(2)

if model == "T2qq":
    gbase1f.append(f0b.Get("gr_obs_smoothed"))
    gbase1f[1].SetLineColor(1)
    gcomp1f.append(f1b.Get("gr_obs_smoothed"))
    gcomp1f[1].SetLineColor(1)
    gbase1f[1].SetLineStyle(2)
    gbase1f[1].SetLineWidth(2)
    gcomp1f[1].SetLineWidth(2)
    
gbase.append(f0.Get("gr_ep1s_smoothed"))
gbase[2].SetLineColor(ROOT.kOrange)
gcomp.append(f1.Get("gr_ep1s_smoothed"))
gcomp[2].SetLineColor(ROOT.kOrange)
gbase[2].SetLineStyle(2)
gbase[2].SetLineWidth(2)
gcomp[2].SetLineWidth(2)

if model == "T2qq":
    gbase1f.append(f0b.Get("gr_ep1s_smoothed"))
    gbase1f[2].SetLineColor(ROOT.kOrange)
    gcomp1f.append(f1b.Get("gr_ep1s_smoothed"))
    gcomp1f[2].SetLineColor(ROOT.kOrange)
    gbase1f[2].SetLineStyle(2)
    gbase1f[2].SetLineWidth(2)
    gcomp1f[2].SetLineWidth(2)
        
gbase.append(f0.Get("gr_em1s_smoothed"))
gbase[3].SetLineColor(ROOT.kOrange)
gcomp.append(f1.Get("gr_em1s_smoothed"))
gcomp[3].SetLineColor(ROOT.kOrange)
gbase[3].SetLineStyle(2)
gbase[3].SetLineWidth(2)
gcomp[3].SetLineWidth(2)

if model == "T2qq":
    gbase1f.append(f0b.Get("gr_em1s_smoothed"))
    gbase1f[3].SetLineColor(ROOT.kOrange)
    gcomp1f.append(f1b.Get("gr_em1s_smoothed"))
    gcomp1f[3].SetLineColor(ROOT.kOrange)
    gbase1f[3].SetLineStyle(2)
    gbase1f[3].SetLineWidth(2)
    gcomp1f[3].SetLineWidth(2)
        

ROOT.gStyle.SetPaintTextFormat(".2f")
ROOT.gStyle.SetOptStat(0)

xmin = 1000
xmax = 2800
ymin = 0
ymax = 3200

if model == "T2tt":
    xmin = 350
    xmax = 1250
    ymin = 0
    ymax = 775

elif model == "T2bb":
    xmin = 350
    xmax = 1600
    ymin = 0
    ymax = 1400

elif model == "T2qq":
    xmin = 600
    xmax = 2400
    ymin = 0
    ymax = 2200

h2 = ROOT.TH2D("h2", "", 1, xmin, xmax, 1, ymin, ymax)
if "T1" in model:
    h2.GetXaxis().SetTitle("m_{#tilde{g}} [GeV]")
elif model == "T2qq":
    h2.GetXaxis().SetTitle("m_{#tilde{q}} [GeV]")
elif model == "T2bb":
    h2.GetXaxis().SetTitle("m_{#tilde{b}} [GeV]")
elif model == "T2tt":
    h2.GetXaxis().SetTitle("m_{#tilde{t}} [GeV]")
h2.GetYaxis().SetTitle("m_{#tilde{#chi}_{1}^{0}} [GeV]")
h2.GetYaxis().SetLabelSize(0.02)
h2.GetXaxis().SetTitleOffset(1.1)
h2.GetYaxis().SetTitleOffset(1.35)

title = ""
if model == "T1qqqq":
    title = "pp #rightarrow #tilde{g}#tilde{g} (light flavor)"
#    title = "pp #rightarrow #tilde{g}#tilde{g}, #tilde{g} #rightarrow q#bar{q}#tilde{#chi}_{1}^{0}"
elif model == "T1bbbb":
    title = "pp #rightarrow #tilde{g}#tilde{g}, #tilde{g} #rightarrow b#bar{b}#tilde{#chi}_{1}^{0}"
elif model == "T1tttt":
    title = "pp #rightarrow #tilde{g}#tilde{g}, #tilde{g} #rightarrow t#bar{t}#tilde{#chi}_{1}^{0}"
elif model == "T2qq":
    title = "pp #rightarrow #tilde{q}#bar{#tilde{q}} (light flavor)"
#    title = "pp #rightarrow #tilde{q}#bar{#tilde{q}}, #tilde{q} #rightarrow q#tilde{#chi}_{1}^{0}"
elif model == "T2bb":
    title = "pp #rightarrow #tilde{b}#bar{#tilde{b}}, #tilde{b} #rightarrow b#tilde{#chi}_{1}^{0}"
elif model == "T2tt":
    title = "pp #rightarrow #tilde{t}#bar{#tilde{t}}, #tilde{t} #rightarrow t#tilde{#chi}_{1}^{0}"
#h2.SetTitle(title)


can = ROOT.TCanvas("can","can", 600,600)
can.cd()
#ROOT.gPad.SetTickx()
ROOT.gPad.SetTicky()

h2.Draw("")
#gcomp[3].Draw("same")
#gcomp[2].Draw("same")
gcomp[1].Draw("same")
gcomp[0].Draw("same")
#gbase[3].Draw("base")
#gbase[2].Draw("same")
gbase[1].Draw("same")
gbase[0].Draw("same")

if model == "T2qq":
    gcomp1f[1].Draw("same")
    gcomp1f[0].Draw("same")
    gbase1f[1].Draw("same")
    gbase1f[0].Draw("same")

diag = ROOT.TLine(xmin, xmin-172.5, 750, 750-172.5)
diag.SetLineColor(ROOT.kGray)
diag.SetLineStyle(2)
diag.SetLineWidth(2)
if model == "T2tt":
    diag.Draw("same")

tdiag = ROOT.TLatex(580, 580-172.5,"m_{#tilde{t}} = m_{t} + m_{#tilde{#chi}_{1}^{0}}")
tdiag.SetTextAngle(47.5) #math.degrees(math.atan(float(800)/float(1200))))
tdiag.SetTextColor(ROOT.kGray+2)
tdiag.SetTextAlign(11)
tdiag.SetTextSize(0.035)
if model == "T2tt":
    tdiag.Draw("same")

#t2qq1 = ROOT.TLatex(850+150, 425+150, "one light #tilde{q}")
#t2qq1.SetTextColor(1)
#t2qq1.SetTextAlign(11)
#t2qq1.SetTextSize(0.035)
##
#t2qq8 = ROOT.TLatex(1125+150, 800+150, "#tilde{q}_{L}+#tilde{q}_{R} (#tilde{u}, #tilde{d}, #tilde{s}, #tilde{c})")
#t2qq8.SetTextColor(1)
#t2qq8.SetTextAlign(11)
#t2qq8.SetTextSize(0.035)
#
t2qq1 = ROOT.TLatex(750, 675, "one light #tilde{q}")
t2qq1.SetTextColor(1)
t2qq1.SetTextAlign(11)
t2qq1.SetTextSize(0.035)
#
t2qq8 = ROOT.TLatex(1600, 1200, "#tilde{q}_{L}+#tilde{q}_{R} (#tilde{u}, #tilde{d}, #tilde{s}, #tilde{c})")
t2qq8.SetTextColor(1)
t2qq8.SetTextAlign(11)
t2qq8.SetTextSize(0.035)
#
if model == "T2qq":
    t2qq1.Draw("same")
    t2qq8.Draw("same")

#leg = ROOT.TLegend(0.102, 0.74, 0.72, 0.89)
leg = ROOT.TLegend(0.102, 0.62, 0.84, 0.82)
leg.SetLineColor(0)
leg.SetFillColor(0)
leg.AddEntry(gbase[1], "Inclusive M_{T2}: observed (95% CL)", "L")
leg.AddEntry(gbase[0], "Inclusive M_{T2}: expected (95% CL)", "L")
leg.AddEntry(gcomp[1], "Disappearing tracks: observed (95% CL)", "L")
leg.AddEntry(gcomp[0], "Disappearing tracks: expected (95% CL)", "L")

leg.Draw("same")

modellabel = ROOT.TLatex(xmin+75, ymax-150, title)
if model == "T2bb":
    modellabel = ROOT.TLatex(xmin+75, ymax-100, title)
modellabel.Draw("same")
modellabel.SetTextSize(0.045)
modellabel.SetTextFont(42)

cmslabel = ROOT.TLatex(xmin, ymax+25, "#font[62]{CMS} #font[52]{Preliminary}")
cmslabel.SetTextAlign(11)
cmslabel.SetTextColor(1)
cmslabel.SetTextSize(0.045)
cmslabel.Draw("same")

energylabel = ROOT.TLatex(xmax-350, ymax+25, "#font[42]{(13 TeV)}")
energylabel.SetTextAlign(11)
energylabel.SetTextColor(1)
energylabel.SetTextSize(0.04)
energylabel.Draw("same")


can.SaveAs(model+"_comparisonST.png")
can.SaveAs(model+"_comparisonST.pdf")

