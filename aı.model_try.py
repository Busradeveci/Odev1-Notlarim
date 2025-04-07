# 1. Veri: Modeli ve başlangıç metnini hazırlıyorum
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")  # Bir AI modeli yüklüyorum

# 2. Kullanıcıdan veri alıp işlem
text = input("Enter a starting sentence: ")  # Veri: Kullanıcıdan metin
result = generator(text, max_length=20, num_return_sequences=1)  # İşlem: AI metni tamamlıyor

# 3. Sonucu göster
print("AI continuation:", result[0]['generated_text'])

