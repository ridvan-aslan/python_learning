from datetime import datetime
# from datetime import date
# from datetime import time
from datetime import timedelta

# import datetime

now = datetime.now()
result = datetime.today()

print(f"Şu anki zaman: {now}")

print(f"Yıl: {now.year}")
print(f"Ay: {now.month}")
print(f"Gün: {now.day}")
print(f"Saat: {now.hour}")
print(f"Dakika: {now.minute}")
print(f"Saniye: {now.second}")

print(f"Detaylı zaman (ctime): {datetime.ctime(now)}")

print("\n--- strftime ile formatlama ---")
print(f"%Y (Yıl): {datetime.strftime(now, '%Y')}")
print(f"%B (Ay ismi): {datetime.strftime(now, '%B')}")
print(f"%A (Gün ismi): {datetime.strftime(now, '%A')}")
print(f"%X (Saat formatı): {datetime.strftime(now, '%X')}")
print(f"Özel format: {datetime.strftime(now, '%Y %B %A')}")

t = "19 August 2025 hour 10:20:30"
print(f"\n--- strptime ile string'den tarih oluşturma ---")
print(f"Parse edilecek string: '{t}'")
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(f"Oluşturulan tarih nesnesi: {dt}")

print("\n--- Tarih ve Zaman Aritmetiği ---")
birthday = datetime(2003, 5, 7, 00, 00, 00)
print(f"Doğum günü: {birthday}")

timestamp = datetime.timestamp(birthday)
print(f"Doğum günü (timestamp): {timestamp}")
from_timestamp = datetime.fromtimestamp(timestamp)
print(f"Timestamp'ten dönüştürülen tarih: {from_timestamp}")

time_since_birth = now - birthday
print(f"Doğumdan bu yana geçen süre: {time_since_birth}")
print(f"Geçen gün sayısı: {time_since_birth.days}")

print("\n--- timedelta kullanımı ---")
print(f"Şu andan 10 gün sonrası: {now + timedelta(days=10)}")
print(f"Şu andan 10 gün öncesi: {now - timedelta(days=10)}")
print(f"Şu andan 730 gün (yaklaşık 2 yıl) sonrası: {now + timedelta(days=730)}")
