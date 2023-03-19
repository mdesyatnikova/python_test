from model.contact import Contact


def test_add_contact(app):
    app.session.login()
    app.contact.create(Contact("vasya", "vasyan", "123"))
    app.session.logout()