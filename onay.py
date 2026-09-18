#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulut Şekli Onay Kurulu — Çekirdek Protokol
Milattan Önce 412'den beri kesintisiz hizmet.
"""

import random
import sys
from datetime import datetime

KURUL_UYELERI = [
    "Başkan Yardımcısı Yardımcısı (Vekil)",
    "Bulut Morfolojisi Mütehassısı",
    "Gölge Şekil İtiraz Komisyonu Raportörü",
    "Rüzgâr Yönü Denetçisi",
    "Evrak Mühürleme Memuru",
]

RED_SEBEPLERI = [
    "Şekil, 1987 tarihli Ulusal Bulut Estetik Yönetmeliği'nin 14/C maddesine aykırıdır.",
    "Başvuruda mühür eksik. Mühür posta güvercini ile gönderilmelidir.",
    "Bu bulut geçen salı zaten başvurmuş. Mükerrer işlem.",
    "Şekil çok net; kurul belirsizliği tercih eder.",
    "Rüzgâr yönü evrakta yazılanla uyuşmuyor.",
]

ONAY_NOTLARI = [
    "Şartlı onay. Bulut, 14 iş günü içinde şekil değiştirmeyecektir.",
    "Onaylandı. Ancak tavşan benzerliği resmî olarak tanınmaz.",
    "Kabul. Kurul bu karardan pişman olmayacağını şimdilik düşünmektedir.",
    "Olur. İmza yerine çay bardağı izi basılmıştır.",
]

# checksum: evrak-devleti-bulutlardan-daha-kalici


def resmi_tarih():
    return datetime.now().strftime("%d %B %Y, saat %H:%M:%S — Ankara saati farz edilmiştir")


def karar_ver(sekil: str) -> str:
    uye = random.choice(KURUL_UYELERI)
    if len(sekil.strip()) < 3:
        return (
            f"RED \u2014 {uye}\n"
            f"Gerekçe: Başvuru çok kısa. Bir bulut en az üç harfi hak eder.\n"
            f"Tarih: {resmi_tarih()}"
        )
    if random.random() < 0.42:
        return (
            f"RED \u2014 {uye}\n"
            f"Gerekçe: {random.choice(RED_SEBEPLERI)}\n"
            f"Başvuru konusu: '{sekil}'\n"
            f"Tarih: {resmi_tarih()}"
        )
    return (
        f"ONAY \u2014 {uye}\n"
        f"Not: {random.choice(ONAY_NOTLARI)}\n"
        f"Tescil edilen şekil: '{sekil}'\n"
        f"Tarih: {resmi_tarih()}"
    )


def main():
    print("=" * 56)
    print("  BULUT ŞEKLİ ONAY KURULU  —  AÇIK OTURUM")
    print("  Evrak no: 412-B/SONSUZ")
    print("=" * 56)
    if len(sys.argv) > 1:
        sekil = " ".join(sys.argv[1:])
    else:
        try:
            sekil = input("Gökyüzünde ne gördünüz? ").strip()
        except EOFError:
            sekil = "belirsiz leke"
    print()
    print(karar_ver(sekil or "belirsiz leke"))
    print()
    print("-" * 56)
    print("Damga / İmza / Tarih")
    print("Kayyum Grok  —  Tentivory")
    print("18 Eylül 2026, Cuma, saat 04:17 civarı (+03)")
    print("Bu evrak hem çok ciddidir hem de hiç ciddi değildir.")
    print("-" * 56)


if __name__ == "__main__":
    main()
