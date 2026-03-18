# Overview of Consolidating to Fund

**Source:** https://edbodmer.com/overview-of-creating-portfolio

---

This webpage reviews the essential points of creating a portfolio of assets. The process of consolidating project finance files into a portfolio or into a corporate model can be done efficientyly with a macro and the creation of a database that defines inputs for different projects. You can also create a portfolio with more complex input structures. One of the keys to consolidating projects requires the inputs to be structured in a particular manner, sometimes with single columns for a project. The big deal for me is to create a completely flexible template where you can add lines, delete sections and change anything you want. This template must be able to handle every single input you made in the database and you must use XLOOKUP or INDEX to efficiently draw inputs in a consistent manner. The template is by far the most important thing you do in this process.

To consolidate after running the macro, use an old fashioned formula from lotus that sums everything in the same cell over a range of sheets. The key formula that consolidates sheets between two sheets is illustrated with the formula below.

SUM(Start:End!A1)
-----------------

![](https://edbodmer.com/wp-content/uploads/2023/10/image-2048x1053.png)

.

The buttons below are attached to excel spreadsheets that you can download. The first excel workbook is a relatively complex example where the input files are complex.

.

 **[Excel File with Projects Consolidating to Portfolio Demonstrating Returns and Financial Ratios](https://edbodmer.com/wp-content/uploads/2025/04/Portfolio-Consolidation.xlsm)
**

**[Excel File with Analysis of Debt Funding for Different Solar Projects in a Portfolio with Macro and Indirect Function](https://edbodmer.com/wp-content/uploads/2021/09/Solar-Fund-Example.xlsm)
**

**[Excel File with Example of Creating a Fund with Common Timeline, Template, Simple Macro and Indirect](https://edbodmer.com/wp-content/uploads/2021/05/Solar-Fund-Example_18052021-1.xlsm)
**

**[Excel File with Portfolio of Different Projects Consolidated to an Aggregate Loan Using Indirect](https://edbodmer.com/wp-content/uploads/2022/01/Debt-Analysis-with-Multiple-Projects.xlsm)
**

.

**[Conslidation Model with Example of Combining Projects that Have Different Input Structures with INDIRECT](https://edbodmer.com/wp-content/uploads/2024/07/Monthly-Hydrogen-with-UDF-V2.xlsm)
**

.

**[Conslidation Model with Example of Consolidating Different Corporate Models into Industry with INDIRECT](https://edbodmer.com/wp-content/uploads/2024/07/Consolidation-Example-Companies-in-Industry.xlsm)
**

.

Financial Model where Different Projects in the Portfolio are Modelled with Separate Projects in a Fund without Separate Financing of Individual Funding
--------------------------------------------------------------------------------------------------------------------------------------------------------

The file available for download below includes separate SPV’s for different facilities using the consolidation method with separately financing the SPV’s.  You go to the master database sheet and set up names of the different facilities that could be residential homes, commercial buildings, solar roof-tops etc. with the start dates, size, construction periods, rental rates and other factors.  Then you can copy the template for a single SPV to other SPV’s (using a macro).  After creating the SPV’s and the sheet names, you can consolidate the SPV’s and put in financing.  Finally, you can evaluate how the consolidated financing works with different scenarios and see how fast the consolidated loan can be paid off. Two files that work through this process are available for downloading by clicking on the buttons below.

**[Financial Model from Separate Solar Rooftop Projects Structured as SPV's that are Consolidate to Financial Model](https://edbodmer.com/wp-content/uploads/2018/08/Development-Analysis-with-Separte-SPVs.xlsm)
**

.

The process of modelling separate SPV’s using a master database and then putting them into a consolidated analysis is illustrated below.  Financing of the cash flow can be made at the consolidated level or the SPV level.  In the first file above, the financing is at the SPV and the consolidated level. The diagram below demonstrates that how you create a database, then make a template model for a single SPV that can accept the various different data items from the database.

.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-6.png)

.

Here is the way that process works on a step by step basis:

1.  **Step 1:** Create a master project database file. This file has the name of each separate SPV and the assumptions that will be used to model the SPV including the start of construction, the end of construction as well as operating and even financial variables.
2.  **Step 2:** Create a template for a single project.  This template accepts the start date of the individual project like a  commercial real estate project or a roof-top solar facility for a commercial building.  Some of the important features of the template file include:
3.  There is a name at the top of the template file that is the same as the excel sheet name.  This is an essential part of the process that allows the template to look-up in the master page and find the inputs. You use the MATCH function with this name to find the row number in the project file.
4.  The format of the template is the same for all projects, but the timeline can be different. In other words, the projects can have different start and end dates, different costs and so forth.  But the template is flexible enough to handle all of the assumptions.  In the case that is illustrated below, the template can handle different currencies and different solar production characteristics from alternative PVSYST files.
5.  Use the macros below (copy them into your file). Alternatively and better yet, write your own macros that loop around all of the projects defined in the database.  Also create a macro the clear the sheets because you may change the SPV template file and want to run the process again.
6.  Create the consolidation file with the INDIRECT function.  For this function you should define the file name in the left column to retrieve the various data and you should also define the row number that you will take from the template file.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=15003&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10092&rand=0.6556949044216577)