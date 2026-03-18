# Looking Up to LOOKUP

**Source:** https://sumproduct.com/thought/looking-up-to-lookup/

---

[Home](https://sumproduct.com/)

\> Looking Up to LOOKUP

*   May 14, 2025

Looking Up to LOOKUP
====================

Looking for a useful function to replace VLOOKUP?.

Looking Up to LOOKUP
====================

_Liam Bastick highlights some of the more useful functions for financial modelling / Excel spreadsheeting. Having driven a bus through the flaws with VLOOKUP and HLOOKUP, he now explains why LOOKUP is actually quite useful for modelling._

### A Useful Function

IF you’ve read a lot of the Thought articles, you will know that I took **VLOOKUP** and **HLOOKUP** to task recently, identifying potential pitfalls in these two lookup functions. Conspicuous by its absence, **LOOKUP** may seem a less versatile function upon first glance, but it is quite useful for modelling. Allow me to explain.

**LOOKUP** has two forms: an **array** form and a **vector** form. I suppose I had better explain the jargon:

*   An **array** is a collection of cells consisting of at least two rows and at least two columns
*   A **vector** is a collection of cells across just one row (row vector) or down just one column (column vector).

The diagram should be self-explanatory:

![](https://sumproduct.com/wp-content/uploads/2025/05/8026c91d7d9479476237e229050a76c3.jpg)

The array form of **LOOKUP** looks in the first row or column of an array for the specified value and returns a value from the same position in the last row or column of the same array:

LOOKUP(lookup\_value,array)

where:

*   **lookup\_value** is the value that **LOOKUP** searches for in an array. The **lookup\_value** argument can be a number, text, a logical value, or a name or reference that refers to a value
*   **array** is the range of cells that contains text, numbers, or logical values that you want to compare with **lookup\_value**.

The array form of **LOOKUP** is very similar to the **HLOOKUP** and **VLOOKUP** functions. The difference is that **HLOOKUP** searches for the value of **lookup\_value** in the first row, **VLOOKUP** searches in the first column, and **LOOKUP** searches according to the dimensions of array.

If **array** covers an area that is wider than it is tall (_i.e._ it has more columns than rows), **LOOKUP** searches for the value of **lookup\_value** in the first row and returns the result from the last row. Otherwise, **LOOKUP** searches for the value of **lookup\_value** in the first column and returns the result from the last column instead.

The alternative form is the vector form:

LOOKUP(lookup\_value,lookup\_vector,\[result\_vector\])

The **LOOKUP** function vector form syntax has the following arguments:

*   **lookup\_value** is the value that **LOOKUP** searches for in the first vector
*   **lookup\_vector** is the range that contains only one row or one column
*   **\[result\_vector\]** is optional – if ignored, **lookup\_vector** is used – this is the where the result will come from and must contain the same number of cells as the **lookup\_vector**.

Like the default versions of **HLOOKUP** and **VLOOKUP**, **lookup\_value** must be located in a range of strictly ascending values, i.e. where each value is larger than the one before and there are no duplicates.

So why do I advocate for **LOOKUP** when I said don’t use the other functions just recently? Well, it’s because it is simpler to use, doesn’t rely on row or index column numbers and allows modellers to create inputs that do not need to be specified for all periods modelled. Let me demonstrate with the following example (the full set of examples may be found in the attached [Excel file](https://sumproduct.com/assets/thought-files/looking-up-to-lookup/sp-lookup-example.xlsm)
):

![](<Base64-Image-Removed>)

Imagine you have an annual model forecasting for many years into the future. Creating inputs will be time consuming if data has to be entered on a period by period basis. But there is a shortcut.

Do you see the data table in cells **F12:K13** above? The value in the final cell of the first row is actually “2020” not “2020+”. It appears that way due to custom number formatting (**CTRL + 1**):

![](<Base64-Image-Removed>)

The syntax “0+” adds a plus sign to the number although Excel still reads the value as 2020.

The formula uses the array version of **LOOKUP**, looking up the year in the first row of the data tabe and returning the corresponding value from the final row. When a year is selected which is greater than 2020, the 2020 value is used as **LOOKUP** seeks out the largest value less than or equal to the value sought. Therefore, we don’t need to have lengthy data tables – once we assume inputs will be constant thereafter, we can just curtail the input section.

Using the array form of **LOOKUP** is dangerous though. What if someone accidentally inserts rows? The lookup will “flip” to look the first and last columns instead, which is not what is required. Using the vector form is safer:

![](<Base64-Image-Removed>)

Whilst the formula contains one more argument, the formula is more stable. Further, the **lookup\_vector** and the **result\_vector** do not need to be in the same worksheet or even the same workbook. In fact, as long as there are the same number of elements in each, one can be a row vector and the other a column vector.

**LOOKUP** is very useful when the **lookup\_vector** contains data in strict ascending order. Where do we find this? Dates in time series – **LOOKUP** is very useful for financial modelling / forecasting. Just be careful though; consider the following scenario:

![](<Base64-Image-Removed>)

Here, the same formula generates an #N/A error. This is because the date is smaller than the smallest value in the data range. **LOOKUP** is not quite clever enough t use the first value unprompted, but a simple tweak of the formula will suffice:

![](<Base64-Image-Removed>)

Here, the formula has been modified to:

\=IF(G$19<$G$12,$G$13,LOOKUP(G$19,$G$12:$K$12,$G$13:$K$13))

The added **IF** statement checks to see if the year is smaller than the first year in the data table and if so, returns the first result. Simple!

It is with this final modification – in its vector form – that I usually use **LOOKUP** to return values for certain time periods where I do not want to have an input for each period modelled. Very useful!

In case you missed it, the Excel file with the examples can be found [here](https://sumproduct.com/assets/thought-files/looking-up-to-lookup/sp-lookup-example.xlsm)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/looking-up-to-lookup/#0)
    
*   [Register](https://sumproduct.com/thought/looking-up-to-lookup/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/looking-up-to-lookup/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/looking-up-to-lookup/#0)

[](https://sumproduct.com/thought/looking-up-to-lookup/#0 "close")

top