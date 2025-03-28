def mad_libs():
    print("🔹 Welcome to the Mad Libs Game! 🔹\n")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")

    story = f"""
    🌟 Here is your Mad Libs Story! 🌟

    One day, {name} went to {place}. It was a very {adjective} place.
    Suddenly, {name} saw a {noun} and decided to {verb}.
    It was an unforgettable experience!

    🎉 Hope you liked your story! 🎉
    """

    print(story)

if __name__ == "__main__":
    mad_libs()
