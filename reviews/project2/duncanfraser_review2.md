# Predicting AirBnB Price
*Duncan Fraser*

## Strengths
- Stating the problem you're trying to solve from the onset
- Your commentary after each heading made it easier to follow your thought process, especially with your rationale for excluding certain features.
- Good idea narrowing the focus to a single neighborhood with a lot of data.  Building a solid self-contained model should allow you to scale it to other places with different characteristics.
- Defining your own categorical target was a great idea.  I'm definitely going to use that strategy in the future.

## Improvements
- You can probably hone down the amount of information presented or combine some of the cells.  It's pretty busy towards the bottom, which makes it easy to lose track.

## Questions
- What made you choose such a low p-value threshold?  Were you trying to just lower it enough to eliminate some features, or was there a more specific reason?

## Code
- Lot of commenting.
- I could be wrong, but it looks like there's a few functions that are introducted but not actually used.  The k-fold stuff, for example.

## Next Steps
- Keep refining the question that you're trying to answer and how you define your target.  Is 1 standard deviation above the mean actually overpriced, or is there something in particular about those listings that justifiably higher than average.
- Defintely keep exploring different features that you can include.  