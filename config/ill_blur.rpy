init python:
    def get_size(d):
        d = renpy.easy.displayable(d)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h

    def soznanie(img):
        img = renpy.easy_displayable(img)
        width, height = get_size(img)

        factor = im.Scale(img, width/10, height/10)
        factor = Transform(factor, size=(width, height))
        renpy.show("blur_effect", what=factor)
        renpy.with_statement(Dissolve(1/2))#init python:
