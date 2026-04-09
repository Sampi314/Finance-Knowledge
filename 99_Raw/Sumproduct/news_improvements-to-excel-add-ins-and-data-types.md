# Improvements to Excel Add-ins and Data Types

**Source:** https://sumproduct.com/news/improvements-to-excel-add-ins-and-data-types/

---

[Home](https://sumproduct.com/)

\> Improvements to Excel Add-ins and Data Types

*   November 23, 2021

Improvements to Excel Add-ins and Data Types
============================================

Improvements to Excel Add-ins and Data Types
============================================

23 November 2021

For many years, Microsoft Excel used to only allow two types of data: text and numbers. But that’s changing: Microsoft is opening up Excel to provide you with the freedom to create your own custom data types that can contain images, arrays and more.

A new JavaScript API was made available in Preview inside Excel in late November, which will allow you to create your own add-ins or extend previously existing ones to utilise the power of Data Types, resulting in a more integrated and next-generation experience within Excel. You can share these Data Types across your entire organisation and create add-ins or solutions which can connect data types to your own service or data.

In essence, Excel developers will be able to create new add-ins or update existing ones to use the JavaScript API.

This will open Excel up to far more custom data types, including content cards, images, matrices, arrays, and formatted number values. Excel has long had support for macros and add-ins, but Microsoft’s new APIs should make this a lot more efficient and easier for developers to implement.

The following is the complete list of types supported in the initial release:

*   entity values
*   formatted number values
*   web images
*   improved errors
*   arrays (only supported as a property of an entity and cannot be a standalone value currently).

With these value types, you are free to use them as both inputs and outputs for your experiences, and you can also arbitrarily combine them.

For example, you can create an entity value that contains properties of all the types, such as a web image for richer context about the entity, formatted values for things like currencies or dates, arrays of types for lists of data, and even additional entities through nesting.

This allows you to take your flat data and package it up into a logical value, as shown in the following example.

As an illustration, consider the following use of the API by Bloomberg:

![](<Base64-Image-Removed>)

By clicking on the icon next to ‘HYG US Equity’, you can inspect the Rich Data Type’s card, _viz._

![](<Base64-Image-Removed>)

If you click on the image presented, you can see the Fund Flows diagram:

![](<Base64-Image-Removed>)

You can make it bigger

![](<Base64-Image-Removed>)

or else reference it formulaically (see the boxed area on the right, referring to cell **F31**):

![](<Base64-Image-Removed>)

_Et voila!_

![](<Base64-Image-Removed>)

The first API being introduced, Range.valuesAsJson, allows you to both read and write data types, which works similarly to the Range.values API already in circulation. The major difference is that this new API can return augmented information about basic types (text, numbers, errors) as well as information about the new data types we have introduced. One other notable difference is the introduction of a schema that conforms to the types that are available to Excel.

Microsoft’s focus has been on exposing the structures so that you can bring your data to Excel using the schema and leverage many of the built-in experiences today. These structures are all driven by the schema. Here are some quick examples of JSON that adheres to the schema and creates a few types. Be sure to take note of the type field, which tells Excel what type a given value is:

![](<Base64-Image-Removed>)

Upon release, to access these new APIs, you will need:

*   a valid Insiders: Beta build of Excel
*   Windows version greater than or equal to 16.0.14626.10000 / Mac version greater than or equal to 16.55.21102600
*   the latest preview version of the js APIs.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/improvements-to-excel-add-ins-and-data-types/#0)
    
*   [Register](https://sumproduct.com/news/improvements-to-excel-add-ins-and-data-types/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/improvements-to-excel-add-ins-and-data-types/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/improvements-to-excel-add-ins-and-data-types/#0)

[](https://sumproduct.com/news/improvements-to-excel-add-ins-and-data-types/#0 "close")

top