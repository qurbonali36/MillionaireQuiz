from rich.console import Console
from itertools import cycle

console = Console()

# 1. Faqat terminalda chiroyli ko'rinadigan, yorqin ranglarni tanlaymiz
chiroyli_ranglar = ["bold cyan", "bold magenta", "bold green", "bold yellow", "bold white"]

# 2. itertools.cycle orqali bu ranglarni cheksiz aylanadigan qilib qo'yamiz
rang_generator = cycle(chiroyli_ranglar)

# 3. O'zimizning shaxsiy avtomatik rangli print funksiyamizni yozamiz
def aprint(*args):
    """Barcha yozuvlarni qabul qilib, o'zi avtomatik xavfsiz rang beradi"""
    # Matnlarni birlashtiramiz
    matn = " ".join(map(str, args))
    
    # Navbatdagi rangni olamiz
    rang = next(rang_generator)
    
    # Rich orqali ekranga chiqaramiz
    console.print(f"[{rang}]{matn}[/{rang}]")

