# №1
class User:
    def __init__(self):
        self.watched_films = []

    def watch(self, film_id: list):
        for i in range(len(film_id)):
            self.watched_films.append(int(film_id[i]))

    def ln(self):
        return len(self.watched_films)


class Films:
    def __init__(self, film_id: int, name: str):
        self.film_id = film_id
        self.name = name
        self.veuvers = 0

    def add_veuver(self):
        self.veuvers += 1

    def __str__(self):
        return f'id:{self.film_id}, name:{self.name}, w:{self.veuvers}'


def recomendation(user_watched_films_id: list):
    # list of films
    films = {}
    with open('all_films.txt') as p:
        for line in p:
            film_id, name = line.strip().split(',')
            film = Films(int(film_id), name)
            films[int(film_id)] = film
    p.close()

    user_f = User()
    user_f.watch(user_watched_films_id)  # list of int films

    with open('users_history.txt') as f:
        for stroks in f:
            list_of_film = set(list(map(int, stroks.strip().split(','))))  # list_of int films
            count = 0
            for film_d in list_of_film:
                if film_d in user_f.watched_films:
                    count += 1

            if count >= (user_f.ln() // 2):  # Если больше половины просмотров совпадает, то добавляем зрителей к id фильму
                for film_d2 in list_of_film:
                    if film_d2 not in user_f.watched_films:
                        films[film_d2].add_veuver()
    f.close()

    most_popular_film_name = -1  # name of film with biggest weuwers
    most_wuwers = 0  # count of weuwers, biggest

    # Ищем фильм с самыми большими просмотрами
    for el in films.keys():
        if films[el].veuvers > most_wuwers:
            most_wuwers = films[el].veuvers
            most_popular_film_name = films[el].name
    if most_popular_film_name == -1:
        return 'We can`t recomend you a film'
    return most_popular_film_name


print(recomendation([6, 7]))


