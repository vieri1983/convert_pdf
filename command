
#to get all the http links under view-source:http://mp.weixin.qq.com/s/QtdMkt9giEEnvFTQzO9u7g
grep -Eoi '<a [^>]+>' source.txt | grep -Eo 'href="[^\"]+"' | grep -E '(http|https)://[^/"]+' | sed 's/^href="//' | sed 's/"$//' > links
