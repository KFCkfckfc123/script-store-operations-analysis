import json,collections
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import openpyxl
root=Path(__file__).resolve().parents[1]
w=openpyxl.load_workbook(root/'workbook/Script_Store_Operations_Synthetic_Compatible.xlsx',data_only=True)
raw=[list(r[:14]) for r in list(w['Raw Data'].values)[1:]]
s=[list(r[:27]) for r in list(w['Script List'].values)[1:]]
raw=[[v.strftime('%Y-%m-%d') if hasattr(v,'strftime') else v for v in r] for r in raw]
j={'threshold':w['Assumptions']['B3'].value,'avgthreshold':w['Assumptions']['B4'].value}
monthly=collections.Counter(r[13][:7] for r in raw);ed=['City-limited','Exclusive','Boxed'];labels=ed;nums=[sum(r[11] for r in raw if r[10]==e)/sum(r[10]==e for r in raw) for e in ed];counts=[sum(r[10]==e for r in raw) for e in ed]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig=plt.figure(figsize=(14,10),facecolor='white');gs=fig.add_gridspec(2,2,left=.08,right=.94,bottom=.15,top=.73,hspace=.45,wspace=.27)
fig.text(.08,.95,'Script Store Operations',fontsize=24,weight='bold',color='#19546B');fig.text(.08,.91,'Synthetic records | Sep 2025–Oct 8, 2026 | Estimated contribution excludes operating expenses')
summary=[f'{len(raw):,}',f'${sum(r[8] for r in raw):,.0f}',f'${sum(r[11] for r in raw):,.0f}',f'{sum(r[17]>0 for r in s):,}']
for x,t,v in zip([.08,.31,.54,.77],['Sessions','Estimated Revenue','Estimated Contribution','Scripts Opened'],summary):fig.text(x,.84,t,color='#526574');fig.text(x,.79,v,fontsize=23,weight='bold',color='#19546B')
a=fig.add_subplot(gs[0,0]);keys=sorted(monthly);vs=[monthly[k] for k in keys];a.plot(range(len(keys)),vs,color='#19546B',marker='o');a.set_xticks(range(len(keys)));a.set_xticklabels(keys,rotation=55,ha='right',fontsize=8);a.set_title('Monthly Sessions');a.set_ylim(0,36);a.yaxis.set_major_locator(MaxNLocator(integer=True));a.annotate('Partial month: 8',xy=(13,8),xytext=(8,12),arrowprops={'arrowstyle':'->'},fontsize=9)
b=fig.add_subplot(gs[0,1]);b.bar(labels,nums,color=['#24758b','#19546B','#7895a6']);b.set_ylim(0,610);b.set_title('Contribution per Session by Edition (USD)')
for i,(v,n) in enumerate(zip(nums,counts)):b.text(i,v+10,f'${v:.2f}\nn={n}',ha='center',fontsize=9)
c=fig.add_subplot(gs[1,:]);opened=[r for r in s if r[17]>0];c.scatter([r[17] for r in opened],[r[23] for r in opened],s=35,color='#24758b',alpha=.65);c.axvline(j['threshold'],color='#B05A4A',ls='--');c.axhline(j['avgthreshold'],color='#B05A4A',ls='--');c.set_title('Script Performance — 136 Opened Scripts');c.set_xlabel('Observed Sessions');c.set_ylabel('Estimated Contribution / Session (USD)');c.text(.98,.96,f"Opened-script medians: {j['threshold']:g} sessions / ${j['avgthreshold']:g}",transform=c.transAxes,ha='right',fontsize=9)
for ax in [a,b,c]:ax.spines[['top','right']].set_visible(False);ax.grid(axis='y',alpha=.15);ax.set_axisbelow(True)
fig.text(.08,.075,'Full-month counts range from 29 to 32. Seven months tie at 32; August is not a unique peak.',fontsize=10)
fig.text(.08,.045,'Scenario acquisition costs are modeled. Edition comparisons do not prove causal effects or justify purchases alone.',fontsize=10)
fig.savefig(root/'assets/dashboard.png',dpi=150);fig.savefig(root/'Script_Store_Operations_Dashboard_Synthetic.pdf');plt.close(fig)
