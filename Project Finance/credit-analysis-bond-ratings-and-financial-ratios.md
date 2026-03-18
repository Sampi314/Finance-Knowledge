# Credit Analysis and Financial Modelling

**Source:** https://edbodmer.com/credit-analysis-bond-ratings-and-financial-ratios

---

This page reviews some fundamental credit analysis principles in corporate finance and project finance.  I begin with some general philosophical questions regarding credit analysis including whether judgment or analysis is best; whether statistical analysis is useful in credit analysis; whether traditional historic financial ratios are useful; whether financial models are good tools in evaluating credit; whether covenants are useful in credit analysis; whether similar credit analysis can be made for borrowers that have stopped growing to companies that are continuing to making on-going capital expenditures; whether good case studies of default can be used to identify patterns; whether high profit is a good or a bad thing when measuring credit analysis; whether character in credit analysis can be measured.

Ratings are simulated using financial ratios and business risk profiles from Standard and Poors. Different credit analysis ratios are contrasted such as the DSCR in project finance and the Debt to EBITDA ratio in corporate finance.  A file that summarizes the difference between corporate finance is introduced first.  Then analysis that you can use to put in benchmarks and come up with simulated credit ratings is described.

There are a few files that you can download that work through the use of financial ratios and business conditions to simulate bond ratings. These files include data provided by S&P on financial ratios, bond ratings and S&P subjective estimates of business risk.  With given financial ratios and given subjective estimates of business risk, the ratings can be estimated using the INTERPOLATE function.

**[Excel File that Includes Analysis of Debt Beta from Analysis of Credit Spreads and Evaluation of Simulated Bond Ratings](https://edbodmer.com/wp-content/uploads/2018/12/Debt-Beta.xlsm)
**

**[Excel File that Includes Data on Financial Ratios, Bond Ratings and Business Risk from Standard and Poor's](https://edbodmer.com/wp-content/uploads/2018/12/Credit-Benchmark-Ratios-and-Ratings-Data.xlsm)
**

**[Excel File that Includes Methods for Computing RORAC for Banks With Probability of Default and Other Statistics](https://edbodmer.com/wp-content/uploads/2020/06/RAROC-Model.xlsm)
**

Philosophical Backdrop for Credit Analysis
------------------------------------------

Before working through some of the details of different analytical issues associated with credit analysis, when discussing credit, we keep coming back to the same points. One of the fundamental ideas that you keep coming back to is that developing some kind of analytical model without using judgement hardly ever works for real credits.

Another fundamental issue for background in discussing credit that one cannot evaluate different types of credit in the same way. In particular, some credits such as project finance and other borrowers that are not growing by making future capital expenditures can be evaluated with cash flow and associated ratios like DSCR and LLCR. Other businesses that do not have contract support or history (e.g. start-ups from business plans) had too high probability of failure to support debt. Yet other businesses continue to grow and make associated capital expenditures meaning that debt is paid from refinancing and not cash flow. Finally, short-term working capital loans may depend on the value of inventory or receivables.

Some of other general ideas regarding credit analysis and the way I address these include:

*   When evaluating cash flow based credit analysis, can analytical methods using statistical analysis from objective statistics be used in credit analysis or should some kind of subjective analysis using judgmental analysis be used.
*   When evaluating credits for companies that are growing, can financial ratios such as debt/EBITDA, interest coverage and debt to capital be used and how should the return on invested capital be used as a backdrop in credit analysis. (Note that other ratios such as FFO/debt; FFO/cash flow are highly correlated with the other ratios).
*   How can different types of financial models be used in evaluating credit using alternative case studies

whether judgment or analysis is best; whether statistical analysis is useful in credit analysis; whether traditional historic financial ratios are useful; whether financial models are good tools in evaluating credit; whether covenants are useful in credit analysis; whether similar credit analysis can be made for borrowers that have stopped growing to companies that are continuing to making on-going capital expenditures; whether good case studies of default can be used to identify patterns; whether high profit is a good or a bad thing when measuring credit analysis; whether character in credit analysis can be measured.

Using Financial Ratios to Simulate Bond Ratings
-----------------------------------------------

In using the financial ratios and the financial ratios to simulate bond ratings, you need the financial ratio and the business risk estimate.  The screenshots below illustrate some of the manners in which S&P presents business risk and the key financial ratios that are used. The first screenshot below illustrates the various ratios used without any accounting for business risk.  You cannot use this for simulating bond ratings (although Damarodan does) because it does not contain any business risk.  You can find this in the excel file that had the S&P data.  It is sometimes difficult to update these files because S&P seems to be obsessed with making things totally un-understandable.

![](https://edbodmer.com/wp-content/uploads/2018/12/Credit-Ratio-1.png)

The two screenshots below shows S&P presentations where the credit rating does not only depend on the financial ratio but it also depends on the the business risk.  The business risk is defined as miniminal modest, aggressive etc. in the first screenshot. In the second screenshot that S&P uses for utility companies, the business risk has an explicit rating. Unlike Damarodan’s simplistic spreadsheet, these business risk profiles must be accounted for in evaluating the credit rating.  Numbers are assigned to the different business risks so that a rating can be assigned.

![](https://edbodmer.com/wp-content/uploads/2018/12/Credit-Ratio-2.png)

![](https://edbodmer.com/wp-content/uploads/2018/12/Credit-Ratio-3.png)

The next two screenshots illustrate how to mechanically compute the bond ratings given a business risk profile and given the financial ratios. The lookup function is not very useful because it makes a step function and when you want to weight different financial ratios it is not very good.  Instead, the INTERPOLATE function is good to use.

![](https://edbodmer.com/wp-content/uploads/2018/12/Rating-Simulaton.png)

![](https://edbodmer.com/wp-content/uploads/2018/12/Bond-Rating-Simulation.png)

Contrast between Credit Analysis in Corporate Finance and Project Finance
-------------------------------------------------------------------------

In project finance it is often appropriate to assert that the source of repayment for a loan is cash flow.  For corporate finance this is generally not the case. If a company is growing, it will continue to grow debt on the balance sheet and re-finance its loans. When lenders lose confidence in the quality of a companies assets, management or ability to generate future cash flow, the lenders may refuse to make new loans.  This is when bankruptcies like for Enron, Worldcom, Lehman Brothers and GM have occurred.  For these companies it is difficult to find obvious declines in cash flow or get much information from the DSCR ratio.

In the very simple model, you can put in different levels of volatility in both the corporate finance model and the project finance model.  The volatility takes one simple equation in excel to simulate — NORMSINV(RAND()).  The project finance model is simulated with volatility cash flow which is the fundamental theory behind the DSCR.  Of course, in the real world cash flow does not follow a normal distribution.  For the corporate model, the EBITDA and the future capital expenditures are modeled using a similar equation.  Here the financial ratios at the time of re-financing cash flow can be examined to evaluate whether lenders are willing to re-finance.  The corporate finance analysis is more difficult to simulate in a similar manner to project finance even though both are driven by volatility.  The manner in which I have attempted to simulate the different approaches is illustrated in the except below.  The associated file with the simple model that you can download is included as well.

![](https://edbodmer.com/wp-content/uploads/2018/04/Corporate-and-Project-1.jpg)

The second excerpt demonstrates the model.  For the corporate finance simulation I assume the loans must be re-financed after a given period and I compute the EV/EBITDA ratio at that period.  The DSCR does not make sense (nor LLCR or PLCR).  If the Debt to EBITDA ratio grows too much you can assume that the corporate finance cannot be re-financed.  The spreadsheet items for this are illustrated below.

![](https://edbodmer.com/wp-content/uploads/2018/04/Corporate-and-Project-2.jpg)

**[Simple Credit Simulation Used to Demonstrate Short-cut Keys in Excel](https://edbodmer.com/wp-content/uploads/2018/04/Project-and-Corprate-Finance-Credit-Example.xlsx)
**

**[Power Point Slides the Provide and Overiview of Credit Analysis and the Associated Modelling Issues](https://edbodmer.com/wp-content/uploads/2018/04/Credit-Analysis-Slides-Summary.pptx)
**

Credit Benchmark Ratios and Simulated Credit Ratings
----------------------------------------------------

Credit analysis has become a mixture of magic potion and BS like many other things in finance. Banks now buy a program from Moody’s that spits out a credit rating.  You end up spending a lot of time manipulating soft inputs related to management to push the rating to your desired level.  To go back to old fashioned credit analysis where you determine credit ratings through analysis of various financial ratios I have included a couple files below that you can download.

**[Power Point Slides that Work Through Various Different Financial Ratios Used in Credit Analysis and the Underlying Theory](https://edbodmer.com/wp-content/uploads/2018/04/Financial-Analysis-Slides-for-Credit.pptx)
**

**[Power Point Slides that Work Through Option Pricing Models and Other Mathematical Models Used in Credit Analysis](https://edbodmer.com/wp-content/uploads/2018/04/Mathematical-Credit-Analysis.pptx)
**

Short-term Analysis with Risk of Value Decline in Inventories and Changes in Demand
-----------------------------------------------------------------------------------

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=6702&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=18112&rand=0.39388746437695965)