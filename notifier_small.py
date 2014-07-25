import urllib.request,re,time
def _(p,t):
	print(p)
l=0
u=urllib.request
while 1:
	m=re.compile('title": "(?P<N>[^"]*)".*utc.*(?P<T>[0-9]+)').search(str(u.urlopen(u.Request("http://www.reddit.com/r/funny/new.json?sort=new",headers={"User-Agent":""})).read()))
	t=int(m.group("T"))
	if t>l:
		l=t
		_(m.group("N"),l)
	time.sleep(90)
