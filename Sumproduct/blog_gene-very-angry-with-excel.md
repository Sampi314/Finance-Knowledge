# Gene Very Angry with Excel

**Source:** https://sumproduct.com/blog/gene-very-angry-with-excel/

---

[Home](https://sumproduct.com/)

\> Gene Very Angry with Excel

*   September 13, 2016

Gene Very Angry with Excel
==========================

Gene Very Angry with Excel
==========================

14 September 2016

Now this _is_ funny. Well, if it wasn’t important it would be. A bad workman always blames his / her tools, but sometimes the problem lies squarely with the interface between computer and chair…

Late August has seen Excel blamed for errors in academic papers on genomics (obviously!). Researchers claim that the spreadsheet software automatically converts the names of certain genes into dates.

For example, there’s a gene called Septin 2 which has the universally recognised (!) symbol SEPT2. Well, Microsoft reckons that’s a date (ain’t nobody got time for that).

Gene symbols like SEPT2 (Septin 2) were found to have been altered to “September 2” in various reports, with similar issues also abounding for MAR1, OCT4 and SEP8. It doesn’t just stop at dates though: going well off into the realms of what I have no idea what I am talking about (pretty much everything, to be honest), there is another default conversion problem for what are known as RIKEN\[4\] clone identifiers of the form **nnnnnnnEnn**, where **n** denotes a digit. It’s estimated approximately 3% of all spreadsheets containing these identifiers have seen the names converted to scientific notation. For example, “2310009E13” was converted to “2.31E+13” which means 2.310009 x 1013. Oops.

The Melbourne-based academic institute Baker IDI scanned 3,597 published scientific papers to conduct their study and found that 704 of these papers contained gene name errors created by Excel, and hence extrapolated to proclaim that “…approximately one-fifth of \[all\] papers” that collated data in Excel documents contain errors. They concluded rather arbitrarily that Excel should only be used “…for lightweight scientific analysis”.

At SumProduct, we can’t help thinking that Excel is getting a bit of a hard time here. There are ways to preserve the formatting / changing of data when it is imported. For example, you can use Microsoft Excel to import data from a text file into a worksheet. The **Text Import Wizard** examines the text file that you are importing and helps you ensure that the data is imported in the way that you want.

To start the Text Import Wizard, on the **Data** tab, in the **Get External Data** group, click **From Text**. Then, in the **Import Text File** dialog box, double-click the text file that you want to import.

![](<Base64-Image-Removed>)

Step 3 is where you need to pay attention. For the (column) data format, you need to select ‘Text’ not ‘General:

![](<Base64-Image-Removed>)

‘General’ will convert numerical values to numbers and date values to dates. “SEP2” will be treated as a date – which is what has caused the problem. This issue can be avoided. Using “Text” converts everything to, er, text. Simple.

Right, I’d love to stop and explain further, but I have a certain academic institute neighbour I need to go and have a friendly chat with…

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/gene-very-angry-with-excel/#0)
    
*   [Register](https://sumproduct.com/blog/gene-very-angry-with-excel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/gene-very-angry-with-excel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/gene-very-angry-with-excel/#0)

[](https://sumproduct.com/blog/gene-very-angry-with-excel/#0 "close")

top