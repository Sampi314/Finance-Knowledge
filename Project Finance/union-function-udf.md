# Union Function (UDF)

**Source:** https://edbodmer.com/union-function-udf

---

This web page demonstrates how to efficiently retrieve data for your financial models.  On this page I focus on how to automate acquiring data from the Securities and Exchange Commission (SEC).  I describe how to create a macro to read in the data and then clean up the data using other VBA programs and how the use the Union function. Other pages demonstrate how to use the Read pdf file to extract data into annual reports and how to read financial statement data from Market Watch into an excel file.  The Securitiy and Exchange Commission in the U.S. publishes a lot of data that can be used in corporate finance and modelling.  This data includes financial statements (10K for annual and 10Q for quarterly), acquisitions, new securities issues and investor analyst presentations.  I have made a file that automatically reads the interactive data published on the SEC website and then compile the data into a set of usable data.  Making the data usable includes a macro described below along with the UNION function. The SEC clean up file allows you to copy the data into an excel file and then it cleans up the data. The SEC clean up data file works with a macro that is somewhat like the read pdf to excel function.  To operate the clean up SEC system, you can download the file that includes the macros below. The file must be opened  after you copy data from the SEC website.  Once the file is opened, follow the instructions in the file.  At the bottom of this webpage I introduce a method to use the interactive data to make an automatic download.  The file below has the macro that you can use to clean up the data.

**[Excel File with Macros that Allow you to Quickly Format HTML Files from the SEC Website into Excel](https://edbodmer.com/wp-content/uploads/2020/04/Format-SEC.xlsm)
**

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=15582&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.3532125546913967)