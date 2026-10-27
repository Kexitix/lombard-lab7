# Работа с базой данных db_blog через модуль sqlite3 (менеджер БД SQLite)
# Запуск: python sqlite_manager.py <команда>
import sqlite3
import sys
from datetime import date

con = sqlite3.connect("db_blog")
cur = con.cursor()


def show():
    print("Таблица articles_article:")
    print("id".ljust(4), "title".ljust(48), "author_id".ljust(10), "created_date")
    for row in cur.execute("SELECT id, title, author_id, created_date FROM articles_article ORDER BY id"):
        print(str(row[0]).ljust(4), row[1].ljust(48), str(row[2]).ljust(10), row[3])


cmd = sys.argv[1] if len(sys.argv) > 1 else "show"

if cmd == "show":
    show()

elif cmd == "edit":
    # изменяем текст одной записи и название другой
    cur.execute("UPDATE articles_article SET text = ? WHERE id = 1",
                ("Чтобы получить займ под залог золота, достаточно паспорта. Оценщик проверяет пробу и вес "
                 "изделия, после чего клиенту сразу выдаются деньги. Текст статьи изменён через менеджер "
                 "базы данных SQLite.",))
    cur.execute("UPDATE articles_article SET title = ? WHERE id = 2",
                ("Большая распродажа зимних вещей",))
    # создаём ещё одну статью
    cur.execute("INSERT INTO articles_article (title, text, created_date, author_id) VALUES (?, ?, ?, ?)",
                ("Как ломбард оценивает технику",
                 "Ноутбуки, смартфоны и инструменты принимаются в залог после проверки работоспособности. "
                 "Сумма займа обычно составляет 50-70% от рыночной стоимости товара, комиссия - 4% в месяц.",
                 date.today().isoformat(), 1))
    con.commit()
    print("UPDATE: изменён текст статьи id=1, название статьи id=2")
    print("INSERT: добавлена статья id=%d" % cur.lastrowid)
    show()

elif cmd == "add":
    # новая запись в блог через менеджер базы
    cur.execute("INSERT INTO articles_article (title, text, created_date, author_id) VALUES (?, ?, ?, ?)",
                ("Срок залога и продление займа",
                 "Если клиент не успевает вернуть деньги в срок, залог можно продлить, оплатив комиссию "
                 "за прошедший период. Если в указанный срок деньги не возвращены и залог не продлён, товар "
                 "переходит в собственность ломбарда.",
                 date.today().isoformat(), 2))
    con.commit()
    print("INSERT: добавлена статья id=%d" % cur.lastrowid)
    show()

con.close()
