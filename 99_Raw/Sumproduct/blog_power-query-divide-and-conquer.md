# Power Query: Divide and Conquer

**Source:** https://sumproduct.com/blog/power-query-divide-and-conquer/

---

[Home](https://sumproduct.com/)

\> Power Query: Divide and Conquer

*   May 7, 2019

Power Query: Divide and Conquer
===============================

Power Query: Divide and Conquer
===============================

8 May 2019

_Welcome to our Power Query blog. Today, I am going to look at a method to extract multiple columns from a single column of mixed data._

John, my star imaginary salesperson, has some new contact details, which he has sent in an Excel workbook. All in one column. I need to create a table from this. I will use a different method from the one I used in [Power Query: Candid Columns](https://sumproduct.com/blog/power-query-candid-columns/)
.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-435.jpg)

There are many ways to approach this, and this time, I am going to use a list. I start by extracting my data into Power Query by using ‘From Table’ on the ‘Get & Transform’ section of the ‘Data’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-450.jpg)

On this occasion, my Table does not have headers, so I uncheck the box.

In case you are wondering why this checkbox is sometimes checked and sometimes isn’t. it’s to with Excel identifying the data type in the first row of each field and comparing it with subsequent rows’ data types. If the first row is text and all subsequent rows are numerical, ‘My table has headers’ would be checked, as this seems quite clear. Here, all rows are text – hence the box is unchecked, as Excel is not so sure.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-423.jpg)

Anyway, I have my data all in one column. Now I transform my column into a list by using the ‘Convert to List’ option on the ‘Transform’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-391.jpg)

This gives me the same data in a list:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-335.jpg)

Since my contact data is consistently comprised of five rows, I can split my list into groups of five. I’d like to see **List.Split()** as a GUI option on the ‘List Tools’ tab, but since it isn’t (yet!), I will need to create some **M** code. The function

List.Split(**list** as list, **pagesize** as number) as list

splits **list** into a list of lists, where the first element of the output list is a list containing the first **pagesize** elements from the source list, the next element of the output list is a list containing the next **pagesize** elements from the source list,etc_._

This function will give me a list of lists – where each ‘sub’ list contains all the data for one contact.

![](<Base64-Image-Removed>)

The **M** code I have entered above is:

**\= List.Split(Column1, 5)**

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-249.jpg)

I can see that each of my lists contains the contact data. My next step is to extract each of my lists into a table. Since each list is a row, I can use **Table.FromRows()**:

Table.FromRows(**rows** as list, optional **columns** as any) as table

This creates a table from the list **rows** where each element of the list is an inner list that contains the column values for a single row. An optional list of column names, a table type, or a number of columns could be provided for the argument **columns**.

This function will allow me to create a table for each of my contact lists. I also like the facility to create column names, so I’ll do this too.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.FromRows(Custom1, {“Name”, “Address Line 1”, “Town”, “Country”, “Post Code”})**

![](<Base64-Image-Removed>)

I now have my contact data in a useful form in just a few steps. I can see the code created in the ‘Advanced Editor’, _viz._

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Table1″\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Column1”, type text}}),**

    **Column1 = #”Changed Type”\[Column1\],**

    **Custom1 = List.Split(Column1, 5),**

    **Custom2 = Table.FromRows(Custom1, {“Name”, “Address Line 1”, “Town”, “Country”, “Post Code”})**

**in**

    **Custom2**

If I wish I can combine the steps I have added into one line of **M** code:

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Table1″\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Column1”, type text}}),**

    **Custom2 = Table.FromRows(List.Split(#”Changed Type”\[Column1\], 5), {“Name”, “Address Line 1”, “Town”, “Country”, “Post Code”})**

**in**

    **Custom2**

(The code differs from the third line of the main body of code onwards.)

![](<Base64-Image-Removed>)

This achieves the same goal in fewer steps:

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-divide-and-conquer/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-divide-and-conquer/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-divide-and-conquer/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-divide-and-conquer/#0)

[](https://sumproduct.com/blog/power-query-divide-and-conquer/#0 "close")

top