# VBA Blogs: Total Eclipse of the Heart

**Source:** https://sumproduct.com/blog/vba-blogs-total-eclipse-of-the-heart/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Total Eclipse of the Heart

*   January 4, 2018

VBA Blogs: Total Eclipse of the Heart
=====================================

VBA Blogs: Total Eclipse of the Heart
=====================================

5 January 2018

The seventh in a series about using ListObjects to manipulate Tables within an Excel workbook in VBA featuring the Totals Row.

“It’s a Heartache” when a table doesn’t have a totals row. Let’s look at the following table:

![](https://sumproduct.com/wp-content/uploads/2025/05/c49e23a2ef1e5c3354bbb9c126dfe54f.jpg)

“Loving You’s a Dirty Job” but displaying the Totals Row of a table is not. The Totals Row is easily found in the Table Menu here (or **Ctrl + Shift + T** for you keyboard shortcut enthusiasts):

![](https://sumproduct.com/wp-content/uploads/2025/05/6b53b045535ced008e15c01ac2de5848.jpg)

However, how can we do this in VBA? It is simply the _ShowTotals_ property of the _ListObject_. This is a Boolean setting, if it is _TRUE_ then the Total Row is displayed (and switch it off by setting it to _FALSE_).

![](https://sumproduct.com/wp-content/uploads/2025/05/06bd1139d1cf748d161e961295b8e215.jpg)

“Faster Than the Speed of Night” the Totals Row appears

![](https://sumproduct.com/wp-content/uploads/2025/05/8e9cccc2142cdad687bd5380a51462e4.jpg)

Notice how that it has put a formula in the last column which is the default setting of showing the totals row.

\=SUBTOTAL(103,\[Album Length\])

“The Reason Why?” Excel makes a rough judgement about which of the **SUBTOTAL** functions it would like to use and in this case has chosen 103 – **COUNT**. “It’s a Heartache” sometimes because it doesn’t always use the right one.

To edit the Totals Row, one could very easily edit it by using the _TotalsRowRange_ property of _ListObject_. Let’s delete the word “Total” in the row.

![](https://sumproduct.com/wp-content/uploads/2025/05/3641765bdfd71f28b3b9238cf1173fac.jpg)

And it comes out like this as expected:

![](https://sumproduct.com/wp-content/uploads/2025/05/ce5ad5101652171c400ebe6e54aea9b0.jpg)

But “I’m A Fool” if this is all one wanted to do with a table. One would want to populate the Totals Row with calculations. This is done using the _ListColumns_ method of _ListObject_. Though _ListColumns_ hasn’t been covered in detail previous articles, let’s “Take A Chance” and muddle through the syntax. Columns in a table can be referred to by the ListColumns property by using the index or by the header. Then we use the TotalsCalculation method to change the calculation in the row. The following calculations may be used:

| Subtotal Number | Excel Function | Function | VBA Syntax |
| --- | --- | --- | --- |
| 101 | AVERAGE | Average | xlTotalsCalculationAverage |
| 102 | COUNTA | Count Numbers | xlTotalsCalculationCountNums |
| 103 | COUNT | Count | xlTotalsCalculationCount |
| 104 | MAX | Max | xlTotalsCalculationMax |
| 105 | MIN | Min | xlTotalsCalculationMin |
| 106 | PRODUCT | Product |     |
| 107 | STDEV.S/STDEV | Standard Deviation Sample | xlTotalsCalculationStdDev |
| 108 | STDEV.P | Standard Deviation Population |     |
| 109 | SUM | Sum | xlTotalsCalculationSum |
| 110 | VAR | Variance | xlTotalsCalculationVar |

With enough info, “My Guns Are Loaded” so let’s give it a go.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Notice that **SUBTOTAL** functions 106 and 108 are not available in the VBA Syntax. “Save Up All Your Tears”, presumably this is because these are not often used. However, there are two further TotalsCalculations that are available: _xlTotalsCalculationNone_ which is identical to clearing the cell and _xlTotalsCalculationCustom_ which doesn’t do much at all.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

_xlTotalsCalculationCustom_ just puts a =0 in the formula which is not very helpful.

But what if for example one wanted to calculate the average song length? Let’s use an Array Formula using the **AVERAGE** function as follows:

{=AVERAGE(Table\_BTDisco\[Album Length\]/Table\_BTDisco\[Number Of Songs\])}

So how could this be achieved?

The _TotalsRowRange_ could be used as above, but _ListColumns_ also has a method _Total_ which allows access to the Totals Range for that particular column. Let’s use ArrayFormula to put the formula in the **\[Album Length\]** column and change the number format to show minutes and seconds.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

“Bye Bye Now My Sweet Love”, next week will be a closer examination of _ListColumns_.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-total-eclipse-of-the-heart/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-total-eclipse-of-the-heart/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-total-eclipse-of-the-heart/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-total-eclipse-of-the-heart/#0)

[](https://sumproduct.com/blog/vba-blogs-total-eclipse-of-the-heart/#0 "close")

top