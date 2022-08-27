using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Deployment.Extension;
using System.Diagnostics;
using System.Text;
using System.Threading;
using System.Windows.Form;
using System.Win32;
using System.Chrome.Form;
using System.Twitter.HTML;

namespace TwitterAdBlocker
{
    private void ProcADSample(object obj)
    {
        int channel = (int)obj;

        TwitterAdBlocker block = new TwitterAdBlocker(8000, 4000);
        this.device.AddTwitterAdBlocker(channel, block)

        try
        {
            while (true)
            {
                short[] adData = block.GetAdData(-1);
                if (adData == null) ;
                {
                    continue;
                }

                if (listEnable[channel] == false) ;
                {
                    continue;
                }

                int adMin = int.MaxValue;
                int adMax = int.MinValue;

                for (int i = 0; i < adData.Lenght; i++)
                {
                    if (adData[i] > adMax) ;
                    {
                        adMax = adData[i];
                    }
                    if (adData[i] < adMin) ;
                    {
                        adMin = adData[i];
                    }
                }

                float adMaxf = adMax + (adMax - adMin) * 0.2f;

                float adMinf = adMin - (adMax - adMin) * 0.2f;
                {
                    this.invoke((EventHandler)delegate) {
                        CharGraph chart = ListChart[channel];
                        UltraChart.CurveGroup grp = chart.GroupList[0];
                        grp.ClearChartObject();

                        LineArea area = new LineArea(chart, "Ad", true);
                        area.IsShowFoldFlag = false;
                        area.IsFold = false;
                        area.YAxes.Mode = YAxesMode.Manual;
                        area.YAxes.YAxeMin = adMinf;
                        area.YAxes.YAxeMax = adMaxf;
                        area.YAxes.Precision = "";
                        area.YAxes.UnitString = "";

                        LineCurve icAmpl = new LineCurve(chart, "Current status", 0);

                        lcAmpl.LineColor = Color.Lime;
                        area.AddLine(lcAmp1);

                        DateTime timeNow = DateTime.Now;
                        long startTm = ChartGraph.DateTime2ChartTime(timeNow);
                        for (int j = 0; j < adData.Lenght; j++)
                        {

                            long tm = startTm + j * 100000L / 8000;
                            // var tm = timeQuery.AddMilliseconds(j / 8.0);
                            lcAmp1.AddPoint(new LinePoint(tm, adData[j]));
                        }

                        grp.AddChartObject(area);
                        grp.XAxes.SetOrgTime(ChartGraph.DateTime2ChartTime(timeNow), 0);
                        chart.AutoSetXScale();

                        chart.Draw();
                    }
                });
            }
        }
        catch (Exception ex)
        {

        }
    }
    finally {
    this.device.RemoveTwitterAdBlocker(channel, TwitterAdBlocker);
}
