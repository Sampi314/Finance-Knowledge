# Charts and Dashboards: Data Tables – Part 4

**Source:** https://sumproduct.com/blog/charts-and-dashboards-data-tables-part-4/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Data Tables – Part 4

*   June 16, 2022

Charts and Dashboards: Data Tables – Part 4
===========================================

Charts and Dashboards: Data Tables – Part 4
===========================================

17 June 2022

_Welcome back to our Charts and Dashboards blog series. This week, we’re going to cover why Data Table inputs should always be hard coded._

Using formulae for inputs in either the first row or column of a Data Table can be problematic. Let me explain why, by considering the following example:

![](<Base64-Image-Removed>)

To be fair, this spreadsheet is arguably too simple to create a Data Table output, but it can be used to highlight the dangers of using formulae for inputs. In this example, all cells in yellow are inputs. The calculation in cell **H15** is very simple: **\=H12\*H13**. But that’s not the point here.

Cell **H20** contains “On”, which is used for the formula in cell **H22**:

\=IF(H20=”On”,H15,)

that is, the formula refers to the Total Revenue in cell **H15** if the value in cell **H20** is “On”. The reason this cell appears to be a heading that says “Total Revenue” is we have used the number formatting (**Ctrl + 1**) trick (covered in [Charts & Dashboards: Data Tables – Part 2](https://sumproduct.com/blog/charts-and-dashboards-data-tables-part-2/)
) again:

![](<Base64-Image-Removed>)

The Number formatting is Custom and has the type

“Total Revenue”;”Total Revenue”

“Total Revenue”;”Total Revenue” This means that if the value is a non-negative number (that is, a zero or a positive number), the value will appear as “Total Revenue” (the text before the delimiting semi-colon), and if it is negative it will also appear as “Total Revenue” (the text after the semi-colon).

After the required input values (100 to 110 inclusive, as displayed) have been hard coded into cells **G23:G33**, the range **G22:H33** has been selected, and then a Data Table has been created by selecting ‘Data Table…’ from the ‘What-If Analysis’ drop-down in the Forecast group of the Data tab of the Ribbon:

![](<Base64-Image-Removed>)

Since the inputs go down a column and the input cell is in cell **H12**, the resulting ‘Data Table’ dialog has been populated thus:

![](<Base64-Image-Removed>)

Assuming workbook calculations are set to Automatic (**Alt + T + O**), that’s all you have to do – simple!

So, what’s the problem? Consider this revised example:

![](<Base64-Image-Removed>)

Here, the columnar inputs (cells **G53:G63**) have been replaced by a formula:

\=IF(G52=””,$H$42,G52+1)

This seems to be fairly innocuous and theoretically, should make the worksheet more efficient as inputs do not need to be typed in twice. However, look closer. The values in cells **H55:H63** are _wrong_. This is a common trap. It’s dangerous using formulaic inputs in a Data Table.

So what went wrong?

A 1-dimensional columnar Data Table works procedurally as follows:

1.  Take the first input and put it in the input cell (so here, the value in cell **G53** – 100 presently – would be copied as a value into cell **H42**)
2.  This would cause the values in the formulaic inputs to update (so cells **G53:G63** would be updated to \[still\] display 100, 101, …, 109, 110)
3.  The result (cell **H45**, $100,000) would be recorded in the first row of outputs (cell **H53**)
4.  The second input – currently 101 (cell **G54**) – would then be pasted as a value into the input cell (cell **H42**)
5.  This would cause the values in the formulaic inputs to update (so cells **G53:G63** would be updated to now display 101, 102, …, 110, 111 – these values have changed)
6.  The result (cell **H45**, $101,000) would be recorded in the second row of outputs (cell **H54**) (this is why this output remains correct)
7.  The third input – now revised to 103, not 102 (cell **G55**) – would then be pasted as a value into the input cell (cell **H42**)
8.  This would cause the values in the formulaic inputs to update (so cells **G53:G63** would be updated to now display 103, 104, …, 112, 113 – these values have changed)
9.  The result (cell **H45**, $103,000, being $103 multiplied by 1,000) would be recorded in the third row of outputs (cell **H55**) (this is why this output is incorrect)
10.  The fourth input – now revised to 106, not 103 (cell **G56**) – would then be pasted as a value into the input cell (cell **H42**)
11.  This would cause the values in the formulaic inputs to update (so cells **G53:G63** would be updated to now display 106, 107, …, 115, 116 – these values have changed)
12.  The result (cell **H45**, $106,000, being $106 multiplied by 1,000) would be recorded in the fourth row of outputs (cell **H56**) (this is why this output is also incorrect)
13.  And so on…
14.  When all outputs have been determined, the Data Table input values (cells **G53:G63**) are then reset to the original values (100 to 110 inclusive).

Explained like this, it’s easy to see the problem. If cell **G53** had been left as a hard-coded value, or linked to an independent cell elsewhere, this would not have happened. However, people don’t get this, and the internet is littered with end users moaning that their Data Tables are wrong and Excel makes errors. It doesn’t; people do. Be careful; use inputs!

That’s it for this week. Come back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-data-tables-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-data-tables-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-data-tables-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-data-tables-part-4/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-data-tables-part-4/#0 "close")

top