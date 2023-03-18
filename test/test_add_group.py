from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("qwe", "qweqw", "qweqer"))
    app.session.logout()
