# Definition of characters
define player = Character("player_name", dynamic=True, color="#d17930")
define boris = Character(_("Борис"), image="boris", color="#2a2a78")
define customer = Character(_("Клиент"), color="#999")
define manager = Character(_("Менеджер"), image="manager")
define lisa = Character(_("Лиза"), image="lisa", color="#ffe5b4")
define priest = Character(_("Батюшка"), image="priest", color="#75a83e")

init:
    transform left_center:
        xalign 0.2
    transform right_center:
        xalign 0.8
    transform grayscale:
        matrixcolor SaturationMatrix(0.5)
    transform silhouette:
        center, yalign 0.53
    transform distance:
        zoom 0.5, align (0.5, 0.8)

label start:
    $ player_name = renpy.input(_("Как вас зовут?"), length=10, default=_("Женя"))
    $ player_name = player_name.strip().capitalize()
    if not player_name:
      $ player_name = _("Женя")
    play music toes
    call act1
    call act2
    call act3
    return

label splash_text(text=None):
    scene black
    if text:
        show text "{size=80}[text]{/size}" with dissolve
        with Pause(2)
        hide text with dissolve
        with Pause(1)
    else:
        pause 2
    return

