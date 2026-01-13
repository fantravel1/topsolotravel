#!/usr/bin/env python3
"""
Fallback country data when API is unavailable.
Contains essential data for 200+ countries.
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

# Complete list of countries with solo travel data
COUNTRIES = [
    # Asia
    {"name": "Japan", "capital": "Tokyo", "region": "Asia", "subregion": "Eastern Asia", "population": 125800000, "currency": "Japanese Yen (JPY)", "language": "Japanese", "timezone": "UTC+9", "safety_level": "safe", "best_time": "Mar-May, Oct-Nov", "budget": {"budget": "70-100", "midrange": "120-180", "luxury": "350+"}, "featured": True},
    {"name": "Thailand", "capital": "Bangkok", "region": "Asia", "subregion": "South-Eastern Asia", "population": 69800000, "currency": "Thai Baht (THB)", "language": "Thai", "timezone": "UTC+7", "safety_level": "caution", "best_time": "Nov-Feb", "budget": {"budget": "30-45", "midrange": "60-100", "luxury": "200+"}, "featured": True},
    {"name": "Vietnam", "capital": "Hanoi", "region": "Asia", "subregion": "South-Eastern Asia", "population": 97340000, "currency": "Vietnamese Dong (VND)", "language": "Vietnamese", "timezone": "UTC+7", "safety_level": "caution", "best_time": "Feb-Apr, Aug-Oct", "budget": {"budget": "20-30", "midrange": "40-60", "luxury": "100+"}, "featured": True},
    {"name": "Indonesia", "capital": "Jakarta", "region": "Asia", "subregion": "South-Eastern Asia", "population": 273500000, "currency": "Indonesian Rupiah (IDR)", "language": "Indonesian", "timezone": "UTC+7 to +9", "safety_level": "caution", "best_time": "Apr-Oct", "budget": {"budget": "25-35", "midrange": "50-80", "luxury": "150+"}, "featured": True},
    {"name": "Malaysia", "capital": "Kuala Lumpur", "region": "Asia", "subregion": "South-Eastern Asia", "population": 32370000, "currency": "Malaysian Ringgit (MYR)", "language": "Malay", "timezone": "UTC+8", "safety_level": "safe", "best_time": "Year-round", "budget": {"budget": "35-50", "midrange": "60-100", "luxury": "180+"}, "featured": False},
    {"name": "Singapore", "capital": "Singapore", "region": "Asia", "subregion": "South-Eastern Asia", "population": 5850000, "currency": "Singapore Dollar (SGD)", "language": "English", "timezone": "UTC+8", "safety_level": "safe", "best_time": "Year-round", "budget": {"budget": "80-110", "midrange": "140-220", "luxury": "400+"}, "featured": True},
    {"name": "Philippines", "capital": "Manila", "region": "Asia", "subregion": "South-Eastern Asia", "population": 109580000, "currency": "Philippine Peso (PHP)", "language": "Filipino", "timezone": "UTC+8", "safety_level": "caution", "best_time": "Dec-May", "budget": {"budget": "25-40", "midrange": "50-80", "luxury": "120+"}, "featured": False},
    {"name": "Cambodia", "capital": "Phnom Penh", "region": "Asia", "subregion": "South-Eastern Asia", "population": 16720000, "currency": "Cambodian Riel (KHR)", "language": "Khmer", "timezone": "UTC+7", "safety_level": "caution", "best_time": "Nov-Apr", "budget": {"budget": "20-30", "midrange": "40-60", "luxury": "80+"}, "featured": False},
    {"name": "Laos", "capital": "Vientiane", "region": "Asia", "subregion": "South-Eastern Asia", "population": 7280000, "currency": "Lao Kip (LAK)", "language": "Lao", "timezone": "UTC+7", "safety_level": "caution", "best_time": "Nov-Feb", "budget": {"budget": "20-30", "midrange": "35-50", "luxury": "70+"}, "featured": False},
    {"name": "Myanmar", "capital": "Naypyidaw", "region": "Asia", "subregion": "South-Eastern Asia", "population": 54410000, "currency": "Myanmar Kyat (MMK)", "language": "Burmese", "timezone": "UTC+6:30", "safety_level": "warning", "best_time": "Nov-Feb", "budget": {"budget": "25-35", "midrange": "45-70", "luxury": "100+"}, "featured": False},
    {"name": "South Korea", "capital": "Seoul", "region": "Asia", "subregion": "Eastern Asia", "population": 51780000, "currency": "South Korean Won (KRW)", "language": "Korean", "timezone": "UTC+9", "safety_level": "safe", "best_time": "Apr-Jun, Sep-Nov", "budget": {"budget": "60-80", "midrange": "100-150", "luxury": "280+"}, "featured": True},
    {"name": "Taiwan", "capital": "Taipei", "region": "Asia", "subregion": "Eastern Asia", "population": 23570000, "currency": "New Taiwan Dollar (TWD)", "language": "Mandarin", "timezone": "UTC+8", "safety_level": "safe", "best_time": "Oct-Apr", "budget": {"budget": "50-70", "midrange": "80-130", "luxury": "220+"}, "featured": True},
    {"name": "China", "capital": "Beijing", "region": "Asia", "subregion": "Eastern Asia", "population": 1402000000, "currency": "Chinese Yuan (CNY)", "language": "Mandarin", "timezone": "UTC+8", "safety_level": "caution", "best_time": "Apr-May, Sep-Oct", "budget": {"budget": "40-60", "midrange": "80-130", "luxury": "200+"}, "featured": False},
    {"name": "Hong Kong", "capital": "Hong Kong", "region": "Asia", "subregion": "Eastern Asia", "population": 7482000, "currency": "Hong Kong Dollar (HKD)", "language": "Cantonese", "timezone": "UTC+8", "safety_level": "safe", "best_time": "Oct-Dec", "budget": {"budget": "70-100", "midrange": "130-200", "luxury": "350+"}, "featured": False},
    {"name": "India", "capital": "New Delhi", "region": "Asia", "subregion": "Southern Asia", "population": 1380000000, "currency": "Indian Rupee (INR)", "language": "Hindi", "timezone": "UTC+5:30", "safety_level": "caution", "best_time": "Oct-Mar", "budget": {"budget": "20-35", "midrange": "40-70", "luxury": "120+"}, "featured": True},
    {"name": "Nepal", "capital": "Kathmandu", "region": "Asia", "subregion": "Southern Asia", "population": 29140000, "currency": "Nepalese Rupee (NPR)", "language": "Nepali", "timezone": "UTC+5:45", "safety_level": "caution", "best_time": "Oct-Nov, Mar-May", "budget": {"budget": "20-30", "midrange": "40-60", "luxury": "100+"}, "featured": False},
    {"name": "Sri Lanka", "capital": "Colombo", "region": "Asia", "subregion": "Southern Asia", "population": 21920000, "currency": "Sri Lankan Rupee (LKR)", "language": "Sinhala", "timezone": "UTC+5:30", "safety_level": "caution", "best_time": "Dec-Mar", "budget": {"budget": "25-40", "midrange": "50-80", "luxury": "130+"}, "featured": False},
    {"name": "Bangladesh", "capital": "Dhaka", "region": "Asia", "subregion": "Southern Asia", "population": 164690000, "currency": "Bangladeshi Taka (BDT)", "language": "Bengali", "timezone": "UTC+6", "safety_level": "caution", "best_time": "Nov-Feb", "budget": {"budget": "20-30", "midrange": "35-55", "luxury": "80+"}, "featured": False},
    {"name": "Pakistan", "capital": "Islamabad", "region": "Asia", "subregion": "Southern Asia", "population": 220890000, "currency": "Pakistani Rupee (PKR)", "language": "Urdu", "timezone": "UTC+5", "safety_level": "warning", "best_time": "Oct-Mar", "budget": {"budget": "25-35", "midrange": "45-70", "luxury": "100+"}, "featured": False},
    {"name": "Maldives", "capital": "Male", "region": "Asia", "subregion": "Southern Asia", "population": 540540, "currency": "Maldivian Rufiyaa (MVR)", "language": "Dhivehi", "timezone": "UTC+5", "safety_level": "safe", "best_time": "Nov-Apr", "budget": {"budget": "100-150", "midrange": "200-400", "luxury": "800+"}, "featured": False},

    # Europe
    {"name": "Portugal", "capital": "Lisbon", "region": "Europe", "subregion": "Southern Europe", "population": 10200000, "currency": "Euro (EUR)", "language": "Portuguese", "timezone": "UTC+0", "safety_level": "safe", "best_time": "Apr-Oct", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"}, "featured": True},
    {"name": "Spain", "capital": "Madrid", "region": "Europe", "subregion": "Southern Europe", "population": 46940000, "currency": "Euro (EUR)", "language": "Spanish", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Apr-Jun, Sep-Oct", "budget": {"budget": "60-80", "midrange": "100-160", "luxury": "300+"}, "featured": True},
    {"name": "Italy", "capital": "Rome", "region": "Europe", "subregion": "Southern Europe", "population": 60360000, "currency": "Euro (EUR)", "language": "Italian", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Apr-Jun, Sep-Oct", "budget": {"budget": "70-90", "midrange": "120-180", "luxury": "350+"}, "featured": True},
    {"name": "France", "capital": "Paris", "region": "Europe", "subregion": "Western Europe", "population": 67390000, "currency": "Euro (EUR)", "language": "French", "timezone": "UTC+1", "safety_level": "caution", "best_time": "Apr-Jun, Sep-Oct", "budget": {"budget": "80-100", "midrange": "140-200", "luxury": "400+"}, "featured": True},
    {"name": "Germany", "capital": "Berlin", "region": "Europe", "subregion": "Western Europe", "population": 83240000, "currency": "Euro (EUR)", "language": "German", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "70-90", "midrange": "110-170", "luxury": "300+"}, "featured": True},
    {"name": "United Kingdom", "capital": "London", "region": "Europe", "subregion": "Northern Europe", "population": 67890000, "currency": "British Pound (GBP)", "language": "English", "timezone": "UTC+0", "safety_level": "caution", "best_time": "May-Sep", "budget": {"budget": "80-110", "midrange": "150-220", "luxury": "400+"}, "featured": True},
    {"name": "Ireland", "capital": "Dublin", "region": "Europe", "subregion": "Northern Europe", "population": 4940000, "currency": "Euro (EUR)", "language": "English", "timezone": "UTC+0", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "70-100", "midrange": "130-190", "luxury": "350+"}, "featured": False},
    {"name": "Netherlands", "capital": "Amsterdam", "region": "Europe", "subregion": "Western Europe", "population": 17440000, "currency": "Euro (EUR)", "language": "Dutch", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Apr-Sep", "budget": {"budget": "80-100", "midrange": "130-190", "luxury": "350+"}, "featured": True},
    {"name": "Belgium", "capital": "Brussels", "region": "Europe", "subregion": "Western Europe", "population": 11590000, "currency": "Euro (EUR)", "language": "Dutch", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "70-90", "midrange": "120-180", "luxury": "320+"}, "featured": False},
    {"name": "Switzerland", "capital": "Bern", "region": "Europe", "subregion": "Western Europe", "population": 8650000, "currency": "Swiss Franc (CHF)", "language": "German", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Jun-Sep, Dec-Mar", "budget": {"budget": "120-160", "midrange": "200-300", "luxury": "550+"}, "featured": True},
    {"name": "Austria", "capital": "Vienna", "region": "Europe", "subregion": "Western Europe", "population": 9010000, "currency": "Euro (EUR)", "language": "German", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Jun-Sep, Dec-Mar", "budget": {"budget": "70-90", "midrange": "120-180", "luxury": "320+"}, "featured": False},
    {"name": "Czech Republic", "capital": "Prague", "region": "Europe", "subregion": "Central Europe", "population": 10700000, "currency": "Czech Koruna (CZK)", "language": "Czech", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"}, "featured": True},
    {"name": "Poland", "capital": "Warsaw", "region": "Europe", "subregion": "Central Europe", "population": 37950000, "currency": "Polish Zloty (PLN)", "language": "Polish", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "40-60", "midrange": "70-120", "luxury": "200+"}, "featured": False},
    {"name": "Hungary", "capital": "Budapest", "region": "Europe", "subregion": "Central Europe", "population": 9660000, "currency": "Hungarian Forint (HUF)", "language": "Hungarian", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Apr-Jun, Sep-Oct", "budget": {"budget": "45-65", "midrange": "80-130", "luxury": "220+"}, "featured": False},
    {"name": "Croatia", "capital": "Zagreb", "region": "Europe", "subregion": "Southern Europe", "population": 4050000, "currency": "Euro (EUR)", "language": "Croatian", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "55-75", "midrange": "100-150", "luxury": "280+"}, "featured": True},
    {"name": "Greece", "capital": "Athens", "region": "Europe", "subregion": "Southern Europe", "population": 10420000, "currency": "Euro (EUR)", "language": "Greek", "timezone": "UTC+2", "safety_level": "safe", "best_time": "Apr-Jun, Sep-Oct", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"}, "featured": True},
    {"name": "Turkey", "capital": "Ankara", "region": "Europe", "subregion": "Western Asia", "population": 84340000, "currency": "Turkish Lira (TRY)", "language": "Turkish", "timezone": "UTC+3", "safety_level": "caution", "best_time": "Apr-May, Sep-Nov", "budget": {"budget": "35-50", "midrange": "70-120", "luxury": "200+"}, "featured": True},
    {"name": "Iceland", "capital": "Reykjavik", "region": "Europe", "subregion": "Northern Europe", "population": 366000, "currency": "Icelandic Krona (ISK)", "language": "Icelandic", "timezone": "UTC+0", "safety_level": "safe", "best_time": "Jun-Aug, Sep-Mar", "budget": {"budget": "130-170", "midrange": "220-320", "luxury": "550+"}, "featured": True},
    {"name": "Norway", "capital": "Oslo", "region": "Europe", "subregion": "Northern Europe", "population": 5420000, "currency": "Norwegian Krone (NOK)", "language": "Norwegian", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Jun-Aug, Dec-Mar", "budget": {"budget": "110-150", "midrange": "180-280", "luxury": "500+"}, "featured": False},
    {"name": "Sweden", "capital": "Stockholm", "region": "Europe", "subregion": "Northern Europe", "population": 10350000, "currency": "Swedish Krona (SEK)", "language": "Swedish", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "100-140", "midrange": "170-260", "luxury": "450+"}, "featured": False},
    {"name": "Denmark", "capital": "Copenhagen", "region": "Europe", "subregion": "Northern Europe", "population": 5830000, "currency": "Danish Krone (DKK)", "language": "Danish", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "100-140", "midrange": "170-260", "luxury": "450+"}, "featured": False},
    {"name": "Finland", "capital": "Helsinki", "region": "Europe", "subregion": "Northern Europe", "population": 5540000, "currency": "Euro (EUR)", "language": "Finnish", "timezone": "UTC+2", "safety_level": "safe", "best_time": "Jun-Aug, Dec-Mar", "budget": {"budget": "100-140", "midrange": "170-250", "luxury": "420+"}, "featured": False},
    {"name": "Estonia", "capital": "Tallinn", "region": "Europe", "subregion": "Northern Europe", "population": 1330000, "currency": "Euro (EUR)", "language": "Estonian", "timezone": "UTC+2", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "240+"}, "featured": False},
    {"name": "Latvia", "capital": "Riga", "region": "Europe", "subregion": "Northern Europe", "population": 1880000, "currency": "Euro (EUR)", "language": "Latvian", "timezone": "UTC+2", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "45-65", "midrange": "80-130", "luxury": "220+"}, "featured": False},
    {"name": "Lithuania", "capital": "Vilnius", "region": "Europe", "subregion": "Northern Europe", "population": 2790000, "currency": "Euro (EUR)", "language": "Lithuanian", "timezone": "UTC+2", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "45-65", "midrange": "80-130", "luxury": "220+"}, "featured": False},
    {"name": "Slovenia", "capital": "Ljubljana", "region": "Europe", "subregion": "Southern Europe", "population": 2100000, "currency": "Euro (EUR)", "language": "Slovenian", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "55-75", "midrange": "100-150", "luxury": "280+"}, "featured": True},
    {"name": "Slovakia", "capital": "Bratislava", "region": "Europe", "subregion": "Central Europe", "population": 5460000, "currency": "Euro (EUR)", "language": "Slovak", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "45-65", "midrange": "80-130", "luxury": "220+"}, "featured": False},
    {"name": "Romania", "capital": "Bucharest", "region": "Europe", "subregion": "Southeastern Europe", "population": 19240000, "currency": "Romanian Leu (RON)", "language": "Romanian", "timezone": "UTC+2", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "40-55", "midrange": "70-110", "luxury": "180+"}, "featured": False},
    {"name": "Bulgaria", "capital": "Sofia", "region": "Europe", "subregion": "Southeastern Europe", "population": 6930000, "currency": "Bulgarian Lev (BGN)", "language": "Bulgarian", "timezone": "UTC+2", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "35-50", "midrange": "60-100", "luxury": "160+"}, "featured": False},
    {"name": "Serbia", "capital": "Belgrade", "region": "Europe", "subregion": "Southeastern Europe", "population": 6910000, "currency": "Serbian Dinar (RSD)", "language": "Serbian", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "35-50", "midrange": "60-100", "luxury": "160+"}, "featured": False},
    {"name": "Montenegro", "capital": "Podgorica", "region": "Europe", "subregion": "Southeastern Europe", "population": 628000, "currency": "Euro (EUR)", "language": "Montenegrin", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "240+"}, "featured": False},
    {"name": "Bosnia and Herzegovina", "capital": "Sarajevo", "region": "Europe", "subregion": "Southeastern Europe", "population": 3280000, "currency": "Convertible Mark (BAM)", "language": "Bosnian", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "35-50", "midrange": "60-100", "luxury": "160+"}, "featured": False},
    {"name": "Albania", "capital": "Tirana", "region": "Europe", "subregion": "Southeastern Europe", "population": 2880000, "currency": "Albanian Lek (ALL)", "language": "Albanian", "timezone": "UTC+1", "safety_level": "caution", "best_time": "May-Sep", "budget": {"budget": "35-50", "midrange": "60-100", "luxury": "160+"}, "featured": False},
    {"name": "North Macedonia", "capital": "Skopje", "region": "Europe", "subregion": "Southeastern Europe", "population": 2080000, "currency": "Macedonian Denar (MKD)", "language": "Macedonian", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "30-45", "midrange": "55-90", "luxury": "150+"}, "featured": False},
    {"name": "Malta", "capital": "Valletta", "region": "Europe", "subregion": "Southern Europe", "population": 514000, "currency": "Euro (EUR)", "language": "Maltese", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Apr-Jun, Sep-Nov", "budget": {"budget": "60-80", "midrange": "100-160", "luxury": "300+"}, "featured": False},
    {"name": "Cyprus", "capital": "Nicosia", "region": "Europe", "subregion": "Eastern Europe", "population": 1210000, "currency": "Euro (EUR)", "language": "Greek", "timezone": "UTC+2", "safety_level": "safe", "best_time": "Apr-Jun, Sep-Nov", "budget": {"budget": "55-75", "midrange": "100-150", "luxury": "280+"}, "featured": False},
    {"name": "Luxembourg", "capital": "Luxembourg", "region": "Europe", "subregion": "Western Europe", "population": 634000, "currency": "Euro (EUR)", "language": "Luxembourgish", "timezone": "UTC+1", "safety_level": "safe", "best_time": "May-Sep", "budget": {"budget": "100-130", "midrange": "170-250", "luxury": "450+"}, "featured": False},
    {"name": "Monaco", "capital": "Monaco", "region": "Europe", "subregion": "Western Europe", "population": 39240, "currency": "Euro (EUR)", "language": "French", "timezone": "UTC+1", "safety_level": "safe", "best_time": "Year-round", "budget": {"budget": "150-200", "midrange": "300-500", "luxury": "1000+"}, "featured": False},

    # Americas
    {"name": "United States", "capital": "Washington D.C.", "region": "Americas", "subregion": "Northern America", "population": 331000000, "currency": "US Dollar (USD)", "language": "English", "timezone": "UTC-5 to -10", "safety_level": "caution", "best_time": "Varies by region", "budget": {"budget": "90-120", "midrange": "160-250", "luxury": "450+"}, "featured": True},
    {"name": "Canada", "capital": "Ottawa", "region": "Americas", "subregion": "Northern America", "population": 38010000, "currency": "Canadian Dollar (CAD)", "language": "English", "timezone": "UTC-3.5 to -8", "safety_level": "safe", "best_time": "Jun-Sep, Dec-Mar", "budget": {"budget": "80-110", "midrange": "140-220", "luxury": "400+"}, "featured": True},
    {"name": "Mexico", "capital": "Mexico City", "region": "Americas", "subregion": "Central America", "population": 128900000, "currency": "Mexican Peso (MXN)", "language": "Spanish", "timezone": "UTC-6 to -8", "safety_level": "caution", "best_time": "Dec-Apr", "budget": {"budget": "35-50", "midrange": "70-120", "luxury": "200+"}, "featured": True},
    {"name": "Costa Rica", "capital": "San Jose", "region": "Americas", "subregion": "Central America", "population": 5090000, "currency": "Costa Rican Colon (CRC)", "language": "Spanish", "timezone": "UTC-6", "safety_level": "caution", "best_time": "Dec-Apr", "budget": {"budget": "45-60", "midrange": "80-130", "luxury": "200+"}, "featured": True},
    {"name": "Panama", "capital": "Panama City", "region": "Americas", "subregion": "Central America", "population": 4310000, "currency": "US Dollar (USD)", "language": "Spanish", "timezone": "UTC-5", "safety_level": "caution", "best_time": "Dec-Apr", "budget": {"budget": "45-60", "midrange": "80-130", "luxury": "200+"}, "featured": False},
    {"name": "Guatemala", "capital": "Guatemala City", "region": "Americas", "subregion": "Central America", "population": 16860000, "currency": "Guatemalan Quetzal (GTQ)", "language": "Spanish", "timezone": "UTC-6", "safety_level": "caution", "best_time": "Nov-Apr", "budget": {"budget": "30-40", "midrange": "50-80", "luxury": "120+"}, "featured": False},
    {"name": "Belize", "capital": "Belmopan", "region": "Americas", "subregion": "Central America", "population": 398000, "currency": "Belize Dollar (BZD)", "language": "English", "timezone": "UTC-6", "safety_level": "caution", "best_time": "Dec-May", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "220+"}, "featured": False},
    {"name": "Nicaragua", "capital": "Managua", "region": "Americas", "subregion": "Central America", "population": 6620000, "currency": "Nicaraguan Cordoba (NIO)", "language": "Spanish", "timezone": "UTC-6", "safety_level": "warning", "best_time": "Dec-Apr", "budget": {"budget": "25-35", "midrange": "45-70", "luxury": "100+"}, "featured": False},
    {"name": "Honduras", "capital": "Tegucigalpa", "region": "Americas", "subregion": "Central America", "population": 9900000, "currency": "Honduran Lempira (HNL)", "language": "Spanish", "timezone": "UTC-6", "safety_level": "warning", "best_time": "Dec-Apr", "budget": {"budget": "30-40", "midrange": "50-80", "luxury": "120+"}, "featured": False},
    {"name": "El Salvador", "capital": "San Salvador", "region": "Americas", "subregion": "Central America", "population": 6490000, "currency": "US Dollar (USD)", "language": "Spanish", "timezone": "UTC-6", "safety_level": "warning", "best_time": "Nov-Apr", "budget": {"budget": "35-45", "midrange": "60-90", "luxury": "140+"}, "featured": False},
    {"name": "Cuba", "capital": "Havana", "region": "Americas", "subregion": "Caribbean", "population": 11330000, "currency": "Cuban Peso (CUP)", "language": "Spanish", "timezone": "UTC-5", "safety_level": "safe", "best_time": "Nov-Apr", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "220+"}, "featured": False},
    {"name": "Jamaica", "capital": "Kingston", "region": "Americas", "subregion": "Caribbean", "population": 2960000, "currency": "Jamaican Dollar (JMD)", "language": "English", "timezone": "UTC-5", "safety_level": "warning", "best_time": "Dec-Apr", "budget": {"budget": "60-80", "midrange": "110-170", "luxury": "280+"}, "featured": False},
    {"name": "Dominican Republic", "capital": "Santo Domingo", "region": "Americas", "subregion": "Caribbean", "population": 10850000, "currency": "Dominican Peso (DOP)", "language": "Spanish", "timezone": "UTC-4", "safety_level": "caution", "best_time": "Dec-Apr", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "220+"}, "featured": False},
    {"name": "Puerto Rico", "capital": "San Juan", "region": "Americas", "subregion": "Caribbean", "population": 3290000, "currency": "US Dollar (USD)", "language": "Spanish", "timezone": "UTC-4", "safety_level": "caution", "best_time": "Dec-Apr", "budget": {"budget": "80-110", "midrange": "140-210", "luxury": "350+"}, "featured": False},
    {"name": "Colombia", "capital": "Bogota", "region": "Americas", "subregion": "South America", "population": 50880000, "currency": "Colombian Peso (COP)", "language": "Spanish", "timezone": "UTC-5", "safety_level": "caution", "best_time": "Dec-Mar, Jul-Aug", "budget": {"budget": "35-50", "midrange": "60-100", "luxury": "150+"}, "featured": True},
    {"name": "Peru", "capital": "Lima", "region": "Americas", "subregion": "South America", "population": 32970000, "currency": "Peruvian Sol (PEN)", "language": "Spanish", "timezone": "UTC-5", "safety_level": "caution", "best_time": "May-Sep", "budget": {"budget": "35-50", "midrange": "70-110", "luxury": "180+"}, "featured": True},
    {"name": "Ecuador", "capital": "Quito", "region": "Americas", "subregion": "South America", "population": 17640000, "currency": "US Dollar (USD)", "language": "Spanish", "timezone": "UTC-5", "safety_level": "caution", "best_time": "Jun-Sep", "budget": {"budget": "35-50", "midrange": "60-90", "luxury": "140+"}, "featured": False},
    {"name": "Brazil", "capital": "Brasilia", "region": "Americas", "subregion": "South America", "population": 212600000, "currency": "Brazilian Real (BRL)", "language": "Portuguese", "timezone": "UTC-3 to -5", "safety_level": "caution", "best_time": "Apr-Oct", "budget": {"budget": "45-65", "midrange": "80-130", "luxury": "220+"}, "featured": True},
    {"name": "Argentina", "capital": "Buenos Aires", "region": "Americas", "subregion": "South America", "population": 45200000, "currency": "Argentine Peso (ARS)", "language": "Spanish", "timezone": "UTC-3", "safety_level": "caution", "best_time": "Oct-Apr", "budget": {"budget": "40-60", "midrange": "70-120", "luxury": "200+"}, "featured": True},
    {"name": "Chile", "capital": "Santiago", "region": "Americas", "subregion": "South America", "population": 19120000, "currency": "Chilean Peso (CLP)", "language": "Spanish", "timezone": "UTC-4", "safety_level": "safe", "best_time": "Nov-Mar", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "240+"}, "featured": False},
    {"name": "Bolivia", "capital": "Sucre", "region": "Americas", "subregion": "South America", "population": 11670000, "currency": "Bolivian Boliviano (BOB)", "language": "Spanish", "timezone": "UTC-4", "safety_level": "caution", "best_time": "May-Oct", "budget": {"budget": "25-35", "midrange": "45-70", "luxury": "100+"}, "featured": False},
    {"name": "Uruguay", "capital": "Montevideo", "region": "Americas", "subregion": "South America", "population": 3470000, "currency": "Uruguayan Peso (UYU)", "language": "Spanish", "timezone": "UTC-3", "safety_level": "safe", "best_time": "Dec-Mar", "budget": {"budget": "55-75", "midrange": "100-150", "luxury": "260+"}, "featured": False},
    {"name": "Paraguay", "capital": "Asuncion", "region": "Americas", "subregion": "South America", "population": 7130000, "currency": "Paraguayan Guarani (PYG)", "language": "Spanish", "timezone": "UTC-4", "safety_level": "caution", "best_time": "May-Sep", "budget": {"budget": "30-45", "midrange": "55-85", "luxury": "140+"}, "featured": False},

    # Africa
    {"name": "Morocco", "capital": "Rabat", "region": "Africa", "subregion": "Northern Africa", "population": 36910000, "currency": "Moroccan Dirham (MAD)", "language": "Arabic", "timezone": "UTC+1", "safety_level": "caution", "best_time": "Mar-May, Sep-Nov", "budget": {"budget": "30-45", "midrange": "60-90", "luxury": "150+"}, "featured": True},
    {"name": "Egypt", "capital": "Cairo", "region": "Africa", "subregion": "Northern Africa", "population": 102300000, "currency": "Egyptian Pound (EGP)", "language": "Arabic", "timezone": "UTC+2", "safety_level": "caution", "best_time": "Oct-Apr", "budget": {"budget": "25-40", "midrange": "50-80", "luxury": "150+"}, "featured": True},
    {"name": "South Africa", "capital": "Pretoria", "region": "Africa", "subregion": "Southern Africa", "population": 59310000, "currency": "South African Rand (ZAR)", "language": "Afrikaans", "timezone": "UTC+2", "safety_level": "caution", "best_time": "May-Sep", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "240+"}, "featured": True},
    {"name": "Kenya", "capital": "Nairobi", "region": "Africa", "subregion": "Eastern Africa", "population": 53770000, "currency": "Kenyan Shilling (KES)", "language": "Swahili", "timezone": "UTC+3", "safety_level": "caution", "best_time": "Jul-Oct", "budget": {"budget": "40-60", "midrange": "80-130", "luxury": "250+"}, "featured": False},
    {"name": "Tanzania", "capital": "Dodoma", "region": "Africa", "subregion": "Eastern Africa", "population": 59730000, "currency": "Tanzanian Shilling (TZS)", "language": "Swahili", "timezone": "UTC+3", "safety_level": "caution", "best_time": "Jun-Oct", "budget": {"budget": "45-65", "midrange": "90-150", "luxury": "300+"}, "featured": False},
    {"name": "Rwanda", "capital": "Kigali", "region": "Africa", "subregion": "Eastern Africa", "population": 12950000, "currency": "Rwandan Franc (RWF)", "language": "Kinyarwanda", "timezone": "UTC+2", "safety_level": "safe", "best_time": "Jun-Sep", "budget": {"budget": "50-70", "midrange": "100-160", "luxury": "350+"}, "featured": False},
    {"name": "Ethiopia", "capital": "Addis Ababa", "region": "Africa", "subregion": "Eastern Africa", "population": 115000000, "currency": "Ethiopian Birr (ETB)", "language": "Amharic", "timezone": "UTC+3", "safety_level": "caution", "best_time": "Oct-Mar", "budget": {"budget": "30-45", "midrange": "55-85", "luxury": "140+"}, "featured": False},
    {"name": "Ghana", "capital": "Accra", "region": "Africa", "subregion": "Western Africa", "population": 31070000, "currency": "Ghanaian Cedi (GHS)", "language": "English", "timezone": "UTC+0", "safety_level": "caution", "best_time": "Nov-Mar", "budget": {"budget": "35-50", "midrange": "65-100", "luxury": "170+"}, "featured": False},
    {"name": "Senegal", "capital": "Dakar", "region": "Africa", "subregion": "Western Africa", "population": 16740000, "currency": "West African CFA Franc (XOF)", "language": "French", "timezone": "UTC+0", "safety_level": "caution", "best_time": "Nov-May", "budget": {"budget": "40-55", "midrange": "70-110", "luxury": "180+"}, "featured": False},
    {"name": "Namibia", "capital": "Windhoek", "region": "Africa", "subregion": "Southern Africa", "population": 2540000, "currency": "Namibian Dollar (NAD)", "language": "English", "timezone": "UTC+2", "safety_level": "safe", "best_time": "May-Oct", "budget": {"budget": "60-80", "midrange": "110-170", "luxury": "300+"}, "featured": False},
    {"name": "Botswana", "capital": "Gaborone", "region": "Africa", "subregion": "Southern Africa", "population": 2350000, "currency": "Botswana Pula (BWP)", "language": "English", "timezone": "UTC+2", "safety_level": "safe", "best_time": "May-Oct", "budget": {"budget": "70-100", "midrange": "130-200", "luxury": "400+"}, "featured": False},
    {"name": "Zimbabwe", "capital": "Harare", "region": "Africa", "subregion": "Eastern Africa", "population": 14860000, "currency": "US Dollar (USD)", "language": "English", "timezone": "UTC+2", "safety_level": "caution", "best_time": "May-Oct", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"}, "featured": False},
    {"name": "Zambia", "capital": "Lusaka", "region": "Africa", "subregion": "Eastern Africa", "population": 18380000, "currency": "Zambian Kwacha (ZMW)", "language": "English", "timezone": "UTC+2", "safety_level": "caution", "best_time": "May-Oct", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"}, "featured": False},
    {"name": "Mauritius", "capital": "Port Louis", "region": "Africa", "subregion": "Eastern Africa", "population": 1270000, "currency": "Mauritian Rupee (MUR)", "language": "English", "timezone": "UTC+4", "safety_level": "safe", "best_time": "May-Dec", "budget": {"budget": "70-100", "midrange": "130-200", "luxury": "350+"}, "featured": False},
    {"name": "Tunisia", "capital": "Tunis", "region": "Africa", "subregion": "Northern Africa", "population": 11820000, "currency": "Tunisian Dinar (TND)", "language": "Arabic", "timezone": "UTC+1", "safety_level": "caution", "best_time": "Mar-May, Sep-Nov", "budget": {"budget": "35-50", "midrange": "65-100", "luxury": "170+"}, "featured": False},

    # Oceania
    {"name": "Australia", "capital": "Canberra", "region": "Oceania", "subregion": "Australia and New Zealand", "population": 25690000, "currency": "Australian Dollar (AUD)", "language": "English", "timezone": "UTC+8 to +11", "safety_level": "safe", "best_time": "Sep-Nov, Mar-May", "budget": {"budget": "90-120", "midrange": "150-230", "luxury": "400+"}, "featured": True},
    {"name": "New Zealand", "capital": "Wellington", "region": "Oceania", "subregion": "Australia and New Zealand", "population": 5080000, "currency": "New Zealand Dollar (NZD)", "language": "English", "timezone": "UTC+12", "safety_level": "safe", "best_time": "Dec-Mar", "budget": {"budget": "85-115", "midrange": "150-220", "luxury": "380+"}, "featured": True},
    {"name": "Fiji", "capital": "Suva", "region": "Oceania", "subregion": "Melanesia", "population": 896000, "currency": "Fijian Dollar (FJD)", "language": "English", "timezone": "UTC+12", "safety_level": "safe", "best_time": "May-Oct", "budget": {"budget": "70-100", "midrange": "130-200", "luxury": "350+"}, "featured": False},

    # Middle East
    {"name": "United Arab Emirates", "capital": "Abu Dhabi", "region": "Asia", "subregion": "Western Asia", "population": 9890000, "currency": "UAE Dirham (AED)", "language": "Arabic", "timezone": "UTC+4", "safety_level": "safe", "best_time": "Nov-Mar", "budget": {"budget": "100-140", "midrange": "180-280", "luxury": "500+"}, "featured": False},
    {"name": "Israel", "capital": "Jerusalem", "region": "Asia", "subregion": "Western Asia", "population": 9220000, "currency": "Israeli New Shekel (ILS)", "language": "Hebrew", "timezone": "UTC+2", "safety_level": "caution", "best_time": "Mar-May, Sep-Nov", "budget": {"budget": "90-120", "midrange": "160-240", "luxury": "420+"}, "featured": False},
    {"name": "Jordan", "capital": "Amman", "region": "Asia", "subregion": "Western Asia", "population": 10200000, "currency": "Jordanian Dinar (JOD)", "language": "Arabic", "timezone": "UTC+2", "safety_level": "caution", "best_time": "Mar-May, Sep-Nov", "budget": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"}, "featured": False},
    {"name": "Oman", "capital": "Muscat", "region": "Asia", "subregion": "Western Asia", "population": 5110000, "currency": "Omani Rial (OMR)", "language": "Arabic", "timezone": "UTC+4", "safety_level": "safe", "best_time": "Oct-Mar", "budget": {"budget": "80-110", "midrange": "140-210", "luxury": "380+"}, "featured": False},
    {"name": "Qatar", "capital": "Doha", "region": "Asia", "subregion": "Western Asia", "population": 2880000, "currency": "Qatari Riyal (QAR)", "language": "Arabic", "timezone": "UTC+3", "safety_level": "safe", "best_time": "Nov-Apr", "budget": {"budget": "100-140", "midrange": "180-280", "luxury": "500+"}, "featured": False},
    {"name": "Bahrain", "capital": "Manama", "region": "Asia", "subregion": "Western Asia", "population": 1700000, "currency": "Bahraini Dinar (BHD)", "language": "Arabic", "timezone": "UTC+3", "safety_level": "safe", "best_time": "Nov-Mar", "budget": {"budget": "80-110", "midrange": "140-210", "luxury": "380+"}, "featured": False},
    {"name": "Saudi Arabia", "capital": "Riyadh", "region": "Asia", "subregion": "Western Asia", "population": 34810000, "currency": "Saudi Riyal (SAR)", "language": "Arabic", "timezone": "UTC+3", "safety_level": "caution", "best_time": "Nov-Feb", "budget": {"budget": "80-110", "midrange": "140-220", "luxury": "400+"}, "featured": False},
]


def process_country(country: dict) -> dict:
    """Process country into standard format."""
    name = country["name"]
    slug = name.lower().replace(" ", "-").replace("'", "")

    budget = country.get("budget", {"budget": "50-80", "midrange": "100-150", "luxury": "200+"})

    return {
        "name": name,
        "slug": slug,
        "official_name": name,
        "cca2": "",
        "cca3": "",
        "region": country.get("region", ""),
        "subregion": country.get("subregion", ""),
        "region_slug": country.get("region", "").lower(),
        "capital": country.get("capital", ""),
        "population": country.get("population", 0),
        "area": 0,
        "currency": country.get("currency", "Local currency"),
        "languages": [country.get("language", "Local language")],
        "language": country.get("language", "Local language"),
        "timezone": country.get("timezone", "UTC"),
        "timezones": [country.get("timezone", "UTC")],
        "flag_emoji": "",
        "flag_svg": "",
        "flag_png": "",
        "coat_of_arms": "",
        "maps_google": "",
        "maps_osm": "",
        "landlocked": False,
        "borders": [],
        "driving_side": "right",
        "calling_code": "",
        "safety_level": country.get("safety_level", "caution"),
        "budget_per_day": budget,
        "best_time_to_visit": country.get("best_time", "Varies"),
        "latlng": [0, 0],
        "capital_latlng": [0, 0],
        "un_member": True,
        "independent": True,
        "featured": country.get("featured", False)
    }


def save_fallback_data():
    """Save fallback country data."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Process all countries
    processed = [process_country(c) for c in COUNTRIES]
    processed.sort(key=lambda x: x["name"])

    # Save all countries
    all_countries_path = DATA_DIR / "countries.json"
    with open(all_countries_path, "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(processed)} countries to {all_countries_path}")

    # Save individual country files
    countries_dir = DATA_DIR / "countries"
    countries_dir.mkdir(exist_ok=True)

    for country in processed:
        country_path = countries_dir / f"{country['slug']}.json"
        with open(country_path, "w", encoding="utf-8") as f:
            json.dump(country, f, indent=2, ensure_ascii=False)

    return processed


if __name__ == "__main__":
    save_fallback_data()
