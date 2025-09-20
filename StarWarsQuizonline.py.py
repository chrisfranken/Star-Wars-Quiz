import streamlit as st

print = st.write
import random

st.title("My Quiz")

print("🌌 Welcome young Padawan to the STAR WARS QUIZ! 🚀")
print("You will get 20 random questions out of 200. May the Force be with you!\n")
input("Press Enter to start the quiz")
# Each question is stored as: ("Question", ["list of correct answers"])
questions = [
    ("What is the name of Luke Skywalker’s father?", ["anakin", "anakin skywalker"]),
    ("What is the other name of Darth Vader?", ["anakin", "anakin skywalker", "vader"]),
    ("What is the name of Princess Leia’s brother?", ["luke", "luke skywalker"]),
    ("Who trained Luke to be a Jedi?", ["yoda", "obi-wan", "obi wan", "obi-wan kenobi"]),
    ("What color is Yoda’s lightsaber?", ["green"]),
    ("What is Yoda’s homeworld?", ["unknown"]),
    ("Who is Han Solo’s best friend?", ["chewbacca", "chewie"]),
    ("What kind of creature is Chewbacca?", ["wookiee", "wookie"]),
    ("Who is the golden protocol droid?", ["c-3po", "c3po", "threepio"]),
    ("Who is the small astromech droid with blue and white?", ["r2-d2", "r2d2"]),
    ("What ship did Han Solo fly?", ["millennium falcon", "falcon"]),
    ("Who trained Anakin Skywalker?", ["obi-wan", "obi wan", "obi-wan kenobi"]),
    ("Who was Anakin Skywalker’s secret wife?", ["padme", "padmé", "padme amidala"]),
    ("Who is Luke and Leia’s mother?", ["padme", "padmé", "padme amidala"]),
    ("Who was the Sith master of Darth Vader?", ["palpatine", "emperor", "sidious", "darth sidious"]),
    ("What is Emperor Palpatine’s Sith name?", ["darth sidious", "sidious"]),
    ("What weapon do Jedi use?", ["lightsaber", "laser sword"]),
    ("What planet did Luke grow up on?", ["tatooine"]),
    ("What color is Mace Windu’s lightsaber?", ["purple"]),
    ("Who is the wise old Jedi Grand Master?", ["yoda"]),
    ("Who said 'Do or do not. There is no try'?", ["yoda"]),
    ("What color is Darth Vader’s lightsaber?", ["red"]),
    ("What planet is Princess Leia from?", ["Naboo"]),
    ("Who built C-3PO?", ["anakin", "anakin skywalker"]),
    ("What is the name of Jabba?", ["jabba the hutt", "jabba"]),
    ("Who is Boba Fett’s father?", ["jango fett", "jango"]),
    ("Who is the clone army based on?", ["jango fett", "jango"]),
    ("What clones fought in the Clone Wars?", ["clone troopers", "clones"]),
    ("What are the enemies of the clones called?", ["droids", "battle droids"]),
    ("What is the weapon of stormtroopers?", ["blaster", "blaster rifle"]),
    ("Who is the Sith apprentice of Darth Sidious before Vader?", ["darth maul", "maul", "count dooku", "dooku"]),
    ("Who killed Count Dooku?", ["anakin", "anakin skywalker"]),
    ("Who killed Darth Maul (first time)?", ["obi-wan", "obi wan", "obi-wan kenobi"]),
    ("Who was the Jedi friend of Anakin with a blue lightsaber?", ["obi-wan", "obi wan", "obi-wan kenobi"]),
    ("What is Obi-Wan’s nickname?", ["ben", "ben kenobi"]),
    ("Who is Padmé’s daughter?", ["leia", "princess leia"]),
    ("Who is Padmé’s son?", ["luke", "luke skywalker"]),
    ("Who did Han Solo marry?", ["leia", "princess leia"]),
    ("Who froze Han Solo in carbonite?", ["darth vader", "vader", "boba fett", "jabba"]),
    ("What is the desert planet with twin suns?", ["tatooine"]),
    ("Who was the podracer boy from Tatooine?", ["anakin", "anakin skywalker"]),
    ("What was Anakin’s podracer number?", ["7"]),
    ("What animal did Luke ride on Hoth?", ["tauntaun"]),
    ("What snow monster attacked Luke on Hoth?", ["wampa"]),
    ("What is the big ice planet in Empire Strikes Back?", ["hoth"]),
    ("What is the forest moon where Ewoks live?", ["endor"]),
    ("What little teddy bear-like creatures helped the Rebels?", ["ewoks", "ewok"]),
    ("What planet is covered in cities and is the home of the Senate?", ["coruscant"]),
    ("What is the giant space station that can destroy planets?", ["death star"]),
    ("Who destroyed the first Death Star?", ["luke", "luke skywalker"]),
    ("Who led the Rebel Alliance?", ["mon mothma", "princess leia"]),
    ("Who is Lando Calrissian’s friend who flies with him?", ["lando", "lando calrissian"]),
    ("What is the name of Anakin’s Jedi son?", ["luke", "luke skywalker"]),
    ("Who said 'I am your father'?", ["darth vader", "vader", "anakin"]),
    ("Who killed Jabba the Hutt?", ["leia", "princess leia"]),
    ("What color is Luke’s lightsaber in Return of the Jedi?", ["green"]),
    ("What is the weapon of stormtroopers?", ["blaster"]),
    ("What droid speaks in beeps and whistles?", ["r2-d2", "r2d2"]),
    ("What bounty hunter captured Han Solo?", ["boba fett", "boba"]),
    ("What species is Yoda?", ["unknown"]),
    ("What order made the clones attack the Jedi?", ["order 66", "66"]),
    ("Who gave the clones Order 66?", ["palpatine", "sidious", "emperor"]),
    ("Who is General Grievous?", ["cyborg", "general", "sith general", "grievous"]),
    ("How many lightsabers can General Grievous use?", ["4", "four"]),
    ("Who killed General Grievous?", ["obi-wan", "obi-wan kenobi"]),
    ("Who was Queen of Naboo?", ["padme", "padmé", "padme amidala"]),
    ("What color is Leia’s famous dress?", ["white"]),
    ("Who is the rebel pilot with orange hair and mustache?", ["wedge", "wedge antilles"]),
    ("What is the name of Luke’s X-Wing droid?", ["r2-d2", "r2d2"]),
    ("Who is Luke Skywalker’s sister?", ["leia", "princess leia"]),
    ("Who is Luke Skywalker’s father?", ["anakin", "anakin skywalker"]),
    ("Who is Princess Leia’s father?", ["anakin", "anakin skywalker"]),
    ("Who is Princess Leia’s mother?", ["padme", "padmé", "padme amidala"]),
    ("What planet was Princess Leia born on?", ["alderaan"]),
    ("Who adopted Princess Leia?", ["organa", "bail organa", "queen breha"]),
    ("Who raised Luke on Tatooine?", ["beru", "beru whitesun"]),
    ("What color is Luke’s first lightsaber?", ["blue"]),
    ("What color is Luke’s lightsaber in Return of the Jedi?", ["green"]),
    ("What nickname does Obi-Wan use when hiding Luke?", ["ben", "ben kenobi"]),
    ("What was Darth Vader’s name before turning to the dark side?", ["anakin", "anakin skywalker"]),
    ("What is Anakin Skywalker's Sith name?", ["darth vader", "vader"]),
    ("Who trained Anakin Skywalker?", ["obi-wan", "obi wan", "obi-wan kenobi"]),
    ("Who was Anakin Skywalker’s wife?", ["padme", "padmé", "padme amidala"]),
    ("Who are Anakin’s children?", ["luke", "leia"]),
    ("What color is Anakin’s lightsaber?", ["blue"]),
    ("Who said 'I am your father'?", ["darth vader", "vader", "anakin"]),
    ("Who turned Anakin to the dark side?", ["palpatine", "emperor", "sidious", "darth sidious"]),
    ("What planet did Anakin grow up on?", ["Curuscant"]),
    ("What sport did Anakin race in as a boy?", ["podracing", "pod race"]),
    ("Who was the small green Jedi Master?", ["yoda"]),
    ("What color was Yoda’s lightsaber?", ["green"]),
    ("What is Yoda’s homeworld?", ["unknown"]),
    ("Who trained Luke on Dagobah?", ["yoda"]),
    ("Who said 'Do or do not. There is no try'?", ["yoda"]),
    ("Who was the Jedi with a purple lightsaber?", ["mace windu", "mace"]),
    ("What order did the clones follow to attack the Jedi?", ["order 66", "66"]),
    ("Who gave the order to destroy the Jedi?", ["palpatine", "emperor", "sidious"]),
    ("Who was the Jedi General that fought General Grievous?", ["obi-wan", "obi wan", "obi-wan kenobi"]),
    ("Who was the Queen that worked with the Jedi on Naboo?", ["padme", "padmé", "padme amidala"]),
    ("Who is Han Solo’s best friend?", ["chewbacca", "chewie"]),
    ("What kind of creature is Chewbacca?", ["wookiee", "wookie"]),
    ("What is the name of Han Solo’s ship?", ["millennium falcon", "falcon"]),
    ("Who married Princess Leia?", ["han solo", "han"]),
    ("Who won the Millennium Falcon from Lando?", ["han solo", "han"]),
    ("Who froze Han Solo in carbonite?", ["boba fett", "boba", "darth vader", "vader"]),
    ("Who rescued Han Solo from Jabba’s palace?", ["leia", "princess leia"]),
    ("What did Han say instead of 'I love you'?", ["i know"]),
    ("Who shot first in the cantina?", ["han solo", "han"]),
    ("Who did Han owe money to?", ["gambler", "jakku", "lando", "lando calrissian"]),  # simple placeholder
    ("What is the name of the golden protocol droid?", ["c-3po", "c3po", "threepio"]),
    ("Who built C-3PO?", ["anakin", "anakin skywalker"]),
    ("What is the name of the little astromech droid with blue and white?", ["r2-d2", "r2d2"]),
    ("What droid speaks in beeps and whistles?", ["r2-d2", "r2d2"]),
    ("Who was R2-D2’s best friend?", ["c-3po", "c3po", "threepio"]),
    ("What droid often says 'Oh my!'?", ["c-3po", "c3po", "threepio"]),
    ("Which droid carried the Death Star plans in A New Hope?", ["r2-d2", "r2d2"]),
    ("What kind of droid army fought the Jedi?", ["battle droids", "droids"]),
    ("What color is C-3PO?", ["gold"]),
    ("What letters are in R2-D2’s name?", ["r", "2", "d"]),
    ("What desert planet has twin suns?", ["tatooine"]),
    ("What ice planet was the Rebel base on?", ["hoth"]),
    ("What forest moon had Ewoks?", ["endor"]),
    ("What planet was covered in cities and had the Senate?", ["coruscant"]),
    ("Where did Luke meet Yoda?", ["dagobah"]),
    ("Where was the podrace in The Phantom Menace?", ["tatooine"]),
    ("What planet is known for lava rivers and volcanoes?", ["mustafar"]),
    ("Where was the clone army made?", ["kamino"]),
    ("Who is the Sith Lord that was also an Emperor?", ["palpatine", "emperor", "sidious", "darth sidious"]),
    ("What is the Sith name of Emperor Palpatine?", ["darth sidious", "sidious"]),
    ("Who was the Sith with red and black face paint?", ["darth maul", "maul"]),
    ("Who had a double-bladed red lightsaber?", ["darth maul", "maul"]),
    ("Who was the Sith after Darth Maul?", ["count dooku", "dooku", "darth tyranus"]),
    ("Who fought with four lightsabers at once?", ["general grievous", "grievous"]),
    ("Who was Boba Fett’s father?", ["jango fett", "jango"]),
    ("Who captured Han Solo for Jabba?", ["boba fett", "boba"]),
    ("Who is Jabba the Hutt?", ["jabba the hutt", "jabba"]),
    ("Who ordered the clones to execute Order 66?", ["palpatine", "emperor", "sidious"]),
    ("Who led the Rebel Alliance?", ["mon mothma", "princess leia"]),
    ("Who destroyed the first Death Star?", ["luke", "luke skywalker"]),
    ("Who flew with Luke in the Battle of Hoth?", ["wedge", "wedge antilles"]),
    ("Who betrayed Han on Cloud City?", ["lando", "lando calrissian"]),
    ("Who turned against the Empire and helped the Rebels?", ["lando", "lando calrissian"]),
    ("What were the small furry creatures on Endor?", ["ewoks", "ewok"]),
    ("Who helped the Rebels fight on Endor?", ["ewoks", "ewok"]),
    ("Who did Leia disguise herself as in Jabba’s palace?", ["slave leia", "leia"]),
    ("Who fought alongside Leia and Han in Return of the Jedi?", ["luke", "leia", "han"]),
    ("Who said 'It’s a trap!'?", ["admiral ackbar", "ackbar"]),
    ("What giant space station could blow up planets?", ["death star"]),
    ("How many Death Stars were built?", ["2", "two"]),
    ("Who destroyed the second Death Star?", ["luke", "luke skywalker"]),
    ("What ship did Darth Vader fly?", ["tie fighter", "tie"]),
    ("What starfighters did the Rebels use?", ["x-wing", "y-wing"]),
    ("What starfighters did the Empire use?", ["tie fighter", "tie"]),
    ("What ship did Obi-Wan and Qui-Gon take to Naboo?", ["naboo starfighter"]),
    ("What color were the lasers on the Death Star?", ["green", "red"]),  # simplified
    ("What did the Rebels call the attack on the Death Star?", ["battle of yavin"]),
    ("What ship was 'faster than the Kessel Run in 12 parsecs'?", ["millennium falcon", "falcon"]),
    ("What giant snow monster attacked Luke?", ["wampa"]),
    ("What creatures did the Rebels ride on Hoth?", ["tauntaun"]),
    ("What giant slug ruled on Tatooine?", ["jabba the hutt", "jabba"]),
    ("What huge creature lived in Jabba’s dungeon?", ["rancor"]),
    ("What monster lived in the trash compactor?", ["sarlacc", "sarlacc pit"]),  # simplified
    ("What creatures carried Ewoks’ weapons?", ["ewoks", "ewok"]),
    ("What animal pulled Padmé’s chariot on Naboo?", ["horse", "tauntaun", "gungan boat"]),  # simplified
    ("What creature did Obi-Wan ride on Utapau?", ["varactyl", "oya"]),
    ("Who was the podracer boy from Tatooine?", ["anakin", "anakin skywalker"]),
    ("What was Anakin’s podracer number?", ["7"]),
    ("Who is Luke and Leia’s mentor in the Force?", ["obi-wan", "obi wan", "obi-wan kenobi", "yoda"]),
    ("What color is Mace Windu’s lightsaber?", ["purple"]),
    ("Who says 'May the Force be with you' most often?", ["obi-wan", "yoda", "han", "luke"]),
    ("What is the name of the bounty hunter who works for Darth Vader?", ["boba fett", "boba"]),
    ("Who killed Count Dooku?", ["anakin", "anakin skywalker"]),
    ("Who killed Darth Maul (first time)?", ["obi-wan", "obi wan", "obi-wan kenobi"]),
    ("Who was Queen of Naboo?", ["padme", "padmé", "padme amidala"]),
    ("What color is Leia’s famous dress?", ["white"]),
    ("Who is the rebel pilot with orange hair and mustache?", ["wedge", "wedge antilles"]),
    ("What is the name of Luke’s X-Wing droid?", ["r2-d2", "r2d2"]),
    ("Who is the leader of the Trade Federation in Episode I?", ["nute gunray"]),
    ("What is the name of Anakin’s mother?", ["shmi", "shmi skywalker"]),
    ("Who is the Jedi Master that discovers Anakin on Tatooine?", ["qui-gon", "qui-gon jinn"]),
    ("What creature does Qui-Gon fight in the Boonta Eve podrace?", ["pit droid", "racer"]),
    ("Who is Anakin’s podracing rival?", ["sebulba"]),
    ("What kind of droid is R2-D2?", ["astromech droid", "astromech"]),
    ("What kind of droid is C-3PO?", ["protocol droid", "protocol"]),
    ("Who trains Obi-Wan as a Jedi?", ["qui-gon", "qui-gon jinn"]),
    ("Who becomes Darth Vader?", ["anakin", "anakin skywalker", "vader", "darth vader"]),
    ("What is the name of the desert planet with podracing?", ["tatooine"]),
    ("What is the capital city of Naboo?", ["theed"]),
    ("Who is the Sith apprentice of Darth Sidious in Episode I?", ["darth maul", "maul"]),
    ("Who says 'Fear is the path to the dark side'?", ["yoda"]),
    ("What are the clone soldiers made from?", ["jango fett", "clone template"]),
    ("What planet is the Jedi Temple on?", ["coruscant"]),
    ("Who leads the Separatist droid army?", ["count dooku", "darth tyranus"]),
    ("Who is the general with four arms who fights the Jedi?", ["general grievous", "grievous"]),
    ("What color is Anakin’s lightsaber in Episode III?", ["blue"]),
    ("Who kills General Grievous?", ["obi-wan", "obi wan", "obi-wan kenobi"]),
    ("Who is the leader of the Galactic Senate?", ["palpatine", "emperor", "sidious"]),
    ("What is the official title of Darth Sidious?", ["emperor", "galactic emperor"]),
    ("Who says 'So this is how liberty dies… with thunderous applause'?", ["padme", "padmé", "padme amidala"]),
    ("Who says 'Help me, Obi-Wan Kenobi. You’re my only hope'?", ["leia", "princess leia"]),
    ("Who is the Wookiee that helps Han Solo?", ["chewbacca", "chewie"]),
]

# Pick 20 random questions each game
selected_questions = random.sample(questions, 20)
score = 0

for q, answers in selected_questions:
    user_answer = input(q + " ").lower().strip()
    if user_answer in answers:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is one of: {', '.join(answers)}")
    print()

# Final result
print("🎉 Quiz finished! 🎉")
print(f"You got {score} out of {len(selected_questions)} right!")
if score == len(selected_questions):
    print("🏆 Amazing! You are a true Jedi Master!")
elif score >= 7:
    print("🌟 Great job, young Padawan! The Force is strong with you!")
elif score >= 4:
    print("👍 Not bad! Keep training with the Force!")
else:
    print("😅 Oops... more training with Yoda you need!")

print ("Developed by Chris 🤖")
print ("Version 1.0.0 beta")
print ("new update coming soon... 🚀")
print ("Check out my other projects!")
print ("may the Force be with you! ✨")

input("Druk op Enter om het programma af te sluiten...")

