# Power Query: Going for the Record

**Source:** https://sumproduct.com/blog/power-query-going-for-the-record/

---

[Home](https://sumproduct.com/)

\> Power Query: Going for the Record

*   October 6, 2020

Power Query: Going for the Record
=================================

Power Query: Going for the Record
=================================

7 October 2020

_Welcome to our Power Query blog. This week, I put the spotlight on records._

This week_,_ I am going to look at several ways to create a record.

The first and perhaps simplest method is to define a record in **M**. I have created a record as below:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-130-1.jpg)

The **M** code I have used is:

**\= \[A = “Kathryn”, B = “Record”\]**

In other words, create a record with two fields A and B where A is “Kathryn” and B is “Record”. The result is a record.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-120-1.jpg)

I could use a field name more complex than ‘A’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-113-1.jpg)

The **M** code I have used is:

**\= \[this is the first field = “Kathryn”, this is the second field = “Record”\]**

I can do this without surrounding my field name with quotes (**“”**), and I do not need to include a **#**, even if there are spaces in my field name.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-99-1.jpg)

I can also create fields of different types without specifying a datatype. The **M** code I used in the previous screenshot is:

**\= \[this is the first field  = “Kathryn”, this is the second field which is a number = 1.5\]**

However, I can’t use the same field name in a record.

![](<Base64-Image-Removed>)

I can enter lots of fields in one record though.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= \[field 1  = “Kathryn”, field 2 = 1.5, field 3 = \[inset field 1 = “hello”, inset field 2 = “world”\]\]**

In this case, my record has three fields, and the last field is a record, which itself contains two fields.

I can also use **M** functions to create records. There are many functions which output records, so I will look at just a few of them. I will start with **Record.FromTable()**:

**Record.FromTable(table**as table**)** as record

This returns a record from a **table** containing field names and value names \[**Name** = name, **Valu****e** = value\]. An exception is yielded if the field names are not unique.

![](<Base64-Image-Removed>)

I have converted my record to a table, so I should be able to use **Record.FromTable()** to go back to my original record.

![](<Base64-Image-Removed>)

The **M** code I enter is:

**\= Record.FromTable( #”Converted to Table”)**

where “Converted to Table” is my previous step. I enter this to get the following result:

![](<Base64-Image-Removed>)

My table has been converted into a record. I can also create a record from a list using **Record.FromList()**:

**Record.FromList(list** as list, **fields** as any**)** as record

This returns a record given a **list** of field values and a set of **fields**. The fields can be specified either by a list of text values, or a record type. An error is generated if the fields are not unique.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Record.FromList(Source, {“Fruit 1″,”Fruit 2″,”Fruit 3″,”Fruit 4”})**

This should create a record from my list values and the list of field names that I have specified.

![](<Base64-Image-Removed>)

I have the record I expected. I can also use the function **Record.Combine()**:

**Record.Combine(records** as list**)** as record

This combines the records in the given records. If the records contain non-record values, an error is returned.

I can combine the records I have created:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Record.Combine({Custom1,Query1})**

This should combine the record I just created in step Custom1, and the record I created in **Query1**.

![](<Base64-Image-Removed>)

The records have been combined to create a new record with seven fields.

There are other Power Query **M** functions that output records, such as **Time.ToRecord()**:

**Time.ToRecord(time** as time**)** as record

This returns a record containing the parts of the given **time**:

*   **time**: this is a time value for from which the record of its parts is to be calculated.

![](<Base64-Image-Removed>)

I have created a time 10:15.30, and I am going to convert this into a record.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Time.ToRecord(Source)**

This should convert the source time to a record.

![](<Base64-Image-Removed>)

A record has been created with field names “Hour”, “Minute”, and “Second”.

Finally, I can get a record by specifying a row of a table:

![](<Base64-Image-Removed>)

I have created a table from my record, and now I can specify just one row of that table to get a new record.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= #”Converted to Table”{4}**

This should get the fifth row of my table and present it as a record, since the count starts at 0.

![](<Base64-Image-Removed>)

The fifth row has been converted to a record with field names ‘**Name**‘ and ‘**Value**‘, and field values ‘**Field 1**‘ and ‘**Kathryn**‘ respectively.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-going-for-the-record/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-going-for-the-record/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-going-for-the-record/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-going-for-the-record/#0)

[](https://sumproduct.com/blog/power-query-going-for-the-record/#0 "close")

top