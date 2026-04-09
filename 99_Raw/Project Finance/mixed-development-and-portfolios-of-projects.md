# Mixed Development and Investment Portfolios of Projects

**Source:** https://edbodmer.com/mixed-development-and-portfolios-of-projects

---

This page describes the modelling of mixed development projects in real estate. Mixed developments consist of a portfolio of different projects with different construction start dates, occupancy dates and holding periods.  The mixed development projects could have different types of project with commercial, and residential. The page includes detailed discussion of how to construct a model with multiple SPV’s where you set-up a database of project characteristics with the name and the assumptions for the SPV’s.  Once this is set-up you can use a macro along with the INDIRECT function to create separate models for each SPV from a template file and then consolidate the SPV’s in a separate spreadsheet.

Introduction to Mixed Development Modelling and PDF File
--------------------------------------------------------

To big difference between real estate finance and other project finance are: (1) in real estate there is a generally a portfolio of projects with different occupancy dates (TOP) and different construction schedules; and (2) in real estate, the projects are often sold after a few years meaning that you must evaluate cap rates.  Real estate models are also very similar to solar roof-top analysis.

**[Mixed Use Real Estate Model in PDF Format that Demonstrates Statistics and Input Layout](https://edbodmer.com/wp-content/uploads/2018/09/Mixed_Use_Model.pdf)
**

Portfolio Issues in Real Estate Models
--------------------------------------

This is a solar rooftop analysis that involves identical issues to real estate analysis that include creating a portfolio with different characteristics including start dates, end dates changes in utilisation and operating expenses. It includes detail methods for computing working and financing. There is a set of 15 videos that constitutes a course associated with both basic and advanced issues associated with this analysis.

.

.

Financial Model where Different Projects in the Portfolio are Modelled with Separate SPV’s
------------------------------------------------------------------------------------------

The file available for download below includes separate SPV’s for different facilities.  You set up names of the different facilities that could be residential homes, commercial buildings, solar roof-tops etc. with the start dates, size, construction periods, rental rates and other factors.  Then you can copy the template for a single SPV to other SPV’s.  After creating the SPV’s and the sheet names, you can consolidate the SPV’s and put in financing.  Finally, you can evaluate how the consolidated financing works with different scenarios and see how fast the consolidated loan can be paid off. Two files that work through this process are available for downloading by clicking on the buttons below.

**[Financial Model from Separate Solar Rooftop Projects Structured as SPV's that are Consolidate to Financial Model](https://edbodmer.com/wp-content/uploads/2018/08/Development-Analysis-with-Separte-SPVs.xlsm)
**

The process of modelling separate SPV’s using a master database and then putting them into a consolidated analysis is illustrated below.  Financing of the cash flow can be made at the consolidated level or the SPV level.  In the first file above, the financing is at the SPV and the consolidated level. The diagram below demonstrates that how you create a database, then make a template model for a single SPV that can accept the various different data items from the database.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-6.png)

Here is the way that process works on a step by step basis:

Step 1: Create a master project database file. This file has the name of each separate SPV and the assumptions that will be used to model the SPV including the start of construction, the end of construction as well as operating and even financial variables.

Step 2: Create a template for a single project.  This template accepts the start date of the individual project like a  commercial real estate project or a roof-top solar facility for a commercial building.  Some of the important features of the template file include:

1\. There is a name at the top of the template file that is the same as the excel sheet name.  This is an essential part of the process that allows the template to look-up in the master page and find the inputs. You use the MATCH function with this name to find the row number in the project file.

2\. The format of the template is the same for all projects, but the timeline can be different. In other words, the projects can have different start and end dates, different costs and so forth.  But the template is flexible enough to handle all of the assumptions.  In the case that is illustrated below, the template can handle different currencies and different solar production characteristics from alternative PVSYST files.

Step 3: Use the macros below (copy them into your file). Alternatively and better yet, write your own macros that loop around all of the projects defined in the database.  Also create a macro the clear the sheets because you may change the SPV template file and want to run the process again.

Step 4: Create the consolidation file with the INDIRECT function.  For this function you should define the file name in the left column to retrieve the various data and you should also define the row number that you will take from the template file.

Data from the Master to the Template
------------------------------------

The first screenshot below illustrates how you can start the process with a master database.  The one thing the database must have is the title for each of the SPV’s. Other data that will be imported into a separate file that simulates the SPV must be in the same row because of the way MATCH and INDEX are used.  The data can be expanded and the template SPV file can be changed to read in new data.  Note that if the template model is monthly and you have a whole lot of SPV’s, then the model can become slow.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-7.png)

The key idea about the process is the sheet name in the template file and how this sheet name is used to find the input data in the master page.  Later you will see how to create many different sheets from the template sheet with different names that will in turn select different inputs.  In the example below the file name in the template file is “Irani Brothers”.  This name will be changed to the other names in the master page (Ghana Beer in the example below).  Once you have the name, you use the MATCH function to find the row number of the project in the master sheet as shown below. You must use the 0 on the MATCH function because the names will not be in alphabetical order. Note that if you want to add columns to the master page you must be careful because the letters are defined in the INDEX function. So to add columns, you should put them at the right in an additional column.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-5.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-2.png)

Once you have the row number in the template model defined using the MATCH function, you can find any of the data that you will need.  To do this, you can use the INDEX function with an entire column where you define the entire column.  Then you refer to the row number defined from the MATCH function in the INDEX function (the old INDEX/MATCH).  In the first example in the screenshot below, the row number of 8 is defined from the match function.  Then you can find the start date of the project from column D in the master page.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-1.png)

![](https://edbodmer.com/wp-content/uploads/2018/11/spv-3.png)

After creating the template file, you can create inputs for a lot of different projects.  Each of the projects is defined by a name that becomes the sheet name.  You can then run or create a macro to copy the template sheet to another sheet. Once you have a lot of templates, you can consolidate the templates into a consolidation.  The consolidation uses the INDIRECT function to gather data from the different files. A few screenshots may give you an idea of how the file to consolidate different SPV’s works.  The first picture is intended to give you an idea of how the final consolidated process works.  This consolidation works by using the INDIRECT function to add together cash flows and balances from individual sheets. The second screenshot below shows how you can use the INDIRECT function. The INDIRECT function looks painful, but you can get the hang of it quickly.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-4-1.png)

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

This is an analysis where multiple SPV’s are consolidated into a portfolio. A major innovation in the analysis is use of a flexible template for the SPV that includes currency risks and different types of financing. A macro copies that SPV to multiple different sheets. The INDIRECT function along with MATCH and INDEX are used to consolidate the SPV’s and analyse the results.

### 

The third set of screenshots demonstrate the outputs of individual SPV’s that are eventually rolled-up into the consolidated analysis.  This depends on the financing structure of at the SPV and whether debt is issued on a project basis. The graphs show how debt service is paid at the individual SPV and how the individual SPV receives cash flow from the solar project in different scenario cases.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-3.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-2.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-6.jpg)

Problem of Interest During Construction and Circularity in Real Estate Models
-----------------------------------------------------------------------------

Interest during construction must be allocated to different projcects.  To do this you need to keep track of the amount of plant in service and the construction work in progress.

.

.

The following files are associated with the videos that explain the probelms with interest during construction and circularity.

PDF Model of Mixed Development that You Can Covert and Evaluated
----------------------------------------------------------------

This model is in a pdf file that demonstrates that type of issues that you may face in constructing a mixed use model of commercial, residential and maybe even industrial.  I will eventually replicate this model with an excel file.  If this is very interesting to you please send me an e-mail at edwardbodmer@gmail.com.

Files on Resource Library Not Yet Uploaded
------------------------------------------

Other files that I have not yet put on this website are show below. You can find these files in the resource library by e-mailing me at edwardbodmer@gmail.com. They are in the Real Estate Folder of Chapter 1.  I will try to get these uploaded soon.

*   Portfolio of Small Developments.xlsm
*   Mixed Use Analysis.xlsm
*   Mixed Use and Residential Model with Financing.xlsm

*   IDC and Circularity with Real Estate.xlsm
*   IDC and Circularity with Real Estate – Function.xlsm
*   IDC and Circularity with Real Estate – Copy and Paste.xlsm
*   Mixed Use Analysis.xlsm

*   Comprehensive Real Estate Exercise.xlsm
*   Mixed Use and Residential Model with Financing.xlsm
*   Exercise 6 – Mixed Development.xls
*   Exercise 7 – Portfolio Data Table.xls
*   Exercise 11 – Comprehensive Mixed Use Exercise.xls
*   Exercise 1 – Simple Portfolio.xls
*   Exercise 3 – Investment Portfolio.xls

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3237&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9596&rand=0.29319508486925616)