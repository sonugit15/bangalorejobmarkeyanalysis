from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/job_listings_sample.csv'); out=ROOT/'outputs'; out.mkdir(exist_ok=True)
print('SAMPLE LISTINGS:',len(df))
print('\nLISTINGS BY ROLE\n',df.role.value_counts())
print('\nAVERAGE SAMPLE CTC BY ROLE (LPA)\n',df.groupby('role').annual_ctc_lpa.mean().round(2).sort_values(ascending=False))
skills=df.skills.str.split(';').explode().str.strip().value_counts()
print('\nSKILLS FREQUENCY\n',skills)
df.role.value_counts().sort_values().plot(kind='barh',title='Sample Listings by Role')
plt.xlabel('Count'); plt.tight_layout(); plt.savefig(out/'listings_by_role.png'); plt.close()
df.groupby('role').annual_ctc_lpa.mean().sort_values().plot(kind='barh',title='Average Sample CTC by Role')
plt.xlabel('LPA — synthetic sample'); plt.tight_layout(); plt.savefig(out/'sample_ctc_by_role.png'); plt.close()
skills.sort_values().plot(kind='barh',title='Skills Mentioned in Sample')
plt.xlabel('Count'); plt.tight_layout(); plt.savefig(out/'skills_frequency.png'); plt.close()
