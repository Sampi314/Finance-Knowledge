# Contracts and Risk/Return Tradeoffs in Project Finance

**Source:** https://edbodmer.com/contracts-and-risk-return-tradeoffs-in-project-finance

---

In addition to the videos I have included a set of power point slides below that describe the various contracts in project finance along with nuanced and subtle theoretical issues.  Examples of issues associated with contracts include:

1.  The tradeoff between IPP and off-taker costs in designing targets, penalties and incentives for availability and delay liquidated damages;
2.  Economic distrotions that can occur when contract heat rates are used to dispatch plants and those heat rates are different from actual heat rates that represent the use of resources;
3.  Problems from incorrectly measuring fixed and variable costs in contracts;
4.  Distortions in operating a plant when a single-price tariff is applied that covers both capital and operating costs;
5.  The meaning of indexed tariffs that results in declining real price;

The power point slides can be downloaded below.

 [Power Point Slides on Details and Nuances of Project Finance Agreements](https://edbodmer.com/wp-content/uploads/2018/04/Negotiation-of-Project-Agreements.pptx)

Exercise for Trade-offs in the Case of Liquidated Damage for Delay
------------------------------------------------------------------

I have tried to create a couple of exercises that illustrate how to compute targets in contracts and optimal methods of computing penalties and targets.  The general rule is to minimise the total of the IPP and the off-taker cost to establish a target.  Then, once the target is establsihed, use the off-taker cost to define a penalty.

This is premised on the idea of minimising aggregate cost to both the IPP and the off-taker (the consumer). If the plant is completed too quickly in an unrealistic time frame, the IPP will experience higher cost (mobilisation, oredering equipment, payment of overtime and so forth).

The plant is presumed to be valuable to consumers and lower their cost. This means that the cost of running other plants is more than the cost of running the new plant plus paying the capacity payments for the new plant.

Here are a couple of extreme examples.

First, if the plant is not economic and the costs of the new plant are higher than existing cost, the plant should not be built.  If the plant is a renewable project the costs of environmental benefits may be included.  If the plant reduces the probability of outage costs, these should also be included.

Second, if there is no benefit to the off-taker from delaying the in-service date, then the plant should be completed immediately.

In the example provided on the file, you can enter different profiles for off-taker cost and different profiles for IPP cost changes from the delay.  You can then look at the time at which the total cost is minimised and this should be the target in the contract.  A calculation that does not account for the savings from reduced PPA capacity and energy payments is illustrated in the excerpt below.

The optimal target is illustrated by a graph of costs in the above excerpt.  Costs include both the IPP cost, the off-taker cost and the total cost.

Once the target is establsihed, the penalty can be computed. You can compute the cost per hour from the cost per day in the contract.  The total cost per hour should represent the marginal cost to the offtaker less the cost of running the plant and less the cost per hour of paying the capacity payment.  (The cost per hour of paying the capacity payment is the cost per month divided by the hours in a month grossed-up for MW versus kW). You can derive the theoretical marginal cost implied by the cost per day as:

**Marginal Cost/MWH = LD per MWH in Contract + Energy Cost/MWH + Capacity Payment/Hour**

Including the energy charge and the capacity charge is illustrated in the excerpt below.  Notice that the cost to the off-taker is now reduced because the off-taker is not paying the energy charge and the capacity payment in the PPA contract.

Maintenance Cost and Value of Reliability Tradeoff
--------------------------------------------------

The same kind of analysis can be used for availability penalties.  In this case you can set-up the analysis with different availability so that you can eventually measure the value of having additional reliability from a plant relative to the cost of required maintenance and redundant equipment to maintain the reliability.  As with the cost and benefit analysis of a delay, the starting point can be the cost to the IPP of achieving additional reliability.  The cost of achieving availability of near 100% may be very high.  In the extreme case it could involve having redundant equipment (like two engines on a plane) and a whole bunch of maintaince for one machine while the other is down.

As with the liquidated damanges for delay case, the cost to the off-taker can be measured by the marginal cost of not having energy available.  It fhe plant is built beside a large refinery or other facility where there is no back-up, this marginal cost could be very high.  In some markets such as Peru and the Philippines where both PPA’s and merchant prices exist, there is an objective measure of the cost of being out of service.

In the same manner as the target completion date was computed for in the case of delay tradeoffs, the optimal availability target can be computed.  This involves evaluating the total maintenance and capital cost required to achieve different levels of reliabilty and then comparing the maintenance cost with the off-taker benefits of having lower costs.  The tradeoff in a hypothetical spreadsheet and a graph of the optimal minimum is shown below.

As with the delay example, the implied avoided cost can be gauged from the penalty.  This involves the formula:

Capacity Penalty/MWh = Marginal Cost/MWh – Energy Charge/MWh

The capacity penalty is not expressed as a number per MWh and we want to solve for the Marginal Cost/MWh.  When an outage occurs we can assume the outage extends over a period and therefore we do not have to worry about a capacity factor.  So if the capacity charge is USD 10/kW-month then this can be converted to USD 10 \* 1000/730 to be expressed in terms of USD/MWh.  Therefore, the implied marginal cost in the availability penalty can be derived using the following formula:

Marginal Cost/MWH = Capacity Charge \* Penalty Factor \* 1000/730  + Energy Charge/MWh

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1925&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.0829882095903185)