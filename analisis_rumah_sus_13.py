{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "DATA SUSENAS 2013 KELOMPOK RUMAH TANGGA\n",
    "\n",
    "Analisis Kepemilikan tempat tinggal rumah tangga Indonesia 2013"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**READ DATA**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
   "source": [
    "rumah = pd.read_csv('sn13_krt.csv',)\n",
    "\n",
    "rumah = rumah[['b1r1','b1r5','b2r1','b6r1','b6r2','b6r3','b6r5','b6r6','b6r7','exp_cap','wert']]\n",
    "rumah.columns = ['prov','desa_kota','anggota_rt','tipe_bangunan','jumlah_rt','status_milik','atap','dinding','lantai','exp_cap','bobot']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "saya akan gunakan beberapa variabel di atas yang sudah saya ganti namanya. Awalnya masih menggunakan status kepemilikan rumah saja, nanti akan menggunakan variabel lain untuk menganalisis kualitas rumah."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>bobot</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>exp_cap</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>lantai</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dinding</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>atap</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>status_milik</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>jumlah_rt</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>tipe_bangunan</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>anggota_rt</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>desa_kota</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>prov</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Total  Percent\n",
       "bobot              0      0.0\n",
       "exp_cap            0      0.0\n",
       "lantai             0      0.0\n",
       "dinding            0      0.0\n",
       "atap               0      0.0\n",
       "status_milik       0      0.0\n",
       "jumlah_rt          0      0.0\n",
       "tipe_bangunan      0      0.0\n",
       "anggota_rt         0      0.0\n",
       "desa_kota          0      0.0\n",
       "prov               0      0.0"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total = rumah.isnull().sum().sort_values(ascending=False)\n",
    "percent = (rumah.isnull().sum()/rumah.isnull().count()).sort_values(ascending=False)\n",
    "missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])\n",
    "missing_data.head(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Data sudah bersih dan tidak ada missing value."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**CLEANSING DATA**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
   "source": [
    "#memberi label desa atau kota\n",
    "rumah.loc[rumah['desa_kota']==1,'desa_kota']='kota'\n",
    "rumah.loc[rumah['desa_kota']==2,'desa_kota']='desa'\n",
    "\n",
    "#memberi label kepemilikan rumah\n",
    "rumah.loc[rumah['status_milik']==1,'kepemilikan']=1\n",
    "rumah.loc[rumah['status_milik']==2,'kepemilikan']=0\n",
    "rumah.loc[rumah['status_milik']==3,'kepemilikan']=0\n",
    "rumah.loc[rumah['status_milik']==4,'kepemilikan']=0\n",
    "rumah.loc[rumah['status_milik']==5,'kepemilikan']=0\n",
    "rumah.loc[rumah['status_milik']==6,'kepemilikan']=0\n",
    "rumah.loc[rumah['status_milik']==7,'kepemilikan']=0\n",
    "\n",
    "#memberi label untuk jawa dan non-jawa"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Guna untuk visualisasi analisis saya ganti nilai variabelnya supaya langsung terlihat labelnya.\n",
    "\n",
    "Sedikit mengenai kepemilikan rumah. label 1 merupakan milik sendiri, sedangkan 2 - 7 bukan milik sendiri(sewa/kontrak/bebas sewa/dinas). Mengapa yang lain saya kategorikan bukan_milik_sendiri? karena dengan memiliki sendiri lebih menunjukan kemampuan ekonomi. kemungkinan lain yang tidak bisa dilihat mungkin jika kepemilikan itu berasal dari hak waris."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [],
   "source": [
    "#perhitungan bobot\n",
    "wt_sum = lambda x: np.sum(x, weights=rumah.loc[x.index, \"bobot\"])\n",
    "wt_mean = lambda x: np.average(x, weights=rumah.loc[x.index, \"bobot\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "**Analisis tingkat kepemilikan tempat tinggal pada rumah tangga Nasional**\n",
    "\n",
    "1. Hipotesis pertama adalah seberapa banyak tingkat kepemilikan tempat tinggal yang dimiliki sendiri oleh sebuah rumah tangga. Apakah rumah tangga di Indonesia lebih banyak yang memiliki tempat tinggal sendiri atau menyewa(kontrak)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>kepemilikan</th>\n",
       "      <th>bobot</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>13482</td>\n",
       "      <td>13323751</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>57360</td>\n",
       "      <td>49827226</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   kepemilikan     bobot\n",
       "0        13482  13323751\n",
       "1        57360  49827226"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rumah_milik = rumah.groupby(\"kepemilikan\").agg(kepemilikan = (\"kepemilikan\", \"count\"), bobot = (\"bobot\", \"sum\"))\n",
    "rumah_milik.reset_index(drop=True).astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1f97481cbc8>"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#data yang menampilkan tingkat kempemilikikan rumah nasional\n",
    "sns.barplot(x=rumah_milik[\"kepemilikan\"].index, y=rumah_milik[\"bobot\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Dari pemaparan analisis di atas, diketahui rumah tangga di Indonesia lebih banyak yang memiliki tempat tinggal sendiri ketimbang yang tidak memiliki memiliki. Akan tetapi angka yang tidak memiliki masih cukup tinggi, sekitar 21% dari total rumah tangga masih tidak memiliki tempat tinggal sendiri."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Presentase dari rumah tangga yang tidak memiliki rumah keseluruhan:  bobot    21.09825\n",
      "dtype: float64\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\yuha bach\\anaconda3\\lib\\site-packages\\pandas\\core\\ops\\array_ops.py:253: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison\n",
      "  res_values = method(rvalues)\n"
     ]
    }
   ],
   "source": [
    "a = rumah[rumah.status_milik == \"bukan_milik_sendiri\"][[\"bobot\"]].sum().astype(int)\n",
    "b = rumah[rumah.status_milik == \"milik_sendiri\"][[\"bobot\"]].sum().astype(int)\n",
    "prcntg = a/(a+b)*100\n",
    "\n",
    "print(\"Presentase dari rumah tangga yang tidak memiliki rumah keseluruhan: \", prcntg_ass)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Sekarang mari kita coba lihat bagaimana perbandingan kepemilikan rumah di desa dengan kota."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>desa_kota</th>\n",
       "      <th>kepemilikan</th>\n",
       "      <th>bobot</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>desa_kota</th>\n",
       "      <th>kepemilikan</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">desa</th>\n",
       "      <th>0.0</th>\n",
       "      <td>4819</td>\n",
       "      <td>4819</td>\n",
       "      <td>3874197</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1.0</th>\n",
       "      <td>35547</td>\n",
       "      <td>35547</td>\n",
       "      <td>27994185</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">kota</th>\n",
       "      <th>0.0</th>\n",
       "      <td>8663</td>\n",
       "      <td>8663</td>\n",
       "      <td>9449553</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1.0</th>\n",
       "      <td>21813</td>\n",
       "      <td>21813</td>\n",
       "      <td>21833040</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       desa_kota  kepemilikan     bobot\n",
       "desa_kota kepemilikan                                  \n",
       "desa      0.0               4819         4819   3874197\n",
       "          1.0              35547        35547  27994185\n",
       "kota      0.0               8663         8663   9449553\n",
       "          1.0              21813        21813  21833040"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Perbandingan kepemilikan desa dan kota\n",
    "rumah_urban = rumah.groupby([ \"desa_kota\",\"kepemilikan\"]).agg(desa_kota = (\"desa_kota\", \"count\"),\n",
    "                                             kepemilikan = (\"kepemilikan\", \"count\"),\n",
    "                                             bobot = (\"bobot\", \"sum\"))\n",
    "rumah_urban.astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1f974795888>"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x=rumah_urban[\"desa_kota\"].index, y=rumah_urban[\"bobot\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Temuan pada perbandingan tersebut cukup menarik dimana jumlah rumah tangga pedesaan lebih sedikit yang tidak memiliki rumah sendiri dibandingkan dengan perkotaan. Jika kita lihat angkanya, hampir separuh populasi di perkotaan tidak memiliki sendiri. Faktor penyebab ketimpangan ini mungkin bisa dilihat dari harga rumah di perkotaan yang lebih tinggi dan kepadatan penduduk di perkotaan."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. perbandingan tingkat kepemilikan rumah di pulau jawa dan non-jawa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
