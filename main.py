from flask import Flask, render_template ,url_for     # ми беремо "Flask" з бібліотеки. Flask = це інструмент, який вміє робити сайти.

app = Flask(__name__)        # створюємо сайт (об'єкт "app").__name__ передає назву файла
                            # __name__ потрібен, щоб Flask знав, де шукати файли і ресурси.
@app.route("/")              # url адреса головного сайту на якому ми вивогдимо Hello, World! .'/' обовяковий !!ROUTE нова функціяі!!
def hello():                 # тоді виконай цю функцію (hello)
    return render_template("index2.html")   # функція повертає текст. Flask відправляє цей текст у браузер.
                             # Тому користувач бачить саме "Hello, World!"


@app.route("/about")       
def about():
    return render_template("index.html")          


if __name__ == "__main__":   # якщо цей файл буе основним для запуска іменно через цей файл в __name__ Zaide __main__
    app.run()                # запускаємо сервер
 

