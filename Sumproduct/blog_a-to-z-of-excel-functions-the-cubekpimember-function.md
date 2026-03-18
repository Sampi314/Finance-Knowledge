# A to Z of Excel Functions: The CUBEKPIMEMBER Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubekpimember-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CUBEKPIMEMBER Function

*   March 1, 2018

A to Z of Excel Functions: The CUBEKPIMEMBER Function
=====================================================

A to Z of Excel Functions: The CUBEKPIMEMBER Function
=====================================================

2 March 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CUBEKPIMEMBER** function._

**The CUBEKPIMEMBER function**

When the workbook is connected to a Microsoft SQL Server 2005 Analysis Services or later data source, this function returns a key performance indicator (KPI) property and displays the KPI name in the cell. A KPI is a quantifiable measurement, such as monthly gross profit or quarterly employee turnover, that is used to monitor an organisation’s performance.

![](https://sumproduct.com/wp-content/uploads/2025/05/623f0020278cb741ecd8eea805074693.jpg)

The **CUBEKPIMEMBER** function employs the following syntax to operate:

**CUBEKPIMEMBER(connection, kpi\_name, kpi\_property, )**

The **CUBEKPIMEMBER** function has the following arguments:

*   **connection:** this is required and represents a text string of the name of the connection to the cube
*   **kpi\_name:** this is also required. This is a text string of the name of the KPI in the cube
*   **kpi\_property:** again, this is required. This is the KPI component returned and can be one of the following:

![](https://sumproduct.com/wp-content/uploads/2025/05/81bcf54ad5d11e31a368b6db87357dd4.jpg)

*   **caption:** this is optional. This represents an alternative text string that is displayed in the cell instead of **kpi\_name** and **kpi\_property**.

It should be further noted that:

*   the **CUBEKPIMEMBER** function is supported only when the workbook is connected to a Microsoft SQL Server 2005 Analysis Services or later data source
*   when the **CUBEKPIMEMBER** function evaluates, it temporarily displays a “#GETTING\_DATA…” message in the cell before all of the data is retrieved
*   to use the KPI in a calculation, specify the **CUBEKPIMEMBER** function as a **member\_expression** argument in the **CUBEVALUE** function
*   if the connection name is not a valid workbook connection that is stored in the workbook, **CUBEKPIMEMBER** returns an _#NAME?_ error value. If the Online Analytical Processing (OLAP) server is not running, not available or returns an error message, **CUBEKPIMEMBER** returns a _#NAME?_ error value
*   **CUBEKPIMEMBER** returns an _#N/A_ error value when **kpi\_name** or **kpi\_property** is invalid
*   if you specify **KPIValue** for **kpi\_property**, only **kpi\_name** is displayed in the cell
*   **CUBEKPIMEMBER** may return an _#N/A_ error value if you reference a session-based object, such as a calculated member or named set, in a PivotTable when sharing a connection, and that PivotTable is deleted or you convert the PivotTable to formulae (on the ‘Options’ tab in the Ribbon, in the ‘Tools’ group, click ‘OLAP Tools’, and then click ‘Convert to Formulas’).

Please see my examples below:

**\=CUBEKPIMEMBER(“Sales”,”MySalesKPI”,1)**

**\=CUBEKPIMEMBER(“Sales”,”MySalesKPI”, KPIGoal,”Sales KPI Goal”)**

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubekpimember-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubekpimember-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubekpimember-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubekpimember-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubekpimember-function/#0 "close")

top