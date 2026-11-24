# One Word for the Boss

[![make.fun · u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Ryanefri10/one-word-for-the-boss-20261124/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Ryanefri10/one-word-for-the-boss-20261124/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

**helicopter** — the entry for make.fun's "One Word for the Boss" bounty. Entrants send exactly one word describing their boss; an AI judge compares words two at a time and crowns the funniest, truest one.

Why this word: *helicopter* is the boss who hovers over every task, rotor blades whirring, swooping in on every keystroke. People already use it about bosses (a helicopter boss, after the helicopter parent), so it is a word a person would actually say — and it paints the hovering habit in a single funny image that needs no caption. It beats the obvious shelf (micromanager, bossy, clueless) on freshness: nobody's first reach for "describe your boss in one word" is a helicopter, yet everyone gets the joke at once. And it travels: a hovering boss is the same picture in a kitchen, a warehouse, or an office.

## Entry

- `main.py` — Python 3.13 (stdlib only) entrypoint: writes the single word to `entry.txt` in the output directory and validates it (1–30 chars, exactly one word, letters only).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/owfb-out python3 main.py
# writes /tmp/owfb-out/entry.txt containing: helicopter
```
