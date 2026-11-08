import re

kod = "DSC-2026"
corak = r"^[A-Z]{3}-\d{4}$"

print(re.match(corak, kod) is not None)
print(re.match(corak, "dsc-2026") is not None)
print(re.match(corak, "DSC-26") is not None)

email = "aiman@example.com"
corak_email = r"^[\w.+-]+@[\w-]+\.[\w.]+$"
print(re.match(corak_email, email) is not None)
