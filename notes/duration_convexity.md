# Duration And Convexity

## Macaulay Duration

Macaulay duration is the present-value weighted average time to receive a bond's
cash flows.

Intuition:

```text
Longer cash-flow timing -> higher duration -> higher rate sensitivity
```

## Modified Duration

Modified duration estimates first-order price sensitivity to yield changes.

Approximation:

```text
dP / P ~= -D_mod * dy
```

If modified duration is 8 and yields rise by 10bp:

```text
dP / P ~= -8 * 0.001 = -0.8%
```

## Convexity

Convexity adds second-order curvature:

```text
dP / P ~= -D_mod * dy + 0.5 * Convexity * dy^2
```

Convexity matters more when yield moves are large.

## Practical Interpretation

```text
Rate cut -> yields down -> bond prices up
Rate hike -> yields up -> bond prices down
Longer maturity -> higher duration and convexity
```
