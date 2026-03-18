# Power Query: Making Your Mark(up) Part 3

**Source:** https://sumproduct.com/blog/power-query-making-your-markup-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Making Your Mark(up) Part 3

*   January 28, 2025

Power Query: Making Your Mark(up) Part 3
========================================

Power Query: Making Your Mark(up) Part 3
========================================

29 January 2025

_Welcome to our Power Query blog. This week, I look at the **Xml.Document()** function._

Extensible Markup Language (XML) is a markup language which can be read by multiple platforms and also uses text which can be read. It is commonly used to store data which is used by more than one platform. Accounting data may be stored in this way when it is accessed by more than one accounting software system. The example I am using today comes from the Microsoft and is an sample of some accounting data to use with the eConnect system (‘A sample XML document to import Analytical Accounting information on a Payables Transaction when using eConnect’); if you’d like to play along, you may access the data [here](https://learn.microsoft.com/en-us/troubleshoot/dynamics/gp/sample-xml-document-to-import-analytical-accounting-information)
. I have created the file locally, and when I open it with a web browser, the data is shown in black text.

![](<Base64-Image-Removed>)

As indicated by the message at the top of the previous image, I am shown the document tree. XML files often have the data nested, which will require some manipulation in Power Query. I may close some of the nesting to show a single transaction record:

![](<Base64-Image-Removed>)

In [part 1](https://sumproduct.com/blog/power-query-making-your-markup-part-1/)
, I imported the data, and decided that **taPMDistribution** is the query I am most interested in. I looked at the steps of the query, beginning with the Source step:

![](<Base64-Image-Removed>)

The **M** code was:

**\=  
taPMDistribution(File.Contents(“C:\\Users\\kathr\\OneDrive\\Documents\\SUMPRODUCT\\PQ Blog\\xml sample file.xml”), \[\], null)**

When I looked at the syntax in the Microsoft help pages, I found the basic syntax, but no help with the parameters.

Xml.Tables(**contents** as any, optional **options** as  
nullable record, optional **encoding** as nullable number) as table

[Last time](https://sumproduct.com/blog/power-query-making-your-markup-part-2/)
, I entered a step to the **taPMDistribution** query to see if I could find out any more about the parameters:

![](<Base64-Image-Removed>)

I found information for one of my parameters, the optional **encoding** option has the type **Text.Encoding** and had a dropdown for the values:

![](<Base64-Image-Removed>)

However, the **contents** (which should not be optional) were shown as optional and the **options** were not accessible. The possible values for **options** remain a mystery!

This time, I will continue looking at ways of importing XML files. I am going to use the **#shared** functionality which I last used in the blog [Generating the A to Z of **M** Functions](https://sumproduct.com/blog/power-query-generating-the-a-to-z-of-m-functions/)
.

![](<Base64-Image-Removed>)

I convert the record ‘Into Table’ and search for “XML”:

![](<Base64-Image-Removed>)

The last item is **Xml.Tables()**, which I have used. Now, let’s have a look at **Xml.Document()**:

![](<Base64-Image-Removed>)

The good news is that I have the syntax and I can that the difference is that this function ‘returns the contents of the XML document as a hierarchical table’. The bad news is that this also shows the **contents** incorrectly as optional! However, there are no **options** this time:

**Xml.Document(contents** as any, optional **encoding** as nullable number**)** as table

I take a duplicate copy of **taPMDistribution** and change the source step:

![](<Base64-Image-Removed>)

If I compare this source step with the one from the original query:

![](<Base64-Image-Removed>)

I can see that I have different columns this time. I click in the white space next to the ‘Table’ in the **Value** column:

![](<Base64-Image-Removed>)

This shows me the **PMTransactionType** record, which contains the queries that I extracted using the XML connector. I delete the remaining steps, as I will need to recreate the extraction process. If I extract the data from this table, keeping the original column as prefix, I can see the queries:

![](<Base64-Image-Removed>)

I expand the data in the **Value.Value** column:

![](<Base64-Image-Removed>)

Now I can see the structure of the XML file and if I scroll across, I see the table associated with **taPMDistribution** (though it has the suffix “\_items”):

![](<Base64-Image-Removed>)

If I click on this ‘Table’, I might expect to navigate to the same query data:

![](<Base64-Image-Removed>)

Not quite! I have more layers to go. This process explains why the function **Xml.Files()** was needed to extract XML data as it is much easier to access the ‘flattened’ data.

Next time, I will investigate accessing XML files from the web.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-making-your-markup-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-making-your-markup-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-making-your-markup-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-making-your-markup-part-3/#0)

[](https://sumproduct.com/blog/power-query-making-your-markup-part-3/#0 "close")

top