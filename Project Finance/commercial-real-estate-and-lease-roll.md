# Commercial Real Estate and Lease Roll

**Source:** https://edbodmer.com/commercial-real-estate-and-lease-roll

---

This webpage addresses various issues associated with commercial real estate. The fundamentals of commercial analysis are similar to the hotel model. However, modelling of a commercial building can be more complex due to an analysis of the lease roll.  Some real estate models of commercial buildings are presented along with lease roll analysis.  The challenge is determining how long the various leases will be idle and what the commercial lease rates will be for renewed leases.

Basic Models of Commercial Building without Lease Roll Analysis
---------------------------------------------------------------

The file that you can download below is a model I worked on in a financial modelling class a few years ago that has the construction period, sensitivity analysis and other elements related to modelling of a commercial building without detailed analysis of the leases that drive revenues earned from the building.  You can download the financial model by clicking on the button below.

**[Model of Commercial Building with Detailed Cash Flow Waterfall and Frinancing from Land Loan and Term Loan](https://edbodmer.com/wp-content/uploads/2018/09/Commercial-Building-with-Property-Index-and-Financing.xlsm)
**

A few screenshots below illustrate some of the features of the model.  The first screenshot illustrates some of the occupancy, rental rate and tax assumptions.  The second screenshot shows financing assumptions for a land loan and term loan.

![](https://edbodmer.com/wp-content/uploads/2018/09/Commercial-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/09/Commercial-2.jpg)

As the capital expenditures are financed by different types of loans, the cash flow analysis can become more complex.  The cash flow waterfall with a lot of sub-totals and MIN/MAX functions is illustrated in the screenshot below. When the cash flow is negative you can create a MAX function with a MIN function to loan money up to a commitment level.  After the cash flow is positive another MAX and MIN function can be used.

![](https://edbodmer.com/wp-content/uploads/2018/10/Commercial-3.jpg)

Lease Roll Modelling
--------------------

The file available for download below is an example of a real estate model with different types of financing instruments.  It is in PDF format rather than excel format.  One day I will convert the PDF format to excel and back into the excel equations which is not too difficult.

**[Real Estate Model with Cash Flow Waterfall in PDF format that Demonstrates Different Types of Financing](https://edbodmer.com/wp-content/uploads/2018/09/Real-Estate-Waterfall.jpg)
**

![](https://edbodmer.com/wp-content/uploads/2018/09/Lease-Roll-5.jpg)

The manner in which the uncertainty in lease rates can be modelled is demonstrated in the screenshot below. In this case the volatility reflected in a random number that is adjusted for the normal distribution.

![](https://edbodmer.com/wp-content/uploads/2018/09/Lease-Roll-Monte-Carlo-3.jpg)

Results of the volatility and the lease roll are illustrated below.

![](https://edbodmer.com/wp-content/uploads/2018/09/Lease-Roll-Monte-Carlo-2.jpg)

The video below takes you through some of the features for the commercial real estate analysis with the cash flow waterfall analysis.

Lease Rolls and Commercial Building Analysis
--------------------------------------------

Commercial buildings often have a series of leases for different parts of the buildings.  The leases have different terms, different prices and may have other incentives.  When the leases expire, you may need to evaluate how long long the space may be idles or if the lease will be immediately renewed.  When the leases are renewed, the price of the new lease depends on the general market.  Three models in this section demonstrate a few possible modelling techniques for lease rolls.

The first model that you can download below illustrates a simple example of a lease roll.  As for other models, you can download the model by pressing the button below. The first screenshot illustrates a simple layout of leases with the number of the lease, the lease rate and the expiration of the lease.  In a basic lease roll analysis, you should enter a market lease rate and simulate the cash flow that switches to the market rate when the leases expire. The second screenshot demonstrates the market rate which will be subject to sensitivity analysis.

![](https://edbodmer.com/wp-content/uploads/2018/09/Lease-Roll-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/09/LEase-Roll-2.jpg)

To model the lease roll you can develop code numbers.  In this simple case I put in three code numbers as shown in the screenshot above.  The first code number is when the initial lease is active.  The second is for an assumed idle period.  The third is for the second period or a market rate.  With the code numbers defined, you use and IF function to develop code numbers.  With the code numbers you can define the effective lease rates using the CHOOSE function.

![](https://edbodmer.com/wp-content/uploads/2018/09/Lease-roll-3.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/09/Lease-Roll-4.jpg)

A financial model that includes modelling of a lease roll in a simple case is available for download by pressing the button below.  This case forms the basis for more detail analysis that can handle multiple leases, Monte Carlo simulation and monthly idle periods.

**[Excel File that Illustrates Mechanics of Modelling Lease Roll with CHOOSE function and Code Numbers for Lease Periods](https://edbodmer.com/wp-content/uploads/2018/09/Exercise-10-Lease-Roll-Analysis.xls)
**

The second file demonstrates how to incorporate Monte Carlo simulation into the Lease Roll analysis.  The reason Monte Carlo simulation may be interesting in modelling a lease roll can be illustrated by considering different lease roll scenarios.  In one scenario you have a lot of long-term leases and in a second case there is more market exposure.  You can use this to illustrate changes in probability of default and distribution of income.

**[Excel File with Commercial Lease Roll Combined with Monte Carlo Simulation on Market Rates](https://edbodmer.com/wp-content/uploads/2018/09/Exercise-10a-Lease-Book-with-Monte-Carlo-Simulation.xls)
**

![](https://edbodmer.com/wp-content/uploads/2018/09/Commercial-4.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/09/Commercial-5.jpg)

**[Real Estate Model of Commercial Building that Includes Lease Roll and Monte Carlo Simulation of Market Spot Rates](https://edbodmer.com/wp-content/uploads/2018/09/Commercial-with-Lease-Roll.xlsm)
**

Other files that I have not yet put on this website are show below. You can find these files in the resource library by e-mailing me at edwardbodmer@gmail.com. They are in the Real Estate Folder of Chapter 1.

Exercise 10 – Lease Roll Analysis.xls

Commercial with Lease Roll.xlsm

Commercial with Lease Roll.xlsm

Real\_Estate\_Model.xls

The file below is an example of an PDF file that somebody gave me.  It demonstrates that type of structure and the type of outputs that you want in a model.  Please let me know if you would like this model converted to a model so you can work with the equations.  Send an e-mail to edwardbodmer@gmail.c0m.

**[PDF File with Example of Real Estate Model that Will be Converted to an Excel File One Day](https://edbodmer.com/wp-content/uploads/2018/09/72ndCornhuskerRealEstateInvestmentAnalysis.pdf)
**

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3246&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9008&rand=0.34228033293210147)