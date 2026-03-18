# Pro-Rating Over Time

**Source:** https://sumproduct.com/thought/pro-rating-over-time/

---

[Home](https://sumproduct.com/)

\> Pro-Rating Over Time

*   May 14, 2025

Pro-Rating Over Time
====================

How to properly Pro-Rate over time.

Pro-Rating Over Time
====================

Here’s a common problem in financial modelling. Costs (or revenues for that matter) and reporting dates seldom coincide. And that causes problems.

For example, I will consider an annual reporting model and staff costs. Staff have this really irritating habit of not starting jobs on the first day of the financial reporting year (for simplicity, in this illustration, I will consider the reporting year to be the calendar year). They can be quite inconsiderate in this regard. There may be other complications too:

*   They may choose to work part-time
*   Their contracts may only be for a certain period of time or be terminated (and this can happen at any point in the year)
*   They like having pay rises.

In other words, modelling these costs can be _complicated_. Modellers typically react in the only way they know how by constructing formulae Tolstoy would have been proud of and Sheldon Cooper would struggle to understand. More often than not, this all ends in tears – but there is a better way.

Rather than try and build the entire calculation in one cell, _step it out_.

This makes it easier for end users to understand and reduces the risk of errors in formulae too, given the greater transparency. Allow me to explain with an example – as usual supported by an [attached Excel file](https://sumproduct.com/assets/thought-files/prorating/sp-pro-rating-over-time-example.xlsm)
.

In order to explain the logic, let me first create some global assumptions. These are inputs that govern general constraints or parameters in the model. In this instance, I have

![](<Base64-Image-Removed>)

Note I have called these constants rather than variables, although I have then inconsistently formatted them as variables. For the record:

*   A **constant** is an input that rarely changes in a model. Examples include the number of hours in a day, the number of days in a week or the number of months in a year. These numbers are given range names to avoid hard code being incorporated into model formulae
*   A **variable** is an input that may change, particularly when undertaking what-if? analysis. Examples might include staff salaries, sales per month and tax rates
*   Variables are sometimes considered constants when they will not be subject to sensitivity or scenario analysis, or are intended to be constant over the time horizon of the forecast model. That is what has happened here: **Hours\_in\_Working\_Week** and **Probation\_Duration** are really variables, but are assumed to be constant for the time horizon modelled – hence I have decided to refer to them as constants for the purposes of this article. You might disagree. Feel free to email someone who cares. Please note that neither the editor nor I belong to this category.

Next, I need some staffing assumptions:

![](<Base64-Image-Removed>)

Apologies if this screenshot tests your eyesight, but essentially the inputs need to provide:

*   **A method of identifying the employee** (this might be by staff ID number, but here, I have used first and last names)
*   **How many hours each employee will work relative to the hours in a working week**. This is so a Full Time Equivalent (FTE) Rate may be calculated. For example, if someone works 30 hours a week compared to a 40-hour working week, this would represent a 75% FTE Rate
*   **Annual salary for the employee assuming they were working full time**
*   The **envisaged salary increase each year**. For simplicity, my example assumes salary increases are all processed on the first day of the next calendar year
*   **Employee start date**
*   **Employee end date** (where applicable), taking into account probation dates, fixed term contracts, terminations or extensions to original contracts. In the above image, column **Q** calculates the end date the logic of which may change from model to model) or else reports “N/A” where no end date is given, _i.e._ it is assumed the staff member will still be employed at the end of the final reporting period.

The next step is to calculate the proportion of each period each staff member will be available:

![](<Base64-Image-Removed>)

Columns **F**, **G** and **H** refer to the Start Date, End Date and FTE Rate respectively for each employee. The proportion available is then calculated in the table to the right. For example, the formula in the first period for the first employee (Sally Army in December 2019) is provided in cell **J18** and is calculated as

**\=MAX(MIN(J$7,$G18)-MAX(J$6,$F18)+1,0)\*$H18/J$8**

The formula may look a little involved, but it is not that sophisticated:

*   **MIN(J$7,$G18)** calculates the earlier of the final day in the period and the End Date
*   Similarly, **MAX(J$6,$F18)** calculates the later of the first day in the period and the Start Date
*   Therefore, **MIN(J$7,$G18)-MAX(J$6,$F18)+1** calculates the number of relevant days in the period. The adjustment of adding one (1) is to ensure the later of the first day in the period and the Start Date is included
*   Calculating the maximum of this and zero, **MAX(MIN(J$7,$G18)-MAX(J$6,$F18)+1,0)**, is computed just to ensure the End Date is later than or equal to the Start Date
*   Multiplying by the scalar **$H18/J$8** pro-rates by the FTE Rate and then divides by the number of days in the period.

After calculating the relevant periods the staff member is employed, I now need to identify when it is a period that the salary increase should be triggered. I do this by identifying the year of employment. This logic holds even if the periodicity of the model (_i.e._ the duration of each period which may be a month, quarter or year, say) is not a year.

![](<Base64-Image-Removed>)

Let me explain the mechanics behind this calculation using the formula in cell **J38**:

**\=IF(AND(I18=0,J18<>0),1,IF(J18<>0,I38+(COUNTIF($I38:I38,I38)=(Months\_in\_Year/Periodicity))\*1,))**

Again, it’s not pretty, but it’s not that complex:

*   The logical condition at the beginning of the **IF** statement, **\=IF(AND(I18=0,J18<>0),1,…** identifies the first year. The references to row 18 look at the proportion of the period the staff member is available, comparing the current period (**J18**) with the previous period (**I18**). When the current period is non-zero, but the previous period was null, this triggers identification of Year 1
*   The remainder of the formula, **IF(J18<>0,I38+(COUNTIF($I38:I38,I38)=(Months\_in\_Year/Periodicity))\*1,)** calculates the year number of subsequent periods when the proportion of the period the staff member is available is greater than zero. It is not as simple as adding one, in case the periodicity of the model changes. It takes the previous year number and adds one (1) only when the number of subsequent periods equates to a full year (_I.e._ the number of periods equals **Months\_in\_Year/Periodicity**) from the last year change. For example, if the model were quarterly, the Periodicity (number of months) would be three (3) and **Months\_in\_Year/Periodicity** would equal 12/3 which would be four (4) periods.

The next calculation is to work out the annual salary attributable to the period, even if the period does not represent a full 12 months or the employee does not work full-time (the following stage is where this annual salary is then pro-rated for the period). The logic here is to identify the salary for Year 1, and then inflate it when Year 1 changes to Year 2, Year 2 changes to Year 3, and so on.

![](<Base64-Image-Removed>)

The formula in cell **J56** achieves this:

**\=IF(AND(I38=0,J38=1),$F56,I56\*(J38<>0)\*(1+($G56\*(I38<>J38))))**

It’s another longer formula, but the ideas remain simple:

*   The first part, **IF(AND(I38=0,J38=1),$F56,…** checks to see whether the corresponding period is the first occurrence of Year 1 (row 38 is referenced); if so, the initial salary in column **F** is displayed
*   Otherwise, the formula **I56\*(J38<>0)\*(1+($G56\*(I38<>J38)))** is used to check the year in row 38 is non-zero (otherwise the salary is zero). Further, for non-zero years, if the year changes in row 38 between this period and the previous period, the salary in the prior column is grown by the inflationary factor in column **G**. If not, the salary from last year is used.

Creating this formula keeps things simple and does not require salaries being scaled up and scaled down for FTE Rates, mid-period Start Dates or mid-period End Dates. The whole idea is to keep things simple.

It is the next two calculations that then pro-rates these salaries. The first pro-rates for the duration of the period (regardless of whether the employee is full-time or is just starting or ending):

![](<Base64-Image-Removed>)

This is a simple calculation. For example, the formula in cell **J70** is

**\=J56\*MIN(J$8/Days\_in\_Year,1)**

_i.e._ the annual salary is pro-rated based on the number of days in the period (**J$8**) divided by the number of **Days\_in\_Year**.

The final calculation

![](<Base64-Image-Removed>)

is even simpler. For example, the formula in cell **J88** is given by

**\=J70\*J18**

In other words, the salary for the period is multiplied by the proportion of the period that staff member is actually available.

Stepped out like this, others can follow the logic, even if the formula may appear a little daunting initially. Not all formulae in Excel can be short, sweet and elegant like me. Sometimes, brute force and ignorance is used to bulldoze a calculation. Breaking an ugly formula into steps makes it easier for others to follow and therefore trust.

**_Word to the Wise_**

The aim of this article is to communicate that sophisticated calculations are often better stepped out. This example is precisely that – an example. The chances that a problem you may face is identical is unlikely. For example, you may need to consider:

*   The impact and timing of bonuses
*   Real versus nominal growth rates
*   Discretionary pay rises at varying rates
*   Promotions
*   Unpaid leave, _etc._

However, if you think through the ramifications of whatever cost or revenue item you are modelling, with planning, you should be able to construct a similar stepped set of calculations. Practice makes perfect!

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/pro-rating-over-time/#0)
    
*   [Register](https://sumproduct.com/thought/pro-rating-over-time/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/pro-rating-over-time/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/pro-rating-over-time/#0)

[](https://sumproduct.com/thought/pro-rating-over-time/#0 "close")

top