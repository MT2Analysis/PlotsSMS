import ROOT

f0 = ROOT.TFile("/mnt/t3nfs01/data01/shome/casal/CMSSW_7_4_12_patch4/src/combineMT2/MT2Scripts/../limits_28June/limits_T1tttt_full_13Apr_sigContOK.root","READ")
f1 = ROOT.TFile("/mnt/t3nfs01/data01/shome/casal/CMSSW_7_4_12_patch4/src/combineMT2/MT2Scripts/../limits_28June/limits_T1tttt_full_2p3ifb_28June_newBins.root","READ")
f2 = ROOT.TFile("/mnt/t3nfs01/data01/shome/casal/CMSSW_7_4_12_patch4/src/combineMT2/MT2Scripts/../limits_28June/limits_T1tttt_full_4p0ifb_28June_2016.root","READ")
f3 = ROOT.TFile("/mnt/t3nfs01/data01/shome/casal/CMSSW_7_4_12_patch4/src/combineMT2/MT2Scripts/../limits_28June/limits_T1tttt_full_2p3ifb_28June_2015plus2016_uncorr.root","READ")
f4 = ROOT.TFile("/mnt/t3nfs01/data01/shome/casal/CMSSW_7_4_12_patch4/src/combineMT2/MT2Scripts/../limits_28June/limits_T1tttt_full_2p3ifb_28June_2015plus2016_corr.root","READ")

h0 = f0.Get("gr_obs_smoothed"); h0.SetLineColor(2)
h1 = f1.Get("gr_obs_smoothed"); h1.SetLineColor(2); h1.SetLineStyle(2)
h2 = f2.Get("gr_obs_smoothed"); h2.SetLineColor(1)
h3 = f3.Get("gr_obs_smoothed"); h3.SetLineColor(4)
h4 = f4.Get("gr_obs_smoothed"); h4.SetLineColor(4); h4.SetLineStyle(2)

ROOT.gStyle.SetPaintTextFormat(".2f")
ROOT.gStyle.SetOptStat(0)

h3.GetXaxis().SetTitle("m_{#tilde{g}} [GeV]")
h3.GetYaxis().SetTitle("m_{LSP} [GeV]")
h3.GetYaxis().SetLabelSize(0.03)
h3.GetXaxis().SetTitleOffset(1.1)
h3.GetYaxis().SetTitleOffset(1.45)
h3.SetTitle("T1tttt (Obs.)")
#h0.SetTitle("UL gen-syst/before")
#h0.SetMarkerSize(0.8)

h3.GetXaxis().SetRangeUser(700, 2000)
h3.GetYaxis().SetRangeUser(  0, 1200)

can = ROOT.TCanvas("can","can", 600,600)

h3.Draw("")
h1.Draw("same")
h2.Draw("same")
h0.Draw("same")
h4.Draw("same")

leg = ROOT.TLegend(0.14, 0.64, 0.44, 0.89)
leg.AddEntry(h0, "2015", "L")
leg.AddEntry(h1, "2015 new binning", "L")
leg.AddEntry(h2, "2016", "L")
leg.AddEntry(h3, "2015+2016 uncorrelated", "L")
leg.AddEntry(h4, "2015+2016 correlated", "L")

leg.Draw("same")
