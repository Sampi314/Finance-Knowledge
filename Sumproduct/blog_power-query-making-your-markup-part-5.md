# Power Query: Making Your Mark(up) Part 5

**Source:** https://sumproduct.com/blog/power-query-making-your-markup-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Making Your Mark(up) Part 5

*   February 11, 2025

Power Query: Making Your Mark(up) Part 5
========================================

Power Query: Making Your Mark(up) Part 5
========================================

12 February 2025

_Welcome to our Power Query blog. This week, I examine the queries created when I extracted an XML file from the web._

Extensible Markup Language (XML) is a markup language understood by multiple platforms and also uses text which can be read. It is commonly used to store data which is used by more than one platform. Accounting data may be stored in this way when it is accessed by more than one accounting software system. The example I am using today comes is on GitHub, and may be accessed [here](https://niem.github.io/community/biometrics/sample-xml/NIEM5.1_DNA_Crime_Scene_Sample.xml)
 if you wish to follow along. The data represents DNA data from a crime scene sample!

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-making-your-markup-part-4/)
, I accessed the file from the web, using the ‘From Web’ connector in the ‘Get Data’ dropdown. I imported two \[2\] queries:

![](<Base64-Image-Removed>)

The catchily-named **http://www w3 org/2001/XMLSchema-instance** contains information about the original URL. I am more interested in the **DNARecord** query:

![](<Base64-Image-Removed>)

Let’s look at the **M** code in the Source step:

![](<Base64-Image-Removed>)

The syntax being used begins with the **Xml.Tables()** function we first encountered in [Part 1](https://sumproduct.com/blog/power-query-making-your-markup-part-1/)
:

**Xml.Tables(contents** as any, optional **options** as  
nullable record, optional **encoding** as nullable number**)** as table

Here, it is nested around the **Web.Contents()** function.

**\=** **Xml.Tables(Web.Contents(“https://niem.github.io/community/biometrics/sample-xml/NIEM5.1\_DNA\_Crime\_Scene\_Sample.xml”))**

This automatic behaviour is difficult to avoid. I choose to create a new ‘Blank Query’ from ‘Other Sources’ on the ‘New Source’ dropdown on the Home tab:

![](<Base64-Image-Removed>)

I begin by entering the **Web.Contents()** part of the nesting:

![](<Base64-Image-Removed>)

As soon as I enter this code, it is transformed:

![](<Base64-Image-Removed>)

The ‘.xml’ extension triggers inclusion of the **Xml.Tables()** function. If I enter the steps separately in the ‘Advanced Editor’, accessed from the Home tab, I may create two \[2\] separate steps:

![](<Base64-Image-Removed>)

Thus, I have the two steps in the ‘Applied Steps’ pane:

![](<Base64-Image-Removed>)

I may now view the first Source step:

![](<Base64-Image-Removed>)

This way, I may view the XML file. The Markup step then isolates the **Xml.Tables()** step:

![](<Base64-Image-Removed>)

The individual queries may now be accessed by expanding the **Table** column:

![](<Base64-Image-Removed>)

The first expansion shows me the contents of the **http://www w3 org/2001/XMLSchema-instance** query, and I must expand **Table.Table** to get the **DNARecord** query data:

![](<Base64-Image-Removed>)

Accessing the data in this way gives me more information about the source of **DNARecord**, which may be found in the **Name** column.

Next time, I will extract the data from the **DNARecord** query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-making-your-markup-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-making-your-markup-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-making-your-markup-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-making-your-markup-part-5/#0)

[](https://sumproduct.com/blog/power-query-making-your-markup-part-5/#0 "close")

top