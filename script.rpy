# The script of the game goes in this file.

#WARNING INTRO
#---------------------------------------------------------------------------------------------------------------------------------------

default persistent.seen_content_warning = False

label splashscreen:

    if persistent.seen_content_warning:
        return

    scene black
    with Pause(0.5)

    centered "{color=#000000}Contains mature and disturbing themes. Viewer discretion is advised.{/color}"

    centered "{color=#000000}For the full list of content warnings, visit my itch.io page: {a=https://glxysel-le.itch.io/drawntoyou}{u}Drawn to You{/u}{/a}{/color}"

    menu:
        "I understand and want to continue.":
            $ persistent.seen_content_warning = True
            return

        "Exit.":
            $ renpy.quit()

# random defines ##############################################################################################################

transform jumpscare_shake:
    xalign 0.5
    yalign 0.5
    zoom 0.8

    linear 0.08 zoom 1.15
    linear 0.04 xoffset -25
    linear 0.04 xoffset 25
    linear 0.04 xoffset -15
    linear 0.04 xoffset 15
    linear 0.03 xoffset 0

init python:

    def restart_brushes_and_blues():
        renpy.music.play(
            "audio/Brushes_and_Blues.mp3",
            channel="music",
            loop=False,
            fadein=0.0
        )
        renpy.music.set_volume(0.35, delay=0.0, channel="music")


screen brushes_and_blues_loop():

    timer 52.0 action Function(restart_brushes_and_blues) repeat True

transform hop:
    yoffset 0
    ease 0.1 yoffset 20
    ease 0.1 yoffset 0

transform luka_lunge:
    xalign 0.22
    linear 0.18 xalign 0.43

init:
    $ timer_range = 0
    $ timer_jump = ""

screen countdown():

    timer 0.01 repeat True action If(
        time > 0,
        true=SetVariable("time", time - 0.01),
        false=[Hide("countdown"), Jump(timer_jump)]
    )



# VARIABLES ####################################################################################################################'

default luka_interest = 0

default persistent.skin_tone = "light"

image cg_luka_cloth = ConditionSwitch(
    "persistent.skin_tone == 'light'", "cg/luka_cloth_light.png",
    "persistent.skin_tone == 'tan'", "cg/luka_cloth_tan.png",
    "persistent.skin_tone == 'medium'", "cg/luka_cloth_medium.png",
    "persistent.skin_tone == 'dark'", "cg/luka_cloth_dark.png"
)

image cg_luka_cloth_blush = ConditionSwitch(
    "persistent.skin_tone == 'light'", "cg/luka_cloth_blush_light.png",
    "persistent.skin_tone == 'tan'", "cg/luka_cloth_blush_tan.png",
    "persistent.skin_tone == 'medium'", "cg/luka_cloth_blush_medium.png",
    "persistent.skin_tone == 'dark'", "cg/luka_cloth_blush_dark.png"
)

image bg bedroom phone = ConditionSwitch(
    "persistent.skin_tone == 'light'", "bg bedroom phone light",
    "persistent.skin_tone == 'tan'", "bg bedroom phone tan",
    "persistent.skin_tone == 'medium'", "bg bedroom phone medium",
    "persistent.skin_tone == 'dark'", "bg bedroom phone dark"
)

image cg luka caspian = ConditionSwitch(
    "persistent.skin_tone == 'light'", "images/cg/luka_caspian_light.png",
    "persistent.skin_tone == 'tan'", "images/cg/luka_caspian_tan.png",
    "persistent.skin_tone == 'medium'", "images/cg/luka_caspian_medium.png",
    "persistent.skin_tone == 'dark'", "images/cg/luka_caspian_dark.png"
)

init python:
    def luka_affection(amount):
        global luka_interest
        luka_interest = max(0, luka_interest + amount)

default player_gender = "female"

default they = "she"
default them = "her"
default their = "her"
default theirs = "hers"
default themself = "herself"

default be = "is"
default have = "has"

default drink_order = ""
default drink_name = ""

default linked_arms = False
default close = False

default went_on_date = False

default persistent.dialogueBoxOpacity = 0.75

default skin_tone = "light"
default skin_tone_num = 1

default persistent.promise = False
default caspian_flirted = False

default persistent.has_seen_ending = False
default persistent.gallery_recommendation_seen = False


# THIS IS WHERE ALL THE IMAGES ARE DEFINED
#---------------------------------------------------------------------------------------------------------------------------------------

image luka = "sprite/luka/luka.png"
image luka talk = "sprite/luka/luka_talk.png"
image luka shock = "sprite/luka/luka_shock.png"
image luka talk arm = "sprite/luka/luka_talk_arm.png"
image luka shock arm = "sprite/luka/luka_shock_arm.png"
image luka awkward = "sprite/luka/luka_awkward.png"
image luka blush = "sprite/luka/luka_blush.png"
image luka pissed = "sprite/luka/luka_pissed.png"
image luka mad = "sprite/luka/luka_mad.png"
image luka talk blush ="sprite/luka/luka_talk_blush.png"

image luka_blood = "sprite/luka/luka_blood.png"
image luka_blood talk = "sprite/luka/luka_blood_talk.png"

image luka_sit normal= "sprite/luka/luka_sit.png"
image luka_sit talk = "sprite/luka/luka_sit_talk.png"
image luka_sit awkward = "sprite/luka/luka_sit_awkward.png"
image luka_sit shock = "sprite/luka/luka_sit_shocked.png"
image luka_sit down = "sprite/luka/luka_sit_down.png"
image luka_sit happy = "sprite/luka/luka_sit_happy.png"


image cg_luka_blush = "cg/luka_blush.png"
image cg_luka_kiss = ConditionSwitch(
    "persistent.skin_tone == 'light'", "sprite/luka/luka_kiss_light.png",
    "persistent.skin_tone == 'tan'", "sprite/luka/luka_kiss_tan.png",
    "persistent.skin_tone == 'medium'", "sprite/luka/luka_kiss_medium.png",
    "persistent.skin_tone == 'dark'", "sprite/luka/luka_kiss_dark.png"
)
image cg_luka_cheek = ConditionSwitch(
    "persistent.skin_tone == 'light'", "sprite/luka/luka_cheek_light.png",
    "persistent.skin_tone == 'tan'", "sprite/luka/luka_cheek_tan.png",
    "persistent.skin_tone == 'medium'", "sprite/luka/luka_cheek_medium.png",
    "persistent.skin_tone == 'dark'", "sprite/luka/luka_cheek_dark.png"
)

image cg_badend_dooropen = ConditionSwitch(
    "persistent.skin_tone == 'light'", "images/cg/BadEnd_DoorOpen_light.PNG",
    "persistent.skin_tone == 'tan'", "images/cg/BadEnd_DoorOpen_tan.PNG",
    "persistent.skin_tone == 'medium'", "images/cg/BadEnd_DoorOpen_medium.PNG",
    "persistent.skin_tone == 'dark'", "images/cg/BadEnd_DoorOpen_dark.PNG"
)

image vivi ="sprite/vivi/vivi.png"
image vivi pout ="sprite/vivi/vivi_pout.png"
image vivi talk ="sprite/vivi/vivi_talk.png"
image vivi smile ="sprite/vivi/vivi_smile.png"

image bg bench = "images/bg/bench.png"
image vivi sit = "images/sprite/vivi/vivi_sit.png"
image vivi sit up = "images/sprite/vivi/vivi_sit_in.png"
image vivi sit out = "images/sprite/vivi/vivi_sit_out.png"
image vivi sit talk = "images/sprite/vivi/vivi_sit_talk.png"


image caspian = "sprite/caspian/caspian.png"
image caspian talk = "sprite/caspian/caspian_talk.png"
image caspian oh = "sprite/caspian/caspian_oh.png"
image caspian flirt = "sprite/caspian/caspian_flirt.png"
image caspian proud = "sprite/caspian/caspian_proud.png"

image caspian_blood = "images/sprite/caspian/caspian_blood.png"
image caspian_blood talk = "images/sprite/caspian/caspian_blood_talk.png"
image caspian_blood angry = "images/sprite/caspian/caspian_blood_angry.png"

image c_walk eyebrow = "images/sprite/caspian/c_walk_eyebrow.png"
image c_walk grin = "images/sprite/caspian/c_walk_grin.png"
image c_walk talk = "images/sprite/caspian/c_walk_talk.png"
image c_walk shy = "images/sprite/caspian/c_walk_shy.png"
image c_walk = "images/sprite/caspian/c_walk_normal.png"
image c_walk shy out = "images/sprite/caspian/pc_walk_shy.png"


image bg art = "images/bg/classroom.png"
image bg town = "images/bg/town.png"
image bg walkhome = "images/bg/walkhome.png"
image bg store front = "images/bg/store_front.png"
image bg store back = "images/bg/store_back.png"
image bg bedroom = "images/bg/bedroom.PNG"
image bg shop = "images/bg/shop.PNG"
image bg coffee = "images/bg/coffeeshop.png"

image run_basement = "images/bg/run_basement.png"
image run_base_stairs = "images/bg/run_basestairs.png"
image run_bathroom = "images/bg/run_bathroom.png"
image run_dining = "images/bg/run_dining.png"
image run_door = "images/bg/run_door.png"
image run_kitchen = "images/bg/run_kitchen.png"
image run_living_room = "images/bg/run_livingroom.png"
image run_upstairs = "images/bg/run_upstairs.png"


image bg bedroom phone light = "images/bg/bg_phone_light.png"
image bg bedroom phone tan = "images/bg/bg_phone_tan.png"
image bg bedroom phone medium = "images/bg/bg_phone_medium.png"
image bg bedroom phone dark = "images/bg/bg_phone_dark.png"

image cg luka caspian light = "images/cg/luka_caspian_light.png"
image cg luka caspian tan = "images/cg/luka_caspian_tan.png"
image cg luka caspian medium = "images/cg/luka_caspian_medium.png"
image cg luka caspian dark = "images/cg/luka_caspian_dark.png"

# DEFINING CHARACTERS
#---------------------------------------------------------------------------------------------------------------------------------------

define mc = Character("[player_name]")
define i = Character("Intructor")
define ml = Character("Luka")
define u = Character("???")
define b = Character("Barista")
define v = Character("Vivi")
define c = Character("Caspian")


# The game starts here.

label start:

    default player_name = ""


label name_input:

    $ renpy.music.set_volume(0.3, delay=2.0)

    $ player_name = renpy.input("Please enter your name:", default="Jane", length=12)
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Jane"

    "Your name is [player_name]."

    menu:
        "Is this correct?"

        "Yes":
            jump choose_gender
            
        "No":
            jump name_input

    

label choose_gender:

        "How do you identify?"

        menu:
            "Female":
                $ player_gender = "female"

                $ they = "she"
                $ them = "her"
                $ their = "her"
                $ theirs = "hers"
                $ themself = "herself"

                $ be = "is"
                $ have = "has"

            "Male":
                $ player_gender = "male"
       
                $ they = "he"
                $ them = "him"
                $ their = "his"
                $ theirs = "his"
                $ themself = "himself"

                $ be = "is"
                $ have = "has"

            "Non-binary":
                $ player_gender = "non-binary"

                $ they = "they"
                $ them = "them"
                $ their = "their"
                $ theirs = "theirs"
                $ themself = "themself"

                $ be = "are"
                $ have = "have"

        jump skin_tone_choice

label skin_tone_choice:

    "Choose your skin tone."

    menu:
        "Light":
            $ persistent.skin_tone = "light"

        "Tan":
            $ persistent.skin_tone = "tan"

        "Medium":
            $ persistent.skin_tone = "medium"

        "Dark":
            $ persistent.skin_tone = "dark"

    jump chapter_one

label chapter_one:

    play music "audio/jazz2.mp3" fadein 1.0

    scene bg bedroom with fade
    # with dissolve
    # play music "audio/___.ogg" fadein 2.0

    "The past few months have been... frustrating."
    "I still love drawing. I don't think that feeling will ever go away."

    "But every time I open my sketchbook, my mind just goes blank."

    "I sit in my bed with my sketchbook."

    scene bg bedroom phone with dissolve

    "With a sigh, I let my pencil roll across my lap and reached for my phone instead."

    "I open up the app Afterlight"

    "I've had this account forever. It's not really an art account or anything, it's just... me."

    "Pictures with friends, random sunsets, cafe drinks that looked too pretty not to photograph, flowers I found on walks, birthday posts, vacations, songs I couldn't stop listening to, and every now and then, one of my drawings when I actually finished something I liked." 

    "Scrolling through my own profile almost felt nostalgic."

    "I used to post so so much. I wonder if I should get back into it."

    "I take a photo of the empty page."

    "What should the caption be?"

    menu:
        "still waiting for the creativity to come home.":
            $ caption_choice = "still waiting for the creativity to come home."
            jump caption_post

        "haven't disappeared lol.":
            $ caption_choice = "haven't disappeared lol."
            jump caption_post

        "my sketchbook is collecting dust.":
            $ caption_choice = "my sketchbook is collecting dust."
            jump caption_post


label caption_post:

    "Within a few minutes, my phone buzzed with notifications. A couple of my friends left encouraging comments."

    # SHOW THIS IN THE DRAWING
    # "I've missed seeing your drawings."
    #"You'll get your motivation back."
    #"Don't pressure yourself too much."

    "I read the comments and smiled without realizing it. Maybe they were right."

    "I kept scrolling through my feed until an advertisement caught my eye."

    "Riverstone Community Art Studio, Six-Week Illustration Workshop, All Skill Levels Welcome Weekly prompts. Meet local artists. Improve your skills in a relaxed environment!"

    mc  "...Maybe this is exactly what i need."

    "Before I could overthink it, I filled out the registration form. A confirmation email appeared almost instantly."

    "You're all set! We can't wait to meet you this Saturday. "

    "Well… I guess I had plans now."

    jump cafe_one

label cafe_one:

    scene bg coffee
    with dissolve

    "The afternoon before the workshop, I decided to stop by a nearby cafe."

    menu:
        "I'd like a matcha latte with oat milk.":
            $ drink_order = "matcha"
            $ drink_name = "matcha latte"

        "I'd like a black coffee, extra strong.":
            $ drink_order = "black coffee"
            $ drink_name = "black coffee"

        "I'd like a strawberry cream frappe topped with whipped cream.":
            $ drink_order = "frappe"
            $ drink_name = "strawberry cream frappe"

        "I'd like a chocolate mocha with extra drizzle.":
            $ drink_order = "chocolate mocha"
            $ drink_name = "chocolate mocha"

    "Once I found an empty table, pulled out my phone while I waited. The café was peaceful. A few students worked on laptops, someone sat by the window reading a book, and quiet conversations drifted through the room."

    "When my order was ready, I thanked the barista, cleaned up my table, and headed home, hoping tomorrow wouldn't be awkward."

    stop music fadeout 1.0

    jump workshop_one


label workshop_one:

    play music "audio/Brushes_and_Blues.mp3" fadein 2.0 volume 0.35
    show screen brushes_and_blues_loop

    scene bg art with dissolve

    "Saturday came faster than I expected."

    "The community art studio was brighter than I'd imagined. Framed paintings and sketches covered the walls, shelves overflowed with supplies, and the room smelled faintly of paper, graphite, and acrylic paint."

    "Around a dozen people had already arrived, chatting quietly while setting up their sketchbooks."

    "The instructor smiled as everyone settled in."

    i "Welcome, everyone! For the next six weeks, we'll be exploring different prompts each class."

    i "The goal isn't perfection, it's to experiment, improve, and hopefully learn something new about your own creativity. Today's class is nice and easy, so let's start by finding a partner."

    "I looked around the room. Almost every seat was taken. Except one."

    "A guy around my age was quietly organizing his pencils. The chair beside him was empty."

    show luka_sit down
    with dissolve

    mc "Is this seat taken?"

    show luka_sit at hop

    "He looked up and smiled."

    show luka_sit talk at hop

    u "Nope."
    
    "I sat down as he chuckled."

    u "Looks like you're stuck with me."

    show luka_sit normal at hop

    mc "I guess I am."

    "While everyone settled in, we introduced ourselves. We exchanged names, talked about how long we'd been drawing, what kinds of things we liked to draw, and why we'd signed up for the workshop. "

    ml "So... how good would you say you are?"

    menu:
        "I'm pretty good.":
            jump skill_confident

        "I'm still learning. haha":
            jump skill_learning

        "Honestly... I'm kind of terrible.":
            jump skill_bad

    label skill_confident:

    show luka_sit happy at hop

    "He laughed."

    show luka_sit talk at hop

    ml "Confident. I like it."

    show luka_sit normal at hop

    "Before I could respond, the instructor clapped to get everyone's attention."

    i "All right, everyone! Our first exercise is simple. I'd like you to draw the person sitting across from you."

    "The room immediately filled with laughter."

    u "I can't draw faces!"

    u "I've already accepted that mine's going to look cursed."

    "The guy beside me grinned as we turned our chairs toward each other."

    show luka_sit talk at hop

    ml "Try not to make me look too ugly."

    show luka_sit normal at hop

    mc "No promises."

    show luka_sit down at hop
    
    "For the next half hour, the room fell quiet except for pencils scratching across paper. Every few minutes Id glance up to study his face before returning to my sketchbook."
    
    "Eventually the instructor called time."
    
    "I turned my sketchbook around."
    
    "His eyes widened ever so slightly."

    show luka_sit shock at hop
    
    ml "...Wow."
    
    "He looked between me and the drawing."

    show luka_sit talk at hop
    
    ml "You're... actually really skilled."

    show luka_sit normal at hop
    
    mc "Thanks."

    show luka_sit down at hop
    
    "As everyone started packing up, I stared down at the portrait."

    menu:
        "I don't know what do do with this.":
            $ luka_interest += 1
            jump keep_drawing

        "I could give it to him.":
            $ luka_interest += 2
            jump offer_drawing

        "I should throw it away.":
            $ luka_interest -= 1
            jump throw_drawing


label skill_learning:

    show luka_sit happy at hop

    "He laughed."

    show luka_sit talk at hop

    ml "Thats okay, we all are."

    "Before I could respond, the instructor clapped to get everyone's attention."

    show luka_sit normal at hop

    i "All right, everyone! Our first exercise is simple. I'd like you to draw the person sitting across from you."

    "The room immediately filled with laughter."

    u "I can't draw faces!"

    u "I've already accepted that mine's going to look cursed."

    "The guy beside me grinned as we turned our chairs toward each other."

    show luka_sit talk at hop

    ml "Try not to make me look too ugly."

    show luka_sit normal at hop

    mc "No promises."

    show luka_sit down at hop
    
    "For the next half hour, the room fell quiet except for pencils scratching across paper. Every few minutes Id glance up to study his face before returning to my sketchbook."
    
    "Eventually the instructor called time."
    
    "I turned my sketchbook around."

    "He looked at the drawing quietly for a moment."

    "I immediately started feeling nervous."

    mc "I know it's not perfect."

    show luka_sit talk at hop

    ml "I didn't say anything."

    show luka_sit normal at hop

    mc "Your face is a little harder to draw than I expected."

    "He smiled."

    show luka_sit happy at hop

    ml "I'll take that as a compliment."

    "I laughed."

    "The drawing wasn't amazing, but it wasn't bad either. It looked like him. It just had a few rough edges."

    show luka_sit talk at hop

    ml "Honestly?"

    show luka_sit normal at hop

    mc "What?"

    show luka_sit talk at hop

    ml "I like it."

    show luka_sit normal at hop

    "I blinked."

    mc "Really?"

    "He nodded."

    show luka_sit talk at hop

    ml "Yeah. It feels like you actually drew me instead of just copying my face. You know what I mean?"

    show luka_sit normal at hop

    "I looked back at the page."

    "I wasn't sure if that was true, but hearing him say it made me feel a little better."

    show luka_sit down at hop

    "As everyone started packing up, I stared down at the portrait."

    menu:
        "I don't know what do do with this.":
            $ luka_interest += 1
            jump keep_drawing

        "I should offer give it to him.":
            $ luka_interest += 2
            jump offer_drawing

        "I'll just throw it away.":
            $ luka_interest -= 1
            jump throw_drawing


label skill_bad:

    show luka_sit happy at hop

    "He laughed."

    show luka_sit talk at hop

    ml "No no, im sure youre better than you give yourself credit for."

    show luka_sit normal at hop

    "Before I could respond, the instructor clapped to get everyone's attention."

    i "All right, everyone! Our first exercise is simple. I'd like you to draw the person sitting across from you."

    "The room immediately filled with laughter."

    u "I can't draw faces!"

    u "I've already accepted that mine's going to look cursed."

    "The guy beside me grinned as we faced toward each other."

    show luka_sit talk at hop

    ml "Try not to make me look too ugly."

    show luka_sit normal at hop

    mc "No promises."

    show luka_sit down at hop
    
    "For the next half hour, the room fell quiet except for pencils scratching across paper. Every few minutes Id glance up to study his face before returning to my sketchbook."
    
    "Eventually the instructor called time."
    
    "I turned my sketchbook around."

    "The moment he looked at it, I already knew."

    "I covered part of my face with my hand."

    mc "Okay, don't laugh."

    "He stared at the drawing."

    "Then..."

    show luka_sit awkward at hop

    "He smiled."

    mc "You're laughing."

    show luka_sit talk at hop

    ml "I'm not."

    show luka_sit normal at hop

    mc "You totally are."

    show luka_sit happy at hop

    "He shook his head as his smile got even bigger"

    show luka_sit shock at hop

    ml "No, I'm serious."

    "He pointed at the portrait."

    show luka_sit talk at hop

    ml "I think it's kind of adorable."

    show luka_sit normal at hop

    mc "Adorable?"

    show luka_sit talk at hop

    ml "Yeah."

    "I looked back at the drawing."

    "I wasn't sure if adorable was the word I would use."

    "The proportions were a little strange. The eyes weren't exactly even. And somehow I'd made his jaw look way sharper than it actually was."

    show luka_sit talk at hop

    ml "You gave me a very heroic chin."

    "I couldn't help laughing."

    show luka_sit normal at hop

    mc "I did not!"

    show luka_sit talk at hop

    ml "You absolutely did."

    show luka_sit down at hop

    "For some reason, his reaction made me feel less embarrassed."

    "He didn't seem disappointed or like he was judging me."

    "He just seemed happy that I had drawn him."

    show luka_sit talk at hop

    ml "If you ever want help, I could show you some things."

    show luka_sit normal at hop

    mc "You're offering me art lessons?"

    "He shrugged."

    show luka_sit awkward at hop

    ml "Maybe."

    "A small smile appeared on his face."

    ml "I just like drawing."

    show luka_sit happy at hop

    ml "And I wouldn't mind spending more time with you."

    show luka_sit down at hop

    "I looked away, pretending not to notice what he said."

    "As everyone started packing up, I stared down at the portrait."

    menu:
        "I don't know what do do with this.":
            $ luka_interest += 1
            jump keep_drawing

        "I offer give it to him.":
            $ luka_interest += 2
            jump offer_drawing

        "I should throw it away.":
            $ luka_interest -= 1
            jump throw_drawing

label keep_drawing:

    "I shouldnt throw it away"

    "I was so caught up in my own thoughts that I barely noticed him saying something."

    show luka_sit awkward at hop

    ml "...Um..."

    "I looked up."

    " He was rubbing the back of his neck, avoiding eye contact."

    ml "If..."

    "He hesitated."

    ml "If you're not planning on keeping it..."

    ml "Would you mind if I did?"

    "I smiled and laughed to myself."

    show luka_sit normal at hop

    mc "Yeah. Sure."

    # His face lit up.

    show luka_sit happy at hop

    ml "Really? Thank you."

    show luka_sit down at hop

    "He accepted the drawing carefully, sliding it into a protective folder before packing the rest of his things." 

    "We packed up the rest of our things, chatting here and there as the classroom slowly emptied."

    hide screen brushes_and_blues_loop
    stop music fadeout 2.0
    scene bg town with dissolve
    show luka
    with dissolve
    play music "audio/jazz2.mp3" fadein 1.0

    "Before long, it was just the two of us walking out of the studio together."

    "The evening air was cool, and the streets were still busy with people heading home."

    "There was a comfortable silence between us."

    jump goodbyes


label offer_drawing:

    "I looked down at the portrait one more time."

    "It was strange seeing it outside of my sketchbook."

    "Usually when I finished a drawing, I kept it for myself or posted it online."

    "But this was different."

    "I glanced over at him."

    "He was carefully packing away his supplies, placing each pencil back into its case."

    "Before I could overthink it, I spoke."

    mc "Hey."

    show luka_sit normal at hop

    "He looked up."

    mc "Do you want to keep it?"

    show luka_sit shock at hop

    "For a second, he just stared at me."

    show luka_sit talk at hop

    ml "Wait... really?"

    "I smiled."

    show luka_sit normal at hop

    mc "Yeah. I mean, if you want it."

    # His expression brightened.

    show luka_sit talk at hop

    ml "I do."

    "He accepted the drawing carefully, almost like he was afraid of accidentally damaging it."

    "Instead of folding it or putting it loosely in his bag, he pulled out a protective folder and slid it inside."

    "I raised an eyebrow."

    show luka_sit down at hop

    mc "You have a folder just for drawings?"

    "He laughed quietly."

    show luka_sit talk at hop

    ml "You never know when something important might come along."

    "I smiled."

    show luka_sit normal at hop

    mc "I guess that's one way to look at it."

    "We packed up the rest of our things, chatting here and there as the classroom slowly emptied."

    scene bg town 
    with dissolve
    show luka
    with dissolve
    hide screen brushes_and_blues_loop
    stop music fadeout 2.0
    play music "audio/jazz2.mp3" fadein 1.0

    "Before long, it was just the two of us walking out of the studio together."

    "The evening air was cool, and the streets were still busy with people heading home."

    "There was a comfortable silence between us."

    jump goodbyes

label throw_drawing:

    "I looked down at the portrait sitting in my sketchbook."

    "Actually, I was kind of proud of it."

    "But still..."

    "It was just a drawing from the first day of class."

    "I couldn't imagine keeping every single thing I made."

    "Besides, my desk at home was already full of unfinished sketches and old ideas."

    "The instructor announced that class was ending, and everyone slowly started gathering their things."

    "I packed up my pencils and sketchbook, glancing around the room as people said their goodbyes."

    "The guy beside me was still organizing his supplies, carefully putting his pencils away one by one."

    "Maybe someone else would appreciate it more than I would."

    hide luka
    scene bg town 
    with dissolve
    hide screen brushes_and_blues_loop
    stop music fadeout 2.0
    play music "audio/jazz2.mp3" fadein 1.0

    "I walked out of the studio with the rest of the class."

    "On my twords the exit I noticed a trash can near the entrance and dropped the drawing inside without a second thought"

    " But then it felt a little weird throwing away something I had spent time making."

    mc "Nah, its not that big of a deal"

    mc "After all, it was just a sketch."

    #change scene

    "I started walking home but not very soon into my walk I heard hurried footsteps behind me."

    ml "[player_name]... wait up!"

    show luka talk arm
    with dissolve

    "I turned around to see Luka jogging toward me, slightly out of breath."

    show luka awkward at hop

    ml "Sorry... I didn't realize you left."

    show luka talk at hop

    ml "I was hoping I could catch you."

    show luka at hop

    mc "Oh? What's up?"

    show luka talk at hop

    ml "I was wondering..."

    ml "Would you want to walk around for a bit?"

    ml "I don't really feel like going home yet."

    menu:
        "Sure.":
            $ luka_interest += 2
            $ went_on_date = True
            jump hangout_one

        "I'm pretty tired...":
            $ luka_interest -= 1
            show luka awkward at hop

            ml "Oh."

            ml "Okay."

            ml "Maybe another time, then."

            show luka at hop

            "He gives you a small smile."

            "Before you can turn to leave..."

            show luka talk arm at hop

            ml "Actually..."

            ml "One more thing."

            ml "Do you have Afterlight?"

            show luka at hop

            mc "Yeah, I do."

            show luka talk at hop

            ml "Would it be okay if I added you?"

            show luka at hop

            mc "Sure."

            "You pull out your phone."

            "The two of you exchange usernames."

            show luka talk at hop

            ml "Thanks."

            ml "I'll try not to spam your notifications."

            show luka at hop

            mc "Haha. I'd appreciate that."

            show luka talk at hop

            ml "See you around."

            jump maybe_another_time

label goodbyes:

    "I slung my bag over my shoulder."

    "We stepped outside."

    "The evening air was cool, and the sidewalks were still busy with people heading home."

    $ time = 0.5
    $ timer_jump = "luka_interrupt"

    show screen countdown

    menu:

        "See ya!":
            hide screen countdown
            jump player_says_goodbye

        "Goodbye.":
            hide screen countdown
            jump player_says_goodbye


###########################################################
# PLAYER WAS TOO SLOW
###########################################################

label luka_interrupt:

    hide screen countdown

    show luka talk at hop

    ml "Hey..."

    "I looked over."

    show luka awkward at hop

    "He shifted his weight for a moment before smiling."

    ml "I was wondering..."

    ml "Would you want to walk around for a bit?"

    ml "I don't really feel like going home yet."
   
    menu:
        "Sure!":
            $ luka_interest += 1
            $ went_on_date = True
            jump hangout_one

        "I'm pretty tired...":
            $ luka_interest -= 1
            show luka awkward at hop

            ml "Oh."

            ml "Okay."

            ml "Maybe another time, then."

            show luka at hop

            "He gives you a small smile."

            "Before you can turn to leave..."

            show luka talk arm at hop

            ml "Actually..."

            ml "One more thing."

            ml "Do you have Afterlight?"

            show luka at hop

            mc "Yeah, I do."

            show luka talk at hop

            ml "Would it be okay if I added you?"

            show luka at hop

            mc "Sure."

            "You pull out your phone."

            "The two of you exchange usernames."

            show luka talk at hop

            ml "Thanks."

            ml "I'll try not to spam your notifications."

            show luka at hop

            mc "Haha. I'd appreciate that."

            show luka talk at hop

            ml "See you around."

            hide luka at hop

            jump maybe_another_time



###########################################################
# PLAYER CLICKED FAST ENOUGH
###########################################################

label player_says_goodbye:

    show luka shock arm at hop
    with vpunch

    ml "Wait!"

    "I froze for a moment."

    show luka talk arm at hop

    ml "Sorry."

    show luka awkward at hop

    "He laughed awkwardly."

    show luka talk at hop

    ml "I was wondering..."

    ml "Would you want to walk around for a bit?"

    ml "I don't really feel like going home yet."

    menu:
        "Sure!":
            $ luka_interest += 1
            $ went_on_date = True
            jump hangout_one

        "I'm pretty tired...":

            pass

    show luka awkward at hop

    ml "..."

    ml "Are you sure?"

    menu:
        "Actually... yeah, let's go.":

            show luka at hop

            ml "Really?"

            ml "I'm glad."

            ml "Let's go."

            $ went_on_date = True
            jump hangout_one

        "Yeah. I'm sure.":

            $ luka_interest -= 2
            ml "Hah.... I totally get it. Maybe another time!"

            show luka_talk

            ml "Oh, before you go..."

            ml "Do you have Afterlight?"

            show luka

            mc "Yeah."

            show luka_awkward

            ml "Mind if I add you?"

            show luka

            mc "Go for it."

            "You exchange usernames."

            show luka_talk

            ml "Thanks."

            ml "See you around."

            "We wave goodbye."

            hide luka

            jump maybe_another_time


######################################################################################################################################
#IN THE STORE LOL
label sketchbook:

    scene bg store back 
    with dissolve
    show luka
    with dissolve

    "I ran my fingers along the rows of sketchbooks."

    "Some had thick watercolor paper. Others had smooth pages perfect for detailed drawings."

    mc "I always get stuck choosing one."

    show luka talk at hop

    ml "Why?"

    show luka at hop

    mc "Because what if I pick the wrong one?"

    show luka talk at hop

    ml "It's just paper."

    show luka at hop

    mc "Just paper?"

    show luka talk at hop

    ml "Yeah."

    "He picked up a sketchbook and held it out."

    ml "The drawings are what make it important."

    ml "Or who ever drew on the paper"

    show luka at hop

    "I looked at him."

    "For some reason, that made me feel better."

    mc "You make it sound easy."

    show luka talk at hop

    ml "Maybe it's not easy."

    ml "But do I think you should give yourself more credit."

    "I smiled."

    jump stationery_end 

label pen:

    scene bg store back 
    with dissolve
    show luka
    with dissolve

    "The pen section was probably the most dangerous part of the store."

    "There were way too many colors."

    mc "Why are there fifty different shades of the same color?"

    show luka talk at hop

    ml "Because apparently artists need fifty different shades."

    show luka at hop

    mc "You say that like you're not impressed."

    show luka talk at hop

    ml "I'm a little impressed."

    show luka at hop

    "I picked up a pen and tested it on the sample paper."

    mc "Oh."

    show luka talk at hop

    ml "Good?"

    show luka at hop

    mc "Really good."

    show luka talk at hop

    ml "You have a favorite?"

    show luka at hop

    mc "I don't think so."

    show luka talk at hop

    ml "You should."

    show luka at hop

    mc "Why?"

    show luka talk at hop

    ml "Because every artist need a favorite color, no matter the medium."

    show luka at hop

    "I looked back at the pens."

    "Maybe he had a point."

    jump stationery_end

label stickers:

    scene bg store back 
    with dissolve
    show luka
    with dissolve

    "Unlike the other sections, I immediately got distracted by the stickers."

    "There were tiny animals, flowers, stars, and little decorative pieces."

    mc "Okay..."

    mc "These are so so adorable."

    show luka talk at hop

    ml "I knew you'd like these."

    show luka at hop

    mc "You knew?"

    show luka awkward at hop

    ml "You have a cute phone case... So I figured"

    show luka at hop

    mc "Oh."

    "That actually made sense."

    "I picked up a sheet of stickers and looked through them."

    menu:
        "Surprise him.":
            $ luka_interest += 1
            jump sticker_surprise

        "Leave the area.":
            jump stationery_end

label sticker_surprise:

    "I grabbed one of the stickers and stepped closer."

    ml "Hm?"

    show luka shock at hop

    "Before he could react, I placed it on his cheek."

    ml "..."

    "He froze."

    mc "..."

    show luka awkward at hop

    ml "Did you just plant a sticker on me?"

    show luka talk at hop

    "Then he laughed."

    ml "You're lucky."

    show luka at hop

    mc "Why?"

    show luka talk at hop

    ml "Because I think it actually suits you more than me."

    show luka at hop

    "I noticed him slowly reach his hand twords the sticker bowl."

    "I backed up laughing trying to not get stickerd"

    show luka awkward at hop

    "Suddenly he froze"

    show luka talk at hop

    ml "Hold on."

    ml "Don't you have to pay for these?"

    show luka at hop

    mc "Oh."

    "I checked the sticker sheet."

    "A small sign next to them read: 'Free samples! One per customer.'"

    mc "It's free!"

    "He looked at the sign."

    "Then back at me."

    show luka talk at hop

    ml "So you just attacked me with a free sticker?"

    show luka at hop

    mc "Exactly."

    show luka talk at hop

    ml "I see."

    "He smiled."

    ml "I'll have to get you back eventually."

    jump stationery_end

######################################################################################################################################

label hangout_one:

    scene town with fade
    show luka
    with dissolve

    "We ended up walking side by side down the sidewalk."

    show luka talk at hop

    ml "I've been in kind of a slump lately."

    show luka at hop

    mc "Really?"

    show luka talk at hop

    ml "Yeah."

    ml "I still love drawing."

    ml "But lately it's been hard to make myself start."

    show luka at hop

    mc "Oh my gosh... me too."

    mc "I thought I was the only one."

    show luka talk at hop

    ml "Guess we were both at the workshop for the same reason then."

    show luka at hop

    "I smiled."

    "For some reason, hearing someone else say it made me feel a little less guilty."

    "Before I knew it, we'd wandered into a small shopping street lined with tiny local stores."

    show luka talk at hop

    ml "Want to look around?"

    show luka at hop

    mc "Sure."

    hide luka with dissolve
    
    scene bg store front
    with dissolve
    show luka
    with dissolve

    "The first shop we wandered into was a little stationery store."

    "Every shelf was packed with sketchbooks, pens, markers, stickers, and notebooks."

    mc "This place is dangerous..."

    show luka talk at hop

    ml "For your wallet?"

    show luka at hop

    mc "Exactly."

    "I laughed."

    menu:
        "Look at sketchbooks.":
            jump sketchbook

        "Look at pens and markers.":
            jump pen

        "Look at stickers <3.":
            jump stickers


label stationery_end:

    scene bg store front
    with dissolve

    "As we made our way toward the register, Luka quietly picked up a pen."

    show luka talk with fade

    ml "Here."

    show luka at hop

    mc "Hm?"

    show luka talk at hop

    ml "You should try this one. I used it for years, highly reccomend."

    show luka at hop

    "I blinked."

    "It was..."

    mc "...Wait."

    mc "This is the exact pen I've been looking for."

    mc "I lost mine a few weeks ago."

    mc "How did you know?"

    show luka awkward at hop

    ml "..."

    show luka talk at hop

    ml "Lucky guess."

    show luka at hop

    "He grinned."

    "It made me naturally smile too."

    "I reached into my bag for my wallet."

    mc "Thanks for finding it Luka, let me just grab my card-"

    "*beep*"

    "Before I could even pull my card out, Luka had already tapped his."

    mc "Luka!"

    show luka talk at hop

    ml "Too late."

    show luka at hop

    mc "You didn't have to do that."

    show luka talk at hop

    ml "I wanted to."

    show luka at hop

    mc "Now I owe you."

    show luka talk at hop

    ml "Then you'll have to hang out with me again sometime."

    show luka at hop

    "I couldn't help but laugh."

    mc "Was that your plan all along?"

    show luka talk at hop

    ml "Hmm, I wonder."

    show luka at hop

    scene bg town
    with fade
    show luka with dissolve

    "We left the store, each carrying a small paper bag."

    "The afternoon passed surprisingly quickly."

    "We wandered into a bookstore."

    "We stopped at the coffee shop."

    scene bg coffee with dissolve
    show luka with dissolve

    menu:
        "Buy something sweet.":
            mc "I just can't resist."

            show luka talk at hop

            ml "Good choice."

            hide luka

        "Just browse.":
            mc "Everything smells amazing."

            show luka talk at hop

            ml "Next time."

            hide luka

    scene bg town 
    with dissolve

    "By the time the sun started to set, we found ourselves standing at the end of the shopping street."

    show luka awkward
    with dissolve

    ml "..."

    show luka talk at hop

    ml "Hey."

    show luka at hop

    mc "Yeah?"

    show luka talk at hop

    ml "Do you have Afterlight?"

    show luka at hop

    mc "I do!"

    show luka talk at hop

    ml "Do you mind if I add you?"

    menu:
        "Of course!":
            pass

        "Sure.":
            pass

    mc "It's..."

    mc "\"@[player_name].jpeg\""

    show luka talk at hop

    ml "Got it."

    show luka at hop

    "A second later, my phone buzzed."

    "\"@LuvLuka started following you.\""

    mc "That was fast."

    show luka awkward at hop

    ml "If I waited until I got home I might forget!"

    show luka at hop

    "I laughed."

    "Somehow... Today had been a lot more fun than I'd expected. I'm so glad I signed up for that class."

    hide luka

    jump maybe_another_time

label maybe_another_time:

    scene bg bedroom with fade

    "I finally made it home."

    "After kicking off my shoes, I flopped onto my bed with a sigh."

    mc "This day felt so long..."

    scene bg bedroom phone with dissolve

    "*Bzzzt.*"

    "Your phone buzzes."

    "Message from LuvLuka"

    if went_on_date:

        ml "{i}I had a really nice time today. :) {/i}"

        ml "{i}Thanks for walking around with me.{/i}"

        ml "{i}Sleep well, okay?{/i}"

    else:

        ml "{i}I'm glad you made it home safely.{/i}"

        ml "{i}Get some rest, okay?{/i}"

        ml "{i}Maybe we can hang out another time. :) {/i}"

    "A small smile finds its way onto your face."

    scene black with fade

    stop music fadeout 1.0

    jump festival_day






