print("Hello welecome to the Movie Recommendation Program")
print("[1] Would you like to continue with the recommendation or")
print("[2] Would you like to end the program.")

genre = {
    "Action": ("Equlibrium","Mad Max: Fury Road", "Die Hard","Matrix","Terminator 2: Judgment Day"),
    "Comedy": ("Spy","Ghostbusters","Kung Fu Hustle","Golmal","Dhamal"),
    "Sci-Fi": ("A Space Odyssey","Interstellar","Blade Runner 2049","The Matrix","Dune: Part Two"),
    "Horror": ("The Shining","Psycho","Hereditary","Alien","The Exorcist"),
    "Thriller": ("Parasite","Se7en","The Silence of the Lambs","Shutter Island","Prisoners"),
    "Drama": ("The Shawshank Redemption","Oppenheimer","The Godfather","Whiplash","Parasite")
}

user_input = input("Choose the option that you want to continue with: ")

if user_input == "1":
    print("Loading program... \n")
    print("Possible genre selection available are" , sorted(genre))
    user_movie_input = input("Enter the type of genre for which you want to know the movie recommendation: ")
    genresellection = user_movie_input.capitalize()
    if any(gen in genresellection for gen in genre):
        print("The movie recommendtion are:", genre[genresellection])
    else:
        print("!!ERROR!! ..Movie Genre not available.. !!ERROR!!")
else:
    print("Thank you for visiting the program do come again later")