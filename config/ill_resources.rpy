init:

    $ ill_path_img = "illusion/res/images/"
    $ ill_path_mus = "illusion/res/music/"

    # Все нужные изображения для меню

    image ill_menu_background = im.Scale(ill_path_img + "menu/menu_background.jpg",1920,1080)
    image ill_logo = ill_path_img + "menu/logo.png"

    python:

    # BG and CG

        for i in renpy.list_files():
            if i.startswith("illusion/res/images/bg/") and i.endswith((".jpg", ".png")):
                renpy.image(("bg ill_" + str(i)[23:-4]), i)
                renpy.image(("bg ill_glitch_" + str(i)[23:-4]), Glitch(i))
            elif i.startswith("illusion/res/images/cg/") and i.endswith((".jpg", ".png")):
                renpy.image(("cg ill_" + str(i)[23:-4]), i)

    # Музыка и звуки

    $ ill_mus_owl_e = ill_path_mus + "Oceans Who Lied - Emma.mp3"
    $ ill_mus_cas_f = ill_path_mus + "Cigarettes After Sex - Flash.mp3"
    $ ill_mus_dh_atmf = ill_path_mus + "Dustin O'Halloran - All Things Must Fall.mp3"
    $ ill_mus_bda_nw = ill_path_mus + "Birds Die Alone - No way.mp3"
    $ ill_mus_s_vn = ill_path_mus + "Сплин - Выхода нет(Минус).mp3"
    $ ill_mus_a_l = ill_path_mus + "april_lie.mp3"

    $ ill_sfx_photo = "<from 0 to 1>illusion/res/music/sfx/sfx_photo.mp3"

    # Трансформы

    transform ill_right_menu(xal):
        xalign -0.1
        alpha 0.0
        easein 1 xalign xal alpha 1.0
        on hover:
            easein 0.5 zoom 1.05
        on idle:
            easein 0.5 zoom 1.00

    transform ill_left_menu(xal):
        xalign 1.1
        alpha 0.0
        easein 1 xalign xal alpha 1.0
        on hover:
            easein 0.5 zoom 1.05
        on idle:
            easein 0.5 zoom 1.00

    transform ill_up_menu(yal):
        yalign 1.1
        alpha 0.0
        easein 1 yalign yal alpha 1.0
        on hover:
            easein 0.5 zoom 1.05
        on idle:
            easein 0.5 zoom 1.00

    transform ill_down_menu(yal):
        yalign -0.1
        alpha 0.0
        easein 1 yalign yal alpha 1.0

    transform ill_get_achievement_atl:
        pos(0.85, 0.85)
        anchor(0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause 4.0
        ease 0.5 pos(0.8, 0.85)
        ease 0.5 pos(1.0, 0.85) alpha 0.0

    transform ill_right_chapter(xal):
        xalign -0.2
        alpha 0.0
        easein 2 xalign xal alpha 1.0
        linear 3.0 xalign 0.23

    transform ill_left_chapter(xal):
        xalign 1.1
        alpha 0.0
        easein 1 xalign xal alpha 1.0
        linear 3.0 xalign 0.60

    transform ill_photo:
        around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
        rotate 0
        zoom 0.0
        easein 1.5 zoom 0.70
        linear 1 rotate -5

    # Стили

    style ill_headers:
        font "illusion/res/fonts/poiret.ttf"
        outlines [(2, "#32075C", 0, 0), (2, "#32075C", 3, -3)]
        idle_color "#fff"
        hover_color "#4B0082"

    style ill_menu:
        is settings_link
        font "illusion/res/fonts/palette.ttf"

    style ill_mmenu:
        is ill_menu
        size 85
        outlines [(2, "#32075C", 0, 0), (2, "#32075C", 3, -3)]
        idle_color "#fff"

    style ill_achievments:
        font "illusion/res/fonts/elixia.ttf"
        color "#fff"
        outlines [(2, "#4B0082", 0, 0), (2, "#4B0082", 3, -3)]
        drop_shadow [ (1, 1), (1, 1), (1, 1), (1, 1) ]
        drop_shadow_color "#47240A"
        yalign 0.5
        text_align 0.5
        kerning 17.0
        size 90

    style ill_mrroom:
        is music_link
        font "illusion/res/fonts/palette.ttf"
        size 48

    $ style.ill_backdrop_text = Style(style.default)
    $ style.ill_backdrop_text.font = "illusion/res/fonts/palette.ttf"
    $ style.ill_backdrop_text.size = 150

init 998 python:

    # Ачивки

    ill_ach_list = [
        ("prologue", u"Прочитать пролог."),
        ("owl", u"Фотогиеничный совёнок."),
        ("lost_in_time", u"Потеряться во времени.")
    ]

    if persistent.ach_ill_owl:
        persistent.ill_ach["owl"] = True
    if persistent.ach_ill_prologue:
        persistent.ill_ach["prologue"] = True
    if persistent.ach_ill_lost_in_time:
        persistent.ill_ach["lost_in_time"] = True

    if persistent.ill_ach == None:
        persistent.ill_ach = dict()
        for ach in ill_ach_list:
            ach_name = ach[0]
            persistent.ill_ach[ach_name] = False

    for ach in ill_ach_list:
        renpy.image("ill_ach_" + ach[0], im.Scale("illusion/res/images/achievements/ach_" + ach[0] + ".png", 450, 125))
    renpy.image("ill_ach_blank", im.Scale("illusion/res/images/achievements/ach_blank.png", 450, 125))

    # Галерея

    ill_g = Gallery()

    ill_g.transition = fade
    ill_g.locked_button = get_image("gui/gallery/not_opened_idle.png")
    ill_g.unlocked_button = get_image("gui/gallery/blank.png")

    ill_gallery_bg = [
    ]

    ill_gallery_cg = []

    for bg in ill_gallery_bg:
        ill_g.button(bg)
        ill_g.image(im.Scale("illusion/res/images/bg/"+bg+".jpg",1920,1080))
        ill_g.unlock("bg ill_"+bg)

    for cg in ill_gallery_cg:
        ill_g.button(cg)
        ill_g.image(im.Scale("illusion/res/images/cg/"+cg+".png",1920,1080))
        ill_g.unlock("cg ill_"+cg)

    ill_page = 0
    gallery_mode_ill = "bg"

    # Музыкальная комната

    ill_music_list = [
    ("Oceans Who Lied - Emma", "illusion/res/music/Oceans Who Lied - Emma.mp3"),
    ("Dustin O'Halloran - All Things Must Fall", "illusion/res/music/Dustin O'Halloran - All Things Must Fall.mp3"),
    ("Сплин - Выхода нет(Минус)", "illusion/res/music/Сплин - Выхода нет(Минус).mp3"),
    ]

    ill_mr = MusicRoom(fadeout=1.0)

    for name, file in ill_music_list:
        ill_mr.add(file)


    # Фотоальбом(Экран)

    ill_p = Gallery()

    ill_p.transition = fade
    ill_p.locked_button = get_image("gui/gallery/not_opened_idle.png")
    ill_p.unlocked_button = get_image("gui/gallery/blank.png")

    ill_photos = [
        "owl",
    ]

    for photo in ill_photos:
        ill_p.button(photo)
        ill_p.image(im.Scale("illusion/res/images/photos/"+photo+".png",1920,1080))
        ill_p.unlock(photo)

    for i in ill_photos:
        renpy.image("ill_photo_" + i, im.Scale("illusion/res/images/photos/" + i + ".png",1920,1080))

init 3:

    # Персонажи

    $ colors["ill_kir"] = {"night": (196, 151, 376, 255), "sunset": (218, 165, 32, 255), "day": (218, 165, 32, 255), "prolog": (218, 165, 32, 255)}
    $ names["ill_kir"] = u"Кир"
    $ store.names_list.append("ill_kir")

    $ colors["ill_kira"] = {"night": (116, 186, 69, 255), "sunset": (116, 186, 69, 255), "day": (116, 186, 69, 255), "prolog": (116, 186, 69, 255)}
    $ names["ill_kira"] = u"Кира"
    $ store.names_list.append("ill_kira")

    $ colors["ill_marry_guest"] = {"night": (212, 199, 63, 255), "sunset": (212, 199, 63, 255), "day": (212, 199, 63, 255), "prolog": (212, 199, 63, 255)}
    $ names["ill_marry_guest"] = u"Гость на свадьбе"
    $ store.names_list.append("ill_marry_guest")

    # Переменные и флаги

    if persistent.ill_route_complete_count == None: # Счётчик пройденных рутов. При прохождении хотя бы двух открывается истинный.
        $ persistent.ill_route_complete_count = 0

    python:

        if persistent.ill_routes == None:
            persistent.ill_routes = {

                "ill_neutral_route": False,
                "ill_lie_route": False,
                "ill_true_route": False,
                "ill_bad_route": False,
                "ill_real_route": False

            }
