# Power BI Blog: De-duplication Rules for Composite Models

**Source:** https://sumproduct.com/blog/power-bi-blog-de-duplication-rules-for-composite-models/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: De-duplication Rules for Composite Models

*   December 27, 2023

Power BI Blog: De-duplication Rules for Composite Models
========================================================

Power BI Blog: De-duplication Rules for Composite Models
========================================================

28 December 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we review whether Microsoft should make up words such as “de-duplication”. Or maybe that isn’t what this article is about – perhaps it’s about preventing duplication for composite models on Power BI Datasets and Analysis Services._

![](<Base64-Image-Removed>)

Tables and measures in your model must have unique names. If you use composite models on Power BI Datasets and Analysis Services, it’s easy to get into a situation where tables and measure names have duplicate names and are not unique. Up to this point, when that happened one of the tables or measures would be renamed for you.

For example, if you created a composite model from two sources and both sources defined a table called ‘Customers’, one of the tables would be renamed ‘Customer 2’. This resulted in confusing situations as it was not clear which source the ‘Customer 2’ table came from. The same applies to measures: if you had two sources that both contained a measure called ‘Total Sales’ one would be renamed ‘Total Sales 2’ in the composite model.

Now, Microsoft is handing (some) control back. You can now apply a name disambiguation rule to a source in a composite model when you anticipate name conflicts with tables or measures from another source. You can set up a text to be added as a prefix or suffix to table names, measure names or both. Additionally, you can choose to add that text only when a duplication occurs or if you prefer to have it added all the time.

Going back to the example above, let’s say that one of the sources you are combining is about marketing and the other is about sales. You can now set up a de-duplication rule on the source connection so the ‘Customer’ table from the marketing source is named ‘Customer (marketing)’:

![](<Base64-Image-Removed>)

You will find these options under Settings in the dialog that shows when you set up the composite model connection to a Power BI dataset or Analysis Services model:

![](<Base64-Image-Removed>)

After you make the connections and set up the de-duplication rule, your Field list will show both ‘Customer’ and ‘Customer (marketing)’ according to the de-duplication rule you set up:

![](<Base64-Image-Removed>)

It should be noted that you can now:

*   specify whether you want the text to be added to the table or measure name as a prefix or a suffix
*   apply the de-duplication rule to tables, measures or both
*   choose to apply the de-duplication rule only when a name conflict occurs or apply it all the time. The default is to apply the rule only when duplication occurs. In the example above, any table or measure from the marketing source that does not have a duplicate in the sales source will not receive a name change.

Finally, it would be remiss is if we didn’t mention that if you do not specify a de-duplication rule or the de-duplication rules you specified do not resolve the name conflict, the standard deduplication actions will still be applied.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-de-duplication-rules-for-composite-models/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-de-duplication-rules-for-composite-models/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-de-duplication-rules-for-composite-models/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-de-duplication-rules-for-composite-models/#0)

[](https://sumproduct.com/blog/power-bi-blog-de-duplication-rules-for-composite-models/#0 "close")

top