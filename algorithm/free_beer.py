def run_algorithm(name, age, likes_beer):
    if age < 18 or not likes_beer:
        return False

    score = sum(ord(i) - ord("a") for i in name.lower().replace(" ", ""))

    return score > 80
