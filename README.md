# professor_mass_emailer
This essentially scrapes the emails off of university faculty websites and emails each one,
I'll be adding new features as time goes on.

Instructions for use:
1. Edit the script to contain your email and password in the specified fields.
2. Have an "email.txt" file in the current directory containing your message content.

Requires Python 3.x, plus the `requests` module.

Limitations to remove:
- [ ] Only works for GMail
- [ ] No support for 2FA at the moment
- [ ] No support for obfuscated emails (will add soon)
