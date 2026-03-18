# Power Query: Hidden Talents

**Source:** https://sumproduct.com/blog/power-query-hidden-talents/

---

[Home](https://sumproduct.com/)

\> Power Query: Hidden Talents

*   March 29, 2022

Power Query: Hidden Talents
===========================

Power Query: Hidden Talents
===========================

30 March 2022

_Welcome to our Power Query blog. This week, I look at how to find data in hidden sheets._

My fictional salespeople are worried. There is a rumour that someone is in trouble after the latest review. They have found an Excel Workbook, but it seems nothing has been revealed yet:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-49-1.jpg)

I can link to this Excel Workbook from a new Excel Workbook:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-66.jpg)

From the ‘Get Data’ dropdown in the ‘Get & Transform’ section of the Data tab, I can choose ‘From Workbook’. In the browse dialog, I navigate to the correct Excel Workbook:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-48.jpg)

According to the Navigator dialog, there is only one table of data available and that’s not revealing anything. I decide to ‘Transform Data’ anyway.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-43.jpg)

The data has been automatically transformed for me in four \[4\] steps. In reverse order, the ‘Changed Type’ step has picked the data types for the columns, based upon algorithms that look at the data in the columns:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-35.jpg)

**\= Table.TransformColumnTypes(#”Promoted Headers”,{{“Name”, type text}, {“Review Date”, type date}, {“Result”, type text}})**

The previous step, ‘Promoted Headers’ has extracted the column headings from the first row of data:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-28.jpg)

**\= Table.PromoteHeaders(Employees\_Sheet, \[PromoteAllScalars=true\])**

The second step, Navigation, extracted the Employees sheet from the workbook:

![](<Base64-Image-Removed>)

**\= Source{\[Item=”Employees”, Kind=”Sheet”\]}\[Data\]**

The most interesting step for me, is the Source step:

![](<Base64-Image-Removed>)

**\= Excel.Workbook(File.Contents(“C:UserskathrOneDriveDocumentsSUMPRODUCTPQ BlogPQ blog 278 hiding.xlsm”), null, true)**

There is the **Employees** sheet, but what is this? Another sheet: **Management Only**. I click on the ‘Table’ text in the **Data** column next to **Management Only**:

![](<Base64-Image-Removed>)

Power Query warns me that the steps to extract the **Employees** sheet will be replaced. I choose ‘Continue’:

![](<Base64-Image-Removed>)

The steps are replaced, and the new data is revealed. It’s not good news for John, and Newbie should be worried! So why couldn’t we see this data when extracting from the Excel Workbook? The answer is on the Source step:

![](<Base64-Image-Removed>)

The **Hidden** column shows that the **Management Only** sheet was hidden, so it wasn’t shown on the extraction Navigator dialog. This is a useful trick to find hidden data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-hidden-talents/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-hidden-talents/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-hidden-talents/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-hidden-talents/#0)

[](https://sumproduct.com/blog/power-query-hidden-talents/#0 "close")

top