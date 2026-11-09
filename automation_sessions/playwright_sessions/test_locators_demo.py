from playwright.sync_api import Page, expect
import re

# page.get_by_alt_text()
# page.get_by_text()
# page.get_by_role()

def test_verify_pwlocators(page:Page):
    page.goto("https://naveenautomationlabs.com/opencart/")
    
    # page.get_by_alt_text()
    logo = page.get_by_alt_text("naveenopencart")
    expect(logo).to_be_visible()
    
    # page.get_by_text()
    expect(page.get_by_text("Featured")).to_be_visible()
    expect(page.get_by_text("iPhone is a revolutionary")).to_be_visible()
    expect(page.get_by_text(re.compile(".*Intel Core 2.*"))).to_be_visible()
    
    # page.get_by_role()
    expect(page.get_by_role("heading",name="Featured")).to_be_visible()
    
    # page.get_by_label()
    page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/register")
    page.get_by_label("First Name").fill("Zadid")
    page.get_by_label("Last Name").fill("Ahsan")
    page.get_by_label("E-Mail").fill("zadidahsan@email.com")
    page.get_by_label("Telephone").fill("0123456789")

    # page.get_by_placeholder()

    