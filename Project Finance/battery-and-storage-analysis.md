# Battery and Storage Analysis

**Source:** https://edbodmer.com/battery-and-storage-analysis

---

This webpage describes analysis of batteries and storage in different contexts including bulk storage and ancillary services. I have worked on the battery issues for a while and modeified the analysis over time. Various files lead up to a comprehensive battery analysis with solar and diesel in the context of an island grid that is attached to the button below. The analysis of batteries and storage depend on load shapes and the value of power during different time periods. To model the use of batteries you will need some kind of battery dispatch analysis where you decide when to charge and when to discharge the batteries. Your analysis should also consider the degradation of batteries; how the lifetime of batteries is affected by the number of cycles; how the cost of batteries is affected by the amount of storage per cycle; how the round trip efficiency affects the dispach; what are the O&M costs and how does the depth of discharge constraint affect the required battery size. Other issues include how to collect real world data on items including the cost of batteries and other storage, diesel power plants, diesel fuel prices and solar power. I have included power point slides as well as the excel file if you want to see how I evaluate some economic issues associated with batteries.

**[Excel File with Battery Analysis Using Alternative Costs, Load Shapes and Efficiencies with DispatchFactors](https://edbodmer.com/wp-content/uploads/2022/01/Solar-Diesel-and-Battery1.xlsm)
**

.

Playlist of Batteries and Storage
---------------------------------

The set of videos attached to the playlist below demonstrate my various attempts to evaluate the economic cost of batteries. In working through battery issues I have attempted to make differet files that illustrate the cost of storage relative to other alternatives. I hope that as I have worked through the issues the dispatch analysis of batteries combined with the cost analysis is becoming clearer. As with the other playlists, watching all of the videos would be torture and impossible to do. But if you want some help sleeping maybe you can turn on the playlist. I have also included the power point slides that I sometimes refer to when working through the battery issues.

**[Power Point Slides with Analysis of Batteries and Storage Including a Survey of Battery Characteristics (Cost, Degradation etc.)](https://edbodmer.com/wp-content/uploads/2022/01/Battery-Analysis.pptx)
**

### Lesson 1: Analysis of Batteries

_**Illustration with Isolated Island Systems as a Starting Point and the Rubbish Notion of LCOS**_

I have heard a lot of buzz about batteries lately. Some of this comes from the man who makes so many billions from ripping you off with very high fees for Paypal. So I have tried to apply some objective and unbiased economic and finance principles to evaluating the cost and benefits of batteries. In order to do this I begin with an isolated system where the only real alternatives are a diesel plant, some solar panels and maybe some batteries to store electricity. This  
![Island.JPG](https://edbodmer.wikispaces.com/file/view/Island.JPG/615748149/333x306/Island.JPG)  
hypothetical example is in my opinion an effective way to illustrate many of the economic issues associated with battery analysis. It involves solar analysis, the cost of diesel fuel, the demand patterns of people who live on an island and the kind of batteries that would be most effective. If you can understand how the battery analysis works in an island scenario then you can add a portfolio of generating plants instead of the single diesel unit and you can use load patterns with more diversity etc. As with so many issues, I get very lost by trying to jump into a large messy system without understanding the fundamental economics first. One of the major points about using an island system to demonstrate the issues is to show you that concepts of the levelised cost of storage are, basically, rubbish.

The island system analysis demonstrates that the concept of levelised cost of storage makes virtually no sense at all. If you have an island system like in the adjacent picture, you would like to compute the total cost to consumers in a scenario with and with out batteries and with and without different amounts of battery power. The total cost includes the cost of batteries as well as the cost of operating the diesel units and the total cost of the solar plant. If you use batteries you may have install more solar power depending on the load profile of consumers. You may also avoid the use of the diesel plant at minimum generation to provide spinning reserve.

_**General Discussion of Batteries and Storage**_

A dispatchable plant has some measure of capacity that measures the output of the plant in any instant. The input to the plant in any instant (measured in MMBTU or Kcal or Giga Joules or even kWh) is also delivered at a single point in time. For a battery, the output can be delivered over time, given the input. There is some storage. For example, if the battery has a capacity output that can produce 1 kW, that 1 kW may be produced for 8 hours producing an output of 8 kWh. Alternatively it may have less storage and produce power only for one hour producing 1 kWh. The amount of output contrasts with the amount of electricity that is used to “push power” into storage. This amount of power at any instant is like the amount of energy that is delivered to an electricity plant and can be measured with standard units of capacity such as kW. Some people have explained to me that batteries are like a water tower that stores and releases water. The amount of water that is pushed up is measured in kW at any instant. It takes time to charge the battery. The discharge of stored energy also has a time element. This makes measurement and benchmarking of the cost of a battery somewhat more complicated than for a typical electricity plant. For example, one would not express the cost per capacity of a peaking plant as the cost per delivering five hours of electricity. One expresses the number as the Euro or USD relative to the amount of capacity — in kW — that can be delivered at an instant. For batteries, the standard is to measure the cost of the battery relative to the kWh discharge. If we are on an island and we need power at night, we can pay for it with a diesel plant that is benchmarked on a per kW basis. If we want to use a battery instead (which is very difficult) we would have to pay for many batteries with no storage or a lot more for a battery with storage. Without arguing about whether this is a good or a bad benchmark, we should understand that the benchmark is different for a battery than for a standard plant. Further, the output may be able to be produced very quickly for frequency regulation, spinning reserve or voltage regulation (discussed below). I have tried to explain these things a bit in the video below. http://www.youtube.com/embed/Bxf1r4dL5TM

_**Batteries as Capacity and Differences between Batteries and Other Peaking Capacity**_

One way to think about batteries is to compare the discharge from a battery to the generation from a peaking plant such as an open cycle plant or a diesel plant on a large system with a lot of baseload plants. The peaking plant can be switched on during peak periods to meet large increases in demand. Indeed, a load duration can be used to demonstrate that it is efficient to have peaking plants on a system. A battery could be used in the same way if it is charged-up during off-peak periods and then discharged during peak periods. There are, however important differences between a battery and a gas-fired peaking plant.

First, the battery has limited discharge driven by the storage capability of the battery. For example, if the battery has a storage a discharge period (modelling as duration) as four hours, but really hot weather drives up demand all day from early in the morning to sundown, then the battery is not as useful as the peaking plant in providing capacity. On the other hand, as long as the peaking plant can provide energy using natural gas from a pipeline system, then the gas-fired unit does not have this limitation. Economic analysis cannot simply label something as the “levelised cost of storage” without taking account of this limitation.

Second, the source of energy from the battery is electricity itself rather than natural gas. This means the battery can use solar power and move it around. A natural gas plant on the other hand must of course use natural gas. In our island example, if there is sunlight during the day and we need power at night to read books, the battery can move solar power to the evening. The natural gas plant cannot do this.

_**Battery Database — Capital Costs, Efficiencies, Lifetime, Degradation and O&M**_

To evaluate batteries, I use data from Lazard as base. (At first I did not understand why Lazard computed the cost per kWh instead of cost per kW but now I see that they compute the cost per kW x hours from one charge.) I therefore begin by making a database from the Lazard study which contains costs and some storage characteristics and O&M data for different types of batteries. This uses a lot of read pdf stuff and I have made a video on how you can efficiently read the Lazard study from the internet. The battery database derived from the Lazard study is included in the excel file below. I think it is useful to export the excel database into PowerBI so you can more clearly see the different characteristics of various batteries.

_**Importance of Load Profiles in Battery Economic Analysis**_

Once the battery cost data and the diesel data is established, the battery analysis requires careful analysis of load profiles. Take three extreme examples. In one case people on the island only use electricity (perhaps for air conditioning) when the sun is shining. Here the solar power is perfectly correlated with the usage of electricity. Batteries would be useless here. In the second case, people only use electricity at night. Here, supplementing the solar power with diesel would not help and you would need a battery to save the power during the day for use at night. The number of panels correspond to the capacity and not the storage of power. The storage of power corresponds to the power needed at night. Sizing the panels and the batteries to get the power and then produce it can be tricky. The final extreme case is one where there is a flat load. Here the solar power for batteries must compete with used for things like a refrigirator. Therefore, the second set of videos walks through analysis of individual load profiles and solar power profiles.

I evaluate the value of batteries in a hypothetical island situation. An island example is good for examining the fundamental way things work (even in macro economics when thinking about an Robinson Crusoe investment, consumption and implied interest rates). If people on the island want power during the night, they must have some kind of back-up. One strategy is to supplement diesel plants that have really expensive fuel and O&M from running diesel plants with solar projects. If you are going to make this analysis you better have good data on the capital cost, heat rate, diesel cost and the operating costs of a diesel plant. Therefore, the second part of the solar analysis therefore walks through sources and analysis for diesel including forward markets for diesel fuel, conversions of USD per gallon to USD per MMBTU. I also show how to find capital costs from sources other than places like Lazard or EIA which seem to have very general data.

Videos associated with Lesson Set 1: Battery and Solar Analysis
---------------------------------------------------------------

The battery, solar and diesel analysis combines a whole bunch of analytical techniques that are discussed on other pages of the website. It includes techniques to put together a database; methods of converting PDF files; approaches for reading data from the internet to make assumptions about diesel prices; comprehensive methods for developing carrying charge assumptions that involve financial modelling; measuring the cost of solar power from different sources; developing patterns of solar power; integrating demand curves; computing LCOE and other issues. A video that describes the end of the process is available below. Links to other videos that walk through each of the steps are included in the table below the final video. http://www.youtube.com/embed/sjqcHAZcq-8

|     |     |     |
| --- | --- | --- |
| Subject |     | Video Link |
|     |     |     |
| Introduction to Battery Analysis |     | [https://www.youtube.com/watch?v=Bxf1r4dL5TM](https://www.youtube.com/watch?v=Bxf1r4dL5TM) |
| Creating Battery Database with Read PDF File |     | [https://www.youtube.com/watch?v=SwCwi\_C7ycE](https://www.youtube.com/watch?v=SwCwi_C7ycE) |
| Futures Price of Diesel Fuel |     | [https://www.youtube.com/watch?v=2C\_VMdu8lJk](https://www.youtube.com/watch?v=2C_VMdu8lJk) |
| Carrying Charge Introduction |     | [https://www.youtube.com/watch?v=z9s06nXh7U4](https://www.youtube.com/watch?v=z9s06nXh7U4) |
| Carrying Charges and Inflation |     | [https://www.youtube.com/watch?v=9uh8ZN\_SHN4](https://www.youtube.com/watch?v=9uh8ZN_SHN4) |
| Taxes in Carrying Charge Rates |     | [https://www.youtube.com/watch?v=kRLWlWSt05Q](https://www.youtube.com/watch?v=kRLWlWSt05Q) |
| Periodic Analysis in Carrying Charges |     | [https://www.youtube.com/watch?v=kRLWlWSt05Q](https://www.youtube.com/watch?v=kRLWlWSt05Q) |
| Completed Carrying Charge Analysis |     | [https://www.youtube.com/watch?v=ho2RnSHOWfk](https://www.youtube.com/watch?v=ho2RnSHOWfk) |
| Creating Electricity Cost Database |     | [https://www.youtube.com/watch?v=kRLWlWSt05Q](https://www.youtube.com/watch?v=kRLWlWSt05Q) |
| Analysis of Electricity Cost Database |     | [https://www.youtube.com/watch?v=kRLWlWSt05Q](https://www.youtube.com/watch?v=kRLWlWSt05Q) |
| LCOE Analysis |     | [https://www.youtube.com/watch?v=tJJu7c2AnoI](https://www.youtube.com/watch?v=tJJu7c2AnoI) |
| Solar Cost Analysis |     | [https://www.youtube.com/watch?v=BOLhQ92E93s](https://www.youtube.com/watch?v=BOLhQ92E93s) |
| Solar vs Diesel Economic Analysis |     | [https://www.youtube.com/watch?v=Zmm24xwo1LY](https://www.youtube.com/watch?v=Zmm24xwo1LY) |
| Battery Selection Analysis and Database |     | [https://www.youtube.com/watch?v=33v-BZHluFI](https://www.youtube.com/watch?v=33v-BZHluFI) |
| Battery Analysis and Merchant Prices |     | [https://www.youtube.com/watch?v=U6aEeyJDh54](https://www.youtube.com/watch?v=U6aEeyJDh54) |
| Final Battery Analysis |     | [https://www.youtube.com/watch?v=sjqcHAZcq-8](https://www.youtube.com/watch?v=sjqcHAZcq-8) |

Files associated with Lesson Set 1: Battery and Solar Analysis
--------------------------------------------------------------

The first spreadsheet below attempts to replicate the Lazard study where snapshots were presented for different ISO’s in the U.S. I attempt to back into various things like energy for charging, energy for discharge, total capital and demand charges. One area of difficulty I had in understanding the results was the issue of payments for regulation. For example, for the PJM region, the study has a regulation value of USD 40/MWH that is inflated at 2.5%. This USD 40/MWH compares to merchant on-peak prices that have been slightly above USD 30/MWH for the past couple of years. Reconciliation of how battery cycles are modelled, how the energy for storage, efficiency and the energy for discharge are is pretty straightforward. The file also includes replication of degradation assumptions and demand charges.

The second file contains a spreadsheet with all of the data from Lazard on the capital costs, operating costs, storage and efficiency for different types of batteries. It mainly comes from the Lazard study where I read the data from a pdf file into an excel file using new techniques I have developed to straighten out the titles. The database can be sorted by type of project, type of storage device, cost range or capacity amount.

The third file is the most important with analysis of various combinations of solar, diesel and batteries in an island scenario. This file demonstrates the value of batteries using different assumptions with respect to solar irradiation, hourly demand usage, solar capacity installation, solar capacity price, diesel fuel price, carrying charges that depend on a host of factors including return on equity, cost of debt, inflation, taxes, plant life, construction period, replacement and other factors. The file is name solar diesel and battery.xlsm.

[Replication of Lazard Snapshots.xlsx](http://edbodmer.wikispaces.com/file/view/Replication%20of%20Lazard%20Snapshots.xlsx/611617271/Replication%20of%20Lazard%20Snapshots.xlsx)

[Database of Battery Costs from Lazard.xlsx](http://edbodmer.wikispaces.com/file/view/Database%20of%20Battery%20Costs%20from%20Lazard.xlsx/611651071/Database%20of%20Battery%20Costs%20from%20Lazard.xlsx)

[Solar Diesel and Battery.xlsm](http://edbodmer.wikispaces.com/file/view/Solar%20Diesel%20and%20Battery.xlsm/614417039/Solar%20Diesel%20and%20Battery.xlsm)

### Lesson 2: Ancillary Services and Battery Analysis

_**Minimum Operations, Spinning Reserve, Regulation and Voltage Support**_

You may be saying that I am an idiot because the spreadsheets so far do not account for sudden cloud cover and the fact that one cannot simply start a diesel plant when the sun starts going down. Instead, there must be some buffer for being able to quickly replace the solar capacity with diesel. Similarly, there may be a problem with the manner in which the solar provides electricity to the system in that it is not at a proper voltage level (and other things that I really should not be talking about). But I can talk about the economics and I can put things like minimum operating conditions into an economic analysis. And best yet, we can then study the benefits of batteries in terms of providing these things called ancillary services. To do this, we can assume that our diesel plant must be running at a minimum level when the solar power is being produced. Running a diesel power plant in our island case has a few problems. First, as shown in the table below, the efficiency is worse when the loading percent is lower. This is shown by the heat rate that I like to express in MMBTU per MWH (so you can just multiply the fuel price by the cost per MMBTU of diesel fuel or natural gas).  
![Diesel Efficiency.JPG](https://edbodmer.wikispaces.com/file/view/Diesel%20Efficiency.JPG/615827207/800x351/Diesel%20Efficiency.JPG)

I have tried to replicate the Lazard analysis in PJM, NYISO, NEISO, CAISO and ERCOT (but I had some problems, particularly with valuation of regulation services). I have put the data together on batter analysis so you can change carrying charge rates, battery costs (evaluating the break-even battery cost) and fuel costs to test conditions that would make a battery economic. The final videos put everything together. This demonstrates load profiles, battery costs, diesel fuel costs and solar capacity factors that make batteries economic. These videos show how to present scenario data in an effective manner and how to show break-even cases in a careful way. As with other lessons, I am making a set of questions for each video so you can receive a badge and you name on a special page of this website.

### Lesson 3: Comparative Renewable Energy Analysis

The second lesson on this page covers analysis where you can compare the costs of different renewable and dispatchable electricity technologies. Various different files related to comparative analysis of renewable energy costs are shown below. This analysis demonstrates that the project financing terms for renewable analysis are very important in evaluating the costs. The group of files are excel models for various types of projects. The next set of files include selected power point slides that describe renewable technologies, resource assessment and financing of renewable technologies. Subsequent files include various template models for different kinds of renewable projects.

Files associated with Lesson Set 3: Comparative Renewable Energy Analysis
-------------------------------------------------------------------------

[Alternative Tariff and Financing Structures.xlsm](http://edbodmer.wikispaces.com/file/view/Alternative%20Tariff%20and%20Financing%20Structures.xlsm/544261460/Alternative%20Tariff%20and%20Financing%20Structures.xlsm)

[Renewable with Carrying Charges.xlsm](http://edbodmer.wikispaces.com/file/view/Renewable%20with%20Carrying%20Charges.xlsm/539758050/Renewable%20with%20Carrying%20Charges.xlsm)

[Renewable Model with Structuring and Risk Analysis.xlsm](http://edbodmer.wikispaces.com/file/view/Renewable%20Model%20with%20Structuring%20and%20Risk%20Analysis.xlsm/539757920/Renewable%20Model%20with%20Structuring%20and%20Risk%20Analysis.xlsm)

[Renewable Class with wind power analysis.xlsm](http://edbodmer.wikispaces.com/file/view/Renewable%20Class%20with%20wind%20power%20analysis.xlsm/539757864/Renewable%20Class%20with%20wind%20power%20analysis.xlsm)

[Project Finance Model with Instructions.xlsm](http://edbodmer.wikispaces.com/file/view/Project%20Finance%20Model%20with%20Instructions.xlsm/424798612/Project%20Finance%20Model%20with%20Instructions.xlsm)

[Renewable Screening Analysis.xls](http://edbodmer.wikispaces.com/file/view/Renewable%20Screening%20Analysis.xls/353414680/Renewable%20Screening%20Analysis.xls)

[Project Finance Wind Template.zip](http://edbodmer.wikispaces.com/file/view/Project%20Finance%20Wind%20Template.zip/144052441/Project%20Finance%20Wind%20Template.zip)

[Renewable Analysis Revised.xls](http://edbodmer.wikispaces.com/file/view/Renewable%20Analysis%20Revised.xls/346103876/Renewable%20Analysis%20Revised.xls)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1272&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10396&rand=0.4590429666451934)