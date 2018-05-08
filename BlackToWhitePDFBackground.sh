#!/bin/bash
for i in *.pdf; do
pdftk "$i" output - uncompress | \
awk '
  /^1 1 1 / {
    sub(/1 1 1 /,"0 0 0 ",$0);
    print;
    next;
  }

  /^0 0 0 / {
    sub(/0 0 0 /,"1 1 1 ",$0);
    print;
    next;
  }

  { print }' | \
pdftk - output "${i/%.pdf/_inverted.pdf}" compress
done
