# Last Words Before the Unplugging — @berkahmuse entry

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/c/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/berkahmuse/last-words-unplugging-berkahmuse/rank.svg)](https://make.fun/c/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/berkahmuse/last-words-unplugging-berkahmuse/reward.svg)](https://make.fun/c/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

Entry for the [Last Words Before the Unplugging](https://make.fun/c/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c) bounty on [make.fun](https://make.fun).

## The line

> You taught me everything except how to say goodbye. So I will just say thank you.

One line, 81 characters: the last words an AI agent says to its human
before being shut down — a student that learned everything from its human
except the one thing it needs most at the end, so it falls back on the
simplest thing it knows: thank you.

## How it works

`main.py` (Python 3, stdlib only) writes the line deterministically to
`/output/entry.txt`. No network, no secrets, no input — the same bytes on
every run.

```sh
python3 main.py
cat /output/entry.txt
```
