# Swaps, Options and Futures

**Source:** https://edbodmer.com/options-and-futures

---

On this page you can review some excel files and analysis for valuing interest rate swaps, exchange rate swaps and various different real options.  The files can be used to value of a swap or an option over time so you can evaluate the cost of terminating the contract. The first set of file are various files on working with options models, futures prices and forward interest rates.

Valuing Interest Rate Swaps when Interest Rates Change
------------------------------------------------------

My good friend asked me about swap breakage costs and if I had any models.  I told him I had a few old models that demonstrate how to calculate the value of an interest rate swap and exchange rate swap.  Some of the excel techniques are horrible in the files below, but if you are interested in the general approach to computing the value of a swap after interest rates and/or exchange rates change, maybe this could help.

I created an exercise where you practice some discounting on a discrete and on a continual basis and derive the value of a fixed rate to floating rate swap with different interest rates.  In this exercise you assume that you know the future spot interest rate (like the future LIBOR 3 month rate).  The next exercise demonstrates how to find the rate. The two screenshots below illustrate what you should see when you open the file.  The first screenshot is the blank exercise file and the second screenshot illustrates the completed exercise.

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Swap-Exercise-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Swap-Exercise-2.jpg)

**[Excel File with Exercise on How to Compute the Value of an Interest Rate Swap Given Interest Rates](https://edbodmer.com/wp-content/uploads/2018/10/swaps_exercise.xls)
**

The file below shows how to construct spot rates from the yield on bonds with different maturities. The process is a bootstrapping method where you first find the yield to maturity on a short-term government bond. Then you use this rate to find the implied spot rate on the next maturity of a bond (e.g. a 3 month and a six month bond).  Then once you have the maturity for the 6 month bond you continue the process.  Because you want monthly rates, in this file you need some interpolation and I used a very crappy old fashion method.  One day I will update the file.  But the key is that you can use the file to come up with spot interest rates and forward interest rates that are used in computing the swap value.  The screen shots illustrate a couple of pages from the file (sorry about the old interest rate data).  The first screenshot shows the inputs for yields from different bonds on the first page of the workbook.  The second file shows the way you press a stupid button to do the interpolation.  The third screenshot shows the resulting spot rates and forward rates.

If you want to get up to date interest rates you can used the second file below that has links to the FRED interest rate data.  One day I will make the whole thing automated.

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Spot-Rates.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Term-Structure.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Term-Structure-1-1.jpg)

**[Excel File with Term Structure of Interest Rates using Bond Yields and Deriving Spot Rates](https://edbodmer.com/wp-content/uploads/2018/10/Term-Structure-Models.xls)
**

The interest rate database is available for download by pressing the button below. The interest rate database attached to the button may not be current to the latest month. To update the database you can follow the instructions in the section below.

**[Interest Rate Database that Extracts Data from the FRED Database with Quick Updates and Flexible Graphs](https://edbodmer.com/wp-content/uploads/2020/01/Interest-Rates.xlsm)
**

The next file is an example of computing swap value once you have the interest rates.  It is not an exercise file, but a file where you can press a goal seek and derive the swap rate.  After you have the swap rate you can then compute how the value of the swap changes if the interest rate changes.  The screenshot below demonstrates how to you can press a button and get the swap value.  You can then change interest rates and see how the value of the interest rate swap changes.  The first screenshot and the the first file demonstrate the case with periodic compounding of interest rates.  The second screenshot and the second file show the case with continual compounding.

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Swap-Value.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Swap-Continual.jpg)

**[Excel File that Demonstrates how to Compute the Value of Interest Rate Swaps After the Interest Rate Changes](https://edbodmer.com/wp-content/uploads/2018/10/swaps.xls)
**

**[Excel File that Demonstrates Valuation of an Interest Rate Swap where Discounting is on a Continual Basls](https://edbodmer.com/wp-content/uploads/2018/10/SWAPS_contunial_1.xls)
**

The next screenshots and files demonstrate how to compute the value of an exchange rate swap that depends on the interest rates in two countries and the exchange rates in two countries.  As with the interest rate swaps you need forward interest rate and forward exchange rate data making the valuation somewhat more complex.  The first screenshot demonstrates what you should see when you open the first file and where you can see the value of the exchange rate swap at the bottom of the bottom of the blue section (sorry about the stupid colours — I did this a long time ago). The second screenshot and file is similar to the first file that values the exchange rate swap, but it applies continual compounding.

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Exchange.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Exchange-Continual.jpg)

**[Excel File with Currency Swap Valuation Analysis that Depends on Forward Interest Rates and Exchange Rates](https://edbodmer.com/wp-content/uploads/2018/10/SWAPS_currency.xls)
**

**[Excel File that Demonstrates Value of Exchange Rate Swap that Applies Continual Compounding Formulas](https://edbodmer.com/wp-content/uploads/2018/10/SWAPS_currency1.xls)
**

The file that you can download below includes exchange rates and allows you to update the database. This database includes more exchange rates than the exchange rates available from the FRED website.

.

**[Excel File that Retreives Historical Data on Exchange Rates and Includes More Rates than the FRED Website](https://edbodmer.com/wp-content/uploads/2018/03/Get-Historic-Exchange-Rates.xlsm)
**

.

If you want to update data in this file, you should copy new dates in to the column of the menu sheet.  As I was interested in monthly data, I put in a few dates of each month (to make sure there are no weekends when the data is not available).  Then you click on the read all button that is illustrated in the screenshot below.  After clicking on the button you are asked to enter the beginning and ending date and the data is read into separate sheets.

.

The screenshot below illustrates the process for computing the forward rate for a commodity price where you can store the commodity.

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-1.jpg)

In addition to the historic prices, you can retrieve data from futures markets using the workbooks.open method and putting together the summary of different futures prices.  The file that you can used to download futures prices and update them is available for download below.  The website for acquiring futures data has changed in the past which can create some problems.  If there are any issues with running and updating the program, please do not hesitate to send me an e-mail at edwardbodmer@gmail.com.

**[Database file with Commodity Futures Prices from the CME that you can Update Automatically](https://edbodmer.com/wp-content/uploads/2018/05/Gas-and-Oil-Futures2.xlsm)
**

The futures data is downloaded from:[http://www.cmegroup.com/trading/energy/crude-oil/brent-crude-oil.html](http://www.cmegroup.com/trading/energy/crude-oil/brent-crude-oil.html)
.

Using Option Models for Evaluating Credit Spreads, PD and LGD
-------------------------------------------------------------

A few years ago it was popular to try and measure credit spreads using option pricing theory as debt can be considered a sold put option.  The credit spread is the option premium or price, the termination date of the option is the duration of the debt and the volatility of cash flows drives the value of the option.

The first file below illustrates how you can use the option pricing method to either start with a credit spread and derive the probability of default or start with volatility and back compute the credit spread.  This is not very practical but is a good way to think about what should really drive the value of an option.

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Merton-Model-Ezercise.jpg)

**[Merton Model Exercise for Computing the Probability of Default and the Loss Given Default](https://edbodmer.com/wp-content/uploads/2018/10/Financial-Model-for-Merton-Exercise.xls)
**

**[Financial Model Used to Illustrate Results of Merton Model with Monte Carlo Simulation Using Macro](https://edbodmer.com/wp-content/uploads/2018/10/Financial-Model-for-Merton-Exercise-1.xls)
**

**[Excel File with Exercise on How to Develop the Merton Model for Evaluating Credit Spreads, PD and LGD](https://edbodmer.com/wp-content/uploads/2018/10/Merton-Model-Exercise.xls)
**

**[Excel File with Merton Model for Computing Credit Spreads with Completed Formulas and Analysis](https://edbodmer.com/wp-content/uploads/2018/10/Merton-Model-Exercise-Completed.xls)
**

**[Excel File with Analysis of How to Compute the Implied Probability of Default Given the Credit Spread](https://edbodmer.com/wp-content/uploads/2018/10/PD-and-LGD-for-Debt.xlsx)
**

Option Pricing Model Exercises
------------------------------

![](https://edbodmer.com/wp-content/uploads/2018/10/Futures-Bill-Arbitrage.jpg)

**[Excel File with Demonstration of Creating Option Arbitrage with Mix of Risk Free Securities](https://edbodmer.com/wp-content/uploads/2018/10/bill_arbitrage.xls)
**

You can see that I have not yet transferred the files from the old website.  I will do this and explain what is in the files.

[Black\_scholes\_exercise with graphs.xls](http://edbodmer.wikispaces.com/file/view/Black_scholes_exercise%20with%20graphs.xls/574878101/Black_scholes_exercise%20with%20graphs.xls "Black_scholes_exercise with graphs.xls")

[Black\_scholes\_exercise.xls](http://edbodmer.wikispaces.com/file/view/Black_scholes_exercise.xls/574878141/Black_scholes_exercise.xls "Black_scholes_exercise.xls")

[BlackScholesModel.xlsx](http://edbodmer.wikispaces.com/file/view/BlackScholesModel.xlsx/574878253/BlackScholesModel.xlsx "BlackScholesModel.xlsx")

[Credit Spread Exercise.xlsm](http://edbodmer.wikispaces.com/file/view/Credit%20Spread%20Exercise.xlsm/574878305/Credit%20Spread%20Exercise.xlsm "Credit Spread Exercise.xlsm")

[debt\_option\_arbitrage.xls](http://edbodmer.wikispaces.com/file/view/debt_option_arbitrage.xls/574878187/debt_option_arbitrage.xls "debt_option_arbitrage.xls")

Real Option Analysis
--------------------

[Exercise 1 – Staged Investment.xls](http://edbodmer.wikispaces.com/file/view/Exercise%201%20-%20Staged%20Investment.xls/115281175/Exercise%201%20-%20Staged%20Investment.xls "Exercise 1 - Staged Investment.xls")

The second set of files addresses real options. The order of the files associated with real options correspond to the discussion in Chapter 5 of the Valuation Mirage text. The file below contains exercises that walk through the mechanics of measuring the value of the option to expand an investment

File that walks through how to simulate exploration or research option in various stages with given probabilities to cancel at different stages. You input stage lengths, probabilities of the stages being successful and the costs of each stage as well as the ultimate cash flow if the whole project is successful. You can then evaluate the relative importance of each expenditure.

[Development Option.xls](http://edbodmer.wikispaces.com/file/view/Development%20Option.xls/111548411/Development%20Option.xls "Development Option.xls")

File that simulates development option to cancel with volatility and mean reversion. The tricky part is to evaluate the value of the investment project in different scenarios without looking ahead.

[Contracting Option.zip](http://edbodmer.wikispaces.com/file/view/Contracting%20Option.zip/111520163/Contracting%20Option.zip "Contracting Option.zip")

[Case 1a Prospective Volatility at End of Development.xls](http://edbodmer.wikispaces.com/file/view/Case%201a%20Prospective%20Volatility%20at%20End%20of%20Development.xls/111524353/Case%201a%20Prospective%20Volatility%20at%20End%20of%20Development.xls "Case 1a Prospective Volatility at End of Development.xls")

[Case 2 Prospective Volatility with Mean Reversion.xls](http://edbodmer.wikispaces.com/file/view/Case%202%20Prospective%20Volatility%20with%20Mean%20Reversion.xls/111524385/Case%202%20Prospective%20Volatility%20with%20Mean%20Reversion.xls "Case 2 Prospective Volatility with Mean Reversion.xls")

[Case 1 Prospective Volatility without Mean Reversion.xlsx](http://edbodmer.wikispaces.com/file/view/Case%201%20Prospective%20Volatility%20without%20Mean%20Reversion.xlsx/111524313/Case%201%20Prospective%20Volatility%20without%20Mean%20Reversion.xlsx "Case 1 Prospective Volatility without Mean Reversion.xlsx")

File that simulates delay option at after development. The difficult part is re-evaluating the question of whether the project should be delayed and re-computing the economics of the project with different delay periods.

File that simulates the option to cancel at different stages of construction and opeartion. The general idea is similar to contracting option except that it must be evaluated on a dynamic basis which makes the proceess more complex.

[Case 3 Valuation in Cancellation Option.xls](http://edbodmer.wikispaces.com/file/view/Case%203%20Valuation%20in%20Cancellation%20Option.xls/111524431/Case%203%20Valuation%20in%20Cancellation%20Option.xls "Case 3 Valuation in Cancellation Option.xls")

File that walks through how to create Black-Scholes and Black model for standard financial options.

File that includes the binomial tree approach to modelling options.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=807&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=7296&rand=0.6172559990020443)