# Power Query: Making Your Mark(up) Part 1

**Source:** https://sumproduct.com/blog/power-query-making-your-markup-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Making Your Mark(up) Part 1

*   January 14, 2025

Power Query: Making Your Mark(up) Part 1
========================================

Power Query: Making Your Mark(up) Part 1
========================================

15 January 2025

_Welcome to our Power Query blog. This week, I look at importing_ _Extensible Markup Language (XML) files._

Extensible Markup Language (XML) is a markup language which can be followed by multiple platforms and also uses text which may also be read. It is commonly used to store data which is used by more than one platform. Accounting data may be stored in this way when it is accessed by more than one accounting software system.

The example I am using today comes from the Microsoft and is an sample of some accounting data to use with the eConnect system (‘A sample XML document to import Analytical Accounting information on a Payables Transaction when using eConnect’); if you’d like to play along, you may access the data [here](https://learn.microsoft.com/en-us/troubleshoot/dynamics/gp/sample-xml-document-to-import-analytical-accounting-information)
. I have created the file locally, and when I open it with a web browser, the data is shown in black text.

![](<Base64-Image-Removed>)

As indicated by the message at the top of the previous image, I am shown the document tree. XML files often have the data nested, which will require selected manipulation in Power Query. I may close some of the nesting to show a single transaction record:

![](<Base64-Image-Removed>)

To begin the extraction process to Excel, I am going to start in a new Excel workbook. On the Data tab I find the ‘From XML’ option in the ‘From File’ tab of the ‘Get Data’ dropdown:

![](<Base64-Image-Removed>)

I navigate to my file, and choose to Import it:

![](<Base64-Image-Removed>)

Note that since the records are nested within the XML file, it appears as a folder, and I may open the groupings to select the data I wish to transform. I also check the ‘Select multiple items’ box:

![](<Base64-Image-Removed>)

I have opted to select all the tables available to me. I choose to ‘Transform Data’:

![](<Base64-Image-Removed>)

I have three \[3\] queries. The first, **taAnalyticsDistribution**, appears to hold information about which ledgers in the eConnect database should be updated and the distribution. The next query, **taPMDistribution**, holds information about the amounts and document types and is of more interest to me.

![](<Base64-Image-Removed>)

Finally, **taPMTransactionInsert** contains information about the batch that the transaction in linked to:

![](<Base64-Image-Removed>)

Having decided that **taPMDistribution** is the query I am most interested in, let’s look at the steps of the query, beginning with the Source step:

![](<Base64-Image-Removed>)

The **M** code is:

**\=  
Xml.Tables(File.Contents(“C:UserskathrOneDriveDocumentsSUMPRODUCTPQ  
Blogxml sample file.xml”))**

Since this is the first time I’ve looked at the **Xml.Tables()** function, let’s have a look at the syntax.

**Xml.Tables(contents** as any, optional **options** as  
nullable record, optional **encoding** as nullable number**)** as table

Microsoft tells me that this function “returns the contents of the XML document as a nested collection of flattened tables”. However, there is no information about the **options** or the **encoding** parameters!

That’s it for this week, I’ll recover from my disappointment and continue looking at XML tables and the **M** code I may use to manipulate them next time.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-making-your-markup-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-making-your-markup-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-making-your-markup-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-making-your-markup-part-1/#0)

[](https://sumproduct.com/blog/power-query-making-your-markup-part-1/#0 "close")

top