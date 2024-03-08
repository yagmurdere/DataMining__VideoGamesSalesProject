import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/vgsales.csv')
df.head(5)

#NOT
df_sorted=df.sort_values(by="Year",ascending=True)




#ENVIROMENT SET UP
#condada hangi ortamdayım (nredeyim) ENV LARI LİSTELER
conda env list
#ortamımda hangi paketler mevcut (tüm packageların bu enviorment içineki versiyonlarını gösterir) PACKAGES VE VERSİYONLARINI LİSTELİYOR
conda list
#dataset imin daha sonra da çalışabilmesi için pc de olması gereken paket ortamını base den dosyalıyorum
conda env export > enviroment.yaml
#dataset için yeni bir ortam oluşturmak (bu elimizdeki yaml dosyası ie yeni bir ortam oluşturmak istiyorsak )
conda create -n vg_env
#vg_env virtual environmet i active ediyoruz
conda activate vg_env
#tüm paketleri güncelliyorum
conda upgrade -all
#base i orjin kabul ettik .yaml dosyamı vg_env için kullanıyoruz
conda env create -f enviroment.yaml

#1.olarak descriptive statistics incelemeleri yapıyorum

#sayısal değişkenler için ayrı bir tanımlama yapıyorum
#datanın ne kadarı sayısal değerlerden oluşuyor ne kadarı text değerlerden oluşuyor bilmemiz lazım
num_var=[col for col in df.columns if df[col].dtype !='object']
num_var
#numerik değerli kolumlara bazı fonksiyonla uygulayacağız
#temel descriptive fonksiyonlarını listeliyoruz
#her column için aşağıdaki değerleri dönmesini isteyeceğim
desc_agg=['sum','mean','std','var','min','max']
desc_agg
#dess_agg_dict i numeric variablelerime uygula
#bu fonksiyonları sayısal değerlere uyguluyoruz
#descriptive agregationları df nin tüm kolumnlarında uygula
#dictionary oluşturuyoruz
dess_agg_dict={col : desc_agg for col in df}
dess_agg_dict
#her num_var colum için desc_agg değerlerini çıkartıyor
desc_sum=df[num_var].agg(desc_agg) #desc_agg
print(desc_sum)
#numpy array'e dönüştürmek istiyorum
#desc_sum i yani her sutün için olan fonksiyon çıktılarını paired data olarak yazıyor
df_desc_na=np.array(desc_sum)
df_desc_na
#df numpy array olarak kaydetmek istersek
#dataset i paired data olarak yazıyor
df_na=np.array(df)
df_na

#görselleştirir
#bu descriptivleri görsele taşıyoruz
#python un en basic görselleme aracı bu kütüphaneden daha iyileri var
#yukarıdaki gibi çıkartınca çoğu insan anlamayabilir bu nedenle görselleştirmeye ihtiyaç duyuyoruz




import seaborn as sns
df.shape
#(16598, 11) kaç satır kaç sütun var verdi
df.info()
#tablo hakkında bilgiler verdi (sütunlar bu sütunların indexi data type ı , null değer var mı kaç satır dolu)
df.columns
#sütun isimlerini döner

#missing value için kontrol yapıyorum
#içeride hiç boş var mı diye kontrol ediyor
df.isnull().values.any()

#her bir değişkene ait descriptive analytics değerleri bir tabloya transpose şeklinde yeniden yazdırıyorun
#desc_sum da sütun isimleri üstte fonksiyonlar yandaydı burada tam tersi olmasını sağlar
#.T burda virgülden sonrasını yazmıyor sadece .0 olarak biritor
desc_sumv2=df.describe().T
print(desc_sumv2)

#eu_salaes ın değerleri(her satır) mean değerinden büyük olanları ccount eder
#ortalamadan büyük kaç değerim var
#- yönde yığılım daha fazla
df[df.EU_Sales>df.EU_Sales.mean()].EU_Sales.count()#3474
#ortalamadn küçük kaç değerim var
df[df.EU_Sales<df.EU_Sales.mean()].EU_Sales.count()#13124
#EU_Sales = 16598    =3474+13124

#ortalamanın üstündeki değer eğer ortalamanın altındaki değerden daha fazla çıksaydı data çarpık olucaktı
#Ortalamanın üstünde daha fazla veri olması, genellikle bir dağılımın sağa çarpık (positively skewed) olduğunu gösteri




df.loc[df.NA_Sales > df.NA_Sales.mean(),'EU_Sales'].head()
#df.EU_Sales > df.EU_Sales.mean(): Bu kısım, DataFrame'deki 'EU_Sales' sütunundaki her bir değerin, 'EU_Sales' sütununun ortalamasından büyük olup olmadığını kontrol eder. Bu bir koşulu sağlayan satırlar True olarak işaretlenir, aksi takdirde False olarak işaretlenir.
#df.loc[...]: Bu, DataFrame üzerinde yerine getirilen bir konum bazlı indeksleme işlemidir. Koşulu sağlayan satırları seçmeye yöneliktir.
#df.loc[df.EU_Sales > df.EU_Sales.mean(),'EU_Sales']: Bu ifade, sadece 'EU_Sales' sütununu seçer, ancak sadece koşulu sağlayan satırları içerir.
#.head(): Bu, yalnızca ilk birkaç satırı görmemizi sağlar. Bu, özellikle büyük veri setlerinde çalışırken veriyi anlamak için kullanışlıdır.
#Sonuç olarak, bu kod, 'EU_Sales' sütunundaki değerleri, bu sütunun ortalama değerinden daha büyük olan satırlarla sınırlayarak, bu koşulu sağlayan satırların 'EU_Sales' değerlerini döndürür ve bunların yalnızca ilk birkaçını görüntüler.

#2. column dan 11. columa al bunlara sensor de
sensor=df.iloc[:,6:11]
sensor
sensor.columns
#.iloc[:, 2:53]: Bu, DataFrame üzerinde indeks konumlarına dayalı seçim yapmak için kullanılan bir metottur. İlk indeks, satırları temsil eder ve burada : ile tüm satırları seçiyoruz. İkinci indeks, sütunları temsil eder ve burada 2 ile 52 arasındaki (52 dahil değil) sütunları seçiyoruz. Bu, DataFrame'de 2. sütundan başlayarak 52. sütuna kadar olan tüm sütunları içeren bir dilimi ifade eder.
#Sonuç olarak, sensor isimli yeni bir DataFrame oluşturulur ve bu DataFrame, orijinal DataFrame'in 2. sütunundan başlayarak 52. sütununa kadar olan sütunları içerir. Bu tür bir dilimleme genellikle belirli bir alt kümenin analizi veya işlemi için kullanılır.
#name i dahil etmeyip 2.sutün olan platformdan başlıyor
print(df.head(5))

#değişkenlerin görseller ile incelenmesi
from matplotlib import pyplot as plt

#değişkenlerin grafiklerini çıkarıyorum
sns.boxplot(x=sensor["EU_Sales"])
plt.show()

def num_summary(sensor,numerical_col,plot=False):
    #grafikteki aralıkları belirledik
    quantilies=[0.01,0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90]
    print(sensor[numerical_col].describe(quantilies).T)

    if plot:
        sensor[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

num_summary(sensor,"JP_Sales",plot=True)

#her kolon için yapıyour
#tüm değişkenler için bir kod ile grafikler üretiyorum
for col in sensor:
    num_summary(sensor,col,plot=True)

#???????????????????
df.groupby('NA_Sales')["JP_Sales"].mean()
#her bir na_sales değeri için jp_sales in ortalamsını alıyoruz

def target_summary_with_num(dataframe,target,num_col):
    print(dataframe.groupby(target).agg({num_col:"mean"}),end="\n\n\n")
#num_col u aggregate bazında mean ediceksin target a göre guruplayacaksın ve bana pirint edeceksin
#aslında bir üstteki ile aynı işi yapıyor


#fonksiyonu senso içindeki kolumarda çalıştırıcaz
for col in sensor:
    target_summary_with_num(df,"NA_Sales",col)

#tüm korelsayonları çıkartıyor
corr=sensor.corr()

#korelasyon ısı haritası çıkarmak istiyoruz
#bütün değişkenlerin birbirine olan ilişkisini gösteriyor
sns.set(rc={'figure.figsize':(12,12)})
sns.heatmap(corr,cmap='RdBu')
plt.show()

#+++???????????$$$$$$$$



#sensörlerin 3'lü gruplar halinde korelasyonların ortak olduğunu fark ediyorum
#ayrıca korelasyonun yüksek olduğu değişkenleri de ayıklamak istiyorum
cor_matrix=df.corr().abs()

upper_triangle_matrix=cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(bool))
drop_list = [col for col in upper_triangle_matrix.columns if any (upper_triangle_matrix[col]>0.90)] #%90 dan bütük korelasyon deerlerini alıyor
cor_matrix[drop_list]



#MODELİNG DEVELOPMENT
#modeling
#prediction
#evaluation
#hyperparameter optimization
#finalization
#(yukarıdakiler konu başlığı)

from sklearn.metrics import classification_report , roc_auc_score
from sklearn.model_selection import GridSearchCV , cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


Y = df.iloc[:,1:2] #bağımlı değişken
X = df.drop(["Year","NA_Sales"],axis = 1) #bağımsız değişken
#iloc la da yazılabilie

#bağımsız değişkenleri standardize ediyoruz

x_scaled = StandardScaler().fit_transform(X)
x_scaled_NA_Sales=pd.DataFrame(x_scaled,columns=X.columns)