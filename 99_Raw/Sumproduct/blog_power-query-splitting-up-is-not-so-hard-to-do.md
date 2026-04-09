# Power Query: Splitting Up is Not so Hard to Do

**Source:** https://sumproduct.com/blog/power-query-splitting-up-is-not-so-hard-to-do/

---

[Home](https://sumproduct.com/)

\> Power Query: Splitting Up is Not so Hard to Do

*   July 4, 2017

Power Query: Splitting Up is Not so Hard to Do
==============================================

Power Query: Splitting Up is Not so Hard to Do
==============================================

5 July 2017

_Welcome to our Power Query blog. Today I look at dividing a full name column into first and last names._

This is a fairly common scenario. I have a column which is made up of several pieces of data I want to extract, in this case a full name. As a programmer, I used to write chunks of code to do this, carefully stepping through the name until I reached the space. With Power Query, it’s much easier.

I will start from where I ended last week, with a file of expense data, which happens to include the full name of the employees. In order to show how this can be applied to any Excel data, I will load only the name to a query for this example.

![](<Base64-Image-Removed>)

Since my data is already in a table, I take a copy and convert it to a range by using ‘Convert to Range’ option on the ‘TABLE TOOLS DESIGN’ tab (sorry for the shouting – I continue to use Excel 2013 for my examples!). Otherwise, Power Query will assume that the whole table should be loaded.

![](<Base64-Image-Removed>)

This gives me the range, which will no longer be connected to my ‘PQ\_Names\_in\_with\_Data’ query.

![](<Base64-Image-Removed>)

There are several approaches I could take. I could make my ‘Employees’ column an Excel table and load that, but I don’t actually need to take that step in Excel. Instead, on the ‘POWER QUERY’ tab, I choose the ‘From Excel Range/Table’ option. If I don’t specify my data by selecting it first, then Power Query prompts me to confirm the data I want to use:

![](<Base64-Image-Removed>)

So I can either specify cells **D1**:**D18** on here or I can select those cells first and Power Query will automatically load them.

![](<Base64-Image-Removed>)

I now have my little table of data, and I am ready to split up the name.

On the ‘Home’ tab, there is an option to ‘Split Column’, and I can choose to do this ‘By Delimiter’ or ‘By Number of Characters’.

![](<Base64-Image-Removed>)

I choose to split by delimiter, and the ‘Split Column by Delimiter’ screen appears. Power Query has correctly assumed ‘Space’ is my delimiter, but it’s worth taking a look at the other options:

![](<Base64-Image-Removed>)

The most common options are explicitly listed and there is an option to customise my own delimiter for more complex data arrangements.

Also on the screen are a couple of other options:

![](<Base64-Image-Removed>)

I can choose how often to split my data using the delimiter – this would be useful if some of the names included a first and second name as well as a surname, in which case I could choose to keep the first two names together by only splitting at the right-most delimiter. There are also some advanced options which allow me to specify how many columns I want to see. If I were to choose one then I’d only see the first name, if I choose three, the last one would contain _null_ data. I can also choose the quote style. If I had special characters in my columns I could also choose to use them as a delimiter.

I am happy that I want to use the space as my delimiter and I will split each time I see a space (since I know that my data only has one space anyway). I choose to output to two columns.

![](<Base64-Image-Removed>)

My two new columns are named ‘Employee.1’ and ‘Employee.2’, and I opt to ‘Close and Load’ which will load them to a new worksheet in my book. I rename them and insert my new columns into my original worksheet. Easy!

![](<Base64-Image-Removed>)

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-splitting-up-is-not-so-hard-to-do/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-splitting-up-is-not-so-hard-to-do/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-splitting-up-is-not-so-hard-to-do/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-splitting-up-is-not-so-hard-to-do/#0)

[](https://sumproduct.com/blog/power-query-splitting-up-is-not-so-hard-to-do/#0 "close")

top