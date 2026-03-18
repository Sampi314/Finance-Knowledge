# Hydrogen Analysis

**Source:** https://edbodmer.com/levelized-cost-of-hydrogen-and-biomass

---

In this page I discuss analysis of the hydrogen project finance models and the levelized cost of hydrogen (LCOH) and how to create a project finance model of hydrogen production. In evaluating the cost of (green) hydrogen, the analysis must account for the cost and efficiency of an electrolyzer; the replacement of stacks in an electrolyzer; compression and storage of hydrogen; the cost of transporting hydrogen; and the efficiency of dispensing hydrogen. One of the ultimate questions regarding the future of hydrogen in a de-carbonated world is the cost of hydrogen produced from an electrolyzer relative to alternative means for achieving transport, fertilizer, industrial uses, and many other things. Accurately calculating the cost of hydrogen through the LCOH allows you to address different business models such as use of hydrogen for airplanes, garbage trucks, busses and other transport that cannot be accomplished with electric vehicles; comparing the cost of hydrogen from an electrolyzer with the cost of hydrogen from a steam methane reactor (SMR); evaluating the cost and benefits of distributed hydrogen production versus centralized production; and, measuring the effectiveness of a strategy that produces hydrogen during selected time periods when electricity costs are low.

.

.

![](https://edbodmer.com/wp-content/uploads/2021/03/image-61.png)

.

.

**[Power Point Slides with Discussion of Levelised Cost, Characteristics and Financial Analysis of Hydrogen Projects](https://edbodmer.com/wp-content/uploads/2021/12/Hydrogen-Analysis.pptx)
**

.

The question of whether hydrogen can be efficient relative to other strategies demonstrates how levelized cost can be an effective tool to evaluate the details of alternative business strategies. I try to explain that if you carefully compute the levelized cost — not a simplistic project finance model with a goal seek — that you can understand parameters necessary to make a sensible business case. The LCOH can account for different lives of the stack and other equipment in the electrolyzer; for the leaning and reduced cost of replacement of certain items; for the fact that some components of the electrolyzer are driven by hours used rather than by time; for differences between the amount of storage quantity and production; and many other items. This page explains that the cost of computing the unit cost of hydrogen is more complex than calculating the levelized cost of electricity (as electricity typically only has a couple of inputs except in the case of storage). To compute the LCOH you will need many more inputs including the cost of electrolyzers and stacks that use electricity and convert the electricity into hydrogen, the cost of the final use of hydrogen, the cost of the distribution, the cost of storage. The analysis should also cover the cost of compression, storage and dispensing. Finally, in order to make the analysis relevant, the costs of the transportation equipment and the difference in the efficiency of the transport equipment must be accounted for.

**[Excel File with Analysis of Hydrogen Including Demonstration of How to Quantify Project Elements with Different Lives](https://edbodmer.com/wp-content/uploads/2021/09/Green-Ammonia-Case-Study-4.xlsm)
**

Case 1: Hydrogen from Electrolyzer versus Hydrogen from Blue and Grey SMR
-------------------------------------------------------------------------

The first case I address is the difference between the cost of an electrolyzer that uses electricity to separate H2 from O and a Steam Methane Reactor (SMR) that uses natural gas. I understand that the smallest SMR shown in the picture below is larger than the largest electrolyzer (this may change as some very large electrolyzers are planned). The SMR combines natural gas (methane or CH4) with water (H2O) and it produces H2 as well as CO2. If you do not capture any of the CO2, the process is called grey hydrogen production. If you capture most of the CO2 with carbon capture, it is called blue hydrogen production. The cost of hydrogen that comes from the SMR uses a lot of capital and natural gas. A paper by a graduate student in Norway works through the costs and efficiencies and is the basis for the comparison with an electrolyzer which is green hydrogen production. Note that because of the size of the SMR, unless it is attached to production of Ammonia or perhaps a refinery, you will have to compress, store and transport the hydrogen.

![](https://edbodmer.com/wp-content/uploads/2021/03/image-56.png)

An electrolyzer (see the picture below) separates hydrogen from oxygen and does not produce CO2. It is an old technology and my friend Massimiliano has even made an electrolyzer himself. The question is whether you can make the economics of the electrolyzer approach the cost of producing hydrogen from an SMR. In making this analysis I evaluate issues including the cost of distribution and the cost of building a larger electrolyzer with more storage in order to take advantage of low electricity costs. In order to do make this evaluation, I set up a case where a given amount of hydrogen is needed and certain times and compare the costs of an SMR with an electrolyzer.

I have tried to demonstrate the levelized cost with a diagram and some spinner boxes and dropdown boxes. I harp on the point that for the LCOH analysis to be useful, you must be very transparent with the inputs and the formulas. The screenshot below is from the model that I made.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-44.png)

The file with the levelized cost of hydrogen analysis is attached to the button below. In this file you can create your own technology alternatives and/or change the cost and efficiency inputs for different alternatives. As you can see from the screenshot above, the key for me is to see the percent increase or decrease in cost relative to operation with diesel. You can also click on the check boxes to include or not include the cost of hydrogen trucks relative to diesel trucks. I explain how I have created the database below.

**[Excel File that with Levelised Cost per Unit Template with Case Study for Hydrogen Transport Trucks](https://edbodmer.com/wp-content/uploads/2021/02/Hydrogen-Analysis-1.xlsm)
**

**[Excel File with Analysis of The Levelized Cost of Hydrogen Including Databases with Alternative Technology Estimates](https://edbodmer.com/wp-content/uploads/2020/08/Hydrogen-Case-Study_3.xlsm)
**

**[Excel File with Analysis of The Costs and Benefits of Converting Biogas from Palm Oil Into Methane For Use in Trucks](https://edbodmer.com/wp-content/uploads/2020/08/Federico-Model7.xlsm)
**

**[Excel File that with Project Finance Model of Biomass Analysis where Palm Oil Waste is Converted to Transport Fuel](https://edbodmer.com/wp-content/uploads/2021/02/Federico-Model8_temp4.xlsm)
**

I have also used the file to compute a financial model that evaluates the required subsidy that is necessary to attract investment. This file is computed on a monthly basis rather than an annual basis. The file also contains trucks that are not assumed to be built at the same time. With this file you can compute the required subsidy if there are different costs of electricity, sizes of the electrolyzer, capital costs and many other variables. This file is attached to the button below.

 **[Excel File with Financial Model of Hydrogen Project Using Inputs from the Hydrogen LCOH Analysis and Databases](https://edbodmer.com/wp-content/uploads/2020/09/Project-Finance-Case-Studies-and-Principles-May-.2-2018.pdf)
**

### Database for LCOH Analysis

In the above files, I have tried to make it easy to change inputs and compare inputs for the various technologies with other estimates. I used to make databases for wind and solar before the costs became pretty public and easy to find. So I used some costs that I received from a friend along with more difficult to find data on the capacity and the cost of storage, compression and dispensers. In order to compare the costs I put a dropdown box for different data sources and then allow you to select individual characteristics by copying the dropdown box. In addition, I add reset buttons so that you can go back to your starting point. These methods can be applied to any scenario and are explained in the videos near the bottom of the page. The screenshot below illustrates the

![](https://edbodmer.com/wp-content/uploads/2020/08/image-47.png)

For the biomass case I just use spinner buttons that are attached to the inputs. (In the hydrogen case the inputs are collected from the index column of the database). The screenshot below illustrates how this process works. For both projects it is in my opinion essential to keep the different parts of the process separate. In both cases you must make sure that the amount of production can meet the required truck demand and that the equipment is not over- or under-sized. This is analogous to the capacity factor analysis when evaluating LCOE.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-48.png)

### LCOH Model

The model for the LCOH case involves a lot of conversions. You have to convert the amount of electricity to the kg using an efficiency ratio. You have to convert the km of the trucks to the amount of hydrogen and the amount of diesel. You have to convert the amount of hydrogen required per day into the amount of dispenser capacity measured in therms of minutes. The manner by which I try to be explicit about this stuff is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-49.png)

#### Video Discussing Levelised Cost of Hydrogen

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=11001&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12448&rand=0.2686813589152395)