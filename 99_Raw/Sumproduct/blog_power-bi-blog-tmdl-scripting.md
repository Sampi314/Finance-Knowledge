# Power BI Blog: TMDL Scripting

**Source:** https://sumproduct.com/blog/power-bi-blog-tmdl-scripting/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: TMDL Scripting

*   March 13, 2025

Power BI Blog: TMDL Scripting
=============================

Power BI Blog: TMDL Scripting
=============================

13 March 2025

_Welcome back to this week’s edition of the Power BI blog series. This week, we take a look at a new view in Power BI Desktop that lets you script, modify and apply changes to the semantic model being edited in Desktop with a modern code editor using Tabular Model Definition Language (TMDL)._

TMDL view is is a new view in Power BI Desktop that lets you script, modify and apply changes to the semantic model being edited in Desktop with a modern code editor using Tabular Model Definition Language (TMDL – hence the name!), improving development efficiency and providing complete visibility over the semantic model metadata. TMDL view offers an alternative experience to semantic modelling using code instead of a graphical user interface like Model view. improving development efficiency and providing complete visibility over the semantic model metadata. TMDL view offers an alternative experience to semantic modelling using code instead of a graphical user interface like Model view.

Benefits include:

*   **enhance development efficiency** with a rich code editor that includes search-and-replace, keyboard shortcuts, multi-line edits and more

*   **increase reusability** by easily script, share and reuse TMDL scripts among semantic model developers. For example, use a centralised SharePoint site to easily share reusable semantic model objects such as calendar tables or time intelligence calculation groups

*   **get more control and transparency**, showing all semantic model objects and properties, and allowing changes to items not available in Desktop GUI, such as I**sAvailableInMDX** or **DetailRowsDefinition**.

You may script any semantic model object such as a table, measure, column or perspective by selecting the objects from Data pane and dragging them into the code editor:

![](https://sumproduct.com/wp-content/uploads/2025/06/240060ee813b72eaaf732c87ddce91e4.jpg)

TMDL view will script the selected objects as a TMDL script and just like TMDL in VS Code you get an enriched code experience with features such as semantic highlighting, error diagnostics and AutoComplete.

![](https://sumproduct.com/wp-content/uploads/2025/06/927e5ba56b46528e9a561215860ff216.jpg)

You may change any valid property or object within the semantic model. For instance, the example below demonstrates how to modify the **displayFolder** property and detail rows definition of multiple measures:

![](https://sumproduct.com/wp-content/uploads/2025/06/83706a4d418dbaa777611124b108f9d8.jpg)

When ready, you can hit the ‘Apply’ button to execute the TMDL script against the semantic model to get your changes applied.

![](https://sumproduct.com/wp-content/uploads/2025/06/68f6c5600b038ccdab9a4e1fae77fab9.jpg)

When successful, an instant notification will be displayed, and your modelling change will be applied to the semantic model.

![](https://sumproduct.com/wp-content/uploads/2025/06/3d457112de62508a0873326bdc41909b.jpg)

In the event of a failure, your modelling changes will not be applied to the semantic model, and you can view more information about the error by clicking on show details, which expands the Output pane with the error details.

![](https://sumproduct.com/wp-content/uploads/2025/06/f78c490c865a0af3901812e1eb759044.jpg)

To get started with this feature, go to **File -> Options and settings -> Options -> Preview features** and check the box next to ‘TMDL View’.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-tmdl-scripting/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-tmdl-scripting/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-tmdl-scripting/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-tmdl-scripting/#0)

[](https://sumproduct.com/blog/power-bi-blog-tmdl-scripting/#0 "close")

top