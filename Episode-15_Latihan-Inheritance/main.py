"""
Latihan Inheritance

Kriteria latihan :
- Menggunakan inheritance untuk membuat tipe-tipe dari sub class Hero contohnya Hero Intelligent, Hero Strength dsb
"""
from Hero import HeroIntelligent, HeroStrength

lina = HeroIntelligent('lina')
slardar = HeroStrength('slardar')

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250

lina.show_info()
slardar.show_info()

