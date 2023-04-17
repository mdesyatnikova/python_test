from model.contact import Contact


def test_add_contact(app, data_contacts):
    contact = data_contacts
    app.contact.create(contact)
