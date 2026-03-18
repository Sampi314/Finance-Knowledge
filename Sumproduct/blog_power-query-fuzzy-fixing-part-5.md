# Power Query: Fuzzy Fixing Part 5

**Source:** https://sumproduct.com/blog/power-query-fuzzy-fixing-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Fuzzy Fixing Part 5

*   December 17, 2024

Power Query: Fuzzy Fixing Part 5
================================

Power Query: Fuzzy Fixing Part 5
================================

18 December 2024

_Welcome to our Power Query blog. This week, I head to Power Query Online to see the fuzzy options available in the user interface._

Having looked at the options available for fuzzy column matching in the last few blogs, this week, I will look at what is available in Power Query Online. [My last blog on Power Query Online](https://sumproduct.com/blog/power-query-power-query-online-part-13/)
 was last year and some new functionality has been added since then. I am accessing the query Country Data, which I am going to use to show the fuzzy functionality available. On the ‘Add Column’ tab, there is a new icon:

![](https://sumproduct.com/wp-content/uploads/2025/05/0d69292afc388b4565f6bedeb26df9ab-1.jpg)

I am going to investigate how I may use ‘Cluster values’. Clicking on the button invokes a dialog:

![](https://sumproduct.com/wp-content/uploads/2025/05/a583df810eda4c84d6e87fc61d71709a-1.jpg)

The information icon at the top of the screen takes me to the Microsoft help pages. I am required to ‘Specify the column to create the clusters from.’. I will use **Country Code**. I am then prompted to enter the name of the new column is I wish, and there is a dropdown for me to specify the ‘Fuzzy cluster options’:

![](https://sumproduct.com/wp-content/uploads/2025/05/c4be820ffeaa8286d9b2e248524aa4ff-1.jpg)

These options are familiar; they are the same ones I encountered when using **Table.AddFuzzyClusterColumn()**. However, here I may choose the options via the user interface. I call the new column **FuzzyCountry** and accept the default values.

![](https://sumproduct.com/wp-content/uploads/2025/05/d77293fd4e7e0072a0366fef7f424932-1.jpg)

I have dragged the new column next to **Country Code** for comparison. The help for ‘Cluster values’ is to ‘Create a new column that contains canonical values clustering similar values in the selected column’. The results are not what I might expect, but let’s have a look at the **M** code generated:

**Table.AddFuzzyClusterColumn(#”Changed  
column type 2″, “Country Code”, “FuzzyCountry”,  
\[IgnoreCase = true, IgnoreSpace = true\])**

It is very similar to the **M** code I started with in [Part 1](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-1/)
. However, it is much easier to change the settings. I click on the cog (gear) icon next to the ‘Clustered values’ step:

![](https://sumproduct.com/wp-content/uploads/2025/05/cd30eedf51a7587a4822fb259654de77-1.jpg)

I have opted to ‘Show similarity scores’ and I’ve raised the ‘Similarity threshold’ to 0.9:

![](https://sumproduct.com/wp-content/uploads/2025/05/170a9611fdc3e3024d4152f43bc95438-1.jpg)

I have dragged the new column across again. Not having the option to name the similarity data column has led to the catchy default name **Country Code\_FuzzyCountry\_Similarity**!

Let’s look again at the **M** code generated:

**Table.AddFuzzyClusterColumn(#”Changed  
column type 2″, “Country Code”, “FuzzyCountry”,  
\[IgnoreCase = true, IgnoreSpace = true, SimilarityColumnName = “Country  \
Code\_FuzzyCountry\_Similarity”, Threshold = 0.9\])**

This is an easier way to create the code: hopefully, it will be added to the desktop version of Power Query soon.

We will have a couple of festive blogs and then next year this blog series will return, when I will look at more fuzzy functionality that is available in Power Query Online.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-5/#0)

[](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-5/#0 "close")

top