# Power Query: Calendar Creation – Preparing for Dates

**Source:** https://sumproduct.com/blog/power-query-calendar-creation-preparing-for-dates/

---

[Home](https://sumproduct.com/)

\> Power Query: Calendar Creation – Preparing for Dates

*   April 11, 2017

Power Query: Calendar Creation – Preparing for Dates
====================================================

Power Query: Calendar Creation – Preparing for Dates
====================================================

12 April 2017

_Welcome to our Power Query blog. Having explored some Power Query functions and M language, I will combine some of these techniques in order to create a calendar – today I set up the tools I will need to create my calendar, and next time I will populate it._

Building a calendar using Power Query is a collaboration between Excel and Power Query. In my example, I will implement four steps:

1.  Create a table called **_Parameters_** in an Excel Worksheet to hold the calendar boundaries
2.  Create a function **fnGetParameter** which uses the calendar boundaries as its parameters (I can take no credit for this – it is the creation of Ken Puls, author of _‘M is for (DATA) Monkey_‘)
3.  Build the basic dynamic calendar framework
4.  Add any required calendar columns.

Today I will concentrate on the first two steps – creating the tools I need to populate my calendar.

**_Creating Parameters_**

In a new blank Excel Worksheet, I create a new table with some specific properties. My table is called **_Parameters_** and has two columns, **_Parameter_** and **_Value_**.

To begin, I will open a new blank Excel worksheet – in the ‘Insert’ Section, there is an option to ‘Insert Table’ which brings up a ‘Create Table’ dialogue box. I choose an area that covers two columns and three rows (I chose **A7:B9** in the example shown below). I check the box ‘My Table has Headers’ and click OK.

![](<Base64-Image-Removed>)

Just as an aside, normally here at SumProduct, we will advocate always starting Tables in cell **A1** and calling the worksheet the same name as the Table. I am not going to do that here to show it is not necessary, but there is merit in doing this if data is exported to other programs too. It’s best to give data exporting a “helping hand” on occasion.

Returning to my example, the ‘Table Name’ can be changed in the top left of the screen and must be set to **_Parameters_**. Clicking on the column names allows me to set them to **_Parameter_** and **_Value_** as shown below.

![](<Base64-Image-Removed>)

The parameters the function will be using are **_Start Date_** and **_End Date_**, and these are the entries in my first column. In the second column I enter the date I wish my calendar to begin at, and a formula that will show the last day of the current month.

**Parameter       Value**

**Start Date       1/1/2016**

**End Date         =EOMONTH(TODAY(),0)**

This may look like a long number to begin with – the data format on the column needs to be set to **Short Date** as shown below:

![](<Base64-Image-Removed>)

My Parameter table is now ready for the **fnGetParameter** function:

![](<Base64-Image-Removed>)

**_Create the fnGetParameter function_**

In the Power Query menus, I choose to create a new blank query by going to the ‘From Other Sources’ section and choosing ‘Blank Query’ from the dropdown:

![](<Base64-Image-Removed>)

In the ‘Query Editor’ screen I choose the ‘Advanced Editor’ from the ‘Home’ tab.

I enter the following **M** language:

**(ParameterName as text) =>**

 **let**

**ParamSource = Excel.CurrentWorkbook(){\[Name=”Parameters”\]}\[Content\],**

**ParamRow = Table.SelectRows(ParamSource, each (\[Parameter\]=ParameterName)),**

            **Value=**

            **if Table.IsEmpty(ParamRow)=true**

                        **then null**

                        **else Record.Field(ParamRow{0},”Value”)**

**in**

    **Value**

I then rename the query **fnGetParameter.**

When I choose to ‘Close and Load’ from the ‘Home’ tab the new query automatically saves as connection only in the workbook pane:

![](<Base64-Image-Removed>)

Now I have my parameters and a function which will read them, so that next time I may create my calendar framework and add columns to create a useful calendar.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-calendar-creation-preparing-for-dates/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-calendar-creation-preparing-for-dates/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-calendar-creation-preparing-for-dates/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-calendar-creation-preparing-for-dates/#0)

[](https://sumproduct.com/blog/power-query-calendar-creation-preparing-for-dates/#0 "close")

top