import pandas as pd
import matplotlib.pyplot as plt

# CSV'yi oku
df = pd.read_csv('yks_verileri.csv')

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(df['Turkce_Net'], bins=20, color='skyblue', edgecolor='black')
plt.title('Türkçe Net Dağılımı')

plt.subplot(1, 2, 2)
plt.hist(df['Matematik_Net'], bins=20, color='salmon', edgecolor='black')
plt.title('Matematik Net Dağılımı')

plt.tight_layout()

# Grafiği dosya olarak kaydet (İstenen 4. dosya)
plt.savefig('yks_grafik.png')
print("Grafik 'yks_grafik.png' olarak kaydedildi.")
plt.show