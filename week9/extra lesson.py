import matplotlib.pyplot as plt

def coffee_sleep(n = 1):
    coffee = []
    sleep = []
    for person in range (n):
        coffee.append(int(input("Enter the ammount of coffee you drink per week: ")))
        sleep.append(int(input("Enter your average sleep length per night: ")))
    return coffee, sleep

def movie(n=1):
    movies = {}
    for person in range(n):
        m_genre = input("Enter your favourite movie genre: ")
        movies[m_genre] = movies.get(m_genre, 0) + 1
    return movies

def music(n=1):
    songs = dict()
    for i in range(n):
        m_genre = input("Enter your favourite music genre: ")
        songs[m_genre] = songs.get(m_genre, 0) + 1
    return songs

def mm_vs_dd(n=1):
    mm = 0
    dd = 0
    for i in range(n):
        ans = input("Who wins? Micky Mouse or Donald Duck?")
        if ans.upper() == "DD":
            dd += 1
        elif ans.upper() == "MM":
            mm += 1
    return [mm, dd]

def run():
    fig = plt.figure()

    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    n = int(input("Enter the number of people taking part in the survey: "))
    c_s = coffee_sleep(n)
    ms = movie(n)
    ss = music(n)
    lista = []
    for i in ms:
      dist = float(input("How much explosion? "))
      lista.append(dist)

    ax1.plot(c_s[0],c_s[1], "rx")
    ax2.pie(ms.values(), labels = ms.keys(), autopct = "%.f%%", explode = lista)
    ax3.pie(ss.values(), labels = ss.keys(), autopct = "%1.1f%%")
    ax4.bar(["Micky", "Donald"], mm_vs_dd(n))
    ax1.set_xlabel("Coffe intake")
    ax1.set_ylabel("Sleep")
    ax4.set_xlabel("Favourite Character")
    ax4.set_ylabel("Number of responses")
    plt.tight_layout()
    plt.show()

run()