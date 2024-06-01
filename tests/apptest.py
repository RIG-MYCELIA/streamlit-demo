from streamlit.testing.v1 import AppTest

at = AppTest.from_file("../pages/Gebruik.py")
at.run()
assert not at.exception

# Button should appear after a name is filled in
assert len(at.button) == 0
at.text_input[0].set_value("Peter Griffin")
at.run()
assert len(at.button) == 1

# Check that a 17-year-old does not qualify
at.checkbox[0].set_value(True)
at.slider[0].set_value(17)
at.button[0].click()
at.run()
assert at.markdown[1].value == "Nee, helaas"

# Check that an 18-year-old Peter Griffin, who likes beer, qualifies
at.slider[0].set_value(18)
at.button[0].click()
at.run()
assert at.markdown[1].value == "Ja, gefeliciteerd!"
