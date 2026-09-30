
label festival_day:

    scene bg bedroom with fade

    play music "audio/jazz2.mp3" fadein 1.0

    "The morning sunlight peeks through the gap in my curtains."

    "A soft beam of light lands right across my face."

    mc "Mmm..."

    scene black with dissolve
    $ renpy.music.set_volume(0.25, delay=0.2)

    "I groan quietly and pull the blanket over my head."

    "..."

    scene bg bedroom with dissolve
    $ renpy.music.set_volume(1.0, delay=0.2)

    "A few more minutes pass before I finally give in."

    "I sit up with a sleepy stretch."

    mc "..."

    mc "I should probably get moving."

    "Just before hopping out of bed, my phone lights up."

    "I glance at the time."

    mc "Ive got a little while before class starts..."

    mc "Maybe I'll stop by the café."

    scene bg coffee
    with fade

    "The familiar scent of freshly brewed coffee greets me the moment I step inside."   

    "The café is a little busier than yesterday, filled with the quiet chatter of students and the gentle clatter of mugs."

    "I make my way toward the register."

    b "Morning!"

    mc "Morning."

    mc "Could I get a—"

    b "Oh!"

    b "Youre actually all set."

    mc "...Huh?"

    b "Someone already paid for your drink."

    mc "Someone...?"

    "The barista smiles and points toward the pickup counter."

    b "It's waiting for you over there."

    "I make my way over to the pickup counter."

    "Sitting there is a [drink_name]."

    "...My usual."

    "I pick it up, still a little confused."

    mc "Who...?"

    "I glance around the café."

    "That's when I spot him."

    show luka_sit with dissolve

    "He gives me a small wave from a nearby table."

    show luka_sit talk at hop

    ml "Morning."

    show luka_sit at hop

    "I can't help but smile as I walk over."

    mc "You bought this for me?"

    show luka_sit happy at hop

    ml "I did."

    show luka_sit at hop

    mc "You really didn't have to."

    show luka_sit talk at hop

    ml "I know."

    ml "I just wanted to."

    show luka_sit at hop

    "I look down at the cup in my hands."

    mc "This is literally what I always order."

    "I look down at the cup."

    "A [drink_name]."

    show luka_sit awkward at hop
    ml "I asked the barista to give me your usual."

    show luka_sit talk at hop

    ml "Besides..."

    ml "It's not exactly the most complicated order."

    show luka_sit at hop

    "I laugh, taking a small sip."

    "..."

    "Still just as good as yesterday."

    "I take another sip."

    "There's something different about it today."

    "My tiredness seems to melt away almost instantly. The heaviness in my arms disappears, and suddenly I feel... awake."

    "I sit up a little straighter."

    mc "Whoa."

    show luka_sit talk at hop

    ml "What?"

    show luka_sit at hop

    mc "Did you ask for something extra in this?"

    show luka_sit talk at hop

    ml "Something extra?"

    show luka_sit at hop

    mc "I don't know. I just feel... really awake all of a sudden."

    "I take another sip, almost without thinking."

    mc "Like I could run a mile right now."

    show luka_sit at hop

    show luka_sit talk at hop

    ml "Maybe you just needed some caffeine."

    show luka_sit at hop

    mc "There's no way there's that much caffeine in here."

    show luka_sit talk at hop

    ml "I ordered it for you. Of course it's going to be good."

    show luka_sit at hop

    "I narrow my eyes at him."

    mc "That's not an answer."
    

    show luka_sit talk at hop   

    ml "You like it, don't you?"

    show luka_sit at hop

    "I glance down at the cup."

    "I do."

    mc "Yeah..."

    "I take another sip."

    "It's probably just the caffeine."

    show luka_sit shock at hop

    ml "Did you sleep okay?"

    show luka_sit at hop

    menu:
        "Yeah, I actually slept pretty well.":

            mc "Yeah."

            mc "Better than I expected, honestly."

            show luka_sit happy at hop

            ml "I'm glad."

            show luka_sit talk

            ml "You looked pretty tired yesterday."

        "I was exhausted.":
            mc "Barely."

            mc "I don't think I even remembered lying down."

            show luka_sit shock at hop

            ml "Sounds like you needed the rest."

        "I don't really want to think about sleeping right now.":
            mc "I'd rather focus on waking up first."

            show luka_sit awkward at hop

            ml "Fair enough."

            ml "Cafe first."

            show luka_sit at hop

            mc "Exactly."

    show luka_sit down at hop

    "Luka glances down at his phone."

    show luka_sit talk at hop

    ml "We've still got a little while before class."

    ml "Want to head over together?"

    menu:
        "Sure.":
            hide luka
            with dissolve
            stop music fadeout 1.0
            jump art_studio_day2

        "Yeah, let's go.":
            hide luka
            with dissolve
            stop music fadeout 1.0
            jump art_studio_day2


label art_studio_day2:

    scene bg town with dissolve

    "Luka and I walk the rest of the way to the art studio together."

    "The morning air feels refreshing, and the walk goes by faster than I expect."

    "Before I know it, we arrive."

    scene bg art with dissolve
    play music "audio/Brushes_and_Blues.mp3" fadein 2.0 loop volume 0.35
    show luka
    with dissolve

    "The familiar smell of paint and paper fills the room as we step inside."

    "There are already a few people here, setting up supplies and talking amongst themselves."

    "I look around."

    "It feels a little different from yesterday."

    "More lively."
    
    i "Good morning, everyone!"

    "The room slowly quiets down as everyone turns their attention toward the front."

    i"I hope you're all ready for something a little different today."

    i "Normally, our lessons focus on improving your skills as artists."

    i "Learning techniques, practicing, experimenting with different styles..."

    i "But art is not just about what you create."

    i "It's also about the world around you."

    i "The people who view it."

    i "The people who experience it."

    i "And the connections that are made through it."

    "The instructor gestures toward a stack of papers on the table."

    i "Tonight, our community is hosting a small art festival."

    i "Today, we'll be helping prepare different parts of the event."

    i "Some of you will help with displays."

    i "Some of you will work on decorations."
    i "Others will help create interactive pieces for visitors."

    i "This is a chance to experience what art looks like outside of a classroom."

    i "Because being an artist isn't only about making something beautiful."

    i "It's about sharing that beauty with others."

    "The room fills with quiet chatter as everyone looks around excitedly."

    i "I'll be assigning everyone into groups."

    i "You'll be working together for the rest of the day."

    "The instructor starts reading through the list of names."

    i "..."
    i "[player_name]"

    "My attention immediately snaps back."

    i "Luka."

    "I glance over."

    "Luka looks at me at the same time."

    "For a moment, neither of us says anything."

    "Then his expression brightens."

    show luka talk at hop

    ml "Looks like we're together."

    show luka at hop

    mc "Yeah."

    "I can't help but smile a little."

    i "Along with..."

    i "Caspian and Vivienne."    

    show caspian at right with dissolve
    show vivi at left with dissolve

    "Two other young adults step forward to join our group."

    "The four of us gather together as we wait for our assignment."

    i "Your group's assignment will be helping design one of the festival booths."

    i "You'll need to decide on a theme, plan the decorations, and create something that will draw people in."

    i "Remember, this isn't just about making something pretty."

    i "Think about the feeling you want visitors to experience when they walk by."

    i "The booth should tell a story."

    "The four of us look at each other."

    "A story..."

    "That actually sounds kind of fun."

    show vivi talk at hop

    v "Okay, so..."

    v "What kind of theme are we thinking?"

    show vivi at hop
    show caspian talk at hop

    c "Something like The Color of Memories?"

    c "Like visitors pick a color and explain what memory it represents."

    show caspian at hop
    show vivi talk at hop

    v "That could work!"

    show vivi at hop

    "I look over at Luka."

    mc "What do you think?"

    show luka awkward at hop

    ml "Hmm..."

    "He looks around the room for a moment."

    show luka talk at hop

    ml "Maybe something more cozy."

    ml "Like a little letters to someone theme."

    ml "Visitors make an art piece based on a letter they never sent."

    ml "for example To my younger self, To someone I miss, To someone I want to thank."

    "I can picture it immediately."

    "It actually sounds really cute."

    menu:
        "I love that idea.":
            $ luka_interest += 2
            mc "That actually sounds really nice."

            ml "Really?"

            mc "Yeah."

            mc "It feels welcoming."

            show luka at hop

            ml "I'm glad you think so."

            mc "What do you guys think?"

            show caspian talk at hop

            c"Im down if you guys are down."

            show caspian at hop

            show vivi talk at hop

            v "Im cool with whatever, as long as we make it cute."

            hide screen brushes_and_blues_loop
            stop music fadeout 2.0

            jump festival_night


        "I have an idea":
            $ luka_interest -= 2
            mc "I think I have a better idea."

            show luka awkward at hop

            ml "Oh."

            ml "Yeah, go ahead."

            show luka talk at hop

            ml "Let's see what everyone thinks."

    show luka at hop

    mc "I was thinking maybe something more dreamy."

    mc "Like a booth where people can make there own imaginary worlds"

    mc "Like a place where people can interact with the art instead of just looking at it."

    "The group goes quiet for a moment."

    ml "..."

    show luka talk at hop

    ml "Actually..."

    ml "That might be better."

    show luka at hop

    mc "Wait, really?"

    show luka talk at hop

    ml "Yeah."

    ml "I think your idea fits the festival more."

    show luka at hop

    mc "You just said the Letters to Someone idea was good and cozy."

    show luka talk at hop

    ml "It was."

    ml "But yours feels more like something people would remember."

    show luka at hop

    "I blink."

    mc "Wow."

    mc "That was a really fast change of opinion."

    show luka awkward at hop

    mc "Honestly..."

    mc "Three years ago, I probably would have chosen something exactly like your idea."

    ml "..."

    ml "Yeah."

    ml "I could see that."

    mc "What?"

    show luka talk at hop

    ml "Dont worry about it."

    show luka at hop

    show vivi talk at hop

    v "I actually think this theme is sweet!"

    v "The motifs could be like hanging stars, clouds, or even soft lights."

    show vivi smile at hop

    v "Ahh that sounds totally cute!!"

    show vivi at hop
    show caspian talk at hop

    c "Same."

    c "A booth where people can actually make something sounds fun."

    show caspian at hop

    "We all start discussing ideas together."

    "Paint colors."

    "Decorations."

    "This is so much fun."

    hide vivi with dissolve
    hide luka with dissolve
    hide caspian with dissolve

    hide screen brushes_and_blues_loop
    stop music fadeout 2.0

    jump festival_night

image bg festival = "images/bg/festival.png"
image bg stall = "images/bg/stall.png"

label festival_night:

    play music "audio/Winter_in_Watercolor.mp3" loop fadein 2.0 volume 0.35

    scene bg stall with fade

    "The hours pass by faster than I expect."

    "Between painting, decorating, and helping visitors, the day disappears before I even realize it."

    "By the time the festival officially opens, our booth is finally finished."

    "It isn't perfect."

    "But looking at it..."

    "I can't help but feel proud."

    "It feels like something we made together."

    scene bg festival with dissolve

    show vivi at left with dissolve
    show caspian at right with dissolve
    show luka with dissolve

    "After spending most of the day working, the four of us decide to meet up and actually enjoy the festival."

    show vivi talk at hop

    v "I still can't believe we finished everything."

    show vivi at hop
    show caspian proud at hop

    c "Speak for yourself."

    show luka awkward at hop

    c "I was carrying this entire group."

    show vivi pout at hop

    v "theres no way! You did not!"

    "I laugh."

    "Somehow, after spending the entire day together, talking to them feels so easy."

    show vivi at hop
    show caspian talk at hop
    show luka at hop

    c "So..."

    c "I have to say."

    c "The booth turned out pretty good."

    show caspian flirt at hop

    c "Especially because Giselle had such good ideas."

    "I raise an eyebrow and chuckle"

    show caspian at hop

    mc "Are you trying to flatter me?"

    show luka mad at hop
    show caspian flirt at hop

    c "Maybe."

    c "Is it working?"

    show vivi talk at hop
    
    show luka awkward at hop
    show caspian at hop
    show vivi pout at hop

    v "Cas, You literally flirt at everyone."

    show caspian flirt at hop

    c "Not everyone."

    "He glances at me."

    c "Just the most captivating person at the moment."

    show luka talk at hop

    ml "Caspian."

    show caspian proud at hop
    show luka at hop

    c "What?"

    c "I'm just being friendly."

    show vivi talk at hop

    v "Uh huh."

    v "Sure."

    show vivi at hop

    "She looks between Luka and me."

    show vivi talk at hop

    v "You two are obviously together, right?"

    show vivi at hop
    show luka shock arm at hop

    "I freeze."

    show caspian at hop

    mc "..."

    show luka shock at hop

    ml "What?"

    "Suddenly, Luka looks much less confident than he did a second ago."

    menu:

        "Hook my arm through Luka's.":
            
            $ luka_interest += 2
            $ linked_arms = True
            show luka shock at hop

            "Without thinking too much, I hook my arm through his."

            "Luka freezes."

            show luka blush at hop

            ml "..."

            "His face turns slightly red."

            mc "Actually..."

            mc "I think we're pretty close."

            show caspian oh at hop

            c "Oh?"

            show vivi talk at hop

            v "Aww."

            show vivi at hop
            show luka talk blush at hop

            "Luka tries to say something, but he seems to have completely forgotten how words work."

            show caspian at hop

            ml "I..."

            ml "Yeah."

            ml "We're close."

            show vivi smile at hop

            v "you two are too cute!"

            show vivi at hop

        "Laugh it off.":

            $ luka_interest -= 2
            show luka awkward at hop

            mc "What?"

            show caspian oh at hop

            mc "No, we're just friends."

            show luka talk at hop

            ml "Yeah."

            ml "We just met recently."

        "Say nothing.":

            $ luka_interest -= 1
            show luka awkward 

            "I... I don't know what to say."

            "Luka looks away awkwardly."

            show caspian oh at hop

            c "Interesting reaction."

            show vivi pout at hop

            v "caspian."

            show caspian talk at hop

            c "Whatt? I'm just observing."

            show vivi at hop

    show luka talk at hop

    ml "We should probably start before we run out of time."

    show luka at hop
    show caspian at hop

    "The festival continues on, the four of us brushed off the slight conflict and went and had fun."

    "The festival buzzes with music and conversation."

    "Everywhere I look, there's something new."

    "Handmade jewelry."

    "Paintings."

    "Ceramics."

    "Food stands."

    "I'm so distracted looking around that I nearly bump into Vivi."

    show vivi talk at hop

    v "Whoa!"

    v "Careful."

    show vivi at hop

    show caspian oh at hop

    c "Hey!"

    c "There's a ring toss over there."

    show vivi pout at hop

    v "You just want one of the prizes."    

    show caspian talk at hop

    c "Can you blame me?"

    "caspian grabs Vivi by the wrist before she can protest."

    show caspian proud at hop

    c "Come on."

    show vivi smile at hop

    v "Hey!"

    show vivi:
        ease 0.5 xalign -0.5
    show caspian:
        ease 0.5 xalign -0.5

    "They disappear into the crowd, still arguing."

    "I watch them go."

    mc "..."

    mc "I guess it's just us."

    show luka talk at hop

    "Luka smiles."

    ml "Looks like it."

    show luka at hop

    "He glances farther down the row of booths."

    ml "..."

    show luka talk at hop

    ml "Want to look around for a bit?"

    menu:

        "Go with Luka.":

            hide luka
            with dissolve
            jump festival_walk

image cg_luka_cloth = "cg/luka_cloth.png"
image cg_luka_cloth_blush = "cg/luka_cloth_blush.png"

label festival_walk:

    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")

    scene bg stall with fade

    show luka
    with dissolve

    "The festival slowly fades into the background as we wander toward a quieter corner."

    ml "..."

    show luka shock at hop

    ml "Ow."

    mc "Wait..."

    mc "Did you just hit your head?"

    show luka awkward at hop

    "He rubs the top of his head with a sheepish smile."

    ml "Maybe."

    mc "Luka!"

    mc "You literally walked straight into that sign."

    ml "I wasn't paying attention."

    mc "Clearly."

    "I can't help but laugh."

    "A nearby vendor notices us."

    u "Is everything alright?"

    mc "Yeah, he just bumped his head."

    u "Here."

    u "Take this."

    "The vendor hands me a very cold cloth to get rid of any swelling."

    mc "Thank you so much."

    "We thank them before making our way over to one of the benches."

    "I sit down."

    "Luka quietly sits beside me."

    mc "Come here."

    "He hesitates for a second."

    hide luka
    with dissolve

    "Then, without much thought, he rests his head in my lap."

    "My heart skips a beat."

    mc "Hold still."

    show cg_luka_cloth
    with dissolve
    $ persistent.cg_luka_cloth = True
    show screen cg_unlock_notification("Luka", "A Moment Between Lines")

    "I brush his hair back and gently press the cold pack against his hairline where the bump is."

    "I notice him shiver as I brush my hands through his hair."

    ml "It's really not that bad."

    mc "Uh-huh."

    mc "Says the guy who walked into a sign."

    ml "..."

    ml "Fair."

    "Neither of us says anything for a little while."

    "The sounds of the festival feel distant."

    "It's... peaceful."

    if linked_arms:

        show cg_luka_cloth_blush
        with dissolve
        $ persistent.cg_luka_cloth_blush = True

        "I glance down."

        "He's already looking up at me."

        "Our eyes meet."

        "The corners of his eyes soften."

        "A tiny smile spreads across his face."

        "His cheeks slowly begin to turn pink."

        mc "...What?"

        ml "..."

        ml "Nothing."

        ml "I just..."

        ml "I really like being here with you."

        "Heat rushes to my face."

        mc "Y-You're impossible."

        "Before he can say anything else, I slide the cold pack down."

        "It covers his eyes."

        ml "Hey..."

        "I keep lowering it until it covers his entire face."

        ml "..."

        ml "Can I see again?"

        mc "Not until you stop saying embarrassing things."

        "A muffled laugh escapes from underneath the cold pack."

    else:

        "I glance down."

        "He's already looking up at me."

        mc "...What?"

        ml "Nothing."

        ml "I was just thinking..."

        ml "You're so kind."

        mc "I'm literally just holding a cold pack."

        ml "Exactly."

        ml "Most people would've laughed first."

        mc "...I did laugh first."

        ml "..."

        ml "Nevermind."

        "The two of us laugh quietly."

        "After another minute, I lower the cold pack."

        mc "Feeling better?"

        ml "Much."

        ml "Thanks."


    "The two of us sit there for another moment before eventually standing back up."

    mc "Come on."

    mc "Let's keep looking around."

    ml "Lead the way."

    scene black with fade

    jump vivi_hangout




label vivi_hangout:

    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")

    "Eventually, the four of us met back at the main area of the festival."

    scene bg festival with fade
    show luka  at left
    show vivi at center
    show caspian talk at right

    c "There you guys are. Sorry we dipped"

    show caspian at hop

    mc "Haha, its okay."

    show vivi talk at hop

    v "Where did you two disappear to?"

    show vivi at hop

    mc "It's a long story."

    show luka talk at hop

    ml "She had to take care of me."

    show luka at hop

    mc "Because he hit his head."

    show caspian oh at hop

    c "You hit your head?"

    show luka awkward at hop

    ml "It wasn't that bad."

    show caspian at hop
    show vivi talk at hop

    v "clearly it was bad enough for her to take care of you."

    show vivi at hop

    "Luka laughed."

    show luka talk at hop

    ml "I guess."

    "I shook my head."

    show luka at hop

    mc "I'm going to get a breath of fresh air."

    show vivi smile at hop

    v "Oh, I'll come with you."

    show vivi at hop

    mc "Sure."

    "I glanced back at Luka."

    show luka talk arm at hop

    ml "I'll see you later?"

    show luka at hop

    mc "Yeah."

    show luka talk at hop

    ml "Okay."

    show luka at hop

    "He gave me a small smile."

    "I smiled back before turning toward Vivi."

    show vivi talk at hop

    v "Come on."

    scene bg stall with dissolve
    show vivi with dissolve

    "Vivi gently grabbed my arm and pulled me along."

    "We walked away from the group and deeper into the festival."

    "The farther we got, the louder everything seemed to become."

    "Music from one booth mixed with people shouting from another."

    "Someone nearby was laughing loudly."

    "The smell of food, the bright lights, and the constant movement of people started getting to me."

    "I slowed down."

    show vivi talk at hop

    v "You okay?"

    show vivi at hop

    mc "Yeah."

    show vivi talk at hop

    v "You sure?"

    show vivi at hop

    mc "I don't know."

    "I looked around."

    "There were people everywhere."

    mc "It's just..."

    mc "There's so much going on."

    show vivi talk at hop

    v "Yeah."

    show vivi at hop

    mc "I think it's starting to get a little overwhelming."

    show vivi talk at hop

    v "That's okay."

    "Vivi led me toward a quieter area away from the main crowd."

    
    $ renpy.music.set_volume(0.15, delay=1.0, channel="music")

    scene bg bench with dissolve
    show vivi sit talk with dissolve

    $ persistent.cg_vivi_sit = True
    show screen cg_unlock_notification("Vivi", "Sketched in Pink")

    v "Sit with me for a second."

    show vivi sit at hop

    mc "Okay."

    "We sat down on a bench."

    "The sounds of the festival were still there, but they were much quieter now."

    show vivi sit talk at hop

    v "Take a deep breath."

    show vivi sit at hop

    mc "I'm trying."

    show vivi sit talk at hop

    v "I know."

    "She smiled sweetly."

    v "Actually..."

    v "I know something that might help."

    show vivi sit at hop

    mc "What?"

    show vivi sit talk at hop

    v "It's something I do when I get overwhelmed."

    show vivi sit at hop

    mc "Like what?"

    show vivi sit talk at hop

    v "I basically just slow down my breathing."

    show vivi sit at hop

    mc "That's it?"

    show vivi sit talk at hop

    v "Kind of."

    v "You have to actually focus on it."

    show vivi sit up at hop

    "She took a slow breath. In..."

    show vivi sit out at hop

    "And out..."

    show vivi sit talk at hop

    v "Don't try to force it."

    v "Just pay attention to your heartbeat."

    show vivi sit at hop

    mc "My heartbeat?"

    show vivi sit talk at hop

    v "Yeah."

    v "When you're stressed, it gets faster without you even realizing it."

    show vivi sit up at hop

    v "So instead of fighting it, you just..."

    show vivi sit out at hop

    "She took another slow breath."

    v "Let it settle."

    show vivi sit at hop

    mc "How do I know if I'm doing it right?"

    show vivi sit talk at hop

    v "I'll show you."

    "Vivi turned toward me."

    v "Just follow my breathing."

    v "We'll do it together."

    show vivi sit at hop

    mc "Okay."

    show vivi sit up at hop

    v "Close your eyes if you want."

    "I hesitated before closing my eyes."

    v "Ready?"

    mc "Ready."

    show vivi sit up at hop

    v "Okay."

    v "Just focus on your heartbeat."

    v "Don't rush it."

    v "Just breathe."

    call heartbeat_tut from _call_heartbeat_tut

    if _return:

        show vivi sit talk at hop

        v "There you go."

        "I slowly opened my eyes."

        show vivi sit at hop

        mc "Wait..."

        mc "I actually feel better."

        show vivi sit talk at hop

        v "See?"

        show vivi sit at hop

        mc "That was weird."

        show vivi sit talk at hop

        v "Good weird?"

        show vivi sit at hop

        mc "Yeah."

        "I took another slow breath."

        mc "I think my heart actually slowed down."

        show vivi sit talk at hop

        v "That's the point."

        v "You won't always be able to make stressful things disappear."

        v "But you can give yourself a second to breathe through them."

        show vivi sit at hop

        mc "I'll remember that."

        show vivi sit talk at hop

        v "Good."

        "She smiled."

        v "And if you ever get overwhelmed again, try it."

        show vivi sit at hop

        mc "I will."

    else:

        show vivi sit talk at hop

        v "Hey, it's okay."

        mc "I messed up."

        show vivi sit at hop

        v "I know."

        "She laughed softly."

        v "It's harder than it looks."

        show vivi sit at hop

        mc "Apparently I'm terrible at breathing."

        show vivi sit talk at hop

        v "You're doing great."

        "I laughed."

        v "Do you want to try again?"

        menu:

            "Yeah, let's try again.":

                show vivi sit at hop

                mc "Yeah."

                show vivi sit talk at hop

                v "Okay."

                v "One more time."

                show vivi sit up at hop

                call heartbeat_tut from _call_heartbeat_tut_1

                if _return:

                    show vivi sit talk at hop

                    v "There you go!"

                    show vivi sit at hop

                    mc "Oh!"

                    mc "I actually got it."

                    show vivi sit talk at hop

                    v "See?"

                    v "I told you."

                else:

                    show vivi sit talk at hop

                    v "That's okay."

                    v "You'll get it eventually."

                    show vivi sit at hop

                    mc "I'll keep practicing."

                    show vivi sit talk at hop

                    v "That's all you need."

            "No, I'm okay.":
                mc "Maybe I'll try again later."

                show vivi sit talk at hop

                v "Of course."

                v "Just remember what I showed you."

                show vivi sit at hop

                mc "I will."

    "I sat there for another moment."

    "The festival didn't seem nearly as loud anymore."

    show vivi sit talk at hop

    v "Feeling better?"

    show vivi sit at hop

    mc "Yeah."

    mc "A lot better, actually."

    show vivi sit talk at hop

    v "Good."

    "She smiled and nudged my shoulder."

    v "Now..."

    v "Want to go get something sweet?"

    show vivi sit at hop

    mc "Absolutely."

    show vivi sit talk at hop

    v "Knew you'd say yes."

    scene bg festival with dissolve
    show vivi

    "We got up and headed back toward the festival."

    "This time, the noise didn't feel quite so overwhelming."

    "I just took a slow breath."

    "And kept walking."

    stop music fadeout 2.0

    scene black with fade
    hide vivi

    jump model_drawing

    # jump luka_break_in

    #jump a_little_too_close









