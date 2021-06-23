
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rumah = pd.read_csv('sn13_krt.csv')

rumah = rumah[['b1r1', 'b1r5', 'b2r1', 'b6r1', 'b6r2', 'b6r3', 'b6r5', 'b6r6', 'b6r7', 'exp_cap', 'wert']]
rumah.columns = ['prov', 'desa_kota', 'anggota_rt', 'tipe_bangunan', 'jumlah_rt', 'status_milik', 'atap', 'dinding', 'lantai', 'exp_cap', 'bobot']

total = rumah.isnull().sum().sort_values(ascending=False)
percent = (rumah.isnull().sum()/rumah.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)

# memberi label desa atau kota
rumah.loc[rumah['desa_kota'] == 1, 'desa_kota'] = 'kota'
rumah.loc[rumah['desa_kota'] == 2, 'desa_kota'] = 'desa'

# memberi label kepemilikan rumah
rumah.loc[rumah['status_milik'] == 1, 'kepemilikan'] = 1
rumah.loc[rumah['status_milik'] == 2, 'kepemilikan'] = 0
rumah.loc[rumah['status_milik'] == 3, 'kepemilikan'] = 0
rumah.loc[rumah['status_milik'] == 4, 'kepemilikan'] = 0
rumah.loc[rumah['status_milik'] == 5, 'kepemilikan'] = 0
rumah.loc[rumah['status_milik'] == 6, 'kepemilikan'] = 0
rumah.loc[rumah['status_milik'] == 7, 'kepemilikan'] = 0

# perhitungan bobot
wt_sum = lambda x: np.sum(x, weights=rumah.loc[x.index, "bobot"])
wt_mean = lambda x: np.average(x, weights=rumah.loc[x.index, "bobot"])

# untuk melihat berdasarkan status_milik, kita grouping dan reset index
rumah_milik = rumah.groupby("kepemilikan").agg(kepemilikan=("kepemilikan", "count"), bobot=("bobot", "sum"))
rumah_milik.reset_index(drop=True).astype(int)

# 1. data yang menampilkan tingkat kempemilikikan rumah nasional
sns.barplot(x=rumah_milik["kepemilikan"].index, y=rumah_milik["bobot"])

# perhitungan presentase
a = rumah_milik["bobot"].loc[0]
b = rumah_milik["bobot"].loc[1]
prcntg = a/(a+b)*100
print("Presentase dari rumah tangga yang tidak memiliki rumah keseluruhan: ", prcntg)

# 2. Perbandingan kepemilikan desa dan kota
rumah_urban = rumah.groupby(["desa_kota", "kepemilikan"]).agg(desa_kota=("desa_kota", "count"),
                                                              kepemilikan=("kepemilikan", "count"),
                                                              bobot=("bobot", "sum"))
rumah_urban.astype(int)

# Barplot untuk perbandingan desa_kota
sns.barplot(x=rumah_urban["desa_kota"].index, y=rumah_urban["bobot"])


# 3. perbandingan tingkat kepemilikan rumah di pulau jawa dan non-jawa
def perov(x):
    if x > 30 and x < 40:
        return "jawa"
    else:
        return "non_jawa"


rumah["pulau_jawa"] = rumah[["prov"]].applymap(perov)
rumah_prov = rumah.groupby(["pulau_jawa", "kepemilikan"]).agg(pulau_jawa=("pulau_jawa", "count"),
                                                              bobot=("bobot", "sum"))
sns.barplot(x=rumah_prov["pulau_jawa"].index, y=rumah_prov["bobot"])

# 4. Kualitas bangunan rumah secara sederhana (belum)

# 5. korelasi antara pengeluaran dengan tingkat kepemilikan rumah
rumah_bb = rumah.groupby(["status_milik"]).agg(exp=("exp_cap", wt_mean), bobot=("bobot", "sum"))

# Log Pengeluaran per Kapita
x_pce = rumah_bb["bobot"].index
y_pce = np.log(rumah_bb["exp"])

# Plot
plt.scatter(x_pce, y_pce, alpha=0.4, c='red')
plt.title('Pengeluaran per Kapita dan Status Kepemilikan Rumah')
plt.xlabel('Log Per Capita Expenditure')
plt.ylabel('status_milik')
plt.rcParams['figure.figsize'] = [7, 7]
plt.show()
