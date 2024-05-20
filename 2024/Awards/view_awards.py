def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50,"="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class AwardsUserInterface:
    @add_title('Редактирование данных каталога фильмов')
    def wait_awards_user_interface(self):
        print("Действия с фильмами: ")
        print("1 - добавление фильма"
              "\n2 - каталог фильма"
              "\n3 - просмотр определённого фильма"
              "\n4 - перемотка фильма"
              "\n5 - монтаж фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_awards = input("Выберите вариант действия: ")
        print("= * 50")
        return user_awards

    @address('Создание фильма')
    def add_user_awards(self):
        dict_awards = {
            "название": None,
            "жанр": None,
            "режисёр": None,
            "год выпуска": None,
            "длительность": None,
            #"студия": None,
            "актёры": None,
            # "кассовый сбор": None
        }
        print(" Создание фильма: ".center(50, "="))
        for key in dict_awards:
            dict_awards[key] = input(f"Введите  {key} статьи: ")
        print("=" * 50)
        return dict_awards

    def show_all_awards(self, awardes):
        print("Список фильмов: ".center(50, "="))
        for ind, awards in enumerate(awardes, start=1):
            print(f"{ind}. {awards}")
        print("=" * 50)

    @add_title("Каталог фильмов")
    def show_all_movies(self, movies):
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie}")

    @add_title("Ввод названия фильма")
    def get_user_movie(self):
        user_movie = input("Введите название фильма: ")
        return user_movie

    @add_title("Просмотр информации о фильме")
    def show_single_movie(self, movie):
        for key in movie:
            print(f"{key} фильма - {movie[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_movie(self, movie):
        print(f"Фильм {movie} - был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")

