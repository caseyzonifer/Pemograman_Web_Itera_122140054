# ================================================
# MATH_OPERATIONS.PY
# Modul matematika untuk operasi geometri dan konversi suhu
# ================================================

# Konstanta
PI = 3.14159
KELVIN_OFFSET = 273.15
GOLDEN_RATIO = 1.61803398875

# ================================================
# FUNGSI BENTUK GEOMETRI
# ================================================

def luas_persegi(sisi):
    """
    Menghitung luas persegi
    
    Args:
        sisi (float): Panjang sisi persegi
        
    Returns:
        float: Luas persegi
    """
    return sisi ** 2

def keliling_persegi(sisi):
    """
    Menghitung keliling persegi
    
    Args:
        sisi (float): Panjang sisi persegi
        
    Returns:
        float: Keliling persegi
    """
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    """
    Menghitung luas persegi panjang
    
    Args:
        panjang (float): Panjang persegi panjang
        lebar (float): Lebar persegi panjang
        
    Returns:
        float: Luas persegi panjang
    """
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    """
    Menghitung keliling persegi panjang
    
    Args:
        panjang (float): Panjang persegi panjang
        lebar (float): Lebar persegi panjang
        
    Returns:
        float: Keliling persegi panjang
    """
    return 2 * (panjang + lebar)

def luas_lingkaran(radius):
    """
    Menghitung luas lingkaran
    
    Args:
        radius (float): Jari-jari lingkaran
        
    Returns:
        float: Luas lingkaran
    """
    return PI * radius ** 2

def keliling_lingkaran(radius):
    """
    Menghitung keliling lingkaran
    
    Args:
        radius (float): Jari-jari lingkaran
        
    Returns:
        float: Keliling lingkaran
    """
    return 2 * PI * radius

def luas_segitiga(alas, tinggi):
    """
    Menghitung luas segitiga
    
    Args:
        alas (float): Panjang alas segitiga
        tinggi (float): Tinggi segitiga
        
    Returns:
        float: Luas segitiga
    """
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    """
    Menghitung keliling segitiga
    
    Args:
        sisi1 (float): Panjang sisi pertama
        sisi2 (float): Panjang sisi kedua
        sisi3 (float): Panjang sisi ketiga
        
    Returns:
        float: Keliling segitiga
    """
    return sisi1 + sisi2 + sisi3

# ================================================
# FUNGSI KONVERSI SUHU
# ================================================

def celsius_ke_fahrenheit(celsius):
    """
    Mengkonversi suhu Celsius ke Fahrenheit
    
    Args:
        celsius (float): Suhu dalam Celsius
        
    Returns:
        float: Suhu dalam Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_ke_celsius(fahrenheit):
    """
    Mengkonversi suhu Fahrenheit ke Celsius
    
    Args:
        fahrenheit (float): Suhu dalam Fahrenheit
        
    Returns:
        float: Suhu dalam Celsius
    """
    return (fahrenheit - 32) * 5/9

def celsius_ke_kelvin(celsius):
    """
    Mengkonversi suhu Celsius ke Kelvin
    
    Args:
        celsius (float): Suhu dalam Celsius
        
    Returns:
        float: Suhu dalam Kelvin
    """
    return celsius + KELVIN_OFFSET

def kelvin_ke_celsius(kelvin):
    """
    Mengkonversi suhu Kelvin ke Celsius
    
    Args:
        kelvin (float): Suhu dalam Kelvin
        
    Returns:
        float: Suhu dalam Celsius
    """
    return kelvin - KELVIN_OFFSET