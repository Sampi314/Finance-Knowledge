# Consolidating Projects to a Fund

**Source:** https://edbodmer.com/project-with-multiple-spvs

---

This webpage introduces how to efficiently create a model of multiple projects that are put into a fund and then consolidated. I have included a number of examples in the files attached to the buttons below. The method of consolidating many similar — but in no way identical — projects into a fund is useful for both real estate projects (like residential homes), rooftop solar projects on commercial buildings and other projects that can be put into a fund. One approach I suggest is to make a list of projects in a database and then create a template that can handle different project dates; different project sizes and costs; different construction periods etc. A second approach for more complex projects allows you to read a common template from multiple different input sheets. To apply either of these two methods you can gather the data into the template and then create a macro that copies the template for all of the projects. Finally, you can use the INDIRECT function to consolidate the individual projects into a fund. This method may sound a little difficult, but it just requires a couple of simple macros.

When you are finished with a couple of relatively simple macros, individual project sheets and consolidations come from a master sheet and an SPV template file. You can create multiple sheets with different SPV’s and put different projects into separate SPV’s with a relatively simple macro.  Once you have a lot of individual SPV’s in separate sheets, you can consolidate the SPV’s either using the INDIRECT function or using the SUM function that allows you to pull information from multiple sheets — **_SUM(start:end!d8)_**.  In this example, the start and end are sheet names and amounts are summed between the start and end sheets. This method of consolidating many similar (but in no way identical) projects is useful for both real estate projects (like residential homes) or rooftop solar projects on commercial buildings.  The files that are attached to the two buttons below illustrate the process using a macro and the INDIRECT function.

The buttons below include various different examples of putting together consolidated sheets. Other sub-menus to this sheet deal with particular examples that are used to create the consolidated models. The first model includes options to implement different programs. This is illustrated in the diagram below.

.

![](https://edbodmer.com/wp-content/uploads/2024/06/image.png)

.

**[Excel File with Consolidation of Separate Energy Efficiency in the Context of the IRA Using Single Data Sheet](https://edbodmer.com/wp-content/uploads/2024/06/IRA-and-Energy-Efficiency-10.xlsm)
**

.

**[Excel File with Consolidation of Separate Projects for Energy Efficiency Using Single Data Sheet](https://edbodmer.com/wp-content/uploads/2024/06/Energy-Efficiency-Example.xlsm)
**

.

**[Excel File with Analysis of Debt Funding for Different Solar Projects in a Portfolio with Macro and Indirect Function](https://edbodmer.com/wp-content/uploads/2021/09/Solar-Fund-Example.xlsm)
**

.

**[Excel File with Example of Creating a Fund with Common Timeline, Template, Simple Macro and Indirect](https://edbodmer.com/wp-content/uploads/2021/05/Solar-Fund-Example_18052021-1.xlsm)
**

.

**[Excel File with Portfolio of Different Projects Consolidated to an Aggregate Loan Using Indirect](https://edbodmer.com/wp-content/uploads/2022/01/Debt-Analysis-with-Multiple-Projects.xlsm)
**

.

.

Financial Model where Different Projects in the Portfolio are Modelled with Separate Projects in a Fund without Separate Financing of Individual Funding
--------------------------------------------------------------------------------------------------------------------------------------------------------

.

The file available for download below includes separate SPV’s for different facilities using the consolidation method with separately financing the SPV’s.  You go to the master database sheet and set up names of the different facilities that could be residential homes, commercial buildings, solar roof-tops etc. with the start dates, size, construction periods, rental rates and other factors.  Then you can copy the template for a single SPV to other SPV’s (using a macro).  After creating the SPV’s and the sheet names, you can consolidate the SPV’s and put in financing.  Finally, you can evaluate how the consolidated financing works with different scenarios and see how fast the consolidated loan can be paid off. Two files that work through this process are available for downloading by clicking on the buttons below.

.

**[Financial Model from Separate Solar Rooftop Projects Structured as SPV's that are Consolidate to Financial Model](https://edbodmer.com/wp-content/uploads/2018/08/Development-Analysis-with-Separte-SPVs.xlsm)
**

.

The process of modelling separate SPV’s using a master database and then putting them into a consolidated analysis is illustrated below.  Financing of the cash flow can be made at the consolidated level or the SPV level.  In the first file above, the financing is at the SPV and the consolidated level. The diagram below demonstrates that how you create a database, then make a template model for a single SPV that can accept the various different data items from the database.

.

Playlist on creating portfolios

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

Step 1: Create Database and Move from the Master to the Template Financial Model
--------------------------------------------------------------------------------

.

The first screenshot below illustrates how you can start the process with a master database.  The one thing the database must have is the title for each of the SPV’s. Other data that will be imported into a separate file that simulates the SPV must be in the same row because of the way MATCH and INDEX are used.  The data can be expanded and the template SPV file can be changed to read in new data.  Note that if the template model is monthly and you have a whole lot of SPV’s, then the model can become slow.

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

.

.

Macro to Consolidate the Template into Separate Projects
--------------------------------------------------------

After creating the template file, you can create inputs for a lot of different projects.  Each of the projects is defined by a name that becomes the sheet name.  You can then run or create a macro to copy the template sheet to another sheet. Once you have a lot of templates, you can consolidate the templates into a consolidation.  The consolidation uses the INDIRECT function to gather data from the different files. A few screenshots may give you an idea of how the file to consolidate different SPV’s works.  The first picture is intended to give you an idea of how the final consolidated process works.  This consolidation works by using the INDIRECT function to add together cash flows and balances from individual sheets. The second screenshot below shows how you can use the INDIRECT function. The INDIRECT function looks painful, but you can get the hang of it quickly.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-1.jpg)

.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-4-1.png)

.

.

Macro Examples to Consolidate Files
-----------------------------------

.

Sub CreateTemplate()

lastsheet = Sheets.Count ' This is the number of the sheets to move the file to
currentsheet = ActiveSheet.Name ' This is where to go back to after finished

Newspv = row ' This is a public variable from the multiple sheet row

Sheets("Master").Select ' Start with the master sheet

Newname = Cells(Newspv, 2) ' This is the sheet name that you put in the template sheet to define variables

Sheets("Template").Select ' Go to the template sheet
Sheets("Template").Copy After:=Sheets(lastsheet) ' Copy the sheet to the end of the file
Sheets(lastsheet + 1).Select ' Go to the new sheet that you made

Sheets(lastsheet + 1).Name = Newname ' Put the name of the new sheet in the file
Cells(1, 2) = Newname

Sheets(currentsheet).Select ' Go back to the original sheet

End Sub

.
.

Sub multiplesheet()

remember\_calc = Application.Calculation ' Will set calc to manual, so remember last value
Application.Calculation = xlCalculationManual ' Set to manual

Dim startrow, endrow As Single ' Need to dimension the variables that are defined by the input box

startrow = InputBox("Ligne de début ?")
endrow = InputBox("Ligne de fin ?")

For row = startrow To endrow ' Loop around rows in the master page

CreateTemplate ' Run the macro that creates a template
Calculate

Next row

Application.Calculation = remember\_calc ' re-set calculation to original value

End Sub

.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-4.jpg)

.

Corporate Modelling with Consolidated Accounts from the INDIRECT Function
-------------------------------------------------------------------------

.

This is an analysis where multiple SPV’s are consolidated into a portfolio. A major innovation in the analysis is use of a flexible template for the SPV that includes currency risks and different types of financing. A macro copies that SPV to multiple different sheets. The INDIRECT function along with MATCH and INDEX are used to consolidate the SPV’s and analyse the results.

The third set of screenshots demonstrate the outputs of individual SPV’s that are eventually rolled-up into the consolidated analysis.  This depends on the financing structure of at the SPV and whether debt is issued on a project basis. The graphs show how debt service is paid at the individual SPV and how the individual SPV receives cash flow from the solar project in different scenario cases.

.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-3.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-2.jpg)

.

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

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1334&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=7308&rand=0.6987388809590063)