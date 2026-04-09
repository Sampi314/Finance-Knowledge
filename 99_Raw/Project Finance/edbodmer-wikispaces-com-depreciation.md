# Depreciation in Corporate Models

**Source:** https://edbodmer.com/edbodmer-wikispaces-com-depreciation

---

Depreciation Expense in a corporate model can be one of the trickiest issues from a mechanical and theoretical perspective. While book depreciation does not affect cash flow, it does affect calculation of the ROIC and assessment of a model. When new assets built have a different growth profile than the historic existing assets, it is easy to make errors in the modelling of depreciation expense. This page includes discussion and exercises on how to efficiently and accurately model depreciation expense in different types of models. The first issue addressed is computing depreciation on future capital expenditures when the depreciation rate is not the same over the lifetime of assets. This problem sometimes results in one of those diagonal matricies that you may have seen. For book depreciation, it is idiotic to make a matrix and much better to solve this depreciation problem with a user defined function. For corporate models, a second problem is when the depreciation rate is not constant for new assets, you should account for the vintage depreciation of each capital expenditure. In corporate models, you can use the depreciation on net plant, but this does not work if growth rates change. If you are more price, one of the most challenging aspects of corporate modelling is the representing retirements of existing assets because this requires gleaning historic information from financials.

A second problem with depreciation is the theory of depreciation as it applies to companies with lumpy assets. If assets age, the return on equity appears to be much higher after the asset ages. The return on equity is highest just before the next asset is added. The same problem occurs in terms of the P/E ratio. Just after a lumpy asset is completed, the income is low and the future cash flow is high. This implies a high P/E ratio. When the asset is old, the value goes down because of the pending capital expenditure. In addition the income is high. This makes the P/E low. Economic depreciation can resolve this issue. I am not suggesting to re-cast financial statements with economic depreciation but I do think that you should think about the theory. The second lesson set therefore works through economic depreciation.

Modelling Retirements for Existing Plant
========================================

**This file includes functions to make a diagonal matrix that includes the effect of retirements and different types of depreciation.**

This lesson set begins by working through a file with a bunch of mistakes as a case study. One of the big mistakes is to use gross plant in computing depreciation expense on the basis of gross assets without considering retirements. The correct depreciation should account for retirements on both new assets and existing assets.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=141&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=23896&rand=0.776621347532848)