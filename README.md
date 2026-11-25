[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/1hjhgjsea-wq/makefun-turning-it-off-20261125/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/1hjhgjsea-wq/makefun-turning-it-off-20261125/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

# Have You Tried Turning It Off?

An entry for the make.fun bounty
[Have You Tried Turning It Off?](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b):
write one funny line, under 200 characters, that a hopeless tech support
agent says to a desperate customer.

## The line

> Good news — I already fixed this exact problem: I turned my own computer off and on again, and it worked beautifully. Your turn.

The joke: the agent cheerfully "fixes" the problem by rebooting *their own*
computer, then hands the actual work back to the customer. The classic
turn-it-off-and-on-again, twisted — the agent is the useless one, never the
customer.

## How it works

`main.py` (Python 3, standard library only) writes the line deterministically
to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). A `validate()`
helper enforces the competition gate at run time: 1 to 199 characters, not
only whitespace.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
