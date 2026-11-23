define n = Character("Nighten", image="nighten")

define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#To show the dialouge with the phone in screen
screen fixed_dialogue(who, what):
    zorder 100
    style_prefix "say"

    window:
        id "window"

        if who:
            window:
                id "namebox"
                style "namebox"
                text who style "say_label"

        text what style "say_dialogue"

init python:
    def say_fixed(who, what):
        renpy.show_screen("fixed_dialogue", who, what)
        renpy.pause()          # waits for a click
        renpy.hide_screen("fixed_dialogue")

label option_1:
    e_nvl "really."
    show nighten phone e1m2
    $ say_fixed("Nighten", "oh.")
    return

label option_2:
    nvl_narrator "You cannot message this person no longer."
    show nighten phone e1m2
    $ say_fixed("Nighten", "oh.")
    return



# skips the main menu
label main_menu:
    return

label start:
    scene bg village with dissolve
    pause 1.0

    show nighten normal e1m1 at center:
        yoffset 1080
        ease 0.7 yoffset 0

    n "Hello this is a test"
    n e1m1 "this shows my image"
    n e1m2 "and another one"
    n e2m1 "now my eyes are closed"
    n e2m2 "it's closed but now my mouth is also closed"

    show nighten phone e1m2_b:
        ease 0.5 xalign 0.7
    n "i believe im now holding a phone"

    nvl_narrator "Nighten added Eileen to the group chat"
    n_nvl e2m2_b "heya welcome to testing"
    e_nvl "who the hell"
    n_nvl e2m1_b "haha silly you."
    $ say_fixed("Nighten", "i think im looking at my phone now")
    n_nvl e1m2_b "we talked about showing off the phone the other day. didja forget you dummy"
    e_nvl "what."
    e_nvl "I dont even know you."
    
    menu(nvl=True):
        "really?":
            n_nvl "really?"
            jump option_1
        "its-a-me, nighten!": 
            n_nvl "its-a-me, nighten!"
            jump option_2