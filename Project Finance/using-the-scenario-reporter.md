# Scenario Reporter

**Source:** https://edbodmer.com/using-the-scenario-reporter

---

This webpage explains how to use the scenario reporter that allows you to very quickly make a scenario analysis with any model in excel.  You use a file that can be downloaded below which is flexible to use whereby you can fix mistakes and change formats. The scenario reporter associated with the file allows you to record multiple scenarios in a sheet in an automatic fashion. It also allows you to modify the scenarios and to start over with a new set of scenarios.  The scenario reporter uses a little VBA code which adds copies and pastes variables that you want to present. To use the scenario reporter you do not need to know any VBA; all you need to do is to open the file below and add a sheet to your model (you copy the sheet from the file into your file).  This web page explains how to do this in a step-by-step fashion. (Apparently my friend Hedieh uses this even though I did not use it much for a while).

First, lets look at what we are trying to do.  The screenshot below shows the results of the scenario analysis. The list of scenarios was created by pressing the copy scenario button and changing various different factors.

![](https://edbodmer.com/wp-content/uploads/2018/06/Micro-Grid-Scenario-Cases.jpg)

Implementing the Scenario Reporter in Your File – Simple Method
---------------------------------------------------------------

To implement the scenario reporter, you first open the file available for download below. This file must be open for the scenario page to run in a similar manner as the generic macro file must be open to run macros like the copy to right and colour formatting macro.

**[Scenario Reporter File - With this File, you Open the File, then Copy the Scenario Sheet to Your File and Use the Buttons](https://edbodmer.com/wp-content/uploads/2019/04/Scenario-Reporter.xlsm)
**

When you open the file, the file should look like the first screenshot below.  The first thing to do is to copy the sheet named Scenario Output to your file. You can do this by using the ALT, E, M short-cut sequence with the copy box checked as illustrated on the second screenshot below.  Make sure that the create copy box is checked (I made the mistake of not checking the copy box in a class and was embarassed). After pressing the short-cut sequence, use the drop-down to select your file and choose where you want to put the sheet.  Note, do not change the sheet name (Scenario Output).

![](https://edbodmer.com/wp-content/uploads/2018/11/Scenario-1.png)

![](https://edbodmer.com/wp-content/uploads/2018/11/Scenario-2.png)

Once you copy the sheet into your file, you can format the scenario page and link variables from anywhere in your workbook to the scenario sheet.  This means that you should change the titles in row 11 of the screenshot above and then link the variables that you want to present. You do not enter anything in the columns with the scenario number and the scenario name (you will enter this yourself). The screenshot below illustrates the process of linking variables and changing the look of the scenario page.

![](https://edbodmer.com/wp-content/uploads/2018/06/Linking-in-Scenario-Sheet.jpg)

After you link the variables, you can copy the macro button title “Copy Scenario” to other pages of your sheet such as the summary page. Then you can run the macro and make a list of scenarios after you change different inputs. The screenshot below illustrates how you can create the scenarios. After you run the macro, it will take you back to the scenario page and you can start the process again for another scenario.

![](https://edbodmer.com/wp-content/uploads/2018/11/Scenarios-Copy-Scenario-Box.png)

![](https://edbodmer.com/wp-content/uploads/2018/06/Copy-Scenario.jpg)

When entering new scenarios, you enter the name and then press ok as shown in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/11/Scenario-3.png)

If you have made a scenario and then realise that you did not want the scenario in the report, you can just press enter.  This time the scenario will not be copied but the prior scenario will not be deleted.

![](https://edbodmer.com/wp-content/uploads/2018/11/Scenario-5.png)

The next  screenshot shows an important part of the scenario reporter.  When you press an x or an X, the prior scenario is deleted. Note that you want to delete the prior few scenarios, you can repeat the process where you press x and then copy the scenario and then press x again.

![](https://edbodmer.com/wp-content/uploads/2018/11/Scenario-4.png)

The problem with this file is that you create an external link because of the attachment of the macro to the copy scenario and the other buttons.  This is illustrated in the screenshot below.  To get this screen press ALT, E, K (an old short-cut that works in English).

![](https://edbodmer.com/wp-content/uploads/2018/11/Scenario-6.png)

Video Explanation of Scenario Reporter
--------------------------------------

The video below provides and example of a finished file. Other exercises walk through how to start with a simple example and ultimately make a very flexible analysis and a nice summary page.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=4288&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12988&rand=0.5789740548141605)