# A to Z of Excel Functions: The RANDARRAY function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-randarray-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The RANDARRAY function

*   June 9, 2024

A to Z of Excel Functions: The RANDARRAY function
=================================================

A to Z of Excel Functions: The RANDARRAY function
=================================================

10 June 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **RANDARRAY** function._

**The RANDARRAY function**

**RANDARRAY** was one of seven functions heralding the new dawn of arrays – the Dynamic Array.

Before explaining **RANDARRAY**, let’s first consider what a Dynamic Array is. Consider the following data:

![](https://sumproduct.com/wp-content/uploads/2025/05/2ed14e5b42663e0d6a3fe62e3ead95cc-1.jpg)

If I were to type **\=F12:H27** into another cell, Excel in the past would have thought I had gone mad.  I’d need to wrap it in an aggregation function such as **SUM**, **COUNT** or **MAX**, to name but a few.  Otherwise, I would have to wrap it in braces using **CTRL + SHIFT + ENTER** and use it as an array formula.

But no more.

Look at what happens when I type **\=F12:H27** into cell **F33**:

![](https://sumproduct.com/wp-content/uploads/2025/05/899025fd7849f1fc151bde2d5087e9ff-1.jpg)

The formula _automatically extends_ to three columns by 16 rows!  It has _spilled_.  Get used to the vernacular.

Any formula that has the potential to return multiple results can be referred to as a **Dynamic Array** formula.  Formulae that are currently returning multiple results, and are successfully spilling, can be referred to as **Spilled Array Formulae**.

Notice I did not have to highlight all of the cells **F33:H48**.  It _spilled_.  Also take note I formatted cell **F33** – er, that didn’t spill, because presently formatting isn’t propagated.  But don’t let that put you off.

And don’t let this basic example put you off either.  If you feel a general sense of underwhelm coming over you, it’s because I haven’t yet communicated how powerful this all is as my example was too basic.

However, before I carry on there is a question I do need to cover with my far too simple example: what happens if something gets in the way?

![](<Base64-Image-Removed>)

In this example, in cell **G40**, I have typed in the obtrusive text, “I’m in the way”.  And it quite literally is.  Consequently, I have generated the brand new _#SPILL!_ error.  The formula cannot spill, so the error message is generated accordingly.

**_#SPILL! Errors_**

_#SPILL!_ errors are returned when a formula returns multiple results, and Excel cannot return the results to the spreadsheet.  There are various reasons an _#SPILL!_ error could occur:

*   **spill range is not blank:** as in my example _(above)_, this error occurs when one or more cells in the designated spill range are not blank and thus may not be populated.

![](<Base64-Image-Removed>)

When the formula is selected, a dashed border will indicate the intended spill range.

You may select the error “floatie” (believe it or not, this is what Microsoft call these things!), and choose the ‘Select Obstructing Cell’ option to immediately go the obstructing cell.

You can then clear the error by either deleting or moving the obstructing cell’s entry.  As soon as the obstruction is cleared, the array formula will spill as intended

*   **the range is volatile in size:** this means the size is not “set” and can vary.  Excel was unable to determine the size of the spilled array because it’s volatile and resizes between calculation passes.  For example, the new function **SEQUENCE(x)** generates a list of **x** numbers increasing by 1 from 1 to **x**.  That’s fine, but the following formula will trigger this _#SPILL!_ error:

> **\=SEQUENCE(RANDBETWEEN(1,1000))**

Dynamic array resizes may trigger additional calculation passes to ensure the spreadsheet is fully calculated.

If the size of the array continues to change during these additional passes and does not stabilise, Excel will resolve the dynamic array as _#SPILL!_

This error type is generally associated with the use of **RAND**, **RANDARRAY** and **RANDBETWEEN** functions.

Other volatile functions such as **OFFSET**, **INDIRECT** and **TODAY** do not return different values on every calculation pass so tend not to generate this error

*   **extends beyond the worksheet’s edge:** in this situation, the spilled array formula you are attempting to enter will extend beyond the worksheet’s range.  You should try again with a smaller range or array.  For example, moving the following formula to cell **A1** will resolve the error, and the formula will spill correctly

![](<Base64-Image-Removed>)

*   **Table formula:** as I will explain shortly, Tables and Dynamic Arrays are not yet best friends.  Spilled array formulae aren’t supported in Excel Tables (generated by **CTRL + T**).  Try moving your formula out of the Table, or go to **Table Tools -> Convert to range**

![](<Base64-Image-Removed>)

*   **out of memory:** I have forgotten what this one means.  Sorry, I couldn’t resist that.  The spilled array formula you are attempting to enter has caused Excel to run out of memory.  You should try referencing a smaller array or range
*   **spill into merged cells:** spilled array formulae cannot spill into merged cells.  You will need to un-merge the cells in question or else move the formula to another range that doesn’t intersect with merged cells.

![](<Base64-Image-Removed>)

*   When the formula is selected, a dashed border will indicate the intended spill range.  You can again select that wonderfully named error floatie and choose the ‘Select Obstructing Cell’ option to immediately go the obstructing cell.  As soon as the merged cells are cleared, the array formula will spill as intended
*   **unrecognised / fallback error:** the “catch all” variant.  Excel doesn’t recognise, or cannot reconcile, the cause of this error.  Here, you should make sure your formula contains all of the required arguments for your scenario.

**_Returning to Dynamic Arrays_**

Now that we have considered what happens if you block a Dynamic Array, let me now turn my attention to what happens if you _don’t_.  You get the following:

![](<Base64-Image-Removed>)

Do you see I am not having to anchor cells (_i.e._ use dollar \[**$**\] signs)?  The formula just _spills_.  Let me be clear. If I select cell **F34**, I get the following:

![](<Base64-Image-Removed>)

Here’s a first.  Check out the formula in the formula bar.  It’s _greyed out_.  Ever seen that before?  Effectively, cell **F34** contains the value ‘Triangle’ but it does not actually contain an “Excel” formula in the usual sense.  To demonstrate this, let me show you the VBA Immediate Window:

![](<Base64-Image-Removed>)

If you select cells **F33:H48** and use ‘Go To Special’ (**F5 -> Special**), and then select ‘Formulas’, cells **F33:H48** are shown as formula cells.  You can even copy and paste them as values.  Ladies and gentlemen, welcome to this brave new world.

Once you have a Dynamic Array, referring to it is simple using what is known as the **Spilled Range Operator**.  For example, if I want to refer to the following Dynamic Array that refers to a table:

![](<Base64-Image-Removed>)

Initially this had a range of **L57:N72**.  However, once I had added a row and column to the Table, this resized to **L57:O73**.  I can easily refer to this array, whatever its size as follows:

![](<Base64-Image-Removed>)

The formula **\=L57#** allows for variations – you simply type in the top left-hand cell reference (_i.e._ the cell with the non-greyed out formula) and add ‘**#**“, known as the Spilled Range Operator.  Simple!

**_RANDARRAY Function_**

And so, to the function **RANDARRAY**.  The **RANDARRAY** function returns an array of random numbers between 0 and 1.  It’s not clear from Microsoft, but it’s my belief this is analogous to the pre-existing **RAND** function, which generates a number greater than or equal to zero and strictly less than one.  It is noted though that **RANDARRAY** is different from the **RAND** function insofar that **RAND** does not return an array.

The function has the following syntax:

> **\=RANDARRAY(\[rows\], \[columns\], \[min\], \[max\], \[integer\])**

The function has five arguments, all supposedly optional:

*   **rows:** this specifies how many **rows** the results should spill over. If omitted, the default value is 1
*   **columns:** this specifies how many **columns** the results should spill over. If omitted, the default value is also 1
*   **min:** this is the minimum value that may be selected randomly. If this is not specified, it is assumed to be zero (0)
*   **max:** this is the maximum value that may be selected randomly. If this is not specified, it is assumed to be 1
*   **integer:** if this is set to TRUE, only integer outputs are allowed; the default value (FALSE) provides non-integer (decimal) results.

It should be noted that:

*   if **rows** or **columns** refers to a blank cell reference, this will generate the new _#CALC!_ error
*   if **rows** or **columns** are entered as decimals, the values used will be truncated to the number before the decimal point (_g._ 3.9999999 will be treated as 3)
*   if **rows** or **columns** is a value less than 1, _#CALC!_ will be returned
*   if **integer** is set to TRUE and either **min** or **max** is not an integer, this will generate an _#VALUE!_ error
*   **max** must be greater than or equal to **min**, else the error _#VALUE!_ is returned.

Again, I’ll start with a basic demonstration:

![](<Base64-Image-Removed>)

This can be useful for generating “seed” values for simulations analysis, for example.  Anecdotal evidence suggests using **RANDARRAY** in a simulations formula rather than using a macro or Data Table may generate calculation speed efficiencies of greater than 50%.  The jury is still out on this one – but it’s definitely worth exploring.

 Previously, **RANDARRAY** only had two arguments, **rows** and **columns**.  This meant that if you wanted some sort of **RANDBETWEENARRAY** function you needed to construct it yourself:

![](<Base64-Image-Removed>)

Here, in cell **F44**, I have used the formula

**\=ROUNDDOWN(RANDARRAY(H36,H37)\*(H39-H38+1),0)+INT(H38)**

to generate my equivalent **RANDBETWEEN** function. Since **RANDARRAY** generates a random number greater than or equal to zero and strictly less than one, **ROUNDDOWN(RANDARRAY(H36,H37)\*(H39-H38+1),0)** generates a random integer (all equally likely) between zero and nine (this is 9, because the number generated is a whole number greater than or equal to zero but strictly less than 10 \[10 – 1 + 1\]).  Since this is added to 1 (**INT(H38)**), the random whole number will be an integer between 1 and 10.  Simple, if you have a Maths PhD.

However, with the addition of the final 3 arguments, this is much easier now:

![](<Base64-Image-Removed>)

The “new improved” formula in cell **F45** (it’s moved down a row due to the additional argument required in cell **H40**) is simply

> **\=RANDARRAY(H36,H37,H38,H39,H40)**

For a final example, imagine you are a schoolteacher and you have 10 five-year-old children:

![](<Base64-Image-Removed>)

For each of the next 10 weeks, you have topics you want one of them to present on:

![](<Base64-Image-Removed>)

I can use **RANDARRAY** in tandem with **SORTBY** to determine a presentation order for the term:

![](<Base64-Image-Removed>)

Oh dear.  I do hope Diana has prepared well or it could all end in tears.  She could try swapping with Horace, I suppose.  On a serious note, the formula

> **\=SORTBY(F63:F72,RANDARRAY(COUNTA(F63:F72)))**

sorts the ‘Child’ order randomly (and a similar formula is used for ‘Topic’ too).  In a past life, as an independent expert, I once had to attest that drug testing was being performed entirely randomly, _i.e._ free from any material bias. **SORTBY(RANDARRAY)** dries up that well for me once and for all.

**_Dynamic Arrays vs. Legacy Array Formulae_**

Finally, prior to this new functionality, if you wanted to work with ranges in Excel, you used to have to build array formulae, where references would refer to ranges and be entered as **CTRL + SHIFT + ENTER** formulae.  The main differences are as follows:

*   Dynamic Array formulae may spill outside the cell bounds where the formula is entered. The Dynamic Array formula technically only exists in the cell in the top left-hand corner of the spilled range _(as shown earlier)_, whereas with a legacy **CTRL + SHIFT + ENTER** formula, the formula would need to be entered in the entire range
*   Dynamic arrays will automatically resize as data is added or removed from the source range. **CTRL + SHIFT + ENTER** array formulae will truncate the return area if it’s too small, or return _#N/A_ errors if too large
*   Dynamic array formulae will calculate in a 1 x 1 context
*   Any new formulae that return more than one result will automatically spill. There’s simply no need to press **CTRL + SHIFT + ENTER**
*   According to Microsoft, **CTRL + SHIFT + ENTER** array formulae are only retained for backwards compatibility reasons.  Going forward, you should use Dynamic Array formulae instead
*   Dynamic array formulae may be easily modified by changing the source cell, whereas **CTRL + SHIFT + ENTER** array formulae require that the entire range be edited simultaneously
*   Column and row insertion / deletion is prohibited in an active **CRL + SHIFT + ENTER** array formula range.  You first need to delete any existing array formulas that are in the way.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._ _A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-randarray-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-randarray-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-randarray-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-randarray-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-randarray-function/#0 "close")

top