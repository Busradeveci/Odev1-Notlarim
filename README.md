# Odev1-Notlarim
## Proje Amacı

Bu proje, **GPT-2** modelini kullanarak **metin tamamlama** yapmak amacıyla oluşturulmuştur. Kullanıcıdan alınan bir başlangıç cümlesi ile **GPT-2** modeli, o cümleyi tamamlayacak şekilde yeni metinler üretmektedir. 

## Kullanım

1. **Text Generation**: Kullanıcıdan bir başlangıç cümlesi alır.
2. **Model İşlemi**: Alınan metin, GPT-2 modeline gönderilir.
3. **Sonuç**: Model, girilen metni tamamlar ve tamamlanan metin ekrana yazdırılır.

## Nasıl Çalışır?

1. `transformers` kütüphanesini ve GPT-2 modelini yükleriz.
2. Kullanıcıdan metin girişi alırız.
3. Model, verilen metni tamamlar ve sonucu ekrana yazdırır.

## Kullanım Örneği

```bash
$ python text_generator.py
Enter a starting sentence: The future of AI is
AI continuation: The future of AI is an exciting and rapidly evolving field. With advancements in machine learning and natural language processing, AI is poised to revolutionize many industries.
```



