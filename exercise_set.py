oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}

titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}

dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}

avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",
                   "Chris Hemsworth", "Jeremy Renner"}

iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}

legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}

actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}

movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# a
oscar_winners.add("Emma Watson")
print("a. oscar_winners after adding Emma Watson:", oscar_winners)

# b
oscar_winners.clear()
print("b. oscar_winners after clearing:", oscar_winners)

# c
oscar_winners_copy = oscar_winners.copy()
print("c. oscar_winners copy:", oscar_winners_copy)

# d
oscar_winners.discard("Meryl Streep")
print("d. oscar_winners after discarding Meryl Streep:", oscar_winners)

# e
common_actors = titanic_actors.intersection(dark_knight_actors)
print("e. Common actors in Titanic and Dark Knight:", common_actors)

# f
common_actors_iron_avengers = iron_man_actors.intersection(avengers_actors)
print("f. Common actors in Iron Man and Avengers:", common_actors_iron_avengers)

# g
are_all_oscar_winners = actor_list.issubset(oscar_winners)
print("g. Are all actors in actor_list Oscar winners?:", are_all_oscar_winners)

# h
avengers_actor_list_intersection = actor_list.intersection(avengers_actors)
print("h. Actors in actor_list who appeared in Avengers:", avengers_actor_list_intersection)

#  i
random_actor_removed = movie_cast.pop()
print("i. Random actor removed from movie_cast:", random_actor_removed)
print("i. movie_cast after random removal:", movie_cast)

# j
movie_cast.discard("Will Smith")
print("j. movie_cast after discarding Will Smith:", movie_cast)

# k
titanic_non_oscar_winners = titanic_actors.difference(oscar_winners)
print("k. Actors in Titanic who didn't win an Oscar:", titanic_non_oscar_winners)

# l
titanic_or_dark_knight_only = titanic_actors.symmetric_difference(dark_knight_actors)
print("l. Actors who appeared in Titanic or Dark Knight but not both:", titanic_or_dark_knight_only)

# m
oscar_winners.update({"Cate Blanchett", "Daniel Day-Lewis"})
print("m. oscar_winners after adding Cate Blanchett and Daniel Day-Lewis:", oscar_winners)

# n
titanic_and_dark_knight_union = titanic_actors.union(dark_knight_actors)
print("n. Union of Titanic and Dark Knight actors:", titanic_and_dark_knight_union)

# o
dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman", "Tom Hardy", "Joseph Gordon-Levitt"}
all_dark_knight_in_rises = dark_knight_actors.issubset(dark_knight_rises_actors)
print("o. Are all Dark Knight actors in The Dark Knight Rises?:", all_dark_knight_in_rises)

# p
are_all_oscar_winners_in_legendary = oscar_winners.issubset(legendary_actors)
print("p. Does legendary_actors include all Oscar winners?:", are_all_oscar_winners_in_legendary)

# q
avengers_not_in_iron_man = avengers_actors.difference(iron_man_actors)
print("q. Actors in Avengers who didn't appear in Iron Man:", avengers_not_in_iron_man)

# r
dark_knight_or_avengers_only = dark_knight_actors.symmetric_difference(avengers_actors)
print("r. Actors who appeared in Dark Knight or Avengers but not both:", dark_knight_or_avengers_only)

# s
dark_knight_and_iron_man_union = dark_knight_actors.union(iron_man_actors)
print("s. Union of Dark Knight and Iron Man actors:", dark_knight_and_iron_man_union)

# t
legendary_frozen_set = frozenset(legendary_actors)
print("t. Frozen set of legendary actors:", legendary_frozen_set)

# שאלה 2
# גם dict וגם set משתמשים ב-"hash table" לאחסון נתונים מה שעוזר להם להיות מהירים מאוד כשמוסיפים או מחפשים נתונים.
# ב-set שומרים רק על איברים ייחודיים בלי ערכים  וב-dict יש גם מפתחות וגם ערכים אבל שניהם לא שומרים על סדר מסוים של הנתונים

# שאלה 3
#גם dict וגם set משתמשים ב-"hash table" לאחסון נתונים מה שעוזר להם להיות מהירים מאוד כשמוסיפים או מחפשים נתונים
# ב-set שומרים רק על איברים ייחודיים בלי ערכים וב-dict יש גם מפתחות וגם ערכים אבל שניהם לא שומרים על סדר מסוים של הנתונים