# Power Query: Combining Forces

**Source:** https://sumproduct.com/blog/power-query-combining-forces/

---

[Home](https://sumproduct.com/)

\> Power Query: Combining Forces

*   July 23, 2019

Power Query: Combining Forces
=============================

Power Query: Combining Forces
=============================

24 July 2019

Welcome to our Power Query blog. Today, I look at a way to reduce overheads when combining numerous files.

I looked at combining files from a folder in [Power Query: One Folder, One Query](https://sumproduct.com/blog/power-query-one-folder-one-query/)
. In that query, I used the Graphical User Interface (GUI) functions available to combine files.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-394.jpg)

To get to this point, I used the ‘From Folder’ option which is in the dropdown from ‘From File’, located in the ‘New Query’ dropdown in the ‘Get & Transform’ section of the ‘Data’ tab in Excel.

However, there is another path I can take if I am concerned about the overhead of combining lots of files from a folder. Instead of combining the files, I can choose to ‘Transform Data’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-403.jpg)

I don’t need the columns of my data at this point; all I want is to keep the **Content** column. I select this column and right click to remove the other columns. Now I have a single column, I choose to ‘Drill Down’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-380.jpg)

This gives me a list of files:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-353.jpg)

This is useful to me because it means I can use an alternative method to combine my files, namely **Table.Combine()**:

Table.Combine(**tables** as list, optional **columns** as any) as table

This returns a table that is the result of merging a list of **tables**. The resulting table will have a row type structure defined by columns or by a union of the input types if columns is not specified.

Before I combine my files, there is another step I can take, using the **M** function **List.Transform()**:

List.Transform(**list** as list, **transformation** as function)  as list

This performs the transformation on each item in the **list** and returns the new list.

The particular transformation I want to use is **Binary.Buffer**:

Binary.Buffer(**binary** as nullable binary) as nullable binary

This buffers the **binary** value in memory. The result of this call is a stable binary value, which means it will have a deterministic length and order of bytes.

What I am doing is to make the storage of my binary files more efficient. I can apply the required **M** code to the formula bar.

![](<Base64-Image-Removed>)

This has no impact visually, since the function is working on the way the binaries are stored in memory.

I now have a list of binaries which are stored efficiently. In order to use **Table.Combine()**, I need a list of tables. The easiest way to achieve this is to create a transformation that **List.Transform()** can use. I do this by creating a function. I save my current query as ‘**Combining\_Files**‘ and create a new blank query.

My function is a version of **Csv.Document()** which receives a parameter:

Csv.Document(**source** as any, optional **columns** as any, optional **delimiter** as any, optional **extraValues** as nullable number, optional **encoding** as nullable number) as table

![](<Base64-Image-Removed>)

The **M** code I have created is:

**\=(salesfile as binary) => Csv.Document(salesfile, \[Encoding=1252\])**

The “1252” encoding is explicitly requiring single-byte characters that are the defaults for English and other Western languages’ versions of Microsoft Windows.

Having created my function, I can apply it to **Combining\_Files**.

![](<Base64-Image-Removed>)

Once I click to execute this step, my column is transformed:

![](<Base64-Image-Removed>)

I now have a list of tables, and I can use **Table.Combine()**.

![](<Base64-Image-Removed>)

When I execute this step, my files are combined.

![](<Base64-Image-Removed>)

I can now transform my data and apply the usual transformations to remove blank rows / headers and fill down where necessary.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-combining-forces/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-combining-forces/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-combining-forces/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-combining-forces/#0)

[](https://sumproduct.com/blog/power-query-combining-forces/#0 "close")

top