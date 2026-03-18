# Implementing the Parallel Model

**Source:** https://edbodmer.com/technical-details-of-udf-parallel-model-concept

---

This page describes practical issues in implementing the parallel model into your model in a simple and quick manner. I use an example where you want to put the parallel model into your model to resolve issues associated with interest during construction for multiple debt issues. Further, you want to be able to do this in a few minutes. This is a real example, where I made a model for somebody who does not what to touch any buttons and wants to do scenario analysis with spinner buttons and maybe even some data tables. I show you how you can take the parallel model from another file and use a button to copy it into your file. Then you can find about twenty or so inputs from your model to attach to the parallel model — like EBITDA, Capital Expenditures, interest rates and repayments. With these inputs from your model that may take a few minutes to connect, you can retrieve the items that are causing circular references.

Hedieh and I have structured the parallel model so that it is like open source programming where you can add your own modifications and you may even hopefully share your work. The idea is to create a model that parallels your model so that you can avoid copy and paste routines and so you can work in complex things like multiple sculpting issues with curved DSCR’s that meet a minimum requirement. The of philosophy our structure is to give you a template that has a whole bunch of the calculations and formulas. But there is no doubt that you may want to add something or adjust something. For example, you may want to change the way VAT refunds are assumed. If you understand some of the key items you can then implement the concepts using the more comprehensive template model. On this page we begin by illustrating a couple of very simple case. The different examples illustrate how you can read in variables; make some arithmetic calculations to mimic the circular reference calculations; and output the results back to excel.

.

**[Template UDF Parrallel Model that You Can Put Directly in Your Model By Pressing Button and then Following Instructions](https://edbodmer.com/wp-content/uploads/2024/01/Updated-Template.xlsm)
**

.

**[Excel File with Simple Financial Model that you can Use to Work Through the Process of Incorporating the Parallel Model](https://edbodmer.com/wp-content/uploads/2021/09/Simple-Model.xlsm)
**

.

Step 1: Copying the Parallel Model from Another File to Your Model
------------------------------------------------------------------

The first step of the process is to start with a model that contains the parallel model. Then, you go to the page that I call UDFOutputs (you can change the sheet name if you want) and then press the button at the top left of the page. One of the options on the red buttons is to copy the code and UDF sheets to a new file. When you press the button, make sure your new sheet name is the target as illustrated in the screenshots below. In the first screenshot, you can see the grey button behind the screen form. The button is called “Parallel Model Forms”. After you press the grey button you will see the menu with the red buttons. When you press the red button, you will see the second screen shot.

.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-2048x1207.png)

.

Note that sometimes when you go to the UDFOutput you may get NAME’s. In this case try to select the area and then press SHIFT, CNTL, ENTER the way you would resolve a TRANSPOSE function. Make sure you begin in column B.

.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-2-2048x1224.png)

.

After you have read pressed the red button, modules for the UDF programs will be added. You should be able to then begin attaching data from your model to the UDFInputs page. When copying the data you should not use something like onedrive and you make need to change the VBA security to “trust access to VBA project object model.”

.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-11.png)

.

Step 2: Filling in Data for UDFInputs
-------------------------------------

After you have copied the UDFInputs and the UDFOutput is in your sheet, you can begin linking the data. Note that you can use the SHIFT, CNTL, R or your other methods of copying to the right. There are a couple of things that may require explanation. First, use 1’s and 0’s for the flags and not TRUE/FALSE. Second, the depreciation should be without IDC and Fees because depreciation on IDC and Fees are part of the circular reference calculation. Some of the inputs like the DSCR or the switch for the debt sizing option can be entered directly without linking. Note that when you get to the debt issues, you can copy issue number 1 to issue number 4 etc. When you do this, make sure and change the numbers at the back of the variables that are shown in the example below and in this file are in column E. For example, change tenor1 to tenor4 in the block that you have copied. In the example below, I have used the generic macros and for the link to other sheets, I reverse the colours so that you can clearly see where the numbers come from. The green numbers come from the input sheets and the numbers with the blue background come from the calculation sheet — mostly the the financing calculations.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-4-2048x904.png)

.

The net screenshot shows the bottom part of the UDFInputs. In this part you can put in the DSRA inputs and the inputs for how many iterations you want. Depending on the size of your model, if you have re-run the parallel model every time you change items, you may want to turn off the parallel model. You can do a few things to avoid the model slowing you down. The first is to not print out the outputs. The second is to use the turn off switch. The third is to make the number of iterations only one or two.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-5-2048x1036.png)

.

Step 3: Running the Parallel Model without Connecting the Parallel Model to your Model
--------------------------------------------------------------------------------------

Once you have input the numbers, you can check the output page. Please try to remember that the output page takes the inputs from the UDFInputs and runs the program. There is so far no effect on your model.

Adding Debt Facilities to the Parallel Model
--------------------------------------------

You easily add debt facilities to the parallel model. All you do is copy from the block from the prior model and then change the numbers in the variable names. This process is illustrated in the screenshot below. In this case I copied the debt facility number 3 to number 4.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-10.png)

.

### Start with Report, then Construct Inputs and then Equations

Make separate modules with reports and equations.

### Reading, Arithmetic and Writing

Any program that you write whether in Excel, C++, Fortran, VBA or Python has inputs, some kind of process and outputs. In working with Hedieh we have recognized that being really flexible with reading and writing are essential. In terms of the Arithmetic, the idea is to just copy what you are doing in excel.

![](https://edbodmer.com/wp-content/uploads/2020/07/image-74.png)

### Simple Parallel Model Case

### Reading and Writing Variables

I work through a simple example with fees in project finance or interest expense in corporate finance. In these examples, I show how you should read in the variables. This is fine for small applications.

The UDF must read a lot of variables and write out the variables in an efficient manner. Excel has a limit of reading \_\_\_\_ characters into the UDF. If you have a complex circular reference problem, there will be two problems

Note in the example below that the read\_data is not defined as a particular type of an array.

Function UDF\_test(read\_data)

Column\_test = read\_data.Columns.Count
`For i = 1 To Column_test` 
   `read_data_test(i) = read_data(i)` 
`Next i`
UDF\_output\_test

UDF\_test = output\_test
End Function

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=10951&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11672&rand=0.17699465591640973)