import instaloader

# Создаем экземпляр Instaloader
L = instaloader.Instaloader()

# Укажите имя пользователя, профиль которого вы хотите получить
username = "@_aleksandra_muzurantova_"  # Замените на нужное имя пользователя

try:
    # Загружаем профиль
    profile = instaloader.Profile.from_username(L.context, username)

    # Выводим информацию о профиле
    print(f"[+] Profile info: {username}")
    print(f"Biography: {profile.biography}")
    print(f"Posts count: {profile.mediacount}")
    print(f"Followers: {profile.followers}")
    print(f"Following: {profile.followees}")

    # Парсинг фотографий
    print("\n[+] Photos:")
    for post in profile.get_posts():
        # Выводим ссылки на фото (если они есть)
        if post.typename == "GraphImage":  # Одиночное изображение
            print(post.url)
        elif post.typename == "GraphSidecar":  # Галерея изображений
            for edge in post.get_sidecar_nodes():
                print(edge.display_url)

except instaloader.exceptions.ProfileNotExistsException:
    print(f"Profile '{username}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")