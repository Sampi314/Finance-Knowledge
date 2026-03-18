# Power Query: Heading Off – Part 7

**Source:** https://sumproduct.com/blog/power-query-heading-off-part-7/

---

[Home](https://sumproduct.com/)

\> Power Query: Heading Off – Part 7

*   March 26, 2024

Power Query: Heading Off – Part 7
=================================

Power Query: Heading Off – Part 7
=================================

27 March 2024

_Welcome to our Power Query blog. Today, I refine the solution to an issue that occurs when I load to a Table with no headers._

I plan to show a particular issue with Power Query and Tables without headers. However, first I need to create the scenario, and I will show a few methods and tips along the way. I have two Tables of data:

1.  contains my salespeople’s expenses (**Expenses**)
2.  determines the expenses that will be covered by each supplier (**Supplier\_Limit**).

![](https://sumproduct.com/wp-content/uploads/2025/05/ef269a5646089e1768b92c98624ba127-1.jpg)

In [Part 1](https://sumproduct.com/blog/power-query-heading-off-part-1/)
, I created two \[2\] queries, and grouped **Expenses**.

![](https://sumproduct.com/wp-content/uploads/2025/05/b33577bd2e64f672cfc7027595c5b984-1.jpg)

In [Part 2](https://sumproduct.com/blog/power-query-heading-off-part-2/)
, I merged **Expenses** with the **Supplier\_Limit** query to create **Limit\_Exceeded**, which tells me if any limits have been breached.

![](https://sumproduct.com/wp-content/uploads/2025/05/22b34ed6353c424e702ca5312642e9a8-1.jpg)

In [Part 3,](https://sumproduct.com/blog/power-query-heading-off-part-3/)
 I loaded **Limit\_Exceeded** to a new worksheet.

![](https://sumproduct.com/wp-content/uploads/2025/05/38d61042abde2ad560d8d96729ec3f16-1.jpg)

I removed the header row and changed some of the data in **Expenses**.

![](https://sumproduct.com/wp-content/uploads/2025/05/1dc4f4e0b0451373dc0e81129c277761-1.jpg)

In [Part 4](https://sumproduct.com/blog/power-query-heading-off-part-4/)
, I ran the query for a single salesperson.

![](https://sumproduct.com/wp-content/uploads/2025/05/ee3604fc3a88f1f1542e568e3960445a-1.jpg)

I extracted this cell and created a parameter **P\_Salesperson:**

![](https://sumproduct.com/wp-content/uploads/2025/05/478d745575ee5a607eefb7a520fd8969-1.jpg)

I used this parameter to limit the data in **Expenses**:

![](https://sumproduct.com/wp-content/uploads/2025/05/e319f0db2b88b11906de4744e451f26e-1.jpg)

When I refreshed **Limit\_Exceeded**, I checked the results:

![](https://sumproduct.com/wp-content/uploads/2025/05/709c92cdc01897fa9ba8178b328ee768-1.jpg)

The results correctly showed one row of data and no headings. However, things changed in [part 5](https://sumproduct.com/blog/power-query-heading-off-part-5/)
 when I selected a different Salesperson:

![](<Base64-Image-Removed>)

When I refreshed **Limit\_Exceeded**, it had moved the data from the previous selection into the header row.

![](<Base64-Image-Removed>)

When I deleted the top row from the Excel sheet, things got worse!

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-heading-off-part-6/)
, I changed what happens if there is no data returned by **Limit\_Exceeded**. I created a basic query with one \[1\] blank row and appended it to **Limit\_Exceeded**.

![](<Base64-Image-Removed>)

I deleted **Column1**, and loaded the results to the Excel workbook:

![](<Base64-Image-Removed>)

This is looking much better! Clearly, it’s not ideal to have a blank row, but it is better than showing the wrong data. I’ll refine this approach so that I don’t add a blank row if I have data. First, let’s see what happens if I change the selected Salesperson back to ‘Mary’, and refresh **Limit\_Exceeded**:

![](<Base64-Image-Removed>)

As expected, I get two rows, as indicated by the values in the ‘Queries & Connections’ pane.

Back in my query, I look at the **M** code in the ‘Advanced Editor’, which I may access from the Home tab:

![](<Base64-Image-Removed>)

The last two steps pertain to the actions needed when the query doesn’t return any rows for step ‘Removed Columns’. Let’s look at that section:

**#”Removed  
Columns” = Table.RemoveColumns(#”Filtered  
Rows”,{“Flag”}),**

**#”Appended  
Query” = Table.Combine({#”Removed Columns”, NoRows}),**

**  
#”Removed Columns1″ =  
Table.RemoveColumns(#”Appended Query”,{“Column1”})**

**in**

**#”Removed Columns1″**  

To make things clearer, I am going to rename step ‘Removed Columns’ to ‘Limits\_Exceeded’.

**Limits\_Exceeded  
\= Table.RemoveColumns(#”Filtered Rows”,{“Flag”}),**

Next, I determine whether there are any rows returned by step ‘Limits\_Exceeded’. I am going to use the **M** function **Table.IsEmpty()**. This returns ‘TRUE’ or ‘FALSE’ for the query interrogated:

**Table.IsEmpty(table as table) as logical**

I will use this function to construct a condition for appending an empty row:

**Check\_NoRows = Table.IsEmpty(Limits\_Exceeded),**

I can include this to determine what the final two steps do. If there are rows, then I make them equal to Limited\_Exceeded, which means that no changes are made:

       **Limits\_Exceeded  
\= Table.RemoveColumns(#”Filtered Rows”,{“Flag”}),**

       **Check\_NoRows  
\= Table.IsEmpty(Limits\_Exceeded),**

**#”Appended Query” = if Check\_NoRows then  
Table.Combine({Limits\_Exceeded, NoRows}) else Limits\_Exceeded,**

**#”Removed Columns1″ = if Check\_NoRows then  
Table.RemoveColumns(#”Appended Query”,{“Column1”}) else  
Limits\_Exceeded**

**in**

       **#”Removed  
Columns1″**

This gives me the complete query:

![](<Base64-Image-Removed>)

I click Done, and check if this has the desired effect:

![](<Base64-Image-Removed>)

This looks fine so far; I load the query to the Excel workbook:

![](<Base64-Image-Removed>)

One row has been loaded. I change the Salesperson back to ‘Newbie’ and refresh the query:

![](<Base64-Image-Removed>)

I have one blank row loaded, so this works as I intended. Next time, I’ll look at an alternative way to include a blank row when needed.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-heading-off-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-heading-off-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-heading-off-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-heading-off-part-7/#0)

[](https://sumproduct.com/blog/power-query-heading-off-part-7/#0 "close")

top