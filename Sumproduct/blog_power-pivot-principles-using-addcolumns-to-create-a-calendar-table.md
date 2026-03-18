# Power Pivot Principles: Using ADDCOLUMNS to Create a Calendar Table

**Source:** https://sumproduct.com/blog/power-pivot-principles-using-addcolumns-to-create-a-calendar-table/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Using ADDCOLUMNS to Create a Calendar Table

*   March 16, 2020

Power Pivot Principles: Using ADDCOLUMNS to Create a Calendar Table
===================================================================

Power Pivot Principles: Using ADDCOLUMNS to Create a Calendar Table
===================================================================

17 March 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a way of using a DAX function to create a calendar table._

In a previous [blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-addcolumns-function)
, we have introduced the DAX function **ADDCOLUMNS**. This week, we are going to use it in an applied fashion to create a calendar table from scratch.

In the existing connections, we import the table in current worksheet and choose ‘Edit DAX’ option as previously discussed in the blog [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-summarize-function)
. The evaluation function is applied to generate the target table and syntax, as shown below:

![](<Base64-Image-Removed>)

**Evaluate Var Dates = CALENDAR( DATE(2019,1,1), DATE(2020,12,31)) return ADDCOLUMNS(Dates, “Year”, YEAR(\[Date\]), “Month Number”, MONTH(\[Date\]), “Month”, FORMAT(\[Date\],”MMM”))**

We first define a variable **Dates** which is assigned the result returned from the function **CALENDAR**. The **CALENDAR** function returns a **Date** table with one single column of different dates defined between two different dates. In this case, we define the starting date as 1 Jan 2019 and the ending date as 31 Dec 2020. Therefore, **CALENDAR** function returns a single column table with dates starting from 1 Jan 2019 and ending 31 Dec 2020. Then, we use the **ADDCOLUMNS** function to add extra columns based upon the existing field **Date**. The added columns include: **Year**, **Month Number** and **Month**. For the **Year** field, the **YEAR** function returns the value of the year for **Date**. For the column of **Month Number**, the **MONTH** function returns the month for **Date**. For the column of **Month**, we use **FORMAT** function to return the text value of month for **Date** (Jan, Feb or March _etc_.).

The resulting table would be (not displayed in full):

![](<Base64-Image-Removed>)

Next, we can define the name of this table and import to Power Pivot interface by click tab ‘Add to Data Model’. In the interface, we simply choose the calendar table imported and mark it as a **Date Table**.

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog/power-pivot-principles-using-addcolumns-to-create-a-calendar-table/?id=152)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-using-addcolumns-to-create-a-calendar-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-using-addcolumns-to-create-a-calendar-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-using-addcolumns-to-create-a-calendar-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-using-addcolumns-to-create-a-calendar-table/#0)

[](https://sumproduct.com/blog/power-pivot-principles-using-addcolumns-to-create-a-calendar-table/#0 "close")

top