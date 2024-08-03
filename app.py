from flask import Flask, render_template
from student import Student


app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "index.html",
        menu=menu(index),
    )
    # return render_template("index.html", menu=[1, 2, 3, 4])
    # return render_template("index.html", context=context)


@app.get("/results")
def results():
    # list(students()).sort(key=Student.score, reverse=True)
    # students|sort(attribute="score", reverse=True)
    return render_template(
        "results.html",
        menu=menu(results),
        students=students(),
    )


def menu(endpoint: callable) -> tuple[str]:
    if endpoint == index:
        return (
            index.__name__,
            results.__name__,
        )
    return (
        results.__name__,
        index.__name__,
    )


def students() -> tuple[Student]:
    return (
        Student("Вадим Янковський", 65),
        Student("Михайло Ковальчук", 43.3),
        Student("Назар Лазарчук", 95),
        Student("Олексій Оксюта", 95),
        Student("Богдан Сингаївський", 95),
        Student("Ірина Бастрига", 100),
    )


if __name__ == "__main__":
    app.run(debug=True)
