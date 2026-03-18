# Power Query: Moving Date

**Source:** https://sumproduct.com/blog/power-query-moving-date/

---

[Home](https://sumproduct.com/)

\> Power Query: Moving Date

*   March 13, 2018

Power Query: Moving Date
========================

Power Query: Moving Date
========================

14 March 2018

_Welcome to our Power Query blog. This week, I look at how to transform extracted data into a useful table._

Regular readers will be familiar with my fictional salespeople and their tendency to supply data in the wrong format. Let’s meet John.

![](https://sumproduct.com/wp-content/uploads/2025/05/701adb389b1c4eca940b4b7c07609028.jpg)

Whilst John has supplied his expenses, the format I would like to see them in is something like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/ea2e7362925c5794453a3737533722b4.jpg)

To start the process, I extract John’s data into Power Query:

![](https://sumproduct.com/wp-content/uploads/2025/05/cb279155b1e15dcc83188a91a863551b.jpg)

I can select the data and use ‘From Table’ on the ‘Get and Transform’ section of the ‘Data’ tab. My data will be converted to a table as part of the process.

![](https://sumproduct.com/wp-content/uploads/2025/05/5b914784fbdc4cc61a1f36f0ece998b8.jpg)

The first two rows are not useful to me, so my first step is to remove them using the ‘Remove Rows’ option in the ‘Reduce Rows’ section.

![](https://sumproduct.com/wp-content/uploads/2025/05/f23807a3f7adbe29b6029c540a6429ae.jpg)

I could remove them based on a parameter, but I just want to get rid of the first two rows so I choose the ‘Decimal Number’ option. I also remove the row of nulls beneath my ‘Date’ row by removing blank rows.

![](https://sumproduct.com/wp-content/uploads/2025/05/69aa0eee57283b813a4d0861ffd175b9.jpg)

I want to create a column from the ‘Date’ cell. The first step to achieving this is to right click on the **Date** cell and use the option to ‘Add as New Query’. This creates a new query in the queries panel on the left of the screen.

![](https://sumproduct.com/wp-content/uploads/2025/05/2c4ebae188808b961c0a45ce8fe52d79.jpg)

The new query, automatically called ‘Column2’, includes my earlier source steps and the value in the top row of **_Column2_** – the date.

![](https://sumproduct.com/wp-content/uploads/2025/05/6e9d87a1a45eb266adcab4b45ac2943c.jpg)

Having created my query, I need to make sure the next steps I add are to the **Table1** query. Now I can transform the rest of the data to appear in the format that I would like.

![](<Base64-Image-Removed>)

The steps I have taken are;

1.  Removed Top Rows1 – having moved the date to a separate query, I could remove the ‘Date’ row
2.  Promoted Headers – since I wanted to just keep my expense types and values, I promoted the expense to headers to get rid of the generic ‘Column1’ _etc._ (the ‘Changed Type1’ step was an automated Power Query step)
3.  Unpivoted Columns – I didn’t want to keep my expense types as headers, I ultimately want to store them in a column under the heading ‘Expense Type’, so I unpivoted to get the data as it is shown above.

Now all that remains is to rename my columns and add a ‘Date’ column. To do this I will add a custom column.

![](<Base64-Image-Removed>)

Having referenced the other query (which is easy to check as I can see it in the left-hand pane), I click ‘OK’.

![](<Base64-Image-Removed>)

The date appears as a new column.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-moving-date/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-moving-date/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-moving-date/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-moving-date/#0)

[](https://sumproduct.com/blog/power-query-moving-date/#0 "close")

top