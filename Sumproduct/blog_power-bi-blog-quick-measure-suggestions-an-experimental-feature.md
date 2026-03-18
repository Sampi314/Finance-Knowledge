# Power BI Blog: Quick Measure Suggestions (an Experimental Feature)

**Source:** https://sumproduct.com/blog/power-bi-blog-quick-measure-suggestions-an-experimental-feature/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Quick Measure Suggestions (an Experimental Feature)

*   October 26, 2022

Power BI Blog: Quick Measure Suggestions (an Experimental Feature)
==================================================================

Power BI Blog: Quick Measure Suggestions (an Experimental Feature)
==================================================================

27 October 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at a hot-off-the-press experimental feature to complement Power BI’s Quick Measures._

Some time ago, Power BI released a feature called ‘Quick Measures’ that allowed Power BI Desktop users to create **DAX** measures using a built-in template instead of writing the **DAX** from first principles. This feature helped users quickly get started with common measure scenarios. However, the number of templates and flexibility of those templates left much to be desired. Now, Power BI has introduced ‘Quick measure suggestions’, which is a new way to assist the creation of **DAX** measures using natural language instead of using templates or writing **DAX** from scratch.

![](https://sumproduct.com/wp-content/uploads/2025/05/810cf0a0393da3bc065478270ab4a78f.jpg)

To enable the feature, you will need to first navigate to the Options menu of Power BI Desktop and in ‘Preview features’ turn on the switch for ‘Quick measure suggestions’:

![](https://sumproduct.com/wp-content/uploads/2025/05/721daf2facbf195cfdb8d4d7d358ee62.jpg)

To access the Quick measure suggestions, select the Modeling tab within the Ribbon and then select ‘Quick measure’:

![](https://sumproduct.com/wp-content/uploads/2025/05/eb45f6f32c70920f0cea2aae4429047c.jpg)

Then, select the Suggestions tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/6c8a03d1791f5c214fd74f902c5aaf05.jpg)

Here, you can describe the measure you want to create and hit Generate (or the **ENTER** key) to get **DAX** measure suggestions:

![](https://sumproduct.com/wp-content/uploads/2025/05/a560b9241e59e35ee5d96d21f4f2e385.jpg)

Don’t just take it for granted though. You should always validate the **DAX** suggestions to make sure that it will meet your needs. If you’re satisfied with the suggested measure, you may click the ‘Add’ button to automatically add the measure to your model.

Amongst others, these are just some of the supported measure scenarios:

*   Aggregated columns with or without filters
*   Count of rows with or without filters
*   Aggregate per category
*   Mathematical operations
*   Selected value
*   If condition
*   Text operations
*   Time intelligence
*   Relative time filtered value
*   Most / least common value
*   Top **N** values for a category.

There are limitations though (sadly!). It should be noted that:

*   ‘Quick measure suggestions’ should not be seen as a replacement for learning **DAX**. The suggestions provided by the feature are meant to help fast track measure creation. However, you will still need to validate the **DAX** suggestions because they may be wrong or not match your intent
*   this feature is in experimental preview for users to test and give feedback. It should be noted that the design and functionality may go through significant changes – so don’t rely on it _just_ yet
*   the feature is powered by a machine learning model that is currently only deployed to US datacenters (East US and West US). Sadly, if your data is outside the US, the feature will be disabled by default unless your tenant administrator enables the ‘Allow user data to leave their geography tenant’ setting:

![](<Base64-Image-Removed>)

Certainly worth more than a passing glance!

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-quick-measure-suggestions-an-experimental-feature/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-quick-measure-suggestions-an-experimental-feature/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-quick-measure-suggestions-an-experimental-feature/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-quick-measure-suggestions-an-experimental-feature/#0)

[](https://sumproduct.com/blog/power-bi-blog-quick-measure-suggestions-an-experimental-feature/#0 "close")

top