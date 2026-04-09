# BESS Project Finance Model and Battery Characteristics

**Source:** https://edbodmer.com/battery-analysis-and-merchant-prices

---

Project finance models of Battery Electricity Storage Systems (BESS) are documented and explained on this page (I had different material on this page before but it was in dire need of updating). As part of the project finance model explanation, the characteristics of batteries that drive economics of battery storage are discussed in a set of power point slides. I begin by including two different battey project finance models below this paragraph. Then, I show the powerpoint slides and a video that explains the model. Items that affect the cost of batteries include the life of the battery, the degradation, the round trip efficiency, the depth of discharge as well as the cost. Instead of simply reporting some numbers that you can argue about for each of these characteristics, I demonstrate how each of the characteristics affect the economic analysis of storage.

The economics of batteries plus renewables are shown on subsequent sections of this webpage. As in other pages, I use an LCOE framework where the economic cost computed from the LCOE is confirmed with a financial model. I demonstrate how storage using batteries can be made analogous to storage of boxes in a warehouse. In the excel file attached to the button I attempt to concentrate on battery costs using a simple example with constant loads and solar costs. The example compares solar plus battery to solar plus thermal to only solar.

.

 **[Project Finance Model with Battery Electric Storage System (BESS) with Solar Used in Video Explanation](https://edbodmer.com/wp-content/uploads/2026/03/Solar-and-Battery.xlsm)
**

.

**[Battery Electric Storage System (BESS) Combined with Solar Used with Different Regional Locations](https://edbodmer.com/wp-content/uploads/2026/03/Copy-of-UZS_Model-25.02.26.v5.xlsm)
**

.

**[Power Point Slides on Renewable Energy and Storage with Technical Details and Debt Structuring Implications](https://edbodmer.com/wp-content/uploads/2026/03/Renewable-Project-Finance-Analysis.pptx)
**

.

.

Playlist of Batteries and Storage
---------------------------------

The set of videos attached to the playlist below demonstrate my various attempts to evaluate the economic cost of batteries. In working through battery issues I have attempted to make differet files that illustrate the cost of storage relative to other alternatives. I hope that as I have worked through the issues the dispatch analysis of batteries combined with the cost analysis is becoming clearer. As with the other playlists, watching all of the videos would be torture and impossible to do. But if you want some help sleeping maybe you can turn on the playlist. I have also included the power point slides that I sometimes refer to when working through the battery issues.

**[Power Point Slides with Analysis of Batteries and Storage Including a Survey of Battery Characteristics (Cost, Degradation etc.)](https://edbodmer.com/wp-content/uploads/2022/01/Battery-Analysis.pptx)
**

Capital and Operating Cost of Battery
-------------------------------------

The cost of a battery is generally expressed as an amount of money that muse be spent per kWh. Although there is also a relationship between cost and the amount of the capacity which can roughly be through of as how fast can the battery be charged and discharged. This means that a battery with low storage relative to capacity will have a higher cost per kWh. The chart below implies that there is value for capacity and for storage as the cost per kWh of storage declines with more storage relative to capacity.  If the lines were flat there would be no premium for capacity relative to storage. Note that the costs in the chart below may not seem to include all of the components of the battery as a battery cost of USD 150/kWh for a 12 hour storage battery is low.

.

**[Power Point Slides Describing Levelised Cost, Resource Analysis and Financial Analysis of Solar Power Projects](https://edbodmer.com/wp-content/uploads/2021/09/Solar-Slides-Presentation-1.pptx)
**

.

**[Excel File with Advanced Project Finance Issues Including Sculpting for Multiple Debt Issues and P50/P99 etc.](https://edbodmer.com/wp-content/uploads/2021/05/Advanced-Course.xlsm)
**

.

![](https://edbodmer.com/wp-content/uploads/2021/03/image-23.png)

A second factor affecting the battery cost is the size of the battery. The chart below illustrates estimated economies of scale from the U.S. DOE. The data is both for 2020 on the left and 2030 on the right.

![](https://edbodmer.com/wp-content/uploads/2021/03/image-26.png)

Battery Life
------------

There are many elements of battery analysis where the numbers are not certain. The battery life is a crucial aspect of measuring the cost and the carrying charge of any asset. The screenshots below illustrate difference estimates of the battery life. A complicating element is that the expected life is not measured by a simple time number in years. Instead the life can be measured in the number of cycles.

Simple Battery Analysis with Different Characteristics
------------------------------------------------------

I received an e-mail that included the following information.  This e-mail illustrates both how to make a simple evaluation of a battery and also the distortions in the analysis.  It may be a good introduction to evaluation of batteries.

*   The cost of an installed 1 MWh battery in Canada is roughly $1M
*   Assuming a 10% interest rate, the daily carrying cost of that is $1M\*10%/365 = $274
*   Assuming one battery cycle per day, the daily revenue the battery would have to generate is $274
*   Assuming an 80% efficiency factor, this grosses up to $342
*   This is the intraday price arbitrage that would be needed; $342; i.e., sell power at $342/MWh higher than you buy it for at another time in the day.

The problems with this analysis include:

1.  The carrying charge can be very different than a simple discount rate.  This is particularly true when the lifetime is short or when there is degradation in the output from a battery.
2.  The amount of money required to generate the income is computed correctly, this can be evaluated by examining the on-peak versus off-peak power as shown below.
3.  The cost of batteries has come down significantly from the USD 1000/kWh shown above.
4.  The ancillary services may add a lot to the value of a battery.

Simple Analysis of Battery
--------------------------

You can construct a simple analysis of a battery using carrying charge rates, the cost per capacity or per cycle of energy and the cost of O&M just like for other technologies.  Then you can compare the cost of the battery on a daily basis with merchant prices.  You can do this for a single day or over the course of a year.

The first step is to understand the fixed costs of a battery which can be converted first to the cost per year and then the cost per day.  In the example below I have used data from Lazard which quotes the cost per kWh.  I have assumed a cost per one cycle of storage per kWh of USD400/kWh.  For a battery with a duration of 4 hours, the cost per kW is USD 1,000/kW.

.

![](https://edbodmer.com/wp-content/uploads/2018/04/Simple-Battery-1.jpg)

.

A big question in the analysis is the annual carrying charge.  You can look at the pages that work through carrying charge to understand this number.  Once the daily cost is computed you can test whether it is possible to achive this value from the difference between off-peak and on-peak prices.  To illustrate this, consider the following prices over the course of a day and the value of storing energy and then releasing that energy with a loss.

.

![](https://edbodmer.com/wp-content/uploads/2018/04/Simple-Battery-2.jpg)

.

The final part of the analysis involves comparing the net benefits with the costs.  Using the example above, the net benefits of the battery are less than the cost of the battery as shown below.

![](https://edbodmer.com/wp-content/uploads/2018/04/Simple-Battery-3.jpg)

Video on Merchant Prices and Use of Batteries for Arbitrage
-----------------------------------------------------------

The video below illustrates how to use merchant prices in evaluating the economics of batteries and storage.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1479&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13948&rand=0.9489988021931146)