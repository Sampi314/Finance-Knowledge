# Volatile Functions: Talk Dirty to Me

**Source:** https://sumproduct.com/thought/volatile-functions-talk-dirty-to-me/

---

[Home](https://sumproduct.com/)

\> Volatile Functions: Talk Dirty to Me

*   May 14, 2025

Volatile Functions: Talk Dirty to Me
====================================

Considering how volatile functions and actions may be slowing down your models unnecessarily.

Volatile Functions: Talk Dirty to Me
====================================

So you’ve developed your Excel spreadsheet and it’s going slower than a snail dragging a tortoise. How can you speed up the calculation time? This article considers the impact of volatile functions in Excel. By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

I have built a large Excel workbook which is taking a long time to calculate. I have larger spreadsheets that calculate much quicker. How can I speed my model up?

Advice
------

There is nothing worse than seeing “CALCULATE” appear in the bottom left-hand corner of your status bar and the calculation percentage status crawl towards 100% (and why does it always start again when it gets to 99%?). One of the worst things modellers can do to counteract this is to set Workbook Calculation to anything other than ‘Automatic’ (**ALT + T + O, Formulas**):

![](https://sumproduct.com/wp-content/uploads/2025/05/b00274cab3afac290ec03065f01d0e9c.jpg)

Calculation Options Should ALWAYS Be Set To Automatic

The reason for this is very simple. Although it allows modellers to continue spreadsheet construction unencumbered, when was the last time you recall ever checking that a model you received was calculating automatically? Everyone just assumes that this is the case and makes managerial decisions accordingly.

This action only addresses the symptom, not the cause.

### Dependency Trees

Obviously, size does have some impact upon calculation speed, but perhaps not as much as you might think. The Excel calculation engine is almost as lazy – sorry, I mean “efficient” – as me.

Rather than recalculate every cell every time any cell is changed, Excel determines which cells are affected by the latest change (known as “**dependent cells**“) and recalculates these dependents and then dependents of these dependents and so on. These long chains are known as **dependency trees**. Depending upon which version of Excel you are using, there may be a limit of how many dependency trees Excel can keep track of (65,536 prior to Excel 2007, with the number debated by experts thereafter) before Excel has to resort to a full (i.e. slower) calculation.

When cells are changed, Microsoft recognises the cells that need recalculating as a consequence. These cells are known as “**dirty**” cells.

Therefore, calculation time is a function of the number of dirty cells and the number of dependency trees, both affected and unaffected.

As a modeller, it is difficult to change the number of dirty cells that genuinely need to be recalculated, short of writing more complex formulae in fewer cells (this is one reason why ‘megaformulae’ often calculate more quickly, although this increases the risk of modelling errors, etc. instead).

However, modellers can do something about those functions and functionalities that Excel has potentially mistakenly considered to be dirty. More often than not, these instances are caused by **volatile functions** and / or **volatile actions**.

### Volatile Functions and Actions

A **volatile function** is one that causes recalculation of the formula in the cell where it resides every time Excel recalculates. This occurs regardless of whether precedent cells / calculations have changed, or whether the formula also contains non-volatile functions. One test to check whether your workbook is volatile is close a file after saving and see if Excel prompts you to save it a second time (this is an indicative test only).

Some functions are obviously volatile, e.g. **NOW()**, **RAND()**, **TODAY()** and perhaps slightly less obviously **CELL(“filename”)** (see [Automated File Names](https://www.sumproduct.com/thought/automated-file-names)
 for further information) (keeping track of whether the filename has changed).

Others are not so obvious. For example:

*   **INDIRECT** (see [Being Direct About INDIRECT](https://www.sumproduct.com/thought/being-direct-about-indirect)
     for further details) has an argument that is constructed out of text, e.g. **INDIRECT(“$A$1?)**. This might look like a cell reference, but it is not, and needs rebuilding each time; and
*   **OFFSET** (see [Onset of OFFSET](https://www.sumproduct.com/thought/onset-of-offset)
     for further information) takes numerical arguments, which point to a cell reference, but are still just numbers that need to be calculated each time.

Just because a function is volatile in one version of Excel does not mean it is volatile in all versions. Perhaps the best example of this is **INDEX** (see [\>INDEX MATCH](https://www.sumproduct.com/thought/index-match)
 for further details), which was volatile prior to Excel 97. Microsoft still states this function is volatile, but this does not appear to be the case except when used as the second part of a range reference, for example **$A$1:INDEX($A$2:A$10,4)**, will also cause the reference to be flagged as dirty when the workbook is opened only.

Another common ‘semi-volatile’ function is **SUMIF**, which has been so since Excel 2002. This function becomes volatile whenever the size of the first range argument is not the same as the second (**sum\_range**) argument, e.g. **SUMIF(A1:A4,1,B1)** is volatile whereas **SUMIF(A1:A4,1,B1:B4)** is not.

**IF** and **CHOOSE** do not calculate all arguments, but if any of the arguments are volatile – regardless of whether they are used – the formula is deemed to be volatile. Therefore, **IF(1>0,1,RAND())** is always volatile, even though the **value\_if\_false** argument will never be calculated. It is not quite as simple as this though. If the formula in cell **A1** is **\=NOW()** then this cell will be volatile, but **IF(1>0,1,A1)** will not be.

In essence, direct references or dependents of volatile functions will always be recalculated, whereas indirect ones will only recalculate when activated or in certain other functions that always calculate all arguments such as **AND** and **OR**.

One area that has caught me out on occasion is the use of using formulae in conditional formats (see [Conditional Formatting](https://www.sumproduct.com/thought/conditional-formatting)
 for further details). These are always volatile so that the formatting is displayed correctly – not just on calculating but when you change worksheet or scroll up, down, left or right even if the calculation mode is set to Manual!

**Volatile actions** are those that trigger recalculation. Microsoft has compiled a list of such actions:

*   **AutoFilter** – filtering data in a range will make any formulae in this range dirty
*   **CSV files** – opening a CSV file will trigger recalculation
*   **Double-clicking on row or column dividers** – Automatic resizing is a trigger when the model is set to calculate automatically (but not in Manual mode), but bizarrely, manually adjusting row heights or column widths is a non-volatile action
*   **Goal Seek** (see [Desperately Seeking Solver](https://www.sumproduct.com/thought/desperately-seeking-solver)
     for further details) – using this scenario analysis tool results in the model requiring recalculation not just once, but for every iteration (which could be a maximum of 32,767 times)
*   **Hiding / unhiding rows** – in Excel 2003 only (but hiding / unhiding columns is not a volatile action). Some think this is because the properties of **SUBTOTAL** (see [SUBTOTAL](https://www.sumproduct.com/thought/subtotal-function-and-functionality)
     for further details) changed in Excel 2003, but this does not explain why this non-volatile in subsequent versions of Excel
*   **Inserting, deleting or moving rows, columns or cells**
*   **Range names** (see [Naming Names](https://www.sumproduct.com/thought/names)
     for further details) – adding, editing or deleting a range name in any way will trigger a calculation event
*   **Worksheets** – deleting, renaming or moving a worksheet is a volatile action. Interestingly, adding a worksheet does not trigger recalculation (this may lead to summation inaccuracies though if formulae sum through sheets).

### Word to the Wise

In order to speed up Excel workbooks, modellers should plan to keep the number of volatile functions and range names to a manageable minimum. Where possible, consider using **INDEX** rather than **OFFSET**, specifying **SUMIF** correctly, etc.

Designing models efficiently so that formulae are copied as frequently as possible will reduce the number of dependency trees, again shortening the calculation time.

Furthermore, reducing the number of volatile actions will also reduce the number of trigger points. In particular, consider how much you really need to have conditional formatting in your models.

As always, efficient model construction is a delicate balancing act: transparency and versatility may sometimes need to be tempered by the need to have the model calculate before the Sun goes supernova. There is no hard and fast rule: it is a judgment call that gets better with (bitter?) experience.

If you have a query for this section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the website [www.sumproduct.com](https://www.sumproduct.com/)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/volatile-functions-talk-dirty-to-me/#0)
    
*   [Register](https://sumproduct.com/thought/volatile-functions-talk-dirty-to-me/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/volatile-functions-talk-dirty-to-me/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/volatile-functions-talk-dirty-to-me/#0)

[](https://sumproduct.com/thought/volatile-functions-talk-dirty-to-me/#0 "close")

top