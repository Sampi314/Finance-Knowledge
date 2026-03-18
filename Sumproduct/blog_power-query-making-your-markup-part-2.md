# Power Query: Making Your Mark(up) Part 2

**Source:** https://sumproduct.com/blog/power-query-making-your-markup-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Making Your Mark(up) Part 2

*   January 21, 2025

Power Query: Making Your Mark(up) Part 2
========================================

Power Query: Making Your Mark(up) Part 2
========================================

22 January 2025

_Welcome to our Power Query blog. This week, I continue examining the syntax of the **Xml.Tables()****M** function__._

Extensible Markup Language (XML) is a markup language which can be read by multiple platforms and also uses text which can be read. It is commonly used to store data which is used by more than one platform. Accounting data may be stored in this way when it is accessed by more than one accounting software system. The example I am using today comes from the Microsoft and is an sample of some accounting data to use with the eConnect system (‘A sample XML document to import Analytical Accounting information on a Payables Transaction when using eConnect’); if you’d like to play along, you may access the data [here](https://learn.microsoft.com/en-us/troubleshoot/dynamics/gp/sample-xml-document-to-import-analytical-accounting-information)
. I have created the file locally, and when I open it with a web browser, the data is shown in black text.

![](<Base64-Image-Removed>)

As indicated by the message at the top of the previous image, I am shown the document tree. XML files often have the data nested, which will require some manipulation in Power Query. I may close some of the nesting to show a single transaction record:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-making-your-markup-part-1/)
, I imported the data, and decided that **taPMDistribution** is the query I am most interested in. I looked at the steps of the query, beginning with the Source step:

![](<Base64-Image-Removed>)

The **M** code is:

**\=  
Xml.Tables(File.Contents(“C:UserskathrOneDriveDocumentsSUMPRODUCTPQ  
Blogxml sample file.xml”))**

When I looked at the syntax in the Microsoft help pages, I found the basic syntax, but no help with the parameters.

Xml.Tables(**contents** as any, optional **options** as  
nullable record, optional **encoding** as nullable number) as table

To see if I can find out any more about this function, I enter a step to the **taPMDistribution** query:

![](<Base64-Image-Removed>)

By entering the **M** code:

**\= Xml.Tables**

I can see more information for one of my parameters, though the other one is not shown! In the ‘Enter Parameters’ section, the optional **encoding** option has the type **Text.Encoding** and has a dropdown for the values:

![](<Base64-Image-Removed>)

However, the **contents** (which should not be optional) is shown as optional, and the **options** are not accessible. If I use this step to access the XML file from the source step, I get the following **M** code in a new query:

![](<Base64-Image-Removed>)

**\=  
taPMDistribution(File.Contents(“C:\\Users\\kathr\\OneDrive\\Documents\\SUMPRODUCT\\PQ Blog\\xml sample file.xml”), \[\], null)**

This **M** code shows where the optional parameters would appear; **options** is a record, which is currently \[\], and **encoding** is _null_. The possible values for **options** remain a mystery!

Next time, I will look at another way of importing XML files.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-making-your-markup-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-making-your-markup-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-making-your-markup-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-making-your-markup-part-2/#0)

[](https://sumproduct.com/blog/power-query-making-your-markup-part-2/#0 "close")

top