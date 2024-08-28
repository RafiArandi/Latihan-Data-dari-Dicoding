
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def stasiun_CO(nama):
  stasiun_CO= nama.resample(rule='Y', on='datetime').agg({
      "CO": "mean",
      })
  stasiun_CO.index = stasiun_CO.index.strftime('%Y') #Mengubah format dalam satuan tahun

  stasiun_CO = stasiun_CO.reset_index()
  stasiun_CO.rename(columns={
    "CO": "CO",
    }, inplace=True)
  return stasiun_CO

def rata_rata(nama):
  senyawa = ('PM2.5', 'PM10', 'SO2', 'NO2', 'CO','O3')
  rata_rata_senyawa = (nama['PM2.5'].mean(), nama['PM10'].mean(), nama['SO2'].mean(),
                 nama['NO2'].mean(), nama['CO'].mean(), nama['O3'].mean())
  return senyawa, rata_rata_senyawa


# Load cleaned data
all_stasiun = pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/all_stasiun.csv")
aotizhongxin_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/aotizhongxin_station.csv")
cangping_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/cangping_station.csv")
dingling_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/dingling_station.csv")
dongsi_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/dongsi_station.csv")
guanyuan_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/guanyuan_station.csv")
gucheng_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/gucheng_station.csv")
huario_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/huario_station.csv")
nongzhanguan_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/nongzhanguan_station.csv")
shunyi_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/shunyi_station.csv")
tiantan_station= pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/tiantan_station.csv")
wanliu_station = pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/wanliu_station.csv")
wanshouxigong_station = pd.read_csv("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/wanshouxigong_station.csv")

names = [all_stasiun, aotizhongxin_station, cangping_station, dingling_station,
dongsi_station, guanyuan_station, gucheng_station, huario_station,
nongzhanguan_station, shunyi_station, tiantan_station,
wanliu_station, wanshouxigong_station]

for nama in names:
  nama["datetime"] = pd.to_datetime(nama[["year", "month", "day", "hour"]])

with st.sidebar:
    # Menambahkan logo
    st.image("https://raw.githubusercontent.com/RafiArandi/Latihan-Data-dari-Dicoding/main/Data%20cleaning%20per%20stasiun/Asap.png")

# st.dataframe(all_stasiun)

# # Menyiapkan berbagai dataframe
aotizhongxin_station_CO = stasiun_CO(aotizhongxin_station)
cangping_station_CO = stasiun_CO(cangping_station)
dingling_station_CO = stasiun_CO(dingling_station)
dongsi_station_CO = stasiun_CO(dongsi_station)
guanyuan_station_CO = stasiun_CO(guanyuan_station)
gucheng_station_CO = stasiun_CO(gucheng_station)
huario_station_CO = stasiun_CO(huario_station)
nongzhanguan_station_CO = stasiun_CO(nongzhanguan_station)
shunyi_station_CO = stasiun_CO(shunyi_station)
tiantan_station_CO = stasiun_CO(tiantan_station)
wanliu_station_CO = stasiun_CO(wanliu_station)
wanshouxigong_station_CO = stasiun_CO(wanshouxigong_station)


# plot tahunan CO


st.header('Polutan CO pada Kawasan Stasiun Beijing')
st.subheader('Rata-rata tahunan CO Pada Tahun (2013-2017)')

col1, col2 = st.columns(2)

with col1:
    total_orders = all_stasiun.CO.mean()
    st.metric("Rata-Rata", value=total_orders)

with col2:
    jumlah_keseluruhan = all_stasiun.CO.sum()
    st.metric("Jumlah Keseluruhan", value=jumlah_keseluruhan)

stasiun = [aotizhongxin_station_CO, cangping_station_CO, dingling_station_CO,
 dongsi_station_CO, guanyuan_station_CO, gucheng_station_CO, huario_station_CO,
 nongzhanguan_station_CO, shunyi_station_CO, tiantan_station_CO,
 wanliu_station_CO, wanshouxigong_station_CO]
stasiun_labels = ['aotizhongxin_station', 'cangping_station', 'dingling_station',
                  'dongsi_station', 'guanyuan_station', 'gucheng_station', 'huario_station',
                  'nongzhanguan_station', 'shunyi_station', 'tiantan_station',
                  'wanliu_station', 'wanshouxigong_station']

fig, ax = plt.subplots(figsize=(16, 8))
for i, stasiun_data in enumerate(stasiun):
    ax.plot(
        stasiun_data["datetime"],
        stasiun_data["CO"],
        marker='o',
        linewidth=2,
        label=stasiun_labels[i]  # Menambahkan label berdasarkan stasiun_labels
    )
plt.title("Mean of CO in station each year", loc="center", fontsize=20)
plt.legend(bbox_to_anchor=( 1.02, 1), loc="upper left", borderaxespad=0)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Jenis-Jenis Polutan lainnya
senyawa, rata_rata_senyawa = rata_rata(aotizhongxin_station)
senyawa2, rata_rata_senyawa2 = rata_rata(cangping_station)
senyawa3, rata_rata_senyawa3 = rata_rata(dingling_station)
senyawa4, rata_rata_senyawa4 = rata_rata(dongsi_station)
senyawa5, rata_rata_senyawa5 = rata_rata(guanyuan_station)
senyawa6, rata_rata_senyawa6 = rata_rata(gucheng_station)
senyawa7, rata_rata_senyawa7 = rata_rata(huario_station)
senyawa8, rata_rata_senyawa8 = rata_rata(nongzhanguan_station)
senyawa9, rata_rata_senyawa9 = rata_rata(shunyi_station)
senyawa10, rata_rata_senyawa10 = rata_rata(tiantan_station)
senyawa11, rata_rata_senyawa11 = rata_rata(wanliu_station)
senyawa12, rata_rata_senyawa12 = rata_rata(wanshouxigong_station)
st.subheader("Perbandingan Senyawa Polutan Lainnya pada Stasiu-Stasiun yang Ada")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))


sns.barplot(x=senyawa, y=rata_rata_senyawa, ax=ax[0])
ax[0].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[0].set_xlabel("Jenis Polutan", fontsize=30)
ax[0].set_title("Polutan di aotizhongxin_station", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x=senyawa2, y=rata_rata_senyawa2, ax=ax[1])
ax[1].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[1].set_xlabel("Jenis Polutan", fontsize=30)
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Polutan di cangping_station", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))


sns.barplot(x=senyawa3, y=rata_rata_senyawa3, ax=ax[0])
ax[0].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[0].set_xlabel("Jenis Polutan", fontsize=30)
ax[0].set_title("Polutan di dingling_station", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x=senyawa4, y=rata_rata_senyawa4, ax=ax[1])
ax[1].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[1].set_xlabel("Jenis Polutan", fontsize=30)
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Polutan di dongsi_station", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)


st.pyplot(fig)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))


sns.barplot(x=senyawa5, y=rata_rata_senyawa5, ax=ax[0])
ax[0].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[0].set_xlabel("Jenis Polutan", fontsize=30)
ax[0].set_title("Polutan di guanyuan_station", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x=senyawa6, y=rata_rata_senyawa6, ax=ax[1])
ax[1].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[1].set_xlabel("Jenis Polutan", fontsize=30)
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Polutan di gucheng_station", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)


st.pyplot(fig)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))


sns.barplot(x=senyawa7, y=rata_rata_senyawa7, ax=ax[0])
ax[0].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[0].set_xlabel("Jenis Polutan", fontsize=30)
ax[0].set_title("Polutan di huario_station", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x=senyawa8, y=rata_rata_senyawa8, ax=ax[1])
ax[1].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[1].set_xlabel("Jenis Polutan", fontsize=30)
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Polutan di nongzhanguan_station", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)


st.pyplot(fig)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))


sns.barplot(x=senyawa9, y=rata_rata_senyawa9, ax=ax[0])
ax[0].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[0].set_xlabel("Jenis Polutan", fontsize=30)
ax[0].set_title("Polutan di shunyi_station", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x=senyawa10, y=rata_rata_senyawa10, ax=ax[1])
ax[1].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[1].set_xlabel("Jenis Polutan", fontsize=30)
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Polutan di tiantan_station", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)


st.pyplot(fig)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))


sns.barplot(x=senyawa11, y=rata_rata_senyawa11, ax=ax[0])
ax[0].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[0].set_xlabel("Jenis Polutan", fontsize=30)
ax[0].set_title("Polutan di wanliu_station", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x=senyawa12, y=rata_rata_senyawa12, ax=ax[1])
ax[1].set_ylabel("Rata-rata selama 5 tahun", fontsize=30)
ax[1].set_xlabel("Jenis Polutan", fontsize=30)
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Polutan di wanshouxigong_station", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)


st.pyplot(fig)
