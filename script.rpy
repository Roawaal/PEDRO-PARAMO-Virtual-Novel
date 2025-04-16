# Declare Characters
define j = Character("Juan", color="#ffffff")  # Main protagonist, Juan
define m = Character("Dolores", color="#c8a2c8")  # Juan's mother, Dolores
define u = Character("Stranger", color="#d3d3d3")  # The mysterious man who speaks to Juan
define ghost_woman = Character("Ghost Woman", color="#a3a3a3")  # The spectral figure in Comala
define old_man = Character("Old Man", color="#808080")  # The elderly figure who gives cryptic advice

label start:

    scene bg_dusty_road
    with fade

    play music "wind.ogg"

    window show
    narrator "That was the promise I made to my mother."
    narrator "Right before she died, she held my hand and said—"

    scene bg_bedroom_dark
    show dolores sad at center
    with dissolve

    m "Go to Comala, Juan. Find your father. His name is Pedro Páramo."
    m "Tell him I’ve died. Tell him… he owes me something."

    hide dolores
    scene bg_dusty_road
    with fade

    j "Pedro Páramo… my father."
    j "I’ve come to find you. And to bring her spirit back to where it began."

    menu:
        "What should Juan do?"

        "Continue forward, enter Comala":
            jump enter_comala

        "Remember mother’s last days":
            jump remember_mother

        "Stop and observe the surroundings":
            jump observe_surroundings

label remember_mother:

    scene bg_bedroom_dark
    play music "piano_sad.ogg"

    narrator "Her breath grew faint, as if her soul had already left, and only her voice remained, echoing from some other place."

    show dolores weak at center

    m "Juan, you must promise me."
    m "Go to Comala… find him."
    m "He’s your father… and my curse."

    j "Why didn’t you ever tell me about him?"

    m "Because I didn’t want you to become like him."
    m "He owns the land, he controls desire. But his heart… has long been buried beneath that soil."
    m "But you must see it for yourself. It’s where you’re from."

    hide dolores
    window hide
    pause 1.5

    narrator "That night, she passed away."
    narrator "No tears. No struggle."
    narrator "As if her soul had already returned to Comala."

    window show

    j "Now I’m here. I don’t know if I’ll find my father... or the ghosts he left behind."

    menu:
        "Continue forward, enter Comala":
            jump enter_comala

        "Stop and observe the surroundings":
            jump observe_surroundings

label enter_comala:

    scene bg_comala_entrance
    play music "whispers.ogg"
    with fade

    narrator "I followed the dust path into the heart of Comala."
    narrator "Mother said this was her hometown. But what I saw looked more like a graveyard."

    j "Is there… anyone living here?"

    show man_thin left

    u "You came looking for Pedro Páramo too?"

    j "You… you know him?"

    u "We all know him. Everyone in Comala knows Pedro Páramo."
    u "But he’s not here anymore… or maybe, he never really left."

    menu:
        "Ask about Pedro Páramo’s whereabouts":
            jump ask_pedro

        "Ask who this man is":
            jump ask_stranger

        "Stay cautious, walk away without talking":
            jump ignore_stranger

label ask_pedro:

    j "Do you know where Pedro Páramo is now?"

    u "Hah. That depends—do you mean where he lived, or where he is now?"

    j "What do you mean?"

    u "Pedro Páramo is buried under this town. Just like the rest of us."

    j "The rest of... us?"

    u "You’ll see. Keep walking. The dead here don’t stay quiet for long."

    narrator "The man smiled strangely, then turned and disappeared into an alleyway, his footsteps leaving no trace in the dust."

    j "What kind of place is this…?"

    menu:
        "Continue into the town":
            jump town_center

label ask_stranger:

    j "Wait—who are you?"

    u "Me? Just a shadow left behind. A name that used to matter."

    j "Are you… alive?"

    u "Sometimes I forget. Sometimes I think I am. You’ll learn what that feels like soon."

    narrator "The wind blew through him like he was smoke. I wasn’t sure if I imagined the chill—or if it passed through my soul."

    menu:
        "Follow the man":
            jump town_center

        "Turn away, disturbed":
            jump ignore_stranger

label ignore_stranger:

    narrator "I turned my face away. Something about him felt wrong—empty, yet heavy."

    j "I’ll find Pedro on my own."

    narrator "I walked past the sign and into the first street of Comala. The buildings leaned in like they were listening."

    menu:
        "Keep walking into town":
            jump town_center

label town_center:

    scene bg_town_center
    play music "droning_ghosts.ogg"
    with fade

    narrator "I entered the heart of Comala. It was… silent. No voices, no birds, no wind. Just the sound of my footsteps—and even those sounded borrowed."

    show ghost_woman right

    narrator "A woman stood by a dry fountain, her dress fluttering without wind."

    ghost_woman "You’re Dolores’ boy, aren’t you?"

    j "How do you know my name?"

    ghost_woman "She told us. Before she left this place, her name still echoed here."

    j "Are you… a ghost?"

    ghost_woman "We all are. You will be too, eventually."

    narrator "Suddenly, I wasn’t sure if I had ever truly arrived… or if I had been dead all along."

    menu:
        "Ask her about Pedro Páramo":
            jump ghost_pedro

        "Run away from the fountain":
            jump flee_scene

label ghost_pedro:

    j "Who is Pedro Páramo, really? What did he do to this place?"

    ghost_woman (somberly) "Pedro... Pedro was the lord of Comala. But not just any lord. He ruled us, yes. But he also bound us."

    ghost_woman (eyes distant) "His greed, his thirst for power... it dragged us all into the grave with him. None of us can leave."

    j "But... why are you here? Why not move on?"

    ghost_woman (sighs) "We can't. He won’t let us. We remain because he left us here. And when the dead can't leave, the living can never escape."

    narrator "Her words were like the rustle of forgotten pages—each one written in sorrow, each one unfinished."

    j "Is there anything I can do to... free you? Free all of you?"

    ghost_woman (shakes her head) "No. Only Pedro can break the curse. But where is he now? Even if you find him, what will you do?"

    j "I'll figure something out. I have to."

    narrator "She looked at me for a moment, a strange sadness in her eyes. Then, like a shadow, she faded into the mist of the town."

    menu:
        "Continue exploring Comala":
            jump town_center

        "Ask more about the curse":
            jump ask_curse

    scene bg_town_center with fade

    j "Where am I? What is this place?"

    narrator "The air was thick with an oppressive silence. The buildings of Comala loomed like forgotten memories, and the streets twisted in ways that made no sense."

    "Juan begins his journey through the town, unsure of what awaits him."

    menu:
        "Walk down the main street":
            jump main_street

        "Approach the fountain":
            jump fountain_scene

        "Ask the nearby woman for directions":
            jump ghost_woman_scene

label main_street:
    scene bg_street with dissolve

    j "Maybe someone knows where I can find answers."

    narrator "Juan walked down the narrow street, the cobblestones old and cracked. Every step felt as if he was being watched."

    menu:
        "Enter a nearby house":
            jump house_scene

        "Continue down the street":
            jump continue_street

label fountain_scene:
    scene bg_fountain with fade

    j "This fountain... something feels strange about it."

    narrator "The fountain, despite being old and chipped, seemed oddly... alive. The water flowed steadily, yet the sound was eerily hollow."

    ghost_woman (appears from the mist) "You’ve come, haven’t you? You’ll never leave."

    j "Who are you?"

    ghost_woman "I am just one of many who remain here. None of us can escape. You will soon understand."

    menu:
        "Ask her why they can't leave":
            jump ask_curse

        "Try to run away from her":
            jump flee_scene

label ghost_woman_scene:
    scene bg_town_square with fade

    j "Excuse me, do you know where I can find Pedro Páramo?"

    ghost_woman (softly) "Pedro Páramo? You’re looking for him in this place? There’s no point. He controls all. He keeps us here, and he will keep you here, too."

    j "I need to find him. I have to know the truth."

    ghost_woman "The truth? The truth is that there is no escape from Comala. The truth is that you are already lost."

    menu:
        "Ask her to help you find Pedro Páramo":
            jump help_find_pedro

        "Leave her and keep searching":
            jump continue_search

label help_find_pedro:
    scene bg_distant_road with fade

    ghost_woman "I can’t help you, Juan. You must find him on your own. But know this—if you truly want to find him, you must face the curse that binds us all."

    j "How do I break the curse?"

    ghost_woman "Only Pedro knows the way. But... even he cannot escape the consequences of his actions."

    narrator "Her figure began to fade into the mist, her words lingering in the air as she disappeared from sight."

    menu:
        "Search the town for clues about Pedro Páramo":
            jump search_for_clues

        "Rest at the fountain and reflect":
            jump rest_fountain

label search_for_clues:
    scene bg_road_ending with fade

    j "I have to keep going. There has to be something here that can lead me to him."

    narrator "Juan walked through the endless streets, finding only echoes of the past. Every building seemed familiar yet alien, each turn leading him further into the unknown."

    menu:
        "Visit the old church":
            jump church_scene

        "Explore the abandoned house":
            jump abandoned_house_scene

label church_scene:
    scene bg_church with fade

    j "A church... maybe someone here knows something."

    narrator "The church was empty, save for the faint scent of incense. The pews were abandoned, and the altar was dimly lit by a single candle."

    old_man (appearing from the shadows) "You’re still looking for answers, I see. But Comala is no place for answers."

    j "Who are you? What is this place?"

    old_man "I am just a soul lost like the rest. But you... you have something different. Perhaps it’s your fate to end up like us."

    menu:
        "Ask the old man about Pedro Páramo":
            jump ask_old_man

        "Leave the church and continue searching":
            jump continue_search

label abandoned_house_scene:
    scene bg_abandoned_house with fade

    j "This house... it looks like it hasn’t been touched in years."

    narrator "The air inside was thick with dust, and the walls creaked under the weight of time. Juan felt the presence of something—or someone—watching him."

    menu:
        "Look for clues inside":
            jump search_house

        "Leave the house and go back to the streets":
            jump continue_search

label search_house:
    narrator "Juan sifted through the forgotten belongings, finding only old letters, broken furniture, and dust. But then, a book caught his eye—its pages old and yellowed, with strange markings on the cover."

    j "What is this?"

    narrator "As Juan flipped through the pages, he discovered that it was a journal—a journal that seemed to speak of Pedro Páramo's rise to power, the curse, and the fates of those trapped in Comala."

    menu:
        "Read more of the journal":
            jump journal_entry

        "Take the journal and leave":
            jump take_journal

label journal_entry:
    narrator "The journal spoke of Pedro Páramo’s greed, his hunger for control, and how he made a deal with forces beyond the living to secure his power. The curse, it seemed, was tied to his very soul."

    j "So Pedro is the cause of all this? The reason why no one can escape?"

    narrator "The journal ended abruptly, with no clear solution, just the chilling notion that the town itself was alive with the curse."

    menu:
        "Leave the house and continue searching":
            jump continue_search

        "Search for Pedro Páramo in the town":
            jump find_pedro

label take_journal:
    narrator "Juan tucked the journal into his coat, a sense of dread washing over him. He now knew more, but he wasn’t sure if it was a blessing or a curse."

    menu:
        "Leave the house and continue searching":
            jump continue_search

        "Search for Pedro Páramo":
            jump find_pedro
label find_pedro:
    scene bg_town_road with fade

    j "I have to find Pedro. If anyone can end this nightmare, it’s him."

    narrator "Juan followed the winding roads of Comala, but with each step, it felt as if the town was changing, warping around him. The air grew heavier, thicker, as though the very walls of the town were closing in."

    menu:
        "Ask the old man for more information":
            jump ask_old_man_more

        "Search for Pedro in the church":
            jump church_search

        "Look for him in the mansion outside of town":
            jump mansion_search

label ask_old_man_more:
    scene bg_church with fade

    j "You... you said there was something different about me. What do you mean?"

    old_man "Ah, so you feel it too? The weight. The curse. You aren’t just a passerby, Juan. You're like us—lost, waiting for the inevitable."

    j "But I need to find Pedro. I have to know the truth."

    old_man "The truth? Pedro is nothing but a shadow now. His deal with the forces beyond this world has sealed all our fates. He controls the very fabric of Comala. He *is* the town. And no one... not even him... can escape."

    narrator "The old man’s voice trembled with an ancient sorrow, as if he knew the horror of which he spoke, but also the futility of trying to escape it."

    menu:
        "Ask how to break the curse":
            jump break_curse

        "Leave the church and go to the mansion":
            jump mansion_search

label break_curse:
    old_man "There’s no breaking the curse, Juan. Not while Pedro lives, not while Comala exists. The only way out is through him. And once you face him, there’s no returning."

    j "But there must be a way. There has to be some hope!"

    narrator "The old man looked at Juan with pity, his eyes filled with the weight of centuries of despair."

    old_man "Hope? Hope is a lie told by those who cannot bear the truth."

    menu:
        "Ask him how to find Pedro":
            jump find_pedro_old_man

        "Leave the church and search on your own":
            jump mansion_search

label find_pedro_old_man:
    old_man "Pedro Páramo is everywhere. You need only listen to the town—he's in the whispers, in the very air you breathe. But be careful, Juan. Some truths are worse than none at all."

    j "I can handle it. I have to know."

    narrator "The old man’s gaze hardened, as if he had warned Juan enough, but the young man was determined to find Pedro, no matter the cost."

    menu:
        "Go to the mansion outside of town":
            jump mansion_search

        "Search the church for clues about Pedro":
            jump church_search

label mansion_search:
    scene bg_mansion with fade

    j "This mansion... It looks like it’s been abandoned for decades, but I know it holds the answers I need."

    narrator "Juan stepped into the dark, crumbling mansion. The air was thick with dust, and the silence pressed in on him. It felt as if the house itself was watching him."

    menu:
        "Search the first floor":
            jump mansion_first_floor

        "Go upstairs to the master bedroom":
            jump mansion_upstairs

label mansion_first_floor:
    narrator "On the first floor, Juan found nothing but rotting furniture and cracked mirrors. Yet, there was something unsettling about the place—an energy that seemed to pulse beneath the surface."

    j "There must be something here... something that tells me more about Pedro."

    menu:
        "Examine the old paintings":
            jump mansion_paintings

        "Look for a hidden door or passage":
            jump hidden_passage

label mansion_upstairs:
    scene bg_master_bedroom with fade

    j "This room... It must have been Pedro’s. The atmosphere is heavy here, as though the walls themselves have witnessed too much."

    narrator "The bedroom was lavishly decorated, but time had ravaged it. The large bed was now a decayed husk, and the windows were shattered, letting in the cold air."

    menu:
        "Search the desk for clues":
            jump desk_clues

        "Examine the mirror on the wall":
            jump mirror_scene

label mansion_paintings:
    narrator "The paintings on the walls were portraits of long-dead figures, some familiar, others strange. They were all staring at Juan, their painted eyes filled with sorrow."

    j "Who are these people? Why do they look so familiar?"

    narrator "As he studied the paintings, Juan began to feel a strange connection to the faces, as if they were a part of him, part of Comala's history. Their expressions seemed to change, their eyes following him wherever he went."

    menu:
        "Look for more clues in the paintings":
            jump more_paintings_clues

        "Leave the mansion and explore the town":
            jump continue_search

label hidden_passage:
    narrator "Juan’s fingers brushed against the wall, and with a faint click, a hidden passageway revealed itself. The passage was narrow and dark, but Juan felt an inexplicable urge to follow it."

    j "I don’t know if I should... but I have to."

    narrator "He stepped inside, the air thick with the scent of mildew and rot. The passage was long, and at the end of it, he saw a faint light."

    menu:
        "Walk down the passage":
            jump walk_passage

        "Turn back and leave the mansion":
            jump continue_search

label walk_passage:
    narrator "The passage led to an underground chamber. In the center of the room stood a large, stone altar, and beneath it, the faint glow of candles illuminated an inscription."

    j "What is this? This is... this must be where Pedro’s dark dealings took place."

    menu:
        "Examine the altar":
            jump altar_examine

        "Leave the chamber and return to the mansion":
            jump mansion_search

label desk_clues:
    narrator "The desk was cluttered with old papers, some faded, some torn. Among them, Juan found a letter addressed to Pedro Páramo. The contents were cryptic, speaking of a deal made and the consequences it would have on the living."

    j "So, it’s true... Pedro made a deal, and now we’re all paying the price."

    menu:
        "Take the letter and leave":
            jump take_letter

        "Search the desk further":
            jump search_more_desk

label mirror_scene:
    narrator "The mirror was cracked, but through the shards, Juan could see a reflection—a distorted, eerie version of himself. It was as if the mirror was showing not his face, but the version of him trapped in the curse of Comala."

    j "What is this... Is this what I’ve become?"

    narrator "The reflection seemed to mock him, showing him the weight of the curse that had already started to claim his soul."

    menu:
        "Smash the mirror":
            jump smash_mirror

        "Leave the room":
            jump mansion_search

label altar_examine:
    narrator "Juan approached the altar with caution. The stone was cold and rough beneath his fingertips. The inscription, barely legible, seemed to pulse with an ancient energy."

    j "What does this say? 'He who sacrifices his soul... binds the town to the land of the dead.'"

    narrator "The words echoed in his mind, sending a chill down his spine. It was clear now: Pedro Páramo’s deal had trapped not just the people of Comala, but the very land itself."

    menu:
        "Search the altar for more clues":
            jump altar_more_clues

        "Leave the underground chamber":
            jump mansion_search

label altar_more_clues:
    narrator "Juan’s fingers traced the surface of the altar, and hidden beneath a layer of dust, he found a small metal key. The key had an odd symbol engraved on it—a crescent moon intertwined with a spiral."

    j "This... this must be important. Maybe it opens something."

    menu:
        "Take the key and return to the mansion":
            jump take_key_return_mansion

        "Examine the key more closely":
            jump examine_key

label take_key_return_mansion:
    narrator "Juan pocketed the key, the weight of it heavy in his hand. The passage seemed to stretch longer, darker, as if the mansion itself was pulling him deeper."

    menu:
        "Search for a locked door to use the key":
            jump search_locked_door

        "Leave the mansion and explore the town":
            jump continue_search

label examine_key:
    narrator "Upon closer inspection, the key seemed ancient—far older than any lock Juan had seen. The crescent moon symbol matched the one in the altar inscription, suggesting it might open something significant, something tied to Pedro’s curse."

    j "This key... it’s more than just a simple tool. It’s part of the puzzle. I need to find what it unlocks."

    menu:
        "Search for a locked door in the mansion":
            jump search_locked_door

        "Return to the town and seek answers":
            jump continue_search

label search_locked_door:
    narrator "Juan wandered through the mansion, checking every room for a locked door. His search led him to a small study at the back of the house, where a large, dusty bookshelf blocked what seemed to be a hidden door."

    j "Could this be it? The key must open this."

    narrator "The bookshelf creaked as Juan pulled it aside, revealing a hidden room. Inside, the air was thick, and the walls were adorned with old maps and strange symbols."

    menu:
        "Enter the hidden room":
            jump enter_hidden_room

        "Return to the mansion entrance":
            jump mansion_search

label enter_hidden_room:
    narrator "As Juan stepped inside, the room seemed to come alive with a strange energy. In the center was an altar similar to the one in the underground chamber. Above it, a portrait of Pedro Páramo loomed, his eyes piercing through the darkness."

    j "This... this must be where Pedro made his final deal. The heart of the curse."

    menu:
        "Examine the altar in this room":
            jump altar_in_hidden_room

        "Look for more clues about Pedro’s deal":
            jump search_hidden_room

label altar_in_hidden_room:
    narrator "The altar was adorned with strange offerings—bones, withered flowers, and unmarked candles. The walls were covered in arcane symbols, some of which were eerily familiar from the journal Juan had found earlier."

    j "Pedro... what did you do here?"

    narrator "The atmosphere felt suffocating, as if the room itself was a tomb, holding the memories of those who had fallen victim to Pedro’s ambition."

    menu:
        "Light the candles and perform a ritual":
            jump perform_ritual

        "Leave the hidden room and search the town":
            jump continue_search

label perform_ritual:
    narrator "Juan hesitated, but his curiosity got the better of him. He lit the candles, the flames flickering to life with unnatural speed. As he did, the air grew colder, and the symbols on the walls began to glow faintly."

    j "What is this? What have I done?"

    narrator "The ground trembled beneath his feet, and the portrait of Pedro Páramo seemed to shift, as if the man was alive within it, watching Juan's every move."

    menu:
        "Ask Pedro for answers":
            jump ask_pedro

        "Leave the hidden room before something worse happens":
            jump mansion_search



    narrator "A voice, cold and distant, echoed in the room, emanating from the portrait of Pedro Páramo."

    pedro (voice) "You think you can understand what I’ve done? You think you can break what has been set in motion for centuries?"

    j "I have to know. Why did you do it? Why curse this town?"

    pedro (voice) "I did what I had to. Power is never free, and Comala... it was always destined to be my kingdom. But in the end, we all pay the price."

    narrator "The portrait’s eyes glowed with a sinister light, and Juan felt the weight of Pedro’s words settle heavily in his chest."

    menu:
        "Demand Pedro tell you how to end the curse":
            jump demand_pedro_answer

        "Leave the room and try to escape the town":
            jump flee_town

label demand_pedro_answer:
    pedro (voice) "The curse can only end when the pact is broken. But be warned, Juan: breaking it will cost you everything. Even your soul."

    j "I’ll do whatever it takes. I have to stop this."

    narrator "The portrait of Pedro Páramo began to fade, leaving only the flickering candles and the oppressive silence of the room."

    menu:
        "Follow the ritual’s final step":
            jump final_step_ritual

        "Leave the mansion and search for Pedro directly":
            jump find_pedro

label flee_town:
    narrator "Juan tried to leave, but the streets of Comala twisted around him, pulling him back to the mansion. It was as if the town itself refused to let him escape."

    j "No... I can’t run. I must face it."

    menu:
        "Return to the mansion and finish the ritual":
            jump final_step_ritual

        "Search for any remaining clues":
            jump continue_search
label final_step_ritual:
    narrator "The candles burned brightly, their flames flickering with unnatural intensity. Juan stood at the altar, the weight of Pedro Páramo's words heavy in the air."

    j "The ritual... I have to follow it through."

    narrator "As Juan recited the final words, the symbols on the walls glowed brighter, and the ground trembled beneath his feet. The very fabric of Comala seemed to shudder, as though something ancient was waking."

    menu:
        "Offer your soul to break the curse":
            jump offer_soul

        "Refuse to offer your soul, but continue the ritual":
            jump ritual_rejection

label offer_soul:
    narrator "Juan’s heart raced, the heat of the candles searing his skin. As he recited the final incantation, a cold voice filled the air."

    pedro (voice) "So, you are willing to pay the price, Juan. But know this: once you offer your soul, there is no turning back. You will never return to the world of the living."

    j "I understand. I can’t let Comala remain like this."

    narrator "The ground beneath Juan’s feet cracked open, revealing a deep, swirling abyss. The light from the candles grew blinding, and the town of Comala seemed to disappear, consumed by the dark energy of the curse."

    menu:
        "Dive into the abyss to confront Pedro":
            jump dive_abyss

        "Turn back and try to escape the curse":
            jump try_escape

label dive_abyss:
    narrator "Without hesitation, Juan stepped into the abyss, his body sinking into the darkness. It felt as though time itself had stopped, and he was falling through an endless void. Then, suddenly, everything went silent."

    j "Where am I? What is this place?"

    narrator "In the distance, Juan saw a faint light. As he moved closer, the shape of **Pedro Páramo** materialized, standing in the center of a vast, empty landscape."

    pedro (voice) "You’ve come to face me, Juan? You think offering your soul will end this? You are but another pawn in the game I’ve set in motion."

    j "I won’t let this town continue to suffer. You’re the reason all of this happened!"

    narrator "Pedro smiled, but his eyes were cold, dead. The shadows around him seemed to stretch, as if the town itself was feeding off his power."

    menu:
        "Confront Pedro directly":
            jump confront_pedro

        "Try to break the curse without Pedro’s help":
            jump attempt_to_break_curse

label confront_pedro:
    pedro "You’re foolish, Juan. You think you can defeat me? I am Comala itself, the town is mine to command. Nothing you do will change that."

    narrator "Juan stepped forward, his resolve stronger than ever. He knew the truth now—Pedro’s power came from the very land, the people, and the curse that bound them all together."

    j "I’ll destroy the curse, even if it costs me everything."

    narrator "With those words, a surge of energy erupted from the altar, and the ground beneath them cracked open further. The entire realm began to tremble as Juan’s determination to end the curse clashed against Pedro’s power."

    menu:
        "Use the key to break Pedro’s hold":
            jump use_key_to_break

        "Sacrifice Pedro’s soul to end the curse":
            jump sacrifice_pedro

label use_key_to_break:
    narrator "Juan held the key high, its crescent moon symbol glowing with an eerie light. He knew this was the key to breaking the curse. He thrust it into the air, and a burst of energy exploded from it."

    pedro (voice) "No! That key… that’s the symbol of the bargain. You can’t—"

    narrator "As the energy from the key enveloped Pedro, his form began to dissipate, his connection to the town unraveling. The land around them twisted, as if the curse was finally being broken."

    j "This is for Comala. This is for everyone you’ve trapped here."

    narrator "Pedro screamed, his voice echoing through the void, but the sound faded, swallowed by the dark abyss. The key burned bright in Juan’s hands, its power finally consuming the man who had caused so much suffering."

    menu:
        "Return to Comala and see the aftermath":
            jump aftermath

        "Stay in the abyss and rest forever":
            jump stay_in_abyss

label sacrifice_pedro:
    narrator "Juan knew that to end the curse, he had to destroy Pedro completely. He turned to face the weakened figure of Pedro Páramo, his eyes filled with rage and sorrow."

    j "You don’t deserve to exist any longer."

    narrator "With a final cry, Juan charged forward, thrusting his hand into Pedro’s chest. A burst of energy erupted from the contact, and Pedro’s form twisted, as if the very essence of his being was being torn apart."

    pedro (voice) "No… You can’t do this! I am the town, Juan. I am Comala…!"

    narrator "As Pedro’s screams faded into nothingness, the ground cracked open, swallowing him whole. The curse was lifted, but at a great cost. The town began to crumble, the people trapped within it now free, but at the cost of Juan’s life."

    menu:
        "Return to Comala and witness the town’s freedom":
            jump aftermath

        "Embrace the darkness of the abyss forever":
            jump stay_in_abyss

label ritual_rejection:
    narrator "Juan hesitated, the weight of the decision pressing on him. He could feel the ritual’s power building around him, but something deep inside told him it wasn’t the right choice."

    j "I can’t offer my soul. I’ll find another way. I can’t become like them."

    narrator "The air in the room grew colder, and the symbols on the walls began to fade. The ritual was breaking down, but the curse remained, a dark force lingering in the shadows."

    menu:
        "Search for another way to break the curse":
            jump find_another_way

        "Leave the mansion and face Pedro directly":
            jump find_pedro

label start:
    # The opening scene where Juan arrives in Comala
    scene bg_comala
    with fade

    j "I have arrived in Comala, the town that’s supposed to hold the answers to my questions."
    j "But the air is thick with silence, like something is watching me, waiting for me to make the first move."

    menu:
        "Explore the town center":
            jump explore_town_center

        "Head toward the mansion":
            jump head_toward_mansion

label explore_town_center:
    scene bg_town_center
    with fade

    j "I walk through the empty streets, but it feels like the town is holding its breath. No one around. Not a single soul."

    ghost_woman "You... you're here. The one who will change everything."

    j "Who’s there? Show yourself!"

    ghost_woman "It is not time for you to know us. But you must learn, Juan, or we will never be free."

    menu:
        "Ask her about Pedro Páramo":
            jump ask_about_pedro

        "Ask her how to break the curse":
            jump ask_about_curse

        "Walk away and continue exploring":
            jump continue_exploring

label head_toward_mansion:
    scene bg_mansion_entrance
    with fade

    j "The mansion looms ahead, dark and imposing. It feels like it holds all the answers I’m seeking."

    old_man "You seek the truth, but the truth here is not kind. You should turn back."

    j "Who are you? What do you know about this place?"

    old_man "I am like you, once living, now lost to the curse of Comala. There is no escaping it."

    menu:
        "Ask him how to break the curse":
            jump ask_old_man_about_curse

        "Ignore him and enter the mansion":
            jump enter_mansion

        "Leave the mansion and head back to the town center":
            jump back_to_town_center

label ask_about_pedro:
    ghost_woman "Pedro Páramo... he is the one who controls us all. His voice, his power, it holds us here in this endless loop. You must confront him if you wish to escape."

    j "How can I defeat him? How do I break his control?"

    ghost_woman "To break his hold, you must first understand the pact he made. Only then can you confront him, but be warned: the cost may be your soul."

    menu:
        "Learn more about Pedro’s pact":
            jump learn_about_pact

        "Ask her if there’s another way":
            jump ask_about_alternative

label ask_about_curse:
    ghost_woman "The curse... it binds us all. We are trapped in this town, repeating the same lives, the same stories. No matter what we do, we are caught in Pedro’s web."

    j "So there’s no way to break it?"

    ghost_woman "There is a way. But the price... you may not want to pay it."

    menu:
        "Ask her what the price is":
            jump ask_about_price

        "Ask how to avoid paying the price":
            jump ask_about_avoiding_price

label continue_exploring:
    j "I continue walking through the empty streets, the silence pressing down on me. There is a sense of dread in the air. It feels as though the town itself is waiting for me to uncover its secrets."

    menu:
        "Go to the church":
            jump visit_church

        "Visit the graveyard":
            jump visit_graveyard

label ask_old_man_about_curse:
    old_man "The curse... it was laid by Pedro Páramo long ago. He has control over every soul here, and there is no escape. Not for me, not for anyone."

    j "Is there no hope? No way out?"

    old_man "There is one way... but it’s not what you think. You must either break the curse by offering something precious... or... confront Pedro himself."

    menu:
        "Ask him what the precious thing is":
            jump ask_precious_thing

        "Ask him how to confront Pedro":
            jump confront_pedro

label enter_mansion:
    j "I push open the massive doors of the mansion. Inside, the air is thick with dust, and the darkness seems to swallow me whole."

    narrator "As Juan steps into the mansion, the sound of footsteps echoes through the halls. He is not alone."

    pedro (voice) "So, you've finally come to face me, Juan. Welcome to my domain."

    j "Pedro Páramo... I’ve come to end this curse. To free the souls trapped here."

    pedro (voice) "End the curse? You cannot even comprehend the power that holds this town together. You think you can defeat me?"

    menu:
        "Confront Pedro directly":
            jump confront_pedro

        "Look for a way to escape the mansion":
            jump find_escape

label back_to_town_center:
    j "I turn away from the mansion, my footsteps echoing in the silence. Something about that place... it’s not right. I need to think this through."

    menu:
        "Visit the church":
            jump visit_church

        "Explore the graveyard":
            jump visit_graveyard

label visit_church:
    scene bg_church
    with fade

    j "The church stands in stark contrast to the rest of the town, its towering spire visible from almost anywhere in Comala. But even here, the air is heavy with despair."

    ghost_woman "The church holds many secrets. But beware, Juan. Some things are better left untouched."

    j "What do you mean?"

    ghost_woman "The past is buried here, and so are the souls of those who tried to escape. But none succeeded."

    menu:
        "Enter the church and investigate":
            jump investigate_church

        "Leave the church and go to the graveyard":
            jump visit_graveyard

label visit_graveyard:
    scene bg_graveyard
    with fade

    j "The graveyard is overgrown, the tombstones weathered with age. The wind howls through the trees, and I can’t shake the feeling that I’m being watched."

    old_man "This is where many of us rest. And yet... none of us can truly die. We are bound to this place, even in death."

    j "Is there no peace? No rest for the souls here?"

    old_man "Only through confronting Pedro can peace be achieved. But no one has been able to do that... not yet."

    menu:
        "Search for clues about Pedro’s past":
            jump search_pedro_past

        "Leave the graveyard and head back to the mansion":
            jump head_back_to_mansion


label confront_pedro:
    scene bg_pedro_room
    with fade

    j "Pedro Páramo, I’ve come to put an end to this madness. To free all the souls you've trapped here."

    pedro (voice) "You think you can free them? These souls belong to me, Juan. They are bound to this place as you will soon be. You will never leave Comala."

    j "I refuse to believe that. There must be a way out. A way to free everyone."

    pedro (voice) "You cannot escape what is already written, Juan. This town, this curse... it is your inheritance. And now, you must accept it."

    menu:
        "Confront Pedro about the pact":
            jump confront_pedro_pact

        "Try to break the curse by force":
            jump break_curse_by_force

        "Beg for mercy and ask for a way out":
            jump beg_for_mercy

label confront_pedro_pact:
    j "I know about the pact, Pedro. I’ve heard the whispers. The souls you control, the price you’ve paid... it ends now!"

    pedro (voice) "Ah, so you’ve learned the truth. The pact was made long ago, when your mother died, Juan. She agreed to give me her soul in exchange for your life. You were always meant to be mine."

    j "You... you took my mother’s soul?! That’s why I’ve been drawn here, isn’t it? To pay for her bargain?"

    pedro (voice) "Yes. Her sacrifice was for nothing. And now, you too will be bound to me forever. There is no escaping what is already done."

    menu:
        "Try to find a way to break the pact":
            jump break_the_pact

        "Accept the truth and join Pedro":
            jump accept_pedro

label break_curse_by_force:
    j "I won’t accept this! There must be another way!"

    narrator "In a fit of rage, Juan tries to break the curse by force, but the room itself seems to resist him, as if Comala is pushing back against his will."

    pedro (voice) "You cannot fight what is inevitable, Juan. You are powerless here."

    j "I’ll fight until my last breath!"

    narrator "Juan’s body trembles with the force of his determination, but the curse presses harder. The walls close in on him, and the light fades."

    menu:
        "Keep resisting, hoping for a miracle":
            jump keep_resisting

        "Give up and accept defeat":
            jump accept_defeat

label beg_for_mercy:
    j "Please, Pedro... there must be a way out. I beg you. Let me go. Let everyone go."

    pedro (voice) "Mercy? You think mercy can undo what has been done? You are no different from the others who came before you. Desperate, hopeless... weak."

    j "I’ll do anything. Anything to escape this place, to free the souls trapped here."

    pedro (voice) "Then you must make a choice, Juan. Sacrifice yourself, or sacrifice someone else. That is the only way out of this."

    menu:
        "Sacrifice myself":
            jump sacrifice_myself

        "Sacrifice someone else":
            jump sacrifice_someone_else

label break_the_pact:
    j "There must be a way to break the pact! I won’t let you control me!"

    narrator "Juan’s mind races as he tries to recall the stories he’s heard, the whispers of broken pacts and forbidden rituals. He begins to piece together a ritual that could sever the bond between him and Pedro."

    pedro (voice) "You think you can break what is already done? It’s too late for that."

    j "It’s never too late. I won’t let you win."

    narrator "With newfound determination, Juan starts the ritual, reciting the words that could break the pact. The air crackles with power as the ground trembles beneath him."

    menu:
        "Complete the ritual":
            jump complete_ritual

        "Fail and face Pedro’s wrath":
            jump fail_ritual

label accept_pedro:
    j "If it is my fate, then so be it."

    narrator "Juan falls to his knees, overwhelmed by the weight of Pedro’s words. The town of Comala begins to shift around him as he accepts his fate."

    pedro (voice) "Welcome, Juan. You have become part of the town, part of the curse. Together, we will never leave."

    narrator "The town of Comala becomes his prison, and his name is lost in the wind, like all the other souls trapped here."

    return

label keep_resisting:
    narrator "Despite the overwhelming power of Pedro, Juan continues to fight. His body is exhausted, but his spirit refuses to break. And then, something miraculous happens."

    j "I won’t stop! I can’t let this be the end!"

    narrator "A sudden burst of energy surges through Juan. The curse weakens, the mansion shakes, and the walls crack open. It’s as if the entire town is reacting to his defiance."

    menu:
        "Keep fighting, even if it means death":
            jump die_fighting

        "Let the energy guide me out":
            jump escape_with_energy

label accept_defeat:
    narrator "Juan collapses to the ground, defeated. The walls of the mansion close in around him, and Pedro’s voice fills the air."

    pedro (voice) "You were always too weak to face me, Juan. Now, you will be part of Comala, just like all the others."

    return

label sacrifice_myself:
    j "I will sacrifice myself, for the town, for the souls trapped here."

    narrator "Juan steps forward, offering himself as the final sacrifice. A beam of light envelops him, and the air grows still."

    pedro (voice) "You have chosen wisely, Juan. Now, the curse will be lifted, but at the cost of your soul."

    narrator "The light fades, and the curse is broken. The souls of Comala are freed, but Juan’s body is left behind, a mere echo of the man he once was."

    return

label sacrifice_someone_else:
    j "I can’t sacrifice myself... but maybe there’s someone else."

    narrator "Juan looks around, trying to find someone—anyone—who might be able to bear the burden of sacrifice. But in the end, he knows the curse demands a price."

    menu:
        "Sacrifice the Old Man":
            jump sacrifice_old_man

        "Sacrifice the Ghost Woman":
            jump sacrifice_ghost_woman

label complete_ritual:
    narrator "With every ounce of strength, Juan completes the ritual, and a burst of light engulfs the room. The air shudders as the bond between him and Pedro is broken."

    pedro (voice) "No! This cannot be happening!"

    narrator "The ground trembles, the walls crack, and Pedro’s voice fades into silence. The curse is broken, and Comala begins to crumble."

    menu:
        "Escape the collapsing town":
            jump escape_town

        "Stay behind to witness the collapse":
            jump stay_and_watch

label fail_ritual:
    narrator "The words falter, and the ritual collapses. The ground shakes violently, and Pedro’s power surges back with full force."

    pedro (voice) "Fool! You cannot break me. I will make you regret this."

    menu:
        "Attempt to flee":
            jump attempt_to_flee

        "Face Pedro one last time":
            jump face_pedro_last_time

label escape_with_energy:
    narrator "With the surge of energy guiding him, Juan breaks through the walls of the mansion, feeling the oppressive weight of the curse lighten. The air around him shifts, and he senses that Comala itself is weakening."

    j "This... this is my chance. I can feel the town crumbling, the curse lifting."

    narrator "As Juan moves forward, the mansion begins to shake violently, and the ground cracks open. The town is collapsing. The souls of the dead watch in silence as Juan runs toward freedom."

    menu:
        "Run as fast as I can towards the light":
            jump escape_light

        "Look back at the town one last time":
            jump look_back_at_comala

label die_fighting:
    narrator "Juan continues to fight, even as his body grows weaker. With one last cry of defiance, he collapses. The walls of the mansion close in on him, and the curse consumes him fully."

    pedro (voice) "Foolish boy. You never understood. You are mine now."

    narrator "Juan's soul is trapped in Comala forever, his struggle only a distant memory as the town reverts to its original cursed state."

    return

label escape_town:
    narrator "With the curse broken, Juan runs, feeling the earth tremble beneath him. The very ground of Comala is crumbling as the curse that held it together begins to fall apart."

    j "I have to get out of here. There’s no time to waste."

    narrator "As Juan reaches the town's edge, he hears the distant sound of voices calling his name. The souls of Comala are free, but their whispers linger in the air."

    menu:
        "Keep running, never looking back":
            jump keep_running

        "Stop and listen to the voices":
            jump listen_to_voices

label stay_and_watch:
    narrator "Juan stays behind, watching as Comala collapses around him. The dust rises, the walls crack, and the sound of the curse breaking fills the air."

    pedro (voice) "This is the end, Juan. The curse is broken. But it is too late for you."

    narrator "As the town crumbles, Juan’s body begins to turn to dust, his soul becoming one with Comala forever."

    return

label attempt_to_flee:
    narrator "Juan tries to escape, but the power of the curse holds him in place. The walls close in, and Pedro’s laughter echoes in the air."

    pedro (voice) "You cannot run from what you are, Juan. Comala will always pull you back."

    menu:
        "Fight back with all my strength":
            jump fight_back_with_strength

        "Give in to the curse":
            jump give_in_to_curse

label face_pedro_last_time:
    narrator "Juan stands face to face with Pedro, his eyes filled with rage and sorrow. The town has collapsed around them, and only Pedro’s figure remains standing amidst the ruins."

    j "This is the end, Pedro. I will not let you win."

    pedro (voice) "You cannot stop what has already been set in motion. You are mine, Juan."

    menu:
        "Strike at Pedro with all my might":
            jump strike_pedro

        "Beg for one final chance":
            jump beg_for_chance

label escape_light:
    narrator "Juan bursts through the last barrier, feeling the warm light of freedom touch his skin. The ground beneath him shakes violently as the town collapses behind him."

    j "I’m free... I’ve made it out."

    narrator "The light envelops him fully, and for a moment, everything is still. When it fades, Juan finds himself in a place beyond Comala, a peaceful land far away from the curse."

    return

label look_back_at_comala:
    narrator "Juan stops for a moment, looking back at Comala, the cursed town that has been his prison. The souls of the dead can still be heard in the distance, their whispers fading into nothingness."

    j "I won’t forget any of this... but I have to move on."

    narrator "As Juan walks away from the decaying town, he feels a sense of closure, as though the town’s curse is no longer his burden to carry."

    return

label keep_running:
    narrator "Juan runs, the sound of his footsteps echoing through the collapsing town. The ground shakes, the buildings crumble, but he doesn’t stop. He’s finally free."

    j "I’m free... I’m finally free."

    narrator "As the town disappears behind him, Juan knows that the souls of Comala have been freed, and the curse has been broken. He is the last to leave, and with him, the memories of Comala are carried away."

    return

label listen_to_voices:
    narrator "Juan stops, hearing the faint whispers of the souls he’s left behind. Their voices reach out to him, a mixture of gratitude and sorrow."

    j "I can’t stay. I have to keep moving forward."

    narrator "But as the voices grow fainter, Juan feels a weight lifted from his shoulders. The curse is broken, and Comala’s spirits can now rest in peace."

    return

label sacrifice_old_man:
    narrator "Juan turns to the old man, his weary eyes full of sorrow. He knows that the only way to break the curse is to sacrifice another."

    j "I’m sorry. You’ve suffered enough. It’s my turn to save you all."

    narrator "With a heavy heart, Juan performs the ritual, and the old man’s spirit is released. The town shudders as the curse begins to lift."

    return

label sacrifice_ghost_woman:
    narrator "Juan looks at the ghost woman, who has been his companion through this journey. Her spirit is strong, but she too is bound by the curse."

    j "I’m sorry. This is the only way."

    narrator "With a sad farewell, Juan sacrifices the ghost woman, and her spirit is freed. The curse weakens, and Comala begins to fade away."

    return

label fight_back_with_strength:
    narrator "With all his might, Juan strikes back at the force that holds him, his body shaking with the effort. The curse pushes back, but Juan’s strength grows with every blow."

    pedro (voice) "You cannot fight me forever, Juan."

    j "I’ll fight until the end. I won’t be your prisoner."

    menu:
        "Strike harder, keep fighting":
            jump strike_harder

        "Rest for a moment, then continue":
            jump rest_then_continue

label give_in_to_curse:
    narrator "Juan’s body gives in, the power of the curse overwhelming him. His will fades as the darkness consumes him, and Comala becomes his eternal prison."

    return

label strike_pedro:
    narrator "With one final surge of strength, Juan strikes at Pedro, his fist landing squarely on Pedro’s chest. The curse wavers, but Pedro remains standing."

    pedro (voice) "Is this all you have, Juan?"

    j "I’ll fight until the end!"

    return

label beg_for_chance:
    narrator "Juan falls to his knees, pleading with Pedro for one last chance. The ground trembles beneath them, and Pedro’s figure looms larger, mocking his weakness."

    pedro (voice) "You’ve had your chance, Juan. It’s too late."

    return

label peaceful_ending:
    # Transition to the final moment
    scene comala_ruins with dissolve
    play music "music/peaceful_ending.mp3" fadein 2.0
    
    narrator "As the curse finally dissolves, the remnants of Comala crumble to the ground. The air grows still, and the oppressive presence of the ghosts fades away."
    
    # Spirits speaking to Juan
    ghost_woman "Thank you, Juan. You have set us free."
    old_man "We can now move on, into the light. We are no longer bound to this cursed town."
    
    # Juan reflecting on his actions
    j "I never thought I'd see this day. The ghosts are free, but at what cost?"
    
    narrator "Juan stands among the ruins of the town, the wind blowing softly through the debris. A faint light breaks through the clouds above."
    
    # Final moment of peace
    j "Maybe... maybe it's for the best. Comala was never meant to last forever."
    
    narrator "As Juan walks away from the ruins, the spirits of Comala can be seen walking into the light, leaving the town behind."
    
    # Peaceful conclusion
    scene comala_light with fade
    narrator "The air feels lighter, and the curse is no more. Juan walks towards an uncertain future, but a future nonetheless."
    
    return

label escape_ending:
    # Transition to the moment of escape
    scene comala_ruins_dark with fade
    play music "music/escape_ending.mp3" fadein 2.0
    
    narrator "Juan sprints through the collapsing streets of Comala, the sound of crumbling buildings echoing around him."
    
    j "I need to get out... before it’s too late!"
    
    # Sound of rumbling and destruction
    play sound "sound/earthquake_rumble.mp3"
    
    narrator "The ground shakes beneath his feet, and dust fills the air as Comala starts to fall apart. The curse, though broken, has left the town in ruins."
    
    j "Is this really freedom? Or am I just running away?"
    
    narrator "Despite his doubt, Juan presses on, his footsteps quickening as he nears the edge of the town."
    
    # Final choice moment: looking back
    j "I can’t look back... can’t stay here."
    
    # Juan escapes but the spirit’s voices call after him
    ghost_woman "You cannot escape, Juan. You carry us with you."
    
    # Visual of Juan escaping, but Comala’s shape distorts behind him
    scene comala_escape with dissolve
    
    narrator "Juan looks back once more before disappearing into the night, the wreckage of Comala slowly dissolving behind him."
    
    # Final somber note
    narrator "The wind carries away his footsteps, and the town is no more. Juan is free, but the echoes of Comala will follow him forever."
    
    return

label tragic_ending:
    # Transition to the moment of Pedro's victory
    scene comala_ruins_ghostly with fade
    play music "music/tragic_ending.mp3" fadein 2.0
    
    narrator "Pedro’s ghost reappears, his form even more powerful than before. The ground beneath Juan’s feet trembles as the curse tightens its grip."
    
    pedro "You cannot win, Juan. The town, the curse—it is all mine."
    
    j "No... this can’t be happening!"
    
    narrator "Despite Juan’s best efforts, Pedro’s power overwhelms him. The town around them distorts, and the spirits of Comala grow restless, their wails growing louder."
    
    ghost_woman "We are trapped... forever. You cannot break this cycle."
    
    # Visual effect of time loop
    scene comala_time_loop with fade
    
    narrator "Juan stumbles through the streets of Comala, realizing with horror that no matter how far he runs, he always ends up back in the same place."
    
    j "Why can’t I leave? I’m stuck here... forever."
    
    narrator "The ghostly voices of Comala’s inhabitants surround him, their cries echoing in his ears as he realizes he is forever bound to this cursed town."
    
    # Final moment of realization
    j "I was never meant to leave. I will always be a part of Comala."
    
    return
