# Operating Tax, Depreciation and Currency Adjustments

**Source:** https://edbodmer.com/operating-tax-and-depreciation

---

This page demonstrates how to deal with taxes and depreciation in a project finance model and how to compute project cash flow after tax and project IRR after tax. An important complication when dealing with depreciation and taxes is where the taxes are computed in a different currency than in the main currency of the model. When there is a different currency, you also have to compute a currency translation adjustment when you put your balance sheet together.  The currency adjustments are discussed at the bottom of this page. In a model, whether an agriculture model, a model of a toilet paper factory in Jamica, a model of an airport or an electricity project, do not start with any thing that has money (Euro, USD, CFA etc.) Instead, start with the capacity and volumes and what the machine or the project is really doing.  This is the subject of the second part of the course. [In this section the INTERPOLATE UDF function](https://edbodmer.com/interpolate-lookup-function/)
 is introduced to illustrate how to make volumes, capacity factor or other items gradually increase or decrease (a simple way to interpolate is not in excel).  You can download a file with the interpolate function below so that you can add the function to any of your models and do interpolate really fast.

[Download Excel File with the Function for Interpolation Using Either Compound Growth or Linear Interpolation](https://edbodmer.com/wp-content/uploads/2019/04/Lookup-and-Interpolate.xlsm)

Problems with not using lookup or interpolate\_lookup are illustrated in the screenshot below.  In this case somebody thought they were really cool by using MATCH and INDEX together.  But this just creates a long mess.  It is much better to use the LOOKUP function with an entire line.

![](https://edbodmer.com/wp-content/uploads/2019/02/A-Z-Not-Using-Lookup.png)

Pre-Tax Operating Cash Flow and Pre-tax IRR
-------------------------------------------

The third part of the course begins with some equations that involve money.  In any project from a PPP for a University, a toll road, a co-generation plant or any electricity project, you should start with EBITDA and Capital Expenditures (and, maybe working capital).  These items define the pre-tax project IRR of the project.  With the pre-tax project IRR you have the essential information on the project.  In this page I use the IRR even though I believe there are a number of problems with the IRR.  To see a discussion of problems with the IRR you can go to my separate page that deals with the subject.

Depreciation and Taxes to Compute Project IRR After Tax
-------------------------------------------------------

The second set of videos complete the model with no debt and begin adding debt to the models. The last video in this section begins to add a circular resolution template to the model. This is an important idea in project finance where you would like to maintain flexibility in the face of natural circular references.

In adding on-going depreciation on future capital expenditures, I have included a function that enables you to select the entire line of future capital expenditures and remaining lives.  With these data items and the lifetime of the equipment, you can derive the depreciation on future capital expenditures.  The future depreciation is either from standard depreciation if the lifetime is greater than the remaining life.  Alternatively it is computed from the remaining life when the remaining life is less than the asset life.  A file that contains the function is available for download by pressing the button below (note that you have to press Shift, CNTL, Enter instead of enter and you cannot use the entire line).  The file also contains a function that is more flexible and will simulate variable declining balance depreciation.

**[Spreadsheet that Includes Functions for Computing Depreciation on Future Capital Expenditures (Use ALT F8 to Transfer)](https://edbodmer.com/wp-content/uploads/2018/05/Depreciation-2.jpg)
**

The screenshots below illustrate how to use the function with straight line depreciation.  The first screen shot demonstrates how to function works in the case where the remaining life is greater than the asset life and the asset can be fully depreciated over the remaining life. In this case, the capital expenditure occurs in year 20 and the remaining life is 34 years. Note that two capital expenditures are entered and the depreciation stabalises at a level of 150.  After the first asset is retired in period 24, the depreciation will fall to 100. The second screen shot shows the case where the remaining life is less than the asset life. In this case the depreciation is computed over the remaining life of the asset.  The inputs for this function include the remaining life, the capital expenditure array and the asset life as shown in both screen shots.

![](https://edbodmer.com/wp-content/uploads/2018/06/Depreciation-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/06/Depreciation-2.jpg)

The video below works through various depreciation and issues related to future capital expenditures and explains why the problem of future capital expenditures and depreciation would be very messy without a function.  You would have to make one of those diagonal matrices and adjust for situations where the depreciation would expend beyond the life of the project.

.

.

The VBA code for the depreciation function is available for download below. Because this is a function, you must copy the code into your model rather than simply having the file with the VBA code open (with regular old macros you can do this). You can get this function with the VBA code into your project finance model in three different ways:

1.  The first way is to open the file above and press ALT, F8.  Then edit the VBA page with the subroutine named A\_Depreciation\_functions.  Copy the entire contents.  After that, go to your sheet and press ALT, F8 again.  Then create a blank VBA subroutine and copy the contents above that routine.
2.  The second way is to copy the function that is on the form that appears when you open the file.  You just copy the code, go to your sheet, press ALT, F8, create a dummy macro and paste.
3.  The third method is similar to above, but you just copy the code from below.

Option Base 1

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''' Depreciation Functions
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Sub A\_Depreciation\_Functions()

End Sub
Function depreciation\_remaining\_life\_2(capital\_expenditure, remaining\_life, max\_life) As Variant ' When the output is an array define as Variant

cap\_exp\_periods = capital\_expenditure.Count ' See how many capital expenditure periods are modelled

Dim Depreciation\_Expense(5000) As Single ' Make a new array variable that is the output
Dim remaining\_life1(5000) As Single

' Determine whether to use remaining life or something shorter

For vintage = 1 To cap\_exp\_periods ' make a second loop to evaluate asset by asset
  If remaining\_life(vintage) >= max\_life Then
  remaining\_life1(vintage) = max\_life
Else
  remaining\_life1(vintage) = remaining\_life(vintage)
End If

Next vintage

For model\_year = 1 To cap\_exp\_periods ' loop around each period and make a square with columns and rows

  For vintage = 1 To cap\_exp\_periods ' make a second loop to evaluate asset by asset

    age = model\_year - vintage + 1 ' calculate the age of each expenditure (the diagonal)

    If (age > 0 And remaining\_life1(vintage) <> 0 And remaining\_life1(vintage) >= age) Then ' Only when asset is alive

      Depreciation\_Expense(model\_year) = \_
      capital\_expenditure(vintage) / remaining\_life1(vintage) + Depreciation\_Expense(model\_year)
    End If

  Next vintage ' Note that the vintage is used for the capital expenditure

Next model\_year

depreciation\_remaining\_life\_2 = Depreciation\_Expense

End Function

.

Balance Sheet and Verification before Financing
-----------------------------------------------

The balance sheet is a good (but not perfect) way to check your model.  A few years ago a student in my class told me that he puts a balance sheet into the model very early on in the process. At first I did not see the value in this. With complex models and solving circular references I think that suggestion was exactly on the mark.  So much so that I put a test right at the top of the model and believe the saying on the t-shirt below from my friend Hedieh (you can order this t-shirt or a mug if you want. Just send an e-mail to edwardbodmer@gmail.com).

![](https://edbodmer.com/wp-content/uploads/2018/06/1.-Balance-Sheet-t-shirt.jpg)

You can put the balance sheet into the model after you have modelled the depreciation expense.  The balance sheet should just collect closing balances from other sections of the model. The video below describes the process of balancing the balance sheet before any debt had been put into the model.

This page includes an exercise where you build the financing part of a project finance model (i.e. starting with EBITDA) and then moves to the issue of resolving circular references. The first part of this page provides instructions on how to build the financing part of a model with flexible construction financing (pro-rata or equity first), sculpting of debt and a funded DSRA account.  The exercise includes an associated video that explains how to work through debt sizing, repayment, interest and the DSRA from a file that includes blank titles. I use this exercise as a pre-course assignment in project courses that are advanced where I deal with nuanced issues of debt sizing, debt funding, debt repayment, debt cost of capital and debt protections.  In these courses I don’t want to take time building an A-Z model and participants can assure themselves that they have the fundamental modelling skills. As this exercise includes circular references for IDC, DSRA and sculpting with taxes, a demonstration of how to implement the parallel model concept and resolve circular references is included. In order to focus on the tricky project finance issues, the exercise is for a case with a single debt issue in the context of an annual model. For the pre-course eercise, you should only focus on the first part of this page.

Currency Adjustment and Depreciation and Different Currencies
-------------------------------------------------------------

Many times the financing and pricing of your project will be in Euro or USD, but the project is located in a country and pays taxes based on the local currency. In these cases the tax should reflect the exchange rate and you need to make translation adjustments to get the balance sheet correct. 

The first point is that all of the cash flow items including capital expenditures, revenues and operating expenses in local currency.  These items will be used for computing local taxes.

When you compute the asset balance in the major currency (e.g. GBP, WON, Euro, USD), the net asset value declines because of the currency adjustment.  Here are a couple of things I try to remember:

1.  When you compute asset value, you need a currency adjustment in the balance sheet of the major currency and this adjustment decreases the asset value because of the depreciation (that is, assuming that the local currency has more depreciation). 
2.  When you compute the debt value in local currency you will also have an adjustment. This time you need to pay less amount in the main currency with devaluation.

The adjustment is required on assets because the depreciation in local currency converted back to the main currency will not fully depreciate the asset. Instead, you must then put in a loss to get the whole asset depreciated.

When making exchange rate adjustments, instead of using a percent change with this period currency/last period currency – 1, you go the other way.  You use the the formula:

Adjustment factor = 1- exchange rate prior period/exchange rate this period

as shown in the screenshot below and also use the opening balance of a debt account or an asset account, the exchange rate adjustments will make the balance come to zero at the end of an asset life.  This is illustrated below.

![](https://edbodmer.com/wp-content/uploads/2019/07/Exchange-Rate-and-Debt.jpg)

The screenshot below illustrates computation of the depreciation in local currency that will be driven by the cost of the project in local currency and by the exchange rate.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-1.png)

Economic Depreciation: Who Cares about Book Depreciation in Project Finance
---------------------------------------------------------------------------

I notice that the depreciation is overly complex in many models.  One problem is why even bother with book depreciation in project finance models.

![](https://edbodmer.com/wp-content/uploads/2019/07/Who-cares-about-book-depreciation.jpg)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8372&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13772&rand=0.9829471467075513)