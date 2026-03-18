# PMT Varying Rates

**Source:** https://edbodmer.com/repayment-function-varying-rates

---

This page demonstrates how to use and create a repayment function in a case where interest rates or discount rates change over time. The PMT or the PPMT functions are extremely useful for a variety of financing issues, but they do not work when the interest varies from period to period.  With the user-defined varying repayment function, you can enter a series of interest rates and a debt tenure and the function produces the repayment percent. To simply enter a function on a the debt tenure and a series of cash flows and find the repayment percent. You use the function =repayment\_varying\_rate(tenure, interest rate series, optional debt repayment flag).  This function is an array function meaning that you have to paint the area where the repayment percent will go.  Technical details below demonstrate how to create the UDF function with VBA code by computing the remaining tenure and the remaining cash flow and then evaluating the PMT for a loan of 1.0.

**[Excel File with Code for Function to Compute Debt Repayment Using Annuity when the Interest Rate Changes over Time](https://edbodmer.com/wp-content/uploads/2019/08/PMT-with-Changing-Interest-Rates.xlsm)
**

Using the Repayment with Varying Interest Rates UDF
---------------------------------------------------

Once you have imported the repayment with varying interest rates UDF function, you can use the =repayment\_varying\_rate(tenure, interest rate series, optional debt repayment flag) function  as shown in the screenshot below. In the example, I have made a simple debt balance and a debt tenure of 20 years.  The example shows that you can click on the entire line to get the repayment percent (the final screenshot). The screenshot below is an illustration of the most basic case for the repayment function.  There is no debt repayment flag and the interest rate is select rather than the whole line.  Don’t forget to press SHIFT, CNTL, ENTER after you have copied the function to the entire row.  (You can copy the function first, then press F2, and then press SHIFT, CNTL, ENTER).

![](https://edbodmer.com/wp-content/uploads/2019/08/Repayment-Selected-Cells-and-No-Flag.jpg)

The screenshot below illustrates use of the function when the option flag is not used.  This illustrates that you do not have to use the optional flag and you can use the entire line.

![](https://edbodmer.com/wp-content/uploads/2019/08/Repayment-Entire-Row-and-No-Flag.jpg)

The final screenshot shows the case where the entire line for the interest rate and the entire line for the flag is read in.  This is by far the most useful case for real models.

![](https://edbodmer.com/wp-content/uploads/2019/08/Repayment-with-Entire-Row-Interest-Rate-and-Flag.jpg)
---------------------------------------------------------------------------------------------------------

Inserting the Varying Repayment Function into a Your Workbook
-------------------------------------------------------------

You can get the function into your workbook using a couple of different methods. The easiest way is to use the generic-macros file. In this file press CNTL, ALT, C first and you should see the menu below. After you get this menu, press the top purple button that is titled “Import Functions”

![](https://edbodmer.com/wp-content/uploads/2021/02/image-3.png)

After you press this menu, you will get something like the menu below. On this menu, find the button for flexible payment and the function will be copied into your model. You should make sure the target model is your model. You can use the dropdown box to find your file. The whole process should take seconds.

![](https://edbodmer.com/wp-content/uploads/2021/02/image-4.png)

After you open the file that is available for download above you can do a few things to get the function into your sheet.  One is to press the button that will produce a user form.  Then, in the text that comes up, just select the VBA code and copy it to your sheet (as shown in the screenshot below the file).  Alternatively, you can press the ALT and F8 key sequence, edit the VBA code, press CNTL, C and then copy it to your file.

![](https://edbodmer.com/wp-content/uploads/2019/08/Get-the-Function.jpg)

Once you have copied the VBA code (either from the userform, from pressing ALT, F8 and copying the entire sheet or from copying the code below), you can copy it into your file.  To do this, you can press ALT, F8 to get the VBA screen.  Then put in any name (e.g. Stormy).  Then go to the top of the file and copy the code (CNTL, V).  Some of this is demonstrated in the couple of  screenshots below.  The first screen shot illustrates how to create a new VBA page after you press ALT, F8; the second shows how you should insert a line to put the code at the top of the page; the third shows the results after you copy.

![](https://edbodmer.com/wp-content/uploads/2018/05/Payback-3.jpg)

After making the new page with you blank macro named Stormy, go above the new macro and enter a couple of blank lines.  When you have entered the blank lines you will press the CNTL, V and copy the code to the top of the page.

![](https://edbodmer.com/wp-content/uploads/2018/05/payback-4.jpg)

After you have copied the code into your sheet, you should see OPTION BASE 1 at the top of the page.  Now you are ready to go and the function should work in your workbook.

![](https://edbodmer.com/wp-content/uploads/2018/05/payback-5.jpg)

Creating the Function for Annuity Repayment with Changing Interest Rates
------------------------------------------------------------------------

The user defined function for creating a varying repayment is presented below.  You can see the adjustment required so that an entire row can be used and you can see how the loop works with counting the number of cash flows.

.

Option Base 1
Sub repayment\_function()
End Sub

' Note: it is important to have the option base 1 at the top if you are using this function

Function repayment\_varying\_rate(tenure, int\_rate, Optional flag) As Variant

Dim output(1, 1000) As Double
Dim int\_rate\_term(1000) As Double
Dim flag\_term(1000) As Single

no\_flag = False ' Test for missing variable

If IsMissing(flag) Then no\_flag = True

max\_num = int\_rate.Count 
' Find the total number of items in the interest rate

' This is to adjust for when you use the entire array
' The term term means that the computation is made over the repayment term

Count = 0
For i = 1 To max\_num

If WorksheetFunction.IsNumber(int\_rate(i)) Then 
' Start when the interest rate is a number
Count = Count + 1

int\_rate\_term(Count) = int\_rate(i) 
' Define new variable that does not have extra stuff before or after the time period in question and so you can input the entire line

If no\_flag = False Then flag\_term(Count) = flag(i)
If no\_flag = True Then flag\_term(Count) = 1
End If
Next i

total\_num = Count ' Total number to work through
remaining\_balance = 1 ' Starting value that will decline
remaining\_tenure = tenure ' Starting value that will decline

For year1 = 1 To total\_num
repayment = 0

If flag\_term(year1) = 1 Then ' Begin the calculations when the flag is 1
If remaining\_tenure = 0 Then Exit For ' Go around the whole interest rate array. When goes negative exit function
interest = remaining\_balance \* int\_rate\_term(year1) ' This is interest on the opening balance
total\_payment = WorksheetFunction.Pmt(int\_rate\_term(year1), remaining\_tenure, -remaining\_balance)
repayment = total\_payment - interest
remaining\_balance = remaining\_balance - repayment
remaining\_tenure = remaining\_tenure - 1
End If
output(1, year1) = repayment
Next year1

repayment\_varying\_rate = output

End Function



.

The function below is very similar, but it includes discounting the cash flow. This discounting can be

.

Video Describing How to Create Repayment Function with Varying Interest Rates
-----------------------------------------------------------------------------

If all of the above explanation does not do enough, then you can watch a video on how to create a payback function.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8941&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13624&rand=0.15673455859802266)