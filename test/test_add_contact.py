from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("vasya", "vasyan", "123"))
