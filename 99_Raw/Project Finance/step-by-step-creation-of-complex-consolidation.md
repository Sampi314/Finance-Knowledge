# Step by Step Creation of Complex Consolidation

**Source:** https://edbodmer.com/step-by-step-creation-of-complex-consolidation

---

This page walks through how to create a consolidated model from a file that has input sheets primarily driven by InputS sheets and the existing model for a single case has multiple model pages. This is somewhat more complex than most of the other examples.

.

**[Conslidation Model with Example of Consolidating Different Corporate Models into Industry with INDIRECT](https://edbodmer.com/wp-content/uploads/2024/07/Consolidation-Example-Companies-in-Industry.xlsm)
**

.

**[Conslidation Model with Example of Combining Projects that Have Different Input Structures with INDIRECT](https://edbodmer.com/wp-content/uploads/2024/07/Monthly-Hydrogen-with-UDF-V2.xlsm)
**

.

Step 1: Consolidate Model into One Sheet
----------------------------------------

Begin by going to your existing models and assure that the you can combine the different sheets into one sheet and maintain the same results. Do things like:

*   Insert columns so that the time line starts at the same column for each sheet that will be consolidated
*   Put some summary statistics at the top of the page of the template model to make sure that you have not changed something fundamental in the model (things like equity IRR)
*   Watch for cirular references that are created by the combining different sheets
*   If it takes a long time to combine sheets do not worry.
*   Cut excess rows and columns from the sheet (after you delete the rows and columns, save the file with CNTL S

*   .

![](https://edbodmer.com/wp-content/uploads/2024/05/image-4.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-5.png)

.

.

Step 2: Make Sure the Inputs All Come from an Input Sheet that is Referred to at the Top of the Sheet
-----------------------------------------------------------------------------------------------------

.

You will want to make different input sheets using the INDIRECT function – there will be many different input sheets unlike the method where all data is included in one sheet and you can use the INDEX function efficiently. If you combine the input sheet into one sheet you can then make a macro that reads different input sheets with different names and then copy different output sheets with the same initial name as the input sheet. You will want to define an input sheet name at the top of the model and then be able to change the input sheet name so that you can copy the model to multiple different sheets. The way I suggest to do this at the writing of this webpage is to replace all links to the model sheet using the INDIRECT function. The screenshot below illustrates the idea of putting the input sheet name at the top of the model sheet. In the screenshot, the yellow cell with the name “Model Inputs” will be changed. The LOOKUP function shown in the screenshot will be changed to include the INDIRECT function that will allow the inputs to come from different sheets. I know this will slow down the model somewhat, but unless you have a really big model, this should not be a really big issue.

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-6.png)

.

Use the generic macro to hilight any number that comes from the input sheet. Before you do that, remove links to the same sheet.

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-7.png)

.

Start with ‘Model Inputs’

Replace with INDIRECT(“‘”&INPUT\_SHEET&”‘”)

Version up means that you save as a new name and then you can go back to your prior versions.

In order to make the process work for more complex situations where you have to read from different input files, it is difficult to change all of the references from the original source to the same source that contains the INDIRECT function.  I have spent a couple of days creating a macro that automatically does this.  To do this please understand that the following does not work and you make an error. You could try to change everything to string formulas with a ‘ but this also causes problems. As you may have to do the conversion a lot, I thought a macro would be best. You can try something like this in the model template file, but it will not work.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-8.png)

To run the replacement macro, you should find the macro button as shown below. It is important to have a range named defined that will be used to replace the existing sheet. An example of this is shown below this paragraph. I have re-set all of the colours so you can better see what is happening. Once you have run the macro, there should be no direct reference to the input file. Instead, all of the references to the input file should use the INDIRECT function. When you are finished, you should be able to change the input file (in cell C2) and you should see completely different inputs.

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-9.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-10.png)

.

.

After you have run the macro you should see a lot of INDIRECT functions wherever there was reference directly to the input file. In the screenshot below I show how the lookup functions are changed to an equation that looks a lot more complicated, but just creates the same old lookup function were the sheet name is replaced to a formula using the input sheet that is defined in C2 with the name INPUT\_SHEET.

The next sheet shows that same conversion, but with an input that refers to a single cell of the input sheet (i.e. without the lookup function).  You can see that this time the original sheet name named ‘Model Sheet’ was replaced by the INDIRECT function that refers to the range name INPUT\_SHEET and the remainder of the of the sheet is the same.

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-13.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-11.png)

.

Once you understand the idea of what the macro is supposed to do, you can look at how I have done this.  An excerpt from the macro is shown in the screenshot below.

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-12.png)

![](https://edbodmer.com/wp-content/uploads/2024/05/image-14.png)

**Section 3: Putting Models Together with Simple VBA**
------------------------------------------------------

In this case with input files that have different time series arranged inputs, I suggest making an Input Start and an Input End Page.  In the example below I have copied the base input sheet to four different sheets with different names (Existing company and then Existing company with competition, New Company etc.)  This is illustrated in the screenshot below with the sheet names.

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-15.png)

The list of companies in the example above is made by simply copying the input page and naming new pages.  The idea is that you can choose to add companies together or alternatively select different consolidation strategies with different combinations of companies. I have made a page with the different macros shown above. The macro to create the list of companies is shown below.

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-16.png)

.

Once you have the list of companies, you can copy the template model file to a new sheet and change the location of the input file at the top of the model template every time that you make a new sheet with a new model. This is created with a macro that runs through each company name and uses the TRUE/FALSE switch in the menu sheet. The screenshot below illustrates where the input sheet name is defined.

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-17.png)

.

The screenshot below shows the macro to create new sheets with new models. Note how the template model is copied and then the range name INPUT\_SHEET is changed. The first part of the macro shows how you can collect the company names and the switches to include or not include the different companies or projects that will be consolidated.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-18.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/05/image-19.png)

.

Step 3:
-------

.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=17478&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.5239166636673545)