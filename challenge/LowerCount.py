#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=138
# A: http://www.hacker.org/challenge/chal.php?answer=410&id=138&go=Submit

def main():
    text = 'mQmPtphqGrboHhmgaqVhCdwTwignlQvjIopDqVpgaNrwkAzVcnkHyNiPdSmgJmgrPiMjpnjdbuPucHnouwfKuPcybromnmbvfxJqRnnOvWsceZeYzRyqnkaaFsffjenxoIhqHnIzorlOdwZoxYmAuNwNnRppguwidvbtOqdbUngpZdbGqwYjfpLzPjRtwVwEqBbYmCqbKwuziCoEwPsIkJgruTbhdyWpvPztAodufjZxLaZcUeFaklSmeRfolohVbXoDfIqMqgIrQhzedqZlFwaBndQkQexBdLsCfXebrEfiOnSgYquyaqohxoDmLdDhwoOpgtkuRzeYziuvnuvnUuOtqasZueYpKfAkmKcJcWeocQvJguVsZfVovgrztAiryZivHqyMjoLyJdklKifmoWeOjVnogiiaBzDfrsWlOeAzPxltamqQiujZrpZrUcIlyktdJbhmNpDbltOlLnAqVhcxgObghpdcScgIiayqygUgwatiEzgzTsZgApUbbPynLfbzehzWsxcPbdcdfMucsCzjkWvjhMkiWuHfquqrcKwedqghiyHyMkSayRegeJcGw'
    print(len(list(filter(str.islower, text))))

if __name__ == '__main__':
    main()
