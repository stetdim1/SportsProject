path = 'Statistics\ADE 4-3 BRI _ Adelaide United - Brisbane Roar _ Statistics.html'
# path = 'Statistics\POL 1-2 POR _ Poland - Portugal _ Statistics.html'
# path = 'Statistics\ENG 0-1 ITA _ England - Italy _ Statistics.html'
file = open(path)
content = file.read()

s ='<div class="statText statText--homeValue">64%</div><div class="statText statText--titleValue">'
print(len(s))


s1 = '</div><div class="statText statText--awayValue">41%</div></div>'
s2 = '%'

f1 = '>Match<'
f2 = '>1st Half<'
f3 = '>2nd Half<'
f4 = '>Extra Time<'

print(content.find(f1))
print(content.find(f2))
print(content.find(f3))
print(content.find(f4))
print('------------------')
print(content.find(f2) - content.find(f1))

d = '>Match</a></span></li><li class="divider"></li><li id="statistics-1-statistic" class="li1"><span><a onclick="detail_tab([&#39;statistics&#39;, &#39;1-statistic&#39;]);">'

print(len(d))