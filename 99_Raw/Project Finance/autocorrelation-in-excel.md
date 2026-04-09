# Autocorrelation in Excel

**Source:** https://edbodmer.com/autocorrelation-in-excel

---

You can probably find very good websites to perform regression analysis in excel. I believe that for economic variables it is important to understand when auto-correlation is present in the data. With auto-correlation, the variables move together, but the error term from the regression is highly correlated with the prior error, violating a fundamental necessity of a standard regression. I don’t think there is an automatic way to adjust for auto-correlation, so I demonstrate how to make this adjustment in the files below. The regression analysis also makes extensive use of the OFFSET function so you can make all of the analysis very flexible.

Step by step process:

1\. Run Normal OLS (In excel, get the slope and the intercept)

2\. Compute the residuals from the regression

3\. Run a regression of the residual versus the lagged residual

4\. Use the slope of the regression in step 3 for transposing the data

You can do this in logs or in absolute amounts.

[Flex Regression with Autocorrelation.xls](https://edbodmer.wikispaces.com/file/view/Flex%20Regression%20with%20Autocorrelation.xls/609975161/Flex%20Regression%20with%20Autocorrelation.xls "Flex Regression with Autocorrelation.xls")

[complaint Regression.xls](https://edbodmer.wikispaces.com/file/view/Complaint%20Regression.xls/609975221/Complaint%20Regression.xls "Complaint Regression.xls")

[Regression Analysis Accounts Receivable.xlsm](https://edbodmer.wikispaces.com/file/view/Regression%20Analysis%20Accounts%20Receivable.xlsm/609975229/Regression%20Analysis%20Accounts%20Receivable.xlsm "Regression Analysis Accounts Receivable.xlsm")

[Regression Proof with Solver.xls](https://edbodmer.wikispaces.com/file/view/Regression%20Proof%20with%20Solver.xls/609975241/Regression%20Proof%20with%20Solver.xls "Regression Proof with Solver.xls")

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1192&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11728&rand=0.42843451756005757)