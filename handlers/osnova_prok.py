async def azaza23():
    from pyrogram import Client, filters, idle
    from pyrogram.handlers import MessageHandler

    my_apps = [
        Client('session1', 15429738, 'c147b713a6e1e7cbcdc0f92565605945'),
        Client('session2', 17863610, '29204188291a4e719ffcb2f47a64465c')
    ]

    def test(number, message):
        if number == 1:
            my_apps[0].create_channel(title='Hello_one')
        else:
            my_apps[1].create_channel(title='Hello_two')


    for app in my_apps:
        print(app)
        app.add_handler(MessageHandler(test))
        app.start()

    idle()

    for app in my_apps:
        app.stop()
