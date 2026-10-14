"""Present reported synthetic PDF figures; this does not recompute source data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig = plt.figure(figsize=(12, 6), facecolor='#f5f7fa')
fig.text(.07, .92, 'Script Store Operations', fontsize=24, weight='bold', color='#15374a')
fig.text(.07, .865, 'Synthetic figures reported in the existing PDF | Sep 2025–Oct 8, 2026', fontsize=11)
for x, title, value in zip([.07,.30,.53,.76], ['Sessions','Est. revenue','Est. contribution','Scripts opened'], ['416','$280,352','$195,440','136']):
 fig.text(x,.75,title,color='#526574',fontsize=12)
 fig.text(x,.68,value,color='#15374a',fontsize=23,weight='bold')
ax=fig.add_axes([.13,.19,.76,.36],facecolor='#f5f7fa')
names=['City-limited','Exclusive','Boxed']; vals=[506,528,431]
bars=ax.barh(names,vals,color=['#24758b','#15374a','#7895a6'],height=.55)
ax.invert_yaxis(); ax.set_xlim(0,620); ax.set_xlabel('Reported average contribution per session (USD)')
for bar,val in zip(bars,vals): ax.text(val+9,bar.get_y()+bar.get_height()/2,f'${val}',va='center',weight='bold')
for spine in ax.spines.values(): spine.set_visible(False)
ax.tick_params(axis='both',length=0); ax.grid(axis='x',alpha=.15); ax.set_axisbelow(True)
fig.text(.07,.07,'Source totals not yet reconciled. Monthly chart and performance matrix excluded pending correction.',fontsize=10,color='#526574')
(root/'assets').mkdir(exist_ok=True)
fig.savefig(root/'assets/metrics-preview.png',dpi=160)
plt.close(fig)
