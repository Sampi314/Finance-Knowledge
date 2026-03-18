# Power Query: Making Your Mark(up) Part 4

**Source:** https://sumproduct.com/blog/power-query-making-your-markup-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Making Your Mark(up) Part 4

*   February 4, 2025

Power Query: Making Your Mark(up) Part 4
========================================

Power Query: Making Your Mark(up) Part 4
========================================

5 February 2025

_Welcome to our Power Query blog. This week, I extract an XML file from the web._

Extensible Markup Language (XML) is a markup language which can be read by multiple platforms and also uses text which can be read. It is commonly used to store data which is used by more than one platform. Accounting data may be stored in this way when it is accessed by more than one accounting software system. The example I am using today comes is on GitHub, and may be accessed [here](https://niem.github.io/community/biometrics/sample-xml/NIEM5.1_DNA_Crime_Scene_Sample.xml)
 if you wish to follow along. The data represents DNA data from a crime scene sample!

![](<Base64-Image-Removed>)

Since I will be accessing the file from the web, I need to use the ‘From Web’ connector in the ‘Get Data’ dropdown:

![](<Base64-Image-Removed>)

I enter the URL of the XML file:

![](<Base64-Image-Removed>)

Since I have not accessed this website using Power Query before, I am prompted for the access details and the level to apply them to.

![](<Base64-Image-Removed>)

I am happy to use the default anonymous access and default level and I click ‘Connect’:

![](<Base64-Image-Removed>)

The Navigator dialog has identified some tables and I choose to ‘Select Multiple Items’ and select everything available:

![](<Base64-Image-Removed>)

I choose to ‘Transform Data’:

![](<Base64-Image-Removed>)

I have two \[2\] queries. The catchily-named **http://www w3 org/2001/XMLSchema-instance** contains information about the original URL. I am more interested in the **DNARecord** query:

![](<Base64-Image-Removed>)

This looks promising; even though I have used the web connector, I have managed to extract Tables of data. Next time, I will check the data and the syntax used to extract it.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-making-your-markup-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-making-your-markup-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-making-your-markup-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-making-your-markup-part-4/#0)

[](https://sumproduct.com/blog/power-query-making-your-markup-part-4/#0 "close")

top