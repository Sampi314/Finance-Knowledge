# Creating a Master Database

**Source:** https://edbodmer.com/creating-a-master-database

---

This webpage descibes the process of creating a database and reading the data from the database into a template model. Maintaining the database in a clear manner is essential in creating the portfolio. The first screenshot below illustrates how you can start the process with a master database.  The one thing the database must have is the title for each of the SPV’s. Other data that will be imported into a separate file that simulates the SPV must be in the same row because of the way MATCH and INDEX are used.  The data can be expanded and the template SPV file can be changed to read in new data.  Note that if the template model is monthly and you have a whole lot of SPV’s, then the model can become slow.

.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-7.png)

.

The key idea about the process is the sheet name in the template file and how this sheet name is used to find the input data in the master page.  Later you will see how to create many different sheets from the template sheet with different names that will in turn select different inputs.  In the example below the file name in the template file is “Irani Brothers”.  This name will be changed to the other names in the master page (Ghana Beer in the example below).  Once you have the name, you use the MATCH function to find the row number of the project in the master sheet as shown below. You must use the 0 on the MATCH function because the names will not be in alphabetical order. Note that if you want to add columns to the master page you must be careful because the letters are defined in the INDEX function. So to add columns, you should put them at the right in an additional column.

.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-5.jpg)

.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-2.png)

.

Once you have the row number in the template model defined using the MATCH function, you can find any of the data that you will need.  To do this, you can use the INDEX function with an entire column where you define the entire column.  Then you refer to the row number defined from the MATCH function in the INDEX function (the old INDEX/MATCH).  In the first example in the screenshot below, the row number of 8 is defined from the match function.  Then you can find the start date of the project from column D in the master page.

.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-1.png)

![](https://edbodmer.com/wp-content/uploads/2018/11/spv-3.png)

.

Corporate Modelling with Consolidated Accounts from the INDIRECT Function
-------------------------------------------------------------------------

.

This is an analysis where multiple SPV’s are consolidated into a portfolio. A major innovation in the analysis is use of a flexible template for the SPV that includes currency risks and different types of financing. A macro copies that SPV to multiple different sheets. The INDIRECT function along with MATCH and INDEX are used to consolidate the SPV’s and analyse the results.

The third set of screenshots demonstrate the outputs of individual SPV’s that are eventually rolled-up into the consolidated analysis.  This depends on the financing structure of at the SPV and whether debt is issued on a project basis. The graphs show how debt service is paid at the individual SPV and how the individual SPV receives cash flow from the solar project in different scenario cases.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-3.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-2.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-6.jpg)

.

Financial Model where Different Projects in the Portfolio are Modelled with Separate SPV’s without Separate Financing
---------------------------------------------------------------------------------------------------------------------

.

The file below has a similar structure with a master database etc.  But this file includes financing in the SPV template and financing assumptions in the master database.  This means that separate financing is included for the separate SPV’s.  When you include financing in separate SPV’s there will be some problems with circular references.  This file resolves the circular references with the parallel model concept.

.

**[Model that Puts Together Multiple SPV's with an SPV Template the Includes Separate Financing for Each SPV](https://edbodmer.com/wp-content/uploads/2019/04/Egypt-Base-File-2.xlsm)
**

.

.

.

*   [The featured solar model page that is linked to this sentence includes completed finance models.](https://edbodmer.com/solar-models/)
    
*   [There is also a file that allows you to automatically download panel prices and the price of silicon used in manufacturing the panels which is linked to this sentence.](https://edbodmer.com/exchange-rate-from-fred-daily/)
    
*   [There is a webpage that works through resource issues including the performance ratio and how to find the best data on solar energy that hits a panel.](https://edbodmer.com/solar-financial-modelling-and-resource-analysis/)
    
*   [There is a webpage that describes computation of the P50 versus P90, P99 etc. with some examples.](https://edbodmer.com/solar-uncertainty-analysis/)
    
*   [There is a webpage that describes the arcane tax equity aspects of financing tax equity in the U.S.](https://edbodmer.com/a-z-tax-equity-model-with-fixed-flip-date/)
    
*   [There is a page that works through how to consolidate multiple roof-top installations into a aggregate file.](https://edbodmer.com/project-with-multiple-spvs/)
    

The file below is an analysis where multiple SPV’s are consolidated into a portfolio. A major innovation in the analysis is use of a flexible template for the SPV that includes currency risks and different types of financing. The INDIRECT function is uses a lot. A macro copies that SPV template to multiple different sheets to develop the separate SPV;s. The INDIRECT function along with MATCH and INDEX are used to consolidate the SPV’s and analyze the results

Development Analysis with Separate SPVs.xlsm

This is a solar rooftop analysis that involves identical issues to real estate analysis that include creating a portfolio with different characteristics including start dates, end dates changes in utilisation and operating expenses. It includes detail methods for computing working and financing. There is a set of 15 videos that constitutes a course associated with both basic and advanced issues associated with this analysis.

Portfolio of Small Developments.xlsm

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=15010&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9416&rand=0.2361081834846881)