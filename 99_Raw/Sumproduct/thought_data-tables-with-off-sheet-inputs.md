# Data Tables with Off-Sheet Inputs

**Source:** https://sumproduct.com/thought/data-tables-with-off-sheet-inputs/

---

[Home](https://sumproduct.com/)

\> Data Tables with Off-Sheet Inputs

*   May 14, 2025

Data Tables with Off-Sheet Inputs
=================================

How Data Tables can reference inputs on other worksheets.

Data Tables with Off-sheet Inputs
=================================

In this article we consider how to circumvent another Excel limitation, revisiting Data Tables. By Liam Bastick, Director (and Excel MVP) with SumProduct Pty Ltd.

Query
-----

I use Excel’s Data Table functionality regularly but would like to keep my Data Tables on different worksheets to the relevant inputs. Is this possible?

Advice
------

I have a saying that anything is possible in Excel. Maybe one day I may come unstuck, but today is not that day.

I have discussed Data Tables before (see [Being Sensitive with Data Tables](https://www.sumproduct.com/thought/data-tables)
 for more details).

In summary, Data Tables are ideal for executive summaries where you wish to show how changes in a particular input affect a key output. They can be:

*   **1-dimensional**, where data is displayed in either a horizontal or vertical table, with the various input values for one variable to be used in either the top row or first column respectively; or
*   **2-dimensional**, where input values for two variables are placed in the first row and first column (with the top left hand corner cell having the output defined).

For more details, please read the aforementioned article.

### The Problem

The issue is that Excel restricts where the referred inputs must be located, i.e. they must be positioned on the same page. If you try and reference cells on another worksheet, or become cunning and use range names which refer to cells on another worksheet (a useful workaround on many occasions), you will encounter the following error message:

![](<Base64-Image-Removed>)

Example Error Message

Most financial modellers will recall the mantra of keeping inputs separate from calculations separate from outputs. Data Tables force you to put outputs on the same worksheet as the inputs which can confuse end users and make it difficult to put all key outputs together.

So how can you get round this? My solution assumes you do not wish to hide Data Tables on the input sheet and then link them to another worksheet (this is cumbersome and can make the model less efficient).

### Suggested Solution

To make things more “difficult”, I will assume that you have already built your financial model and the Data Tables are to be incorporated as an afterthought. There could be two inputs to incorporate. I will explain how to create one of them (you then just follow the process twice).

Firstly, create a “dummy” input cell on the same worksheet as the Data Table. This needs to be protected such that data cannot be entered into this cell. I will assume that this cell is **W44** (say) on the **Sheet2** worksheet, i.e. the same sheet as the Data Table.

![](<Base64-Image-Removed>)

Set Up Dummy Input

Secondly, link the Data Table (**ALT + D + T**) to this dummy input (in the illustration here I assume that the Data Table is a 1-dimensional Data Table:

![](<Base64-Image-Removed>)

Create Data Table Link

Thirdly, let us assume you want actually want the Data Table to link to “Input 1? (cell **D4**) on **Sheet1**:

![](<Base64-Image-Removed>)

Intended Link

Fourthly, since we have already built the model this input will already be linked throughout the model. Since I do not wish to change all the dependent formulae, I first **cut** (NOT copy) the input into an adjacent cell:

![](<Base64-Image-Removed>)

Intended Link Moved Using CUT and Paste

Fifthly, a copy is pasted back into the original cell (here, this was cell **D4**):

![](<Base64-Image-Removed>)

Intended Link Copied Back

Finally, the value in cell **E4** is replaced with the following formula

\=IF(Sheet2!W44=””,D4,Sheet2!W44)

and then formatted / protected to ensure end users do not actually type into this cell:

![](<Base64-Image-Removed>)

Final Input Appearance (Formula Highlighted

The Data Table will now work. This is because:

*   The Data Table links directly to a cell on the same sheet as the Data Table, but indirectly to the input on the other worksheet;
*   Cell **E4** on **Sheet1** is now the cell that drives all calculations throughout the model, even though it appears to have been added; and
*   Cell **D4** on **Sheet1** still appears to be – and acts like – the original input it replaces.

The [attached Excel file](https://sumproduct.com/assets/user-upload/sp-data-table-examples-revisited.xls)
 provides an example based on the original illustrations used in the [Being Sensitive with Data Tables article](https://www.sumproduct.com/thought/data-tables)
.

### Word to the Wise

Data Tables can be really useful for executive summaries, but there are several drawbacks to consider.

Data Tables can slow down the file calculation time dramatically. For example, if you have just three 2-D Data Tables, each with ten inputs on each axis, the model calculation time could increase by a factor of up to 300 (= 3 x 10 x 10).

Microsoft has recognised this issue and allows you to change Excel’s Calculation option (found in **ALT + T + O**, under ‘Calculation’) to ‘Automatic except tables’. I strongly recommend you do not implement this option. End users tend to assume Excel is always calculating everything automatically and some do not know how to check / modify this functionality.

Instead, I would build in ‘On / Off’ switches next to the Data Tables themselves. These are transparent and intuitive and have the same effect (please review the [second attached Excel file](https://sumproduct.com/assets/user-upload/sp-data-table-examples.xls)
 for how to build in this optionality).

Also, this approach may not work where formulae dependent on the input cells selected use **OFFSET** (see [Onset of OFFSET](https://www.sumproduct.com/thought/onset-of-offset)
) or **INDIRECT** (see [Being Direct About INDIRECT](https://www.sumproduct.com/thought/being-direct-about-indirect)
). The technique can still be employed, but it may be safer not to cut and paste but add an input cell elsewhere instead.

If you have a query for this section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the website [www.sumproduct.com](https://www.sumproduct.com/)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/data-tables-with-off-sheet-inputs/#0)
    
*   [Register](https://sumproduct.com/thought/data-tables-with-off-sheet-inputs/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/data-tables-with-off-sheet-inputs/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/data-tables-with-off-sheet-inputs/#0)

[](https://sumproduct.com/thought/data-tables-with-off-sheet-inputs/#0 "close")

top