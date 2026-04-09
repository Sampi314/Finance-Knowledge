# Power BI Blog: Hybrid Tables in Power BI Premium

**Source:** https://sumproduct.com/blog/power-bi-blog-hybrid-tables-in-power-bi-premium/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Hybrid Tables in Power BI Premium

*   January 19, 2022

Power BI Blog: Hybrid Tables in Power BI Premium
================================================

Power BI Blog: Hybrid Tables in Power BI Premium
================================================

20 January 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at Hybrid Tables, including an enhancement to incremental refresh for Power BI Premium._

Power BI Premium now supports Hybrid Tables, including an enhancement to incremental refresh: incremental refresh augmented with real-time data. Now users may see largescale improvements in performance in import mode and the latest data changes in the data warehouse reflected in user reports without having to perform a dataset refresh.

Up until now, dataset creators sometimes had to make hard trade-offs between query performance and the currency of data. Import mode provides better performance, yet data freshness poses challenges if new data arrives at a very high cadence. It is both resource intensive and inefficient to import data into a dataset in very short intervals. DirectQuery mode, on the other hand, delivers data freshness, yet at the expense of report performance. Because Power BI doesn’t import the data but translates the report queries into data source queries, the latest data changes are quicky picked up, but the query / response roundtrips between Power BI and the data source take time and slow down the reports.

As the following diagram illustrates, a Hybrid Table may help to strike the right balance between query performance and data freshness. A Hybrid Table is essentially a (large) table that has one or multiple import-mode partitions as well as another partition in DirectQuery mode. If the DirectQuery partition is sufficiently small in comparison to the import-mode partitions, the query / response roundtrips between Power BI and the data source should still be reasonably fast while access to the bulk of the data is already super-fast in import mode. Import and DirectQuery data is presented to users as a single table with business definitions and calculations.

![](<Base64-Image-Removed>)

The following screenshot shows how to configure an incremental refresh policy with real time in Power BI Desktop. Having published the dataset to a Premium Per User (PPU) workspace or a workspace on a Premium capacity, Power BI will automatically apply the refresh policy and partition the table as a Hybrid Table during data refresh.

![](<Base64-Image-Removed>)

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-hybrid-tables-in-power-bi-premium/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-hybrid-tables-in-power-bi-premium/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-hybrid-tables-in-power-bi-premium/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-hybrid-tables-in-power-bi-premium/#0)

[](https://sumproduct.com/blog/power-bi-blog-hybrid-tables-in-power-bi-premium/#0 "close")

top