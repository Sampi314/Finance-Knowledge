# Monday Morning Mulling: July 2022 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-july-2022-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: July 2022 Challenge

*   July 31, 2022

Monday Morning Mulling: July 2022 Challenge
===========================================

Monday Morning Mulling: July 2022 Challenge
===========================================

1 August 2022

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The challenge this month was to combine multiple rows by a key column. How did you do?

**_The Challenge_**

This month, we had the following problem. There was a table with multiple rows of transactions under the same invoices. Our goal was to group rows so that those with the same Invoice ID would be on the same line, and column ‘Invoice ID’ would only show a unique list of invoices.

This issue may be common for anyone who wants to remove duplicates on a key column while still keeping specific data from others. You can download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/july/fff/sp-combine-rows---challenge.xlsx)
.

This month’s challenge was to combine rows of the provided table by column ‘**Invoice ID**‘. The result should look like the table generated at the bottom of the picture below:

![](<Base64-Image-Removed>)

Below were some conditions

*   ‘**Invoice ID**‘ and ‘**Make**‘ columns only show up once within that invoice group
*   ‘**Transaction ID**‘ and ‘**Description**‘ columns combine all data on the same line with a delimiter (_e.g._ “, “)
*   ‘**Transaction Date**‘ column lists the latest transaction date of each invoice
*   ‘**Plate**‘ column ignores the blanks and shows only the last item within that group
*   ‘**Amount**‘ column calculates sum of the amount of each invoice.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/july/mmm/sp-combine-rows---suggested-solution.xlsx)
 which demonstrates our suggested solution.

There are several ways to accomplish this goal. You may choose either [Excel formulae](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
, [Power Query](https://www.sumproduct.com/thought/power-query-blog-series)
 or [DAX measures](https://www.sumproduct.com/thought/a-to-z-of-dax-functions)
 with a Pivot Table.

In our solution, we use Power Query which we think is the quickest way to solve it. Additionally, it is more dynamic than traditional Excel formulae. We start by extracting the table into Power Query / Get & Transform, using ‘From Table / Range’ in the ‘Get & Transform Data’ section of the Data tab.

![](<Base64-Image-Removed>)

Before continuing to the next step, we want to remove the unnecessary time component of ‘**Transaction Date**‘ using ‘date’ datatype and convert ‘**Transaction ID**‘ into ‘text’ under the same ‘Changed Type’ step.

![](<Base64-Image-Removed>)

Next, we are going to combine rows using the ‘Group By’ option on the Transform tab. We want to group by ‘**Invoice ID**‘. To begin with, we use the ‘Advanced’ option:

![](<Base64-Image-Removed>)

We add more aggregations for all grouped columns, but all the operations are aimed at numerical values. We are going to go ahead and apply a **Max** operation to ‘Transaction Date’ column and a **Sum**operation to the rest, and then amend the **M** code produced.

![](<Base64-Image-Removed>)

This gives us an error, which is not surprising since we are adding up text values!

![](<Base64-Image-Removed>)

Having a look at the **M** code on the Formula bar, Power Query is currently using **List.Sum()** to add up text columns:

**\=  
Table.Group(#”Changed Type”, {“Invoice ID”},**

**{{“Transaction  
ID”, each List.Sum(\[Transaction ID\]), type nullable text},**

**{“Transaction  
Date”, each List.Max(\[Transaction Date\]), type nullable date},**

**{“Make”,  
each List.Sum(\[Make\]), type nullable text},**

**{“Plate”,  
each List.Sum(\[Plate\]), type nullable text},**

**{“Amount”,  
each List.Sum(\[Amount\]), type nullable number},**

**{“Description”,  
each List.Sum(\[Description\]), type nullable text}})**

We need a text function **Text.Combine()** instead to compile a list of text values, separated by a separator of our choice. We have chosen to separate ‘**Transaction ID**‘ and **Description** with a comma and a space “, “.

*   ‘**Transaction ID**‘:

**{“Transaction  
ID”, each Text.Combine(\[Transaction ID\],”, “), type text }**

*   **Description**:

**{“Description”,  
each Text.Combine(\[Description\],”, “), type text }**

![](<Base64-Image-Removed>)

Then, we use **List.Distinct(){0}** to get the distinct value of the **Make** column,

**{“Make”, each  
List.Distinct(\[Make\]){0}, type text}**

and **List.LastN(){0}** as below to get the last item on the **Plate** column.

**{“Plate”,  
each List.LastN(\[Plate\],1){0}, type nullable text}**

The number zero \[0\] in the code above is to get the first item value from the **List** functions. The full step now looks like this:

![](<Base64-Image-Removed>)

**\=  
Table.Group(#”Changed Type”, {“Invoice ID”},**

**{{“Transaction  
ID”, each Text.Combine(\[Transaction ID\],”, “), type text},**

**{“Transaction  
Date”, each List.Max(\[Transaction Date\]), type date},**

**{“Make”, each  
List.Distinct(\[Make\]){0}, type text},**

**{“Plate”,  
each List.LastN(\[Plate\],1){0}, type nullable text},**

**{“Amount”,  
each List.Sum(\[Amount\]), type number},**

**{“Description”,  
each Text.Combine(\[Description\],”, “), type text}})**

Simple!

_The Final Friday Fix will return on Friday 26 August 2022 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-july-2022-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-july-2022-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-july-2022-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-july-2022-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-july-2022-challenge/#0 "close")

top