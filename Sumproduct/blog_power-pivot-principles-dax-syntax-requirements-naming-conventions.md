# Power Pivot Principles: DAX Syntax Requirements – Naming Conventions

**Source:** https://sumproduct.com/blog/power-pivot-principles-dax-syntax-requirements-naming-conventions/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: DAX Syntax Requirements – Naming Conventions

*   November 12, 2018

Power Pivot Principles: DAX Syntax Requirements – Naming Conventions
====================================================================

Power Pivot Principles: DAX Syntax Requirements – Naming Conventions
====================================================================

13 November 2018

_Welcome back to our Power Pivot blog. Today, we go over the DAX syntax naming requirements and conventions when it comes to tables, columns and measures._

A single Power Pivot window can contain numerous tables with several columns in each table. Couple this with the measures associated with each table and things may get a little confusing while working with such a large dataset. It would be only natural for us to give each table, column and measure a unique name… right?

Here are some built-in rules and safety nets in Power Pivot that we should keep borne in mind while working with our datasets.

We have touched in this topic briefly in a different blog explaining the syntax differences between tables, fields and measures, which may be found here >https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-tables-fields-and-measures<.

Here are the rules when naming tables, columns and measures:

*   within a single database all tables must have unique names
*   the names of the columns within each table must be unique
    *   columns in different tables may possess the same names
    *   when the same column name is referenced from two or more tables, we must use a fully qualified name (more on fully qualified names here >link to fully qualified names blog<)
*   all objects (tables, fields, and measures) are **case insensitive**
    *   for instance, the name ‘DATE TABLE’ and ‘Date Table’ would represent the same table.

It might be worth pointing out that Power Pivot does have a built-in duplicate name check, just in case we forget and give two tables or measures the same name:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-533.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-559.jpg)

If we give two columns within the same table duplicate names, Power Pivot will override the name and add a numerical counter at the end of the name, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/e8df3f06ac120382e120e5a095f3676e-5.jpg)

Power Pivot is friendly to work with after all, just remember to give your tables, columns and measures unique and meaningful names!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-dax-syntax-requirements-naming-conventions/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-dax-syntax-requirements-naming-conventions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-dax-syntax-requirements-naming-conventions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-dax-syntax-requirements-naming-conventions/#0)

[](https://sumproduct.com/blog/power-pivot-principles-dax-syntax-requirements-naming-conventions/#0 "close")

top