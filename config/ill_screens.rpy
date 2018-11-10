screen ill_main_menu_pre:
    modal False
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    timer 0.1 action(Hide("ill_main_menu_pre", transition=dissolve), Show("ill_main_menu") )

screen ill_main_menu:
    tag menu
    modal False
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    add "bg black"
    text (u"Иллюзион") at ill_down_menu(0.15):
        style "ill_headers"
        size 125
        kerning 2.2
        xalign 0.85
    textbutton "Начать игру" at ill_left_menu(0.85):
        anchor(0,0.5)
        text_align 0.0
        yalign 0.39
        style "log_button"
        text_style "ill_mmenu"
        action (Hide("ill_main_menu",transition=dissolve), Return("ill_prologue"))
    textbutton "Галерея" at ill_left_menu(0.85):
        anchor(0,0.5)
        text_align 0.0
        yalign 0.49
        style "log_button"
        text_style "ill_mmenu"
        action (Hide("ill_main_menu", transition=dissolve), Show("ill_gallery_bg"))
    textbutton "Музыка" at ill_left_menu(0.85):
        anchor(0,0.5)
        text_align 0.0
        yalign 0.59
        style "log_button"
        text_style "ill_mmenu"
        action (Hide("ill_main_menu", transition=dissolve), Show("ill_music_room"))
    if persistent.illusion_complete:
        textbutton "Экстра" at ill_left_menu(0.85):
            anchor(0,0.5)
            text_align 0.0
            yalign 0.69
            style "log_button"
            text_style "ill_mmenu"
            action (Hide("ill_main_menu", transition=dissolve), Show("ill_extra_room"))
    else:
        text "Экстра" at ill_left_menu(0.85):
            anchor(0,0.5)
            text_align 0.0
            yalign 0.69
            style "ill_mmenu"
            color "#696969"
    if True in persistent.ill_ach.values():
        textbutton "Достижения" at ill_left_menu(0.85):
            anchor(0,0.5)
            text_align 0.0
            yalign 0.79
            style "log_button"
            text_style "ill_mmenu"
            action(Hide("main_menu_illusion", transition=dissolve), Return("ill_achievments") )
    textbutton "Выход" at ill_left_menu(0.85):
        anchor(0,0.5)
        text_align 0.0
        yalign 0.89
        style "log_button"
        text_style "ill_mmenu"
        action (Hide("ill_main_menu", transition=dissolve), Return("exit"))

screen ill_gallery_bg:
    modal False
    tag menu
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    $ len_table = len(ill_gallery_bg)
    window:
        background "cg d5_dv_island"
        textbutton "Иллюстрации":
            style "log_button"
            text_style "ill_mmenu"
            yalign 0.08
            xalign 0.3
            action (SetVariable('ill_page', 0), Hide("ill_gallery_bg", transition=dissolve), Show("ill_gallery_сg"))
        text "Фоны":
            style "ill_mmenu"
            yalign 0.08
            xalign 0.8
            color "#808080"
            outlines [(2, "#cc7722", 0, 0), (2, "#cc7722", 3, -3)]
        textbutton "Назад" at ill_up_menu(0.95):
            style "ill_mmenu"
            text_style "ill_mmenu"
            xalign 0.05
            action (Hide("ill_gallery_bg", transition=dissolve), Show("ill_main_menu") )
        grid 4 3:
            xpos 0.09 ypos 0.20
            $ cg_displayed = 0
#            $ next_page = ill_page + 1
#            if next_page > int(len_table/cells):
#                $ next_page = 0
            for n in range(0, len_table):
#                if n < (ill_page+1)*cells and n>=ill_page*cells:
                python:
                    _t = "illusion/images/bg/"+ill_gallery_bg[n]+".jpg"
                    th = im.Scale(_t, 320, 180)
                    img = im.Composite((336,196),(8,8),im.Alpha(th,0.9),(0,0),im.Image(get_image("gui/gallery/thumbnail_idle.png")))
                    imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image(get_image("gui/gallery/thumbnail_hover.png")))
                add ill_g.make_button(ill_gallery_bg[n], get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                $ cg_displayed += 1
#                    if n+1 == len_table:
#                        $ next_page = 0
            for j in range(0, cells-cg_displayed):
                null
#        if ill_page != 0:
#            imagebutton auto get_image("gui/dialogue_box/day/backward_%s.png") yalign 0.5 xalign 0.01 action (SetVariable('ill_page', ill_page-1), Show("illusion_gallery_bg", transition=dissolve))
#        imagebutton auto get_image("gui/dialogue_box/day/forward_%s.png") yalign 0.5 xalign 0.99 action (SetVariable('ill_page', next_page), Show("illusion_gallery_bg", transition=dissolve))
#        python:
#            def abc(n,k):
#                l = float(n)/float(k)
#                if l-int(l) > 0:
#                    return int(l)+1
#               else:
#                    return l
#            pages = str(ill_page+1)+"/"+str(int(abc(len_table,cells)))
#        text pages style "ill_mmenu" xalign 0.985 yalign 0.92

screen ill_gallery_cg:
    tag menu
    modal False
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    $ len_table = len(ill_gallery_cg)
    window:
        add "cg ill_blur_d5_dv_island"
        textbutton "Фоны":
            style "log_button"
            text_style "ill_mmenu"
            yalign 0.08
            xalign 0.8
            action ( SetVariable('ill_page', 0), Hide("illusion_gallery", transition=dissolve), ShowMenu("ill_gallery_bg"))
        text "Иллюстрации":
            style "ill_mmenu"
            yalign 0.08
            xalign 0.3
            color "#808080"
            outlines [(2, "#cc7722", 0, 0), (2, "#cc7722", 3, -3)]
        textbutton "Назад" at ill_up_menu(0.97) style "log_button" text_style "ill_mmenu" yalign 0.9 action (SetVariable('ill_page', 0), Hide("ill_gallery_cg", transition=dissolve), ShowMenu("ill_main_menu") )
        grid rows cols xpos 0.09 ypos 0.20:
            $ cg_displayed = 0
            $ next_page = ill_page + 1
            if next_page > int(len_table/cells):
                $ next_page = 0
            for n in range(0, len_table):
                if n < (ill_page+1)*cells and n>=ill_page*cells:
                    python:
                        _t = "illusion/images/cg/"+ill_gallery_cg[n]+".png"
                        th = im.Scale(_t, 320, 180)
                        img = im.Composite((336,196),(8,8),im.Alpha(th,0.9),(0,0),im.Image(get_image("gui/gallery/thumbnail_idle.png")))
                        imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image(get_image("gui/gallery/thumbnail_hover.png")))
                    add ill_g.make_button(ill_gallery_cg[n], get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                    $ cg_displayed += 1
                    if n+1 == len_table:
                        $ next_page = 0
            for j in range(0, cells-cg_displayed):
                null
        if ill_page != 0:
            imagebutton auto get_image("gui/dialogue_box/day/backward_%s.png") yalign 0.5 xalign 0.01 action (SetVariable('ill_page', ill_page-1), Show("ill_gallery_cg", transition=dissolve))
        imagebutton auto get_image("gui/dialogue_box/day/forward_%s.png") yalign 0.5 xalign 0.99 action (SetVariable('ill_page', next_page), Show("ill_gallery_cg", transition=dissolve))
        python:
            def abc(n,k):
                l = float(n)/float(k)
                if l-int(l) > 0:
                    return int(l)+1
                else:
                    return l
            pages = str(ill_page+1)+"/"+str(int(abc(len_table,cells)))
        text pages style "ill_mmenu" xalign 0.985 yalign 0.92

screen ill_music_room:
    tag menu
    modal False
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    frame:
        add "ill_pre_chapter"
        textbutton "Назад" at ill_up_menu(0.92):
            style "log_button"
            text_style "ill_mmenu"
            xalign 0.015
            if renpy.music.get_playing(channel='music') != None and not ("illusion/res/music/Сплин - Выхода нет(Минус).mp3" == renpy.music.get_playing(channel='music')):
                action (Hide("ill_music_room", transition=dissolve), Play('music', "illusion/res/music/Сплин - Выхода нет(Минус).mp3", fadeout=1, fadein=1), Show("ill_main_menu") )
            else:
                action (Hide("ill_music_room", transition=dissolve), Show("ill_main_menu") )

        side "c":
            area (0.23, 0.12, 0.61, 0.85)
            viewport id "music_box":
                draggable True
                mousewheel True
                scrollbars None

                has grid 1 len(ill_music_list)
                for name, track in ill_music_list:
                    textbutton name style "log_button" text_style "ill_mrroom" action ill_mr.Play(track)

screen ill_photoalbum:
    tag menu
    modal False
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    $ len_table = len(ill_photos)
    window:
        add "cg d5_dv_island"
        textbutton "Назад" at ill_up_menu(0.95):
            style "ill_mmenu"
            text_style "ill_mmenu"
            xalign 0.05
            action (Hide("ill_photoalbum", transition=dissolve), Show("ill_main_menu") )
        grid rows cols xpos 0.09 ypos 0.20:
            $ cg_displayed = 0
            $ next_page = ill_page + 1
            if next_page > int(len_table/cells):
                $ next_page = 0
            for n in range(0, len_table):
                if n < (ill_page+1)*cells and n>=ill_page*cells:
                    python:
                        _t = "illusion/res/images/photos/"+ill_photos[n]+".png"
                        th = im.Scale(_t, 320, 180)
                        img = im.Composite((336,196),(8,8),im.Alpha(th,0.9),(0,0),im.Image(get_image("gui/gallery/thumbnail_idle.png")))
                        imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image(get_image("gui/gallery/thumbnail_hover.png")))
                    add ill_g.make_button(ill_photos[n], get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                    $ cg_displayed += 1
                    if n+1 == len_table:
                        $ next_page = 0
            for j in range(0, cells-cg_displayed):
                null
        if ill_page != 0:
            imagebutton auto get_image("gui/dialogue_box/day/backward_%s.png") yalign 0.5 xalign 0.01 action (SetVariable('ill_page', ill_page-1), Show("ill_photoalbum", transition=dissolve))
        imagebutton auto get_image("gui/dialogue_box/day/forward_%s.png") yalign 0.5 xalign 0.99 action (SetVariable('ill_page', next_page), Show("ill_photoalbum", transition=dissolve))
        python:
            def abc(n,k):
                l = float(n)/float(k)
                if l-int(l) > 0:
                    return int(l)+1
                else:
                    return l
            pages = str(ill_page+1)+"/"+str(int(abc(len_table,cells)))
        text pages style "ill_mmenu" xalign 0.985 yalign 0.92

#screen ill_download:
