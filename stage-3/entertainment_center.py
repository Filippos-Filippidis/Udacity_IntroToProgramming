import media
import fresh_tomatoes

District_9 = media.Movie("District 9", "The story, which explores themes of humanity, xenophobia, and social segregation, begins in an alternate 1982, when an alien ship appears over Johannesburg, South Africa",
                         "https://upload.wikimedia.org/wikipedia/en/d/d7/District_nine_ver2.jpg",
                         "https://www.youtube.com/watch?v=DyLUwOcR5pk",
                         "http://i.imgur.com/espB8pV.png")

Ex_Machina = media.Movie("Ex Machina", "Caleb Smith wins a contest that enables him to spend a week at the private estate of Nathan Bateman. When he arrives, Caleb learns he is to determine the capabilities and consciousness of Ava, a beautiful robot. However, it soon becomes evident that Ava is far more self-aware and deceptive than either man imagined",
                         "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
                         "https://www.youtube.com/watch?v=XYGzRB4Pnq8&vl=en",
                         "http://i.imgur.com/cYpHynU.png")

Blade_Runner = media.Movie("Blade Runner", "Deckard is forced by the police Boss to continue his old job as Replicant Hunter. His assignment: eliminate four escaped Replicants from the colonies who have returned to Earth. Before starting the job, Deckard goes to the Tyrell Corporation and he meets Rachel, a Replicant girl he falls in love with.",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis",
                           "http://i.imgur.com/cYpHynU.png")

Mad_Max = media.Movie("Mad Max", "Years after the collapse of civilization, the tyrannical Immortan Joe enslaves apocalypse survivors inside the desert fortress the Citadel. When the warrior Imperator Furiosa leads the despot's five wives in a daring escape, she forges an alliance with Max Rockatansky, a loner and former captive. Fortified in the massive, armored truck the War Rig, they try to outrun the ruthless warlord and his henchmen in a deadly high-speed chase through the Wasteland.",
                      "https://resizing.flixster.com/iRABduPrqxHFlSDcW4h_cEToY3Q=/206x305/v1.bTsxMTE5MTI3NjtqOzE3NzY5OzEyMDA7NTA5Ozc1NQ",
                      "https://www.youtube.com/watch?v=cdLl1GVjOrc",
                      "http://i.imgur.com/HCYFJht.png")

ET = media.Movie("E.T. THE EXTRA-TERRESTRIAL", "After a gentle alien becomes stranded on Earth, the being is discovered and befriended by a young boy named Elliott. Bringing the extraterrestrial into his suburban California house, Elliott introduces E.T., as the alien is dubbed, to his brother and his little sister, Gertie, and the children decide to keep its existence a secret. Soon, however, E.T. falls ill, resulting in government intervention and a dire situation for both Elliott and the alien.",
                 "https://resizing.flixster.com/Mc6Z4huvaWUYkKNhBDqRCd5PIuM=/206x305/v1.bTsxMTE2Njc4ODtqOzE3NzY5OzEyMDA7ODAwOzEyMDA",
                 "https://www.youtube.com/watch?v=taMnCjzKgd8",
                 "http://i.imgur.com/8RHeC2D.png")

GRAVITY = media.Movie("GRAVITY", "Dr. Ryan Stone is a medical engineer on her first shuttle mission. Her commander is veteran astronaut Matt Kowalsky, helming his last flight before retirement. Then, during a routine space walk by the pair, disaster strikes: The shuttle is destroyed, leaving Ryan and Matt stranded in deep space with no link to Earth and no hope of rescue. As fear turns to panic, they realize that the only way home may be to venture further into space.",
                      "https://resizing.flixster.com/Qr71qDsGLUaU69il9kWl4u1pB5M=/206x305/v1.bTsxMTE3NjQ1MDtqOzE3NzY5OzEyMDA7ODAwOzEyMDA",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4",
                      "http://i.imgur.com/2AmVX0u.png")

movies = [District_9, Ex_Machina, Blade_Runner, Mad_Max, ET, GRAVITY]
fresh_tomatoes.open_movies_page(movies)