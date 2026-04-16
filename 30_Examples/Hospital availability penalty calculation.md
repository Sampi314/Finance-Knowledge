---
type: example
title: "Hospital availability penalty calculation"
illustrates: ["[[Availability payments]]"]
updated: 2026-04-16
---

# Hospital availability penalty calculation

## Setup

We are modeling a hospital public-private partnership where the project company receives an availability payment. We need to calculate the revenue penalty if the hospital fails to meet its availability requirements due to poor maintenance (e.g., a burst water line).

## Assumptions

- **Total Rooms:** 100 standard rooms
- **Measurement Period:** 90 days
- **Availability Requirement:** At least 95 rooms must be available at any point in time. (Permitted unavailable rooms = 5)
- **Service Fee Structure:** Room availability accounts for 100% of the service fee.
- **Incident:** 55 rooms are unavailable for 45 days.

## Walk-through

1. Calculate the number of unpermitted unavailable rooms:
   - 55 unavailable rooms - 5 permitted unavailable rooms = 50 unpermitted unavailable rooms.
2. Calculate the shortfall in room-days:
   - 50 rooms * 45 days = 2,250 shortfall room-days.
3. Calculate the maximum potential room-days in the period:
   - 100 total rooms * 90 days = 9,000 maximum room-days.
4. Calculate the percentage reduction in the availability fee:
   - 2,250 shortfall room-days / 9,000 maximum room-days = 0.25, or 25%.

## Result

The project company will face a 25% reduction in its availability revenue for the period due to the rooms being out of commission.

## What this teaches

- Penalties are proportional to the shortfall in the defined output specification metric (e.g., room-days).
- Deductions directly impact the project's bottom-line revenue, penalizing poor maintenance.
- Contracts typically allow a small buffer (e.g., 5 permitted unavailable rooms) before penalties trigger.
