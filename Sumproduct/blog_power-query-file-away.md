# Power Query: File Away

**Source:** https://sumproduct.com/blog/power-query-file-away/

---

[Home](https://sumproduct.com/)

\> Power Query: File Away

*   February 19, 2019

Power Query: File Away
======================

Power Query: File Away
======================

20 February 2019

_Welcome to our Power Query blog. This week I look at some of the M functionality for dealing with files._

**File.Contents**

The description of this **M** function in the help pages is that it “…returns the binary contents of the file located at a path”. However, it actually allows more than this, as I will show in the following example.

File.Contents(**path** as text) as binary

where **path** is the path to the file to retrieve contents for.

On the following screen, I have created a blank query where I will retrieve the contents of one of the expense files for my fictional salespeople:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-484.jpg)

The **M** code I have used is

**\=File.Contents(“C:UserskathrOneDriveDocumentsPQ\_StandardExpensesPQ\_StandardExpense\_CSV\_1.csv”)**

When I execute this code, I get the following result.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-499.jpg)

Power Query has not only recognised the format of my file, it has also taken some automatic steps to promote the headers and set the data types for my columns.

If I go back to the first step, Power Query has used CSV functionality to extract the data from my file:

![](<Base64-Image-Removed>)

The **Csv.Document() M** functionality has been used to extract the data, which envelopes the **File.Contents()** functionality that I already specified. I want to see what happens if the file format is not one that is easily imported into Power Query – for example, the Word document containing last week’s blog!

![](<Base64-Image-Removed>)

The **M** code I have used is

**\= File.Contents(“C:UserskathrOneDriveDocumentsPQ\_StandardExpensesPQ BlogPower Query Blog 116.docx”)**

When I execute this code, I get the following result:

![](<Base64-Image-Removed>)

I can see an icon representing my document and I have access to a ‘Binary Tools’ tab. The only option is to convert, which means convert the document to a format that Power Query can import.

![](<Base64-Image-Removed>)

I can choose how to define and open my document using the ‘Open’ options on the menu.

![](<Base64-Image-Removed>)

I can also right click on my document to define how to open it. I’m not expecting Power Query to cope well with the escape codes, since Word is not on the list (yet?), but I choose to open my document as a text file instead.

![](<Base64-Image-Removed>)

As anticipated – not much to work with here thanks to all the formatting, but following this process has allowed me to view the available formats that Power Query can currently convert and input. I have converted last week’s blog to a text format from within Word to remove the formatting layer to see what I may extract from it.

![](<Base64-Image-Removed>)

The **M** code I have used is

**\= File.Contents(“C:UserskathrOneDriveDocumentsPQ\_StandardExpensesPQ BlogPower Query Blog 115 text.txt”)**

When I execute this code, I get the following result:

![](<Base64-Image-Removed>)

Power Query has recognised that this data can be extracted by treating my text file as a CSV file, and I can see the contents of the blog.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-file-away/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-file-away/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-file-away/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-file-away/#0)

[](https://sumproduct.com/blog/power-query-file-away/#0 "close")

top