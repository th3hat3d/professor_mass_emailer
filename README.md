# professor_mass_emailer
This essentially scrapes the emails off of university faculty websites and emails each one,
I'll be adding new features as time goes on.

Instructions for use:
**If using a non-school account: Enable 2FA, create an app password specifically for this script, and use that as the password**

1. Edit the script to contain your email and password in the specified fields.
2. Have an "email.txt" file in the current directory containing your message content.
3. Launch the script and paste in your faculty link.

Requires Python 3.x, plus the `requests` module.

Limitations to remove:
- [ ] Only works for GMail
- [ ] No support for obfuscated emails (will add soon)
- [ ] Will make a website for this to make things easier
- [ ] May add crawling
